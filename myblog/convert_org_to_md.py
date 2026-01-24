#!/usr/bin/env python3
"""
Convert .org files to .md (Markdown) format while preserving YAML frontmatter.

This script:
1. Reads all .org files from myblog/posts/
2. Preserves YAML frontmatter exactly as-is
3. Converts Org content to Markdown using Pandoc
4. Writes new .md files alongside originals
"""

import os
import subprocess
from glob import glob
from pathlib import Path


def convert_org_to_md():
    """Convert all .org files in posts/ directory to .md format."""

    # Ensure we're in the myblog directory
    if os.getcwd().split("/")[-1] != "myblog":
        print("❌ Error: Please run this script from the 'myblog' directory")
        print(f"   Current directory: {os.getcwd()}")
        return

    # Find all .org files
    org_files = sorted(glob("posts/*.org"))

    if not org_files:
        print("❌ No .org files found in posts/ directory")
        return

    print(f"Found {len(org_files)} .org files to convert\n")

    converted = 0
    failed = 0

    for org_file in org_files:
        try:
            # Read original file
            with open(org_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split frontmatter and body
            # Format: ---\nfrontmatter\n---\nbody
            parts = content.split('---', 2)

            if len(parts) != 3:
                print(f"⚠️  Warning: {org_file} - Invalid frontmatter format, skipping")
                failed += 1
                continue

            frontmatter = parts[1]
            org_body = parts[2]

            # Convert body with Pandoc (org -> markdown)
            result = subprocess.run(
                ['pandoc', '-f', 'org', '-t', 'markdown'],
                input=org_body,
                capture_output=True,
                text=True,
                check=True
            )

            md_body = result.stdout

            # Construct new .md file path
            md_file = org_file.replace('.org', '.md')

            # Write new .md file
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(frontmatter)
                f.write('---\n')
                f.write(md_body)

            # Get just the filename for cleaner output
            filename = os.path.basename(org_file)
            print(f"✓ Converted: {filename}")
            converted += 1

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed: {org_file} - Pandoc error")
            print(f"   stderr: {e.stderr}")
            failed += 1
        except Exception as e:
            print(f"❌ Failed: {org_file} - {str(e)}")
            failed += 1

    # Summary
    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"  ✓ Converted: {converted}")
    if failed:
        print(f"  ❌ Failed: {failed}")
    print(f"{'='*50}")

    if converted > 0:
        print("\n📝 Next steps:")
        print("  1. Manually verify 3-5 sample .md files")
        print("  2. Check that headings, links, and lists converted properly")
        print("  3. Once verified, you can delete .org files or keep as backup")


if __name__ == '__main__':
    convert_org_to_md()
