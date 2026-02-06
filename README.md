# simpleblob.github.io

Personal website and blog hosted on GitHub Pages.

## Domain Redirects
- `simpleblob.com`
- `rarelyrandom.com`
- `simpleblob.github.io`

## Overview

Static site generator for personal blog. Posts are written in Markdown with YAML frontmatter and converted to HTML using Pandoc and Jinja2 templates.

## Quick Start

### Requirements
- Python 3.8+
- [Pandoc](https://pandoc.org/installing.html) (for Markdown conversion)
- [uv](https://github.com/astral-sh/uv) (Python package manager)

### Writing Posts

1. Create a new `.md` file in `myblog/posts/`
2. Add YAML frontmatter with required fields:

```markdown
---
title: Your Post Title
created: 2024-01-15
published: 2024-01-15
---

Your content here...
```

**Required frontmatter fields:**
- `title`: Post title
- `created`: Creation date (YYYY-MM-DD)
- `published`: Publication date (YYYY-MM-DD)

**Optional fields:**
- `subtitle`, `description`, `tags`, `status`, `confidence`, `importance`

### Building the Site

Generate HTML from Markdown posts:

```bash
uv run python myblog/sitegen.py
```

No installation needed! The `uv run` command automatically manages dependencies from `pyproject.toml`.

The command can be run from any directory in the repository. It will:
- Convert changed `.md` files to HTML (incremental builds)
- Generate individual post pages in `posts/`
- Update the archive page at `archive.html`

### Local Development

Preview the site locally:

```bash
uv run python -m http.server 8000 --bind localhost
```

Then visit `http://localhost:8000` in your browser.

## Project Structure

```
.
├── myblog/
│   ├── posts/           # Source Markdown files (edit these)
│   ├── templates/       # Jinja2 HTML templates
│   ├── sitegen.py       # Build script
│   └── config.toml      # Site configuration
├── posts/               # Generated HTML files (output)
├── css/                 # Stylesheets
├── assets/              # Static assets
└── *.html               # Root-level pages (index, contact, etc.)
```

## Development Notes

- **Always edit** source files in `myblog/posts/*.md`, never the generated `posts/*.html`
- Incremental builds only regenerate changed posts (cache stored in `myblog/.build_cache`)
- Delete `.build_cache` to force a full rebuild
- Generated HTML files are git-tracked (deployed directly to GitHub Pages)
- Dependencies are automatically managed by `uv` - no separate install step needed

## Configuration

Site settings are in `myblog/config.toml`. Key configurations:
- Template paths and names
- Output directories
- Required frontmatter fields
- Build options (incremental builds, temp file names)
