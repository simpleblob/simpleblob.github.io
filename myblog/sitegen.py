#!/usr/bin/env python3
"""
Static site generator for simpleblob.com ("Marginalia" design).

Reads Markdown notes with YAML frontmatter from myblog/posts/, converts them
with Pandoc, files them into catalogue drawers (frontmatter `topic:`), and
renders every page with Jinja2:

    index.html     preface, reading desk and the card catalogue
    archive.html   every note by date
    contact.html
    posts/*.html   one page per note

Pandoc output is cached by content hash, so unchanged notes skip Pandoc;
the pages themselves are always re-rendered (they link to each other).
"""

from __future__ import annotations

import hashlib
import html
import logging
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

HERE = Path(__file__).parent.resolve()
FILTER = HERE / "sidenotes.lua"
PANDOC_ARGS = ["pandoc", "-f", "markdown", "-t", "html", "--mathjax", "--no-highlight"]
STATUSES = ("draft", "ongoing", "finished")
STATUS_NOTES = {
    "draft": "A draft is a working note: it may be reopened and revised.",
    "ongoing": "An ongoing note is a living document, still being added to.",
    "finished": "A finished note is complete as it stands.",
}

# "Book Summary - Deep Work by Cal Newport" -> form, title, author
FORM_RE = re.compile(r"^((?:Book|Presentation|Project) Summary)\s*[-–]\s*(.+)$")
BY_RE = re.compile(r"^(.+?) by ((?:[A-Z][\w.'’]*\s?){2,4})$")
HEADING_RE = re.compile(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', re.S)
TAG_RE = re.compile(r"<[^>]+>")
NUMBER_WORDS = (
    "zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
).split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


class BuildError(Exception):
    pass


# ---------- small helpers ----------


def clean(value) -> str:
    """Frontmatter text, with the placeholder values "None"/"none" treated as empty."""
    text = "" if value is None else str(value).strip()
    return "" if text.lower() in ("none", "null") else text


def to_date(value) -> date:
    return value if isinstance(value, date) else date.fromisoformat(str(value).strip())


def count_words(markdown: str) -> int:
    text = re.sub(r"\]\([^)]*\)", "]", markdown)  # link targets are not words
    text = re.sub(r"<[^>]+>|https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-z0-9][\w'’-]*", text))


def number_words(n: int) -> str:
    if n < 20:
        return NUMBER_WORDS[n]
    if n < 100:
        tens, ones = divmod(n, 10)
        return TENS[tens] + ("-" + NUMBER_WORDS[ones] if ones else "")
    return f"{n:,}"


def plain_text(fragment: str) -> str:
    return html.unescape(TAG_RE.sub("", fragment)).strip()


def shorten(text: str, limit: int = 180) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",;:—-") + "…"


def year_span(first: int, last: int) -> str:
    return str(first) if first == last else f"{first}–{last}"


# ---------- model ----------


@dataclass
class Post:
    slug: str
    title: str  # as listed in the catalogue, without the "Book Summary" form
    form: str  # "Book Summary", "Project Summary", … or ""
    heading: str  # article h1: title without the author
    author: str
    subtitle: str
    tags: list[str]
    created: date
    published: date
    status: str
    topic: str
    unlisted: bool
    words: int
    markdown: str
    body: str = ""  # Pandoc HTML, filled in by the build
    toc: list[dict] = field(default_factory=list)
    drawer: Drawer | None = None

    @property
    def url(self) -> str:
        return f"posts/{self.slug}.html"

    @property
    def reading_minutes(self) -> int:
        return max(1, round(self.words / Site.words_per_minute))

    @property
    def sections(self) -> list[str]:
        return [h["label"] for h in self.toc]

    @property
    def lede(self) -> str:
        """First top-level paragraph of the note (not one inside a list), as plain text."""
        match = re.search(r"^<p>(.*?)</p>", self.body, re.S | re.M)
        return shorten(plain_text(match.group(1))) if match else ""

    @property
    def has_math(self) -> bool:
        return 'class="math' in self.body

    @property
    def status_note(self) -> str:
        return STATUS_NOTES[self.status]


@dataclass
class Drawer:
    slug: str
    code: str
    name: str
    blurb: str
    see_also: list[Post]
    posts: list[Post] = field(default_factory=list)

    @property
    def years(self) -> str:
        return year_span(
            min(p.published.year for p in self.posts),
            max(p.published.year for p in self.posts),
        )

    @property
    def longest(self) -> Post:
        return max(self.posts, key=lambda p: p.words)

    def neighbours(self, post: Post) -> tuple[Post | None, Post | None]:
        """(older, newer) card in this drawer."""
        i = self.posts.index(post)
        older = self.posts[i + 1] if i + 1 < len(self.posts) else None
        newer = self.posts[i - 1] if i > 0 else None
        return older, newer


def parse_post(path: Path, required: list[str]) -> Post:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise BuildError(f"{path.name}: missing frontmatter")
    try:
        _, front, body = text.split("---", 2)
        meta = yaml.safe_load(front)
    except (ValueError, yaml.YAMLError) as e:
        raise BuildError(f"{path.name}: invalid frontmatter: {e}") from e
    if not isinstance(meta, dict):
        raise BuildError(f"{path.name}: frontmatter must be a mapping")
    missing = [f for f in required if f not in meta]
    if missing:
        raise BuildError(f"{path.name}: missing fields: {', '.join(missing)}")

    title = clean(meta["title"])
    form = ""
    if m := FORM_RE.match(title):
        form, title = m.group(1), m.group(2)
    title = title[:1].upper() + title[1:]
    heading, author = title, ""
    if form == "Book Summary" and (m := BY_RE.match(title)):
        heading, author = m.group(1), m.group(2).strip()

    status = clean(meta.get("status")).lower() or "draft"
    if status not in STATUSES:
        raise BuildError(f"{path.name}: unknown status {status!r}")
    unlisted = bool(meta.get("unlisted", False))
    topic = clean(meta.get("topic"))
    if not topic and not unlisted:
        raise BuildError(f"{path.name}: needs `topic:` (or `unlisted: true`)")

    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = tags.split(",")
    return Post(
        slug=path.stem,
        title=title,
        form=form,
        heading=heading,
        author=author,
        subtitle=clean(meta.get("subtitle")),
        tags=[t for t in (clean(t) for t in tags) if t],
        created=to_date(meta["created"]),
        published=to_date(meta["published"]),
        status=status,
        topic=topic,
        unlisted=unlisted,
        words=count_words(body),
        markdown=body,
    )


# ---------- Pandoc ----------


def pandoc_html(markdown: str, cache_dir: Path | None) -> str:
    # Notes written with "#" as their top heading are shifted so the page
    # keeps a single h1 (the note title).
    args = PANDOC_ARGS + [f"--lua-filter={FILTER}"]
    if re.search(r"^# ", markdown, re.M):
        args.append("--shift-heading-level-by=1")
    key = hashlib.sha256(
        "\0".join(args + [FILTER.read_text(), markdown]).encode()
    ).hexdigest()
    cached = cache_dir / f"{key}.html" if cache_dir else None
    if cached and cached.exists():
        return cached.read_text(encoding="utf-8")
    try:
        out = subprocess.run(
            args, input=markdown, capture_output=True, text=True, check=True
        ).stdout
    except FileNotFoundError as e:
        raise BuildError("pandoc not found on PATH") from e
    except subprocess.CalledProcessError as e:
        raise BuildError(f"pandoc failed: {e.stderr}") from e
    if cached:
        cached.parent.mkdir(exist_ok=True)
        cached.write_text(out, encoding="utf-8")
    return out


def finish_body(body: str, root: str) -> str:
    """Make site-absolute links relative and let wide tables scroll."""
    body = re.sub(r'(href|src)="/(?!/)', rf'\1="{root}', body)
    body = body.replace("<table", '<div class="table-wrap"><table')
    return body.replace("</table>", "</table></div>")


def table_of_contents(body: str) -> list[dict]:
    """h2 entries with their h3 children."""
    toc: list[dict] = []
    for level, anchor, label in HEADING_RE.findall(body):
        entry = {"id": anchor, "label": plain_text(label), "children": []}
        if level == "2" or not toc:
            toc.append(entry)
        else:
            toc[-1]["children"].append(entry)
    return toc


# ---------- site ----------


class Site:
    words_per_minute = 230

    def __init__(self, config_path: Path = HERE / "config.toml", output: Path | None = None):
        with open(config_path, "rb") as f:
            self.config = tomllib.load(f)
        paths = self.config["paths"]
        self.source = HERE / paths["posts_source"]
        self.output = (output or HERE / paths["output"]).resolve()
        Site.words_per_minute = self.config["post"].get("words_per_minute", 230)
        incremental = self.config.get("build", {}).get("incremental", True)
        self.cache_dir = HERE / ".pandoc_cache" if incremental else None

        self.env = Environment(
            loader=FileSystemLoader(HERE / paths["templates"]),
            autoescape=select_autoescape(["html"]),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.env.filters["longdate"] = lambda d: f"{d.day} {d:%B %Y}"
        self.env.filters["shortdate"] = lambda d: f"{d.day} {d:%b %Y}"
        self.env.filters["thousands"] = lambda n: f"{n:,}"
        self.env.filters["words"] = number_words

    def load(self) -> None:
        required = self.config["post"]["required_fields"]
        self.posts = [parse_post(p, required) for p in sorted(self.source.glob("*.md"))]
        if not self.posts:
            raise BuildError(f"no notes in {self.source}")
        by_slug = {p.slug: p for p in self.posts}

        self.drawers = []
        for t in self.config["topics"]:
            unknown = [s for s in t.get("see_also", []) if s not in by_slug]
            if unknown:
                raise BuildError(f"topic {t['slug']}: unknown see_also {unknown}")
            self.drawers.append(
                Drawer(
                    slug=t["slug"],
                    code=t["code"],
                    name=t["name"],
                    blurb=t.get("blurb", ""),
                    see_also=[by_slug[s] for s in t.get("see_also", [])],
                )
            )
        drawers = {d.slug: d for d in self.drawers}
        newest_first = sorted(self.posts, key=lambda p: (p.published, p.slug), reverse=True)
        for post in newest_first:
            if post.unlisted:
                continue
            if post.topic not in drawers:
                raise BuildError(f"{post.slug}: unknown topic {post.topic!r}")
            post.drawer = drawers[post.topic]
            post.drawer.posts.append(post)
        self.drawers = [d for d in self.drawers if d.posts]
        self.listed = [p for p in newest_first if not p.unlisted]

        for post in self.posts:
            post.body = pandoc_html(post.markdown, self.cache_dir)
            post.toc = table_of_contents(post.body)

    # -- page data --

    def desk(self) -> list[dict]:
        """The reading desk: every ongoing note, then the newest card."""
        newest = self.listed[0]
        picks = [p for p in self.listed if p.status == "ongoing" and p is not newest]
        slips = []
        for post in picks + [newest]:
            slip = {"post": post, "kind": post.status.capitalize(), "note": ""}
            if post is newest:
                slip["kind"] = "Newest card"
                if len(self.listed) > 1:
                    gap = (newest.published - self.listed[1].published).days // 365
                    if gap >= 2:
                        slip["note"] = (
                            f"The first new card in more than {number_words(gap)} years: "
                            "the catalogue is open again."
                        )
            if not slip["note"] and len(post.sections) > 3:
                shown = ", ".join(post.sections[:3])
                slip["note"] = f"Sections include {shown} and {len(post.sections) - 3} more."
            slips.append(slip)
        return slips

    def common(self, root: str, nav: str) -> dict:
        years = [p.published.year for p in self.listed] + [p.created.year for p in self.listed]
        return {
            "site": self.config["site"],
            "root": root,
            "nav": nav,
            "years": year_span(min(years), max(years)),
            "first_year": min(years),
        }

    # -- rendering --

    def render(self, template: str, target: str, **context) -> None:
        page = self.env.get_template(template).render(**context)
        path = self.output / target
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page, encoding="utf-8")

    def build(self) -> None:
        self.load()
        newest = self.listed[0]
        counts = {s: sum(p.status == s for p in self.listed) for s in STATUSES}

        self.render(
            "home.html", "index.html",
            **self.common("./", "home"),
            slips=self.desk(), drawers=self.drawers, listed=self.listed,
            newest=newest, counts=counts,
        )
        self.render(
            "archive.html", "archive.html",
            **self.common("./", "notes"), listed=self.listed, counts=counts,
        )
        self.render("contact.html", "contact.html", **self.common("./", "contact"))

        for post in self.posts:
            older, newer = post.drawer.neighbours(post) if post.drawer else (None, None)
            self.render(
                "post.html", post.url,
                **self.common("../", "notes"),
                post=post, body=finish_body(post.body, "../"),
                older=older, newer=newer, newest=newest,
            )
        logger.info(
            "Built %d notes (%d listed in %d drawers) into %s",
            len(self.posts), len(self.listed), len(self.drawers), self.output,
        )


def main() -> None:
    try:
        Site().build()
    except BuildError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
