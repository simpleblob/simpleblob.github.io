"""Tests for myblog/sitegen.py. Run: python3 -m pytest tests"""

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "myblog"))

import sitegen  # noqa: E402
from sitegen import BuildError, Site, count_words, number_words, pandoc_html, parse_post  # noqa: E402

REQUIRED = ["title", "created", "published"]


def note(tmp_path, front: str, body: str = "Body text.\n") -> Path:
    path = tmp_path / "n.md"
    path.write_text(f"---\n{front}\n---\n{body}", encoding="utf-8")
    return path


def test_book_summary_title_splits_into_form_heading_and_author(tmp_path):
    post = parse_post(note(tmp_path, "title: Book Summary - Deep Work by Cal Newport\n"
                                     "created: 2016-07-13\npublished: 2016-07-14\ntopic: bk"), REQUIRED)
    assert (post.form, post.title, post.heading, post.author) == (
        "Book Summary", "Deep Work by Cal Newport", "Deep Work", "Cal Newport")


def test_placeholder_none_values_are_empty_and_titles_get_a_capital(tmp_path):
    post = parse_post(note(tmp_path, "title: food and diet\nsubtitle: None\ntags: food, diet\n"
                                     "created: 2018-12-18\npublished: 2018-12-18\ntopic: bd"), REQUIRED)
    assert post.title == "Food and diet"
    assert post.subtitle == ""
    assert post.tags == ["food", "diet"]
    assert post.status == "draft"


def test_listed_note_without_topic_is_an_error(tmp_path):
    with pytest.raises(BuildError, match="topic"):
        parse_post(note(tmp_path, "title: x\ncreated: 2020-01-01\npublished: 2020-01-01"), REQUIRED)


def test_unknown_status_is_an_error(tmp_path):
    with pytest.raises(BuildError, match="status"):
        parse_post(note(tmp_path, "title: x\ncreated: 2020-01-01\npublished: 2020-01-01\n"
                                  "status: done\ntopic: bk"), REQUIRED)


def test_word_count_ignores_link_targets():
    assert count_words("See [the docs](https://example.com/a/very/long/path) now.") == 4


def test_number_words():
    assert [number_words(n) for n in (2, 6, 30, 21)] == ["two", "six", "thirty", "twenty-one"]


def test_footnotes_become_sidenotes():
    out = pandoc_html("Text[^1] here.\n\n[^1]: The note.\n", cache_dir=None)
    assert '<span class="sidenote" role="note">The note.</span>' in out
    assert "footnotes" not in out


def test_top_level_headings_shift_below_the_page_title():
    out = pandoc_html("# Part\n\ntext\n", cache_dir=None)
    assert "<h2" in out and "<h1" not in out


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    out = tmp_path_factory.mktemp("site")
    site = Site(output=out)
    site.build()
    return site, out


def test_every_note_gets_a_page(built):
    site, out = built
    sources = sorted(p.stem for p in (ROOT / "myblog" / "posts").glob("*.md"))
    assert sorted(p.stem for p in (out / "posts").glob("*.html")) == sources


def test_home_lists_every_listed_note_once_and_hides_unlisted(built):
    site, out = built
    home = (out / "index.html").read_text(encoding="utf-8")
    for post in site.listed:
        assert home.count(f'<li class="card') and f'href="./{post.url}"' in home
    assert 'href="./posts/test_post.html"' not in home
    assert 'href="./posts/example_post.html"' not in home
    assert len(re.findall(r'<li class="card', home)) == len(site.listed)


def test_archive_lists_every_listed_note(built):
    site, out = built
    archive = (out / "archive.html").read_text(encoding="utf-8")
    assert len(re.findall(r'<li class="card', archive)) == len(site.listed)


def test_no_placeholder_text_leaks_into_pages(built):
    _, out = built
    for page in [out / "index.html", out / "archive.html", *sorted((out / "posts").glob("*.html"))]:
        text = page.read_text(encoding="utf-8")
        assert not re.search(r">\s*None\s*<|· None|None ·", text), page.name


def test_note_pages_use_relative_paths(built):
    _, out = built
    ere = (out / "posts" / "book_summary--early-retirement-extreme.html").read_text(encoding="utf-8")
    assert 'src="../assets/diagrams/four-types-matrix.svg"' in ere
    assert 'href="../css/site.css"' in ere
    assert 'src="/' not in ere and 'href="/' not in ere.replace('href="//', "")


def test_math_loads_mathjax_only_where_needed(built):
    _, out = built
    org = (out / "posts" / "org-mode-in-hakyll.html").read_text(encoding="utf-8")
    ere = (out / "posts" / "book_summary--early-retirement-extreme.html").read_text(encoding="utf-8")
    assert "mathjax" in org and "mathjax" not in ere
