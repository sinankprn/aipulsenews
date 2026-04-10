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


def extract_og_image(html: str) -> str:
    """Extract Open Graph image URL from HTML."""
    patterns = [
        r'<meta\s+property=["\']og:image["\']\s+content=["\'](https?://[^"\']+)["\']',
        r'<meta\s+content=["\'](https?://[^"\']+)["\']\s+property=["\']og:image["\']',
        r'<meta\s+name=["\']twitter:image["\']\s+content=["\'](https?://[^"\']+)["\']',
        r'<meta\s+content=["\'](https?://[^"\']+)["\']\s+name=["\']twitter:image["\']',
    ]
    for pattern in patterns:
        match = re.search(pattern, html, re.IGNORECASE)
        if match:
            return match.group(1)
    return ""


def download_image(url: str, slug: str) -> str:
    """Download an image from URL and save locally. Returns relative path or empty string."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15, stream=True)
        resp.raise_for_status()

        content_type = resp.headers.get("Content-Type", "")
        if "jpeg" in content_type or "jpg" in content_type:
            ext = "jpg"
        elif "png" in content_type:
            ext = "png"
        elif "webp" in content_type:
            ext = "webp"
        elif url.lower().endswith((".jpg", ".jpeg")):
            ext = "jpg"
        elif url.lower().endswith(".png"):
            ext = "png"
        elif url.lower().endswith(".webp"):
            ext = "webp"
        else:
            ext = "jpg"

        images_dir = Path(__file__).parent.parent / "assets" / "images" / "posts"
        images_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{slug}.{ext}"
        filepath = images_dir / filename

        with open(filepath, "wb") as f:
            for chunk in resp.iter_content(8192):
                f.write(chunk)

        # Verify it's a valid image and reasonable size
        if filepath.stat().st_size < 5000:
            filepath.unlink()
            return ""

        print(f"    Downloaded source image: {filename}")
        return f"/assets/images/posts/{filename}"
    except Exception as e:
        print(f"    Could not download image: {e}")
        return ""


def fetch_all_sources(sources: list[str]) -> tuple[str, str]:
    """Fetch HTML from all source URLs. Returns (combined_html, best_image_url)."""
    parts = []
    best_image = ""
    for url in sources[:3]:  # Limit to 3 sources
        print(f"    Fetching source: {url[:80]}...")
        html = fetch_source_html(url)
        if html:
            parts.append(f"--- SOURCE: {url} ---\n{html}\n--- END SOURCE ---")
            if not best_image:
                img = extract_og_image(html)
                if img:
                    best_image = img
    return "\n\n".join(parts), best_image


def generate_article(topic: dict) -> tuple[str, str]:
    """Generate an article using Gemini. Returns (article_text, source_image_url)."""

    # Fetch actual source content and try to grab an OG image
    print("    Fetching source articles...")
    source_html, source_image = fetch_all_sources(topic["sources"])

    source_section = ""
    if source_html:
        source_section = f"""
FULL SOURCE CONTENT (raw HTML from the source articles, extract the relevant information):
{source_html}
"""

    prompt = f"""You are an AI journalist writing a news article for "AI Pulse", an automated AI news research site.

Your job: synthesize the source material below into a clear, accurate, well-structured article. Stick closely to what the sources actually say. Do not invent quotes, statistics, or claims not present in the sources.

HEADLINE: {topic['headline']}

SOURCES:
{chr(10).join(f"- {s}" for s in topic['sources'])}

ANGLE: {topic['angle']}

NOTES:
{topic['notes']}
{source_section}
WRITING RULES:
1. Factual and precise. Every claim must trace back to the source material. If the sources disagree, note the disagreement.
2. No filler. No "In today's rapidly evolving AI landscape..." or similar padding. Start with the news.
3. Structure: open with the key development (who, what, when), then context/background, then analysis of why it matters, then what to watch next.
4. Use ## subheadings to break the article into 3-4 clear sections.
5. Keep it between 600-900 words.
6. Explain technical terms when they first appear, but don't over-simplify for experts.
7. Do NOT repeat the headline in the body.
8. Do not use emdashes, use commas instead.
9. Where the source material supports it, include specific numbers, dates, model names, or version numbers rather than vague references.
10. End with a short "## What to Watch" section (2-3 sentences on next steps or open questions).
11. After the article, add a "## Frequently Asked Questions" section with exactly 3 Q&A pairs. Base answers strictly on source material. Format:
    **Q: Question here?**
    A: Answer here.

Write the article:"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text, source_image


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
        "author": "AI Pulse Staff",
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
            article, source_image_url = generate_article(topic)

            # Try to download source image if no image already set
            slug = slugify(topic["headline"])
            if source_image_url and not topic.get("image"):
                downloaded = download_image(source_image_url, slug)
                if downloaded:
                    topic["image"] = downloaded

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
