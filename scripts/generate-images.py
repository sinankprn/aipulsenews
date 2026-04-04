#!/usr/bin/env python3
"""
Branded placeholder image generator for AI Pulse.
Creates gradient PNG cards with article titles for posts missing images.
"""

import re
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import yaml

# Configuration
POSTS_DIR = Path(__file__).parent.parent / "_posts"
QUEUE_DIR = Path(__file__).parent.parent / "_content-queue"
IMAGES_DIR = Path(__file__).parent.parent / "assets" / "images" / "posts"

# Image dimensions (optimal for social sharing)
WIDTH = 1200
HEIGHT = 630

# Brand colors
COLOR_START = (99, 102, 241)    # #6366f1 indigo
COLOR_END = (168, 85, 247)      # #a855f7 purple
COLOR_ACCENT = (34, 211, 238)   # #22d3ee cyan


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:50]


def interpolate_color(c1: tuple, c2: tuple, t: float) -> tuple:
    """Linear interpolation between two RGB colors."""
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def create_gradient(width: int, height: int) -> Image.Image:
    """Create a diagonal gradient background."""
    img = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            # Diagonal gradient
            t = (x / width * 0.6 + y / height * 0.4)
            t = max(0, min(1, t))
            color = interpolate_color(COLOR_START, COLOR_END, t)
            img.putpixel((x, y), color)
    return img


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Get a font, falling back to default if needed."""
    font_names = [
        "arial.ttf", "Arial.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
        "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf",
    ]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def generate_image(title: str, output_path: Path) -> bool:
    """Generate a branded placeholder image for an article."""
    # Create gradient background
    img = create_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)

    # Add accent line at top
    draw.rectangle([(0, 0), (WIDTH, 4)], fill=COLOR_ACCENT)

    # Draw "AI PULSE" brand centered at top
    brand_font = get_font(22, bold=True)
    brand_text = "AI PULSE"
    brand_bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    brand_w = brand_bbox[2] - brand_bbox[0]
    draw.text(((WIDTH - brand_w) // 2, 36), brand_text, fill=(255, 255, 255, 220), font=brand_font)

    # Draw accent line under brand
    accent_w = 40
    draw.rectangle([
        ((WIDTH - accent_w) // 2, 68),
        ((WIDTH + accent_w) // 2, 72)
    ], fill=COLOR_ACCENT)

    # Wrap and draw title centered
    title_font = get_font(46, bold=True)
    wrapped = textwrap.fill(title, width=28)
    lines = wrapped.split("\n")[:4]  # Max 4 lines

    line_height = 60
    total_text_height = len(lines) * line_height
    y_start = (HEIGHT - total_text_height) // 2 + 10

    for i, line in enumerate(lines):
        y = y_start + i * line_height
        line_bbox = draw.textbbox((0, 0), line, font=title_font)
        line_w = line_bbox[2] - line_bbox[0]
        draw.text(((WIDTH - line_w) // 2, y), line, fill=(255, 255, 255), font=title_font)

    # Draw site URL centered at bottom
    from datetime import datetime
    url_font = get_font(16)
    url_text = "artificialintelligencepulse.it.com"
    url_bbox = draw.textbbox((0, 0), url_text, font=url_font)
    url_w = url_bbox[2] - url_bbox[0]
    draw.text(((WIDTH - url_w) // 2, HEIGHT - 44), url_text, fill=(255, 255, 255, 150), font=url_font)

    # Save
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG", quality=95)
    return True


def get_posts_missing_images() -> list[dict]:
    """Find posts and queue files that need images generated."""
    missing = []

    for directory in [POSTS_DIR, QUEUE_DIR]:
        if not directory.exists():
            continue
        for filepath in directory.glob("*.md"):
            if filepath.name.startswith((".", "TEMPLATE", "_")):
                continue
            try:
                content = filepath.read_text(encoding="utf-8")
                if not content.startswith("---"):
                    continue
                parts = content.split("---", 2)
                if len(parts) < 3:
                    continue

                fm = yaml.safe_load(parts[1])
                if not fm:
                    continue

                title = fm.get("headline") or fm.get("title") or ""
                image_path = fm.get("image", "")

                if not title:
                    continue

                # Check if image file actually exists
                if image_path:
                    full_image_path = Path(__file__).parent.parent / image_path.lstrip("/")
                    if full_image_path.exists():
                        continue

                missing.append({
                    "title": title,
                    "filepath": filepath,
                    "frontmatter": fm,
                    "body": parts[2] if len(parts) > 2 else "",
                })
            except Exception as e:
                print(f"  Error reading {filepath.name}: {e}")
                continue

    return missing


def update_frontmatter_image(filepath: Path, image_path: str):
    """Update the image field in a post's frontmatter."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return

    parts = content.split("---", 2)
    if len(parts) < 3:
        return

    fm = yaml.safe_load(parts[1])
    if not fm:
        return

    fm["image"] = image_path

    new_content = "---\n"
    new_content += yaml.dump(fm, default_flow_style=False, allow_unicode=True)
    new_content += "---"
    new_content += parts[2]

    filepath.write_text(new_content, encoding="utf-8")


def main():
    """Generate images for posts that need them."""
    print("AI Pulse Image Generator")
    print("=" * 40)

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    posts = get_posts_missing_images()
    if not posts:
        print("All posts have images. Nothing to generate.")
        return

    print(f"Found {len(posts)} post(s) missing images.\n")

    generated = 0
    for post in posts:
        title = post["title"]
        slug = slugify(title)
        image_filename = f"{slug}.png"
        image_path = IMAGES_DIR / image_filename
        relative_path = f"/assets/images/posts/{image_filename}"

        print(f"Generating image for: {title[:60]}...")
        try:
            if generate_image(title, image_path):
                update_frontmatter_image(post["filepath"], relative_path)
                print(f"  Saved: {image_filename}")
                generated += 1
        except Exception as e:
            print(f"  Error: {e}")
            continue

    print(f"\nDone! Generated {generated} image(s).")


if __name__ == "__main__":
    main()
