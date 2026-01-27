#!/usr/bin/env python3
"""
Modern static site generator for personal blog.

Reads Markdown posts with YAML frontmatter, converts to HTML using Pandoc,
and applies Jinja2 templates. Supports incremental builds.
"""

import os
import sys
import logging
import subprocess
from glob import glob
from pathlib import Path
from os.path import basename, splitext, join, getmtime
from typing import Dict, List, Tuple, Any
import hashlib

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Install with: pip install pyyaml")
    sys.exit(1)

try:
    from jinja2 import Environment, FileSystemLoader, Template
except ImportError:
    print("Error: Jinja2 not installed. Install with: pip install jinja2")
    sys.exit(1)

try:
    if sys.version_info >= (3, 11):
        import tomllib
    else:
        import tomli as tomllib
except ImportError:
    print("Error: tomli not installed. Install with: pip install tomli")
    sys.exit(1)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class Config:
    """Load and store configuration from config.toml."""

    def __init__(self, config_path: str = "config.toml"):
        try:
            with open(config_path, 'rb') as f:
                self.data = tomllib.load(f)
        except FileNotFoundError:
            logger.error(f"Configuration file '{config_path}' not found")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            sys.exit(1)

    def get(self, *keys, default=None):
        """Get nested config value, e.g., config.get('site', 'title')"""
        value = self.data
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return default
            if value is None:
                return default
        return value


class Post:
    """Represents a blog post with metadata and content."""

    def __init__(self, filepath: str, config: Config):
        self.filepath = filepath
        self.config = config
        self.metadata: Dict[str, Any] = {}
        self.content: str = ""
        self.html_content: str = ""

    def parse(self) -> bool:
        """Parse post file and extract metadata and content."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split frontmatter and body
            if not content.startswith('---'):
                logger.error(f"{self.filepath}: Missing frontmatter")
                return False

            parts = content.split('---', 2)
            if len(parts) < 3:
                logger.error(f"{self.filepath}: Invalid frontmatter format")
                return False

            # Parse YAML frontmatter
            try:
                self.metadata = yaml.safe_load(parts[1])
                if not isinstance(self.metadata, dict):
                    logger.error(f"{self.filepath}: Frontmatter must be a dictionary")
                    return False
            except yaml.YAMLError as e:
                logger.error(f"{self.filepath}: YAML parsing error: {e}")
                return False

            self.content = parts[2]

            # Validate required fields
            required = self.config.get('post', 'required_fields', default=['title', 'created', 'published'])
            missing = [field for field in required if field not in self.metadata]
            if missing:
                logger.error(f"{self.filepath}: Missing required fields: {', '.join(missing)}")
                return False

            return True

        except Exception as e:
            logger.error(f"{self.filepath}: Error reading file: {e}")
            return False

    def convert_to_html(self, temp_source: str, temp_output: str) -> bool:
        """Convert Markdown content to HTML using Pandoc."""
        try:
            # Write content to temporary file
            with open(temp_source, 'w', encoding='utf-8') as f:
                f.write(self.content)

            # Run Pandoc conversion
            result = subprocess.run(
                ['pandoc', '-f', 'markdown', '-t', 'html', '-o', temp_output, temp_source],
                capture_output=True,
                text=True,
                check=True
            )

            # Read converted HTML
            with open(temp_output, 'r', encoding='utf-8') as f:
                self.html_content = f.read()

            return True

        except subprocess.CalledProcessError as e:
            logger.error(f"{self.filepath}: Pandoc conversion failed")
            if e.stderr:
                logger.error(f"  {e.stderr}")
            return False
        except Exception as e:
            logger.error(f"{self.filepath}: Error during conversion: {e}")
            return False

    @property
    def output_filename(self) -> str:
        """Get the output HTML filename for this post."""
        return splitext(basename(self.filepath))[0] + ".html"


class SiteGenerator:
    """Main site generator class."""

    def __init__(self):
        # Verify we're in the myblog directory
        if os.getcwd().split("/")[-1] != "myblog":
            logger.error("Please run this script from the 'myblog' directory!")
            logger.error(f"Current directory: {os.getcwd()}")
            sys.exit(1)

        # Load configuration
        self.config = Config()

        # Setup Jinja2 environment
        template_dir = self.config.get('paths', 'templates', default='templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_dir))

        # Cache for tracking file changes (for incremental builds)
        self.cache_file = ".build_cache"
        self.file_hashes: Dict[str, str] = {}
        self._load_cache()

    def _load_cache(self):
        """Load build cache to track file changes."""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    for line in f:
                        if ':' in line:
                            filepath, filehash = line.strip().split(':', 1)
                            self.file_hashes[filepath] = filehash
            except Exception as e:
                logger.warning(f"Could not load build cache: {e}")

    def _save_cache(self):
        """Save build cache."""
        try:
            with open(self.cache_file, 'w') as f:
                for filepath, filehash in sorted(self.file_hashes.items()):
                    f.write(f"{filepath}:{filehash}\n")
        except Exception as e:
            logger.warning(f"Could not save build cache: {e}")

    def _get_file_hash(self, filepath: str) -> str:
        """Get hash of file contents for change detection."""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception:
            return ""

    def _has_file_changed(self, filepath: str) -> bool:
        """Check if file has changed since last build."""
        current_hash = self._get_file_hash(filepath)
        previous_hash = self.file_hashes.get(filepath, "")
        return current_hash != previous_hash

    def _update_file_hash(self, filepath: str):
        """Update hash for a file."""
        self.file_hashes[filepath] = self._get_file_hash(filepath)

    def generate_posts(self) -> Tuple[List[str], List[str], List[str]]:
        """Generate HTML for all posts."""
        logger.info("Generating posts...")

        # Get post source directory
        posts_dir = self.config.get('paths', 'posts_source', default='posts')
        posts_md = sorted(glob(f"{posts_dir}/*.md"))

        if not posts_md:
            logger.warning(f"No .md files found in {posts_dir}/")
            return [], [], []

        # Get output directory and ensure it exists
        output_dir = self.config.get('paths', 'posts_output', default='../posts')
        os.makedirs(output_dir, exist_ok=True)

        # Load templates
        template_default_name = self.config.get('paths', 'template_default', default='default.html')
        template_post_name = self.config.get('paths', 'template_post', default='post.html')

        try:
            template_default = self.jinja_env.get_template(template_default_name)
            template_post = self.jinja_env.get_template(template_post_name)
        except Exception as e:
            logger.error(f"Error loading templates: {e}")
            sys.exit(1)

        # Temporary files for conversion
        temp_source = self.config.get('build', 'temp_source', default='tmp.md')
        temp_output = self.config.get('build', 'temp_output', default='tmp.html')

        # Check if incremental builds are enabled
        incremental = self.config.get('build', 'incremental', default=True)

        posts_name = []
        posts_published = []
        posts_title = []

        processed = 0
        skipped = 0
        failed = 0

        for md_file in posts_md:
            # Check if file has changed (for incremental builds)
            if incremental and not self._has_file_changed(md_file):
                # Still need to collect metadata for archive
                post = Post(md_file, self.config)
                if post.parse():
                    posts_name.append(post.output_filename)
                    posts_published.append(post.metadata['published'])
                    posts_title.append(post.metadata['title'])
                    skipped += 1
                continue

            # Parse post
            post = Post(md_file, self.config)
            if not post.parse():
                failed += 1
                continue

            # Convert to HTML
            if not post.convert_to_html(temp_source, temp_output):
                failed += 1
                continue

            # Fix relative URLs for posts (in subdirectory)
            html_content = post.html_content.replace('href="/', 'href="../')

            # Render post template
            try:
                post_body = template_post.render(
                    created=post.metadata['created'],
                    published=post.metadata['published'],
                    body=html_content
                )

                # Render full page with default template
                full_html = template_default.render(
                    title=post.metadata['title'],
                    body=post_body
                )

                # Fix relative URLs in default template
                full_html = full_html.replace('href="/', 'href="../')

            except Exception as e:
                logger.error(f"{md_file}: Template rendering error: {e}")
                failed += 1
                continue

            # Write output file
            output_path = join(output_dir, post.output_filename)
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(full_html)
                logger.info(f"  ✓ {basename(md_file)}")
                processed += 1
            except Exception as e:
                logger.error(f"{md_file}: Error writing output: {e}")
                failed += 1
                continue

            # Update cache
            self._update_file_hash(md_file)

            # Collect metadata for archive
            posts_name.append(post.output_filename)
            posts_published.append(post.metadata['published'])
            posts_title.append(post.metadata['title'])

        # Clean up temporary files
        for temp_file in [temp_source, temp_output]:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

        # Summary
        logger.info(f"Posts: {processed} generated, {skipped} unchanged, {failed} failed")

        return posts_name, posts_published, posts_title

    def generate_archive(self, posts_name: List[str], posts_published: List[str],
                        posts_title: List[str]):
        """Generate archive page with list of all posts."""
        logger.info("Generating archive...")

        # Load templates
        template_default_name = self.config.get('paths', 'template_default', default='default.html')
        template_archive_name = self.config.get('paths', 'template_archive', default='archive.html')

        try:
            template_default = self.jinja_env.get_template(template_default_name)
            template_archive = self.jinja_env.get_template(template_archive_name)
        except Exception as e:
            logger.error(f"Error loading templates: {e}")
            sys.exit(1)

        # Sort posts by publication date (descending)
        sorted_indices = sorted(
            range(len(posts_published)),
            key=lambda k: posts_published[k],
            reverse=True
        )

        # Create post list HTML
        post_list_html = "\n<ul>\n"
        for i in sorted_indices:
            pub = posts_published[i]
            name = posts_name[i]
            title = posts_title[i]
            post_list_html += (
                f"<li>\n{pub} - "
                f"<a href='./posts/{name}'>{title}</a>"
                f"</li>\n"
            )
        post_list_html += "</ul>\n"

        # Render templates
        try:
            archive_body = template_archive.render(post_list=post_list_html)
            full_html = template_default.render(
                title="Writing",
                body=archive_body
            )

            # Fix relative URLs for archive (in root)
            full_html = full_html.replace('href="/', 'href="./')

        except Exception as e:
            logger.error(f"Archive template rendering error: {e}")
            sys.exit(1)

        # Write output file
        output_path = self.config.get('paths', 'archive_output', default='../archive.html')
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            logger.info(f"  ✓ archive.html")
        except Exception as e:
            logger.error(f"Error writing archive: {e}")
            sys.exit(1)

    def build(self):
        """Run the full build process."""
        logger.info("Starting build...")

        # Generate posts
        posts_name, posts_published, posts_title = self.generate_posts()

        if not posts_name:
            logger.warning("No posts to generate")
            return

        # Generate archive
        self.generate_archive(posts_name, posts_published, posts_title)

        # Save cache
        self._save_cache()

        logger.info("Build complete!")


def main():
    """Main entry point."""
    generator = SiteGenerator()
    generator.build()


if __name__ == "__main__":
    main()
