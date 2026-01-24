# Migration Guide: Modernized Site Generator

## What's Been Done

✅ **Created conversion script** (`myblog/convert_org_to_md.py`)
✅ **Added dependency management** (`pyproject.toml`)
✅ **Added configuration** (`myblog/config.toml`)
✅ **Converted templates to Jinja2** (all templates in `myblog/templates/`)
✅ **Refactored sitegen.py** with modern features:
  - YAML frontmatter parsing
  - Jinja2 templating
  - Proper error handling
  - Incremental builds
  - Logging instead of print statements
  - Configuration from config.toml
  - No more destructive builds!

## What You Need To Do

### Step 1: Install Pandoc

Pandoc is required for converting Markdown to HTML:

```bash
sudo apt install pandoc
```

Or download from: https://pandoc.org/installing.html

### Step 2: Install Python Dependencies

```bash
# From repository root
pip install -e .

# Or install individually
pip install jinja2 pyyaml tomli watchdog
```

### Step 3: Convert Posts from .org to .md

```bash
cd myblog
python3 convert_org_to_md.py
```

This will:
- Convert all .org files to .md format
- Preserve YAML frontmatter exactly
- Use Pandoc to convert Org content to Markdown
- Create .md files alongside .org files

After conversion:
1. Check 3-5 sample .md files to verify conversion quality
2. Compare with original .org files
3. Once satisfied, you can delete the .org files (or keep as backup)

### Step 4: Build the Site

```bash
cd myblog
python3 sitegen.py
```

The new build system will:
- Process all .md files in `myblog/posts/`
- Generate HTML in `posts/` (root level)
- Create `archive.html` with all posts
- Track file changes for incremental builds
- Only rebuild changed posts on subsequent runs

### Step 5: Test Locally

```bash
# From repository root
python3 -m http.server 8000
```

Visit `http://localhost:8000` and verify:
- Homepage works
- Archive page lists all posts
- Individual posts display correctly
- Navigation works
- Styling is preserved

## New Features

### Incremental Builds

The new system tracks file changes and only rebuilds modified posts:

```bash
cd myblog
python3 sitegen.py  # First run: builds all posts
# Edit one .md file
python3 sitegen.py  # Second run: only rebuilds changed post
```

Build cache is stored in `myblog/.build_cache` - delete this file to force full rebuild.

### Better Error Messages

The new system provides clear, helpful error messages:

```
ERROR: posts/example.md: Missing required fields: title, created
ERROR: posts/broken.md: YAML parsing error: mapping values are not allowed here
WARNING: No .md files found in posts/
```

### Configuration

Site settings are now in `myblog/config.toml`. You can customize:
- Site title and metadata
- File paths
- Required frontmatter fields
- Temporary file names
- Build options (incremental builds, etc.)

## Troubleshooting

### "No module named 'yaml'"
```bash
pip install pyyaml
```

### "No module named 'jinja2'"
```bash
pip install jinja2
```

### "pandoc: command not found"
```bash
sudo apt install pandoc
```

### "Please run this script from the 'myblog' directory"
```bash
cd myblog
python3 sitegen.py
```

### Force full rebuild
```bash
cd myblog
rm .build_cache
python3 sitegen.py
```

## Key Improvements

**Before:**
- 143 lines of fragile string manipulation
- Destructive builds (deleted entire posts/ directory)
- No error handling
- Crashed on missing metadata
- Rebuilt everything every time
- Hardcoded paths and settings

**After:**
- ~435 lines of clean, documented code
- Safe incremental builds
- Comprehensive error handling
- Validates metadata with helpful messages
- Only rebuilds changed files
- Configurable via config.toml
- Proper logging
- Type hints
- Class-based architecture

## Next Steps (Optional)

If you want to further improve the system, consider:

1. **Add watch mode** - auto-rebuild on file changes
2. **Add live reload** - auto-refresh browser
3. **Migrate to Nikola** - full-featured static site generator with Org-mode support
4. **Add RSS feed generation**
5. **Add tag/category support**
6. **Improve CSS** - responsive design, dark mode, etc.

## Rollback (if needed)

If you need to rollback to the old system:

```bash
git checkout HEAD -- myblog/sitegen.py myblog/templates/
```

The old .org files will still be in `myblog/posts/` so you can use the original system.
