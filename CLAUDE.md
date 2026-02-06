# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a static personal website/blog hosted on GitHub Pages. Posts are written in Markdown format (`.md` files) and converted to HTML using a custom Python script (`myblog/sitegen.py`) that uses Pandoc for conversion and Jinja2 for templating.

## Architecture

### Content Pipeline

1. **Source Posts**: All posts are written as Markdown (`.md`) files in `myblog/posts/`
   - Each post has YAML frontmatter between `---` delimiters:
     - Required: `title`, `created`, `published` (all dates in YYYY-MM-DD format)
     - Optional: `subtitle`, `description`, `tags`, `status`, `confidence`, `importance`

2. **Site Generator** (`myblog/sitegen.py`):
   - Reads `.md` files from `myblog/posts/`
   - Parses YAML frontmatter using PyYAML
   - Converts Markdown content to HTML using Pandoc
   - Applies Jinja2 templates from `myblog/templates/`:
     - `default.html`: Base page structure with navigation
     - `post.html`: Post metadata wrapper (creation/publication dates)
     - `archive.html`: Archive page template
   - Outputs:
     - Individual post HTML files to `posts/` (root level)
     - `archive.html` (root level) with chronologically sorted post list
   - **Incremental builds**: Only rebuilds changed posts (uses `.build_cache` to track file hashes)
   - Configuration loaded from `myblog/config.toml`

3. **Templating System**:
   - Uses Jinja2 with standard `{{ variable }}` syntax
   - Automatic relative path correction: `href="/` → `href="../` for posts, `href="./` for archive
   - Templates receive: `title`, `created`, `published`, `body`, `post_list`

### Directory Structure

- Root: Static HTML pages (`index.html`, `contact.html`, `experiments.html`, `archive.html`)
- `myblog/`: Build system and source content
  - `posts/`: Source `.md` files (not published directly)
  - `templates/`: Jinja2 HTML templates
  - `sitegen.py`: Build script
  - `config.toml`: Site configuration
- `posts/`: Generated HTML post files (git-tracked, output directory for posts)
- `css/`: Stylesheets
- `assets/`: Static assets

## Build Commands

### Generate Site from Markdown Files

```bash
uv run python myblog/sitegen.py
```

Can be run from any directory in the repository. No installation required - `uv` automatically manages dependencies from `pyproject.toml`.

**Requirements**:
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Pandoc (must be in PATH)

**Dependencies** (automatically handled by uv):
- `jinja2`, `pyyaml`, `watchdog`, `tomli` (for Python < 3.11)

### Local Development Server

From repository root:
```bash
uv run python -m http.server 8000 --bind localhost
```

Then visit `http://localhost:8000` in a browser.

## Important Notes

- **Always edit** content in `myblog/posts/*.md`, never in the generated `posts/*.html`
- Incremental builds are enabled by default - only changed posts are regenerated
- The script uses temporary files (`tmp.md`, `tmp.html`) in `myblog/` during conversion
- Posts are sorted by `published` date (descending) on the archive page
- Build cache is stored in `myblog/.build_cache` - delete to force full rebuild
- Generated `posts/*.html` files are git-tracked (not regenerated on GitHub Pages)
