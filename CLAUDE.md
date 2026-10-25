# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a static personal website/blog hosted on GitHub Pages. Notes are written in Markdown (`.md` files) and converted to HTML by `myblog/sitegen.py`, which uses Pandoc for conversion and Jinja2 for templating. The design is "Marginalia": a scholarly-library notebook with a card catalogue, margin notes and light/dark themes.

## Architecture

### Content Pipeline

1. **Source notes**: `myblog/posts/*.md`, each with YAML frontmatter between `---` delimiters:
   - Required: `title`, `created`, `published` (YYYY-MM-DD)
   - `topic`: the catalogue drawer slug (`bk`, `mm`, `mf`, `mh`, `bd`, `ta`; defined under `[[topics]]` in `myblog/config.toml`). Required unless `unlisted: true`.
   - `unlisted: true`: the page is built but kept out of every list (test posts).
   - Optional: `subtitle`, `tags` (comma-separated), `status` (`draft` | `ongoing` | `finished`, default draft). The literal value `None` means empty. `description`, `confidence` and `importance` are ignored.
   - Titles like `Book Summary - X by Author` are split into a form label, title and author for display.
   - Footnotes (`[^1]`) render as sidenotes in the right margin (`myblog/sidenotes.lua`).
   - Notes that use `#` headings are shifted down one level so the note title stays the only h1.

2. **Site generator** (`myblog/sitegen.py`) renders every page on each run:
   - `index.html`: preface, reading desk (ongoing notes + the newest note), and the card catalogue grouped by topic
   - `archive.html`: every listed note by date
   - `contact.html`
   - `posts/<slug>.html`: one page per note, with metadata margin, contents, and older/newer cards within its drawer
   - Pandoc output is cached by content hash in `myblog/.pandoc_cache/` (git-ignored; delete it to force Pandoc to re-run).

3. **Templates** (`myblog/templates/`): `base.html` (head, masthead, footer), `home.html`, `archive.html`, `contact.html`, `post.html`, `_macros.html`. The `root` variable (`./` or `../`) keeps all links relative.

### Directory Structure

- Root: generated `index.html`, `archive.html`, `contact.html`; `experiments.html` is a redirect stub for the closed Labs page
- `myblog/`: generator, config, templates, Pandoc filter, source notes
- `posts/`: generated note pages (git-tracked; GitHub Pages serves them as-is)
- `css/site.css`, `js/theme.js` (light/dark toggle), `assets/`
- `tests/test_sitegen.py`

## Commands

```bash
python3 myblog/sitegen.py          # build (or: uv run python myblog/sitegen.py)
python3 -m pytest -q tests         # tests
python3 -m http.server 8000 --bind localhost   # preview at http://localhost:8000
```

Requirements: Python 3.12+, Pandoc on PATH, `jinja2`, `pyyaml` (see `pyproject.toml`).

## Important Notes

- **Always edit** content in `myblog/posts/*.md`, never the generated HTML
- New notes need a `topic:` or the build stops with an error naming the file
- Generated pages are git-tracked: rebuild and commit them together with source changes
