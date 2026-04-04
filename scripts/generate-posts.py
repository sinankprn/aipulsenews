#!/usr/bin/env python3
"""
Gemini-powered post generator for AI Pulse.
Reads topics from _content-queue, generates articles, saves to _posts (or _drafts).
"""

import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path

import requests
from google import genai
import yaml

# Configuration
QUEUE_DIR = Path(__file__).parent.parent / "_content-queue"
PROCESSED_DIR = QUEUE_DIR / "_processed"
POSTS_DIR = Path(__file__).parent.parent / "_posts"
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
                    "image": frontmatter.get("image", ""),
                    "notes": body,
                    "filename": filepath.name,
                }
            except yaml.YAMLError:
                print(f"Error parsing YAML in {filepath}")
                return None
    return None


HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; AI-Pulse-Bot/1.0)"
}

# Max HTML size per source (chars) to keep prompt reasonable
MAX_SOURCE_HTML = 50000


def fetch_source_html(url: str) -> str:
    """Fetch raw HTML from a source URL."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        resp.raise_for_status()
        html = resp.text[:MAX_SOURCE_HTML]
        return html
    except Exception as e:
        print(f"    Could not fetch {url}: {e}")
        return ""


def fetch_all_sources(sources: list[str]) -> str:
    """Fetch HTML from all source URLs and combine."""
    parts = []
    for url in sources[:3]:  # Limit to 3 sources to manage prompt size
        print(f"    Fetching source: {url[:80]}...")
        html = fetch_source_html(url)
        if html:
            parts.append(f"--- SOURCE: {url} ---\n{html}\n--- END SOURCE ---")
    return "\n\n".join(parts)


def generate_article(topic: dict) -> str:
    """Generate an article using Gemini."""

    # Fetch actual source content
    print("    Fetching source articles...")
    source_html = fetch_all_sources(topic["sources"])

    source_section = ""
    if source_html:
        source_section = f"""
FULL SOURCE CONTENT (raw HTML from the source articles, extract the relevant information):
{source_html}
"""

    prompt = f"""You are a professional tech journalist writing for "AI Pulse", an AI news blog by Sinan Koparan, a PhD Candidate in Sports Data Science & AI.
Write a well-researched, engaging article based on the following information.

HEADLINE: {topic['headline']}

SOURCES TO REFERENCE:
{chr(10).join(f"- {s}" for s in topic['sources'])}

ANGLE/FOCUS: {topic['angle']}

ADDITIONAL CONTEXT:
{topic['notes']}
{source_section}
REQUIREMENTS:
1. Write in a professional but accessible tone, with confident expert analysis
2. Start with a compelling hook, not "In the world of AI..." or similar cliches
3. Include relevant context and background
4. Explain technical concepts clearly for a general audience
5. Be factual and balanced, avoid hype or speculation
6. Keep it between 600-900 words
7. Use subheadings (## Heading) to break up the content
8. End with a forward-looking section about implications and what to watch for next
9. Do NOT include the headline in the body, just the article content
10. Cite sources where appropriate
11. Do not use emdashes, use commas instead
12. Naturally weave in expert perspective, e.g. "This aligns with broader trends in..." or "From a data science perspective..."
13. At the very end, add a "## Frequently Asked Questions" section with exactly 3 Q&A pairs.
    Format each as:
    **Q: Question here?**
    A: Answer here.

Write the article now:"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text


def parse_faq_from_content(content: str) -> tuple[str, list[dict]]:
    """Extract FAQ section from article content and return (clean_content, faq_list)."""
    faq_pattern = r"##\s*Frequently Asked Questions.*$"
    faq_match = re.search(faq_pattern, content, re.DOTALL | re.IGNORECASE)

    if not faq_match:
        return content, []

    clean_content = content[:faq_match.start()].rstrip()
    faq_section = faq_match.group()

    # Parse Q&A pairs
    qa_pattern = r"\*\*Q:\s*(.+?)\*\*\s*\n\s*A:\s*(.+?)(?=\n\*\*Q:|\Z)"
    matches = re.findall(qa_pattern, faq_section, re.DOTALL)

    faq_list = []
    for q, a in matches:
        faq_list.append({
            "q": q.strip().rstrip("?") + "?",
            "a": a.strip(),
        })

    return clean_content, faq_list


def generate_description(headline: str, content: str) -> str:
    """Generate an SEO-optimized description using Gemini."""
    try:
        prompt = f"""Write a compelling 140-155 character meta description for this article.
It should include the main keyword naturally and entice clicks from Google search results.
Do NOT use emdashes. Do NOT wrap in quotes. Just the description text.

Title: {headline}
First paragraph: {content[:500]}

Meta description:"""
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )
        desc = response.text.strip().strip('"').strip("'")
        if len(desc) > 160:
            desc = desc[:157] + "..."
        return desc
    except Exception:
        # Fallback to first sentence
        first_para = content.split("\n\n")[0] if content else headline
        return first_para[:157].replace("\n", " ").strip() + "..."


def create_post(topic: dict, article_content: str, output_dir: Path) -> Path:
    """Create a Jekyll post file."""

    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(topic["headline"])
    filename = f"{today}-{slug}.md"
    filepath = output_dir / filename

    # Parse FAQ from generated content
    clean_content, faq = parse_faq_from_content(article_content)

    # Generate SEO description
    description = generate_description(topic["headline"], clean_content)

    # Build frontmatter
    frontmatter = {
        "layout": "post",
        "title": topic["headline"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S %z").strip(),
        "author": "Sinan Koparan",
        "tags": topic["tags"],
        "sources": topic["sources"],
        "description": description,
        "toc": True,
    }

    # Add image if available
    if topic.get("image"):
        frontmatter["image"] = topic["image"]

    # Add FAQ if parsed
    if faq:
        frontmatter["faq"] = faq

    # Write post
    post_content = "---\n"
    post_content += yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
    post_content += "---\n\n"
    post_content += clean_content

    filepath.write_text(post_content, encoding="utf-8")
    return filepath


def process_queue(drafts_only: bool = False):
    """Process all files in the content queue."""

    output_dir = DRAFTS_DIR if drafts_only else POSTS_DIR
    output_label = "_drafts" if drafts_only else "_posts"

    # Ensure directories exist
    output_dir.mkdir(exist_ok=True)
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
    print(f"Output directory: {output_label}/")

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
            post_path = create_post(topic, article, output_dir)
            print(f"  Created in {output_label}: {post_path.name}")

            # Move to processed
            dest = PROCESSED_DIR / filepath.name
            shutil.move(str(filepath), str(dest))
            print(f"  Moved to processed/")

        except Exception as e:
            print(f"  Error: {e}")
            continue

    print(f"\nDone! Check {output_label}/ for generated posts.")


if __name__ == "__main__":
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Set it with: export GEMINI_API_KEY='your-api-key'")
        exit(1)

    drafts_only = "--drafts-only" in sys.argv
    process_queue(drafts_only=drafts_only)
