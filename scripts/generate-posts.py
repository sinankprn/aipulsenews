#!/usr/bin/env python3
"""
Gemini-powered post generator for AI Pulse.
Reads topics from _content-queue, generates articles, saves to _drafts.
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path

from google import genai
import yaml

# Configuration
QUEUE_DIR = Path(__file__).parent.parent / "_content-queue"
PROCESSED_DIR = QUEUE_DIR / "_processed"
DRAFTS_DIR = Path(__file__).parent.parent / "_drafts"

# Gemini setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:50]


def parse_queue_file(filepath: Path) -> dict | None:
    """Parse a markdown file from the content queue."""
    content = filepath.read_text(encoding="utf-8")

    # Split frontmatter and body
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return {
                    "headline": frontmatter.get("headline", ""),
                    "sources": frontmatter.get("sources", []),
                    "angle": frontmatter.get("angle", ""),
                    "tags": frontmatter.get("tags", ["AI"]),
                    "notes": body,
                    "filename": filepath.name,
                }
            except yaml.YAMLError:
                print(f"Error parsing YAML in {filepath}")
                return None
    return None


def generate_article(topic: dict) -> str:
    """Generate an article using Gemini."""

    prompt = f"""You are a professional tech journalist writing for an AI news blog called "AI Pulse".
Write a well-researched, engaging article based on the following information.

HEADLINE: {topic['headline']}

SOURCES TO REFERENCE:
{chr(10).join(f"- {s}" for s in topic['sources'])}

ANGLE/FOCUS: {topic['angle']}

ADDITIONAL CONTEXT:
{topic['notes']}

REQUIREMENTS:
1. Write in a professional but accessible tone
2. Start with a compelling hook, not "In the world of AI..." or similar cliches
3. Include relevant context and background
4. Explain technical concepts clearly for a general audience
5. Be factual and balanced - avoid hype or speculation
6. Keep it between 500-800 words
7. Use subheadings to break up the content
8. End with implications or what to watch for next
9. Do NOT include the headline in the body - just the article content

Write the article now:"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text


def create_post(topic: dict, article_content: str) -> Path:
    """Create a Jekyll post file in _drafts."""

    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(topic["headline"])
    filename = f"{today}-{slug}.md"
    filepath = DRAFTS_DIR / filename

    # Build frontmatter
    frontmatter = {
        "layout": "post",
        "title": topic["headline"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S %z").strip(),
        "author": "Sinan Koparan",
        "tags": topic["tags"],
        "sources": topic["sources"],
        "description": article_content[:160].replace("\n", " ").strip() + "...",
    }

    # Write post
    post_content = "---\n"
    post_content += yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
    post_content += "---\n\n"
    post_content += article_content

    filepath.write_text(post_content, encoding="utf-8")
    return filepath


def process_queue():
    """Process all files in the content queue."""

    # Ensure directories exist
    DRAFTS_DIR.mkdir(exist_ok=True)
    PROCESSED_DIR.mkdir(exist_ok=True)

    # Find queue files (skip template and hidden files)
    queue_files = [
        f for f in QUEUE_DIR.glob("*.md")
        if not f.name.startswith((".", "TEMPLATE", "_"))
    ]

    if not queue_files:
        print("No files in content queue.")
        return

    print(f"Found {len(queue_files)} file(s) to process.")

    for filepath in queue_files:
        print(f"\nProcessing: {filepath.name}")

        # Parse the queue file
        topic = parse_queue_file(filepath)
        if not topic or not topic["headline"]:
            print(f"  Skipping - invalid format or missing headline")
            continue

        try:
            # Generate article
            print(f"  Generating article for: {topic['headline']}")
            article = generate_article(topic)

            # Create post
            post_path = create_post(topic, article)
            print(f"  Created draft: {post_path.name}")

            # Move to processed
            dest = PROCESSED_DIR / filepath.name
            shutil.move(str(filepath), str(dest))
            print(f"  Moved to processed/")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    print("\nDone! Check _drafts/ for generated posts.")


if __name__ == "__main__":
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Set it with: export GEMINI_API_KEY='your-api-key'")
        exit(1)

    process_queue()
