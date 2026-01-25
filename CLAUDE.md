# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a static personal website/blog hosted on GitHub Pages. Posts are written in Markdown format (`.md` files) and converted to HTML using a custom Python script that uses Pandoc for conversion.

## Architecture

### Content Pipeline

1. **Source Posts**: All posts are written as `.org` files in `myblog/posts/`
   - Each post has YAML-like frontmatter between `---` delimiters containing metadata:
     - `title`: Post title
     - `created`: Creation date (YYYY-MM-DD)
     - `published`: Publication/update date (YYYY-MM-DD)
     - Other optional fields: `subtitle`, `description`, `tags`, `status`, `confidence`, `importance`

2. **Site Generator** (`myblog/sitegen.py`):
   - Reads `.org` files from `myblog/posts/`
   - Parses frontmatter metadata
   - Converts Org content to HTML using Pandoc (via temporary files)
   - Applies templates from `myblog/templates/`:
     - `default.html`: Base page structure with navigation
     - `post.html`: Post metadata wrapper (creation/publication dates)
     - `archive.html`: Archive page template
   - Outputs:
     - Individual post HTML files to `posts/` (root level)
     - `archive.html` (root level) with chronologically sorted post list
   - **Important**: The script deletes and recreates the `posts/` directory each run

3. **Template Variable System**:
   - Templates use `$variable$` placeholders
   - Variables: `$title$`, `$created$`, `$published$`, `$body$`, `$post-list$`
   - Relative path correction: `href="/` is replaced with `href="../` for posts, `href="./` for archive

### Directory Structure

- Root: Static HTML pages (`index.html`, `about.html`, `contact.html`, `archive.html`)
- `myblog/`: Build system and source content
  - `posts/`: Source `.org` files (not published directly)
  - `templates/`: HTML templates
  - `sitegen.py`: Build script
- `posts/`: Generated HTML post files (git-tracked, regenerated on each build)
- `css/`: Stylesheets
- `assets/`: Static assets

## Build Commands

### Generate Site from Org Files

```bash
cd myblog
python3 sitegen.py
```

**Requirements**:
- Python 3
- Pandoc (must be in PATH)
- Must run from `myblog/` directory (script checks `os.getcwd()`)

### Local Development Server

From repository root:
```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000` in a browser.

## Important Notes

- The site generator **destructively recreates** the `posts/` directory - any manual edits to generated HTML will be lost
- Always edit content in `myblog/posts/*.org`, never in the generated `posts/*.html`
- The script uses temporary files (`tmp.org`, `tmp.html`) in the `myblog/` directory during conversion
- Posts are sorted by `published` date in descending order on the archive page
