#!/usr/bin/env python3
"""
YouTube AI video discovery for AI Pulse.
Fetches latest videos from popular AI YouTube channels via public RSS feeds.
Saves to _data/videos.yml for Jekyll to consume.
"""

import re
from datetime import datetime, timedelta
from pathlib import Path

import feedparser
import yaml

# Configuration
DATA_DIR = Path(__file__).parent.parent / "_data"
MAX_VIDEOS = 12  # Total videos to keep

# Popular AI YouTube channels (channel_id: display_name)
# Public RSS: https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
CHANNELS = {
    "UCWN3xxRkmTPphYit932FJoA": "Two Minute Papers",
    "UCbfYPyITQ-7l4upoX8nvctg": "Two Minute Papers",  # alt
    "UCZHmQk67mSJgfCCTn7xBfew": "ByteByteGo",
    "UCXUPKJO5MZQN11PqgIvyuvQ": "AI Explained",
    "UCbRP3c757lWg9M-U7TyEkXA": "Yannic Kilcher",
    "UCMLtBahI5DMrt0NPvDSoIRQ": "Matt Wolfe",
    "UCLXo7UDZvByw2ixzpQCufnA": "Wes Roth",
    "UCSHZKyawb77ixDdsGog4iWA": "Lex Fridman",
    "UCo8bcnLyZH8tBIH9V1mLgqQ": "TheAIGRID",
    "UC9-y-6csu5WGm29I7JiwpnA": "Computerphile",
    "UCVHFbqXqoYvEWM1Ddxl0QDg": "AI Jason",
    "UCnUYZLuoy1rq1aVMwx4piYw": "Jeff Su",
}

# AI-related keywords for filtering non-AI videos from general channels
AI_KEYWORDS = [
    "ai", "artificial intelligence", "machine learning", "deep learning",
    "neural", "llm", "gpt", "openai", "anthropic", "claude", "gemini",
    "chatgpt", "transformer", "diffusion", "generative", "copilot",
    "language model", "foundation model", "ai agent", "agi",
    "nvidia", "meta ai", "mistral", "llama", "reasoning",
]


def is_ai_related(title: str, channel: str) -> bool:
    """Check if a video is AI-related. AI-focused channels pass automatically."""
    ai_focused_channels = [
        "Two Minute Papers", "AI Explained", "Yannic Kilcher",
        "Matt Wolfe", "Wes Roth", "TheAIGRID", "AI Jason",
    ]
    if channel in ai_focused_channels:
        return True
    title_lower = title.lower()
    return any(kw in title_lower for kw in AI_KEYWORDS)


def extract_video_id(link: str) -> str:
    """Extract YouTube video ID from a URL."""
    match = re.search(r"(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})", link)
    return match.group(1) if match else ""


def fetch_channel_videos(channel_id: str, channel_name: str) -> list[dict]:
    """Fetch recent videos from a YouTube channel RSS feed."""
    videos = []
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # Latest 5 per channel
            title = entry.get("title", "")
            link = entry.get("link", "")
            published = entry.get("published", "")
            video_id = extract_video_id(link)

            if not title or not video_id:
                continue

            if not is_ai_related(title, channel_name):
                continue

            # Parse date
            try:
                pub_date = datetime(*entry.published_parsed[:6])
            except (TypeError, AttributeError):
                pub_date = datetime.now()

            # Only include videos from the last 14 days
            if datetime.now() - pub_date > timedelta(days=14):
                continue

            # Get thumbnail
            thumbnail = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

            videos.append({
                "title": title,
                "video_id": video_id,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "channel": channel_name,
                "thumbnail": thumbnail,
                "published": pub_date.strftime("%Y-%m-%d"),
                "published_display": pub_date.strftime("%b %d, %Y"),
            })
    except Exception as e:
        print(f"  Error fetching {channel_name}: {e}")

    return videos


def load_existing_videos() -> list[dict]:
    """Load existing videos from _data/videos.yml."""
    videos_file = DATA_DIR / "videos.yml"
    if videos_file.exists():
        try:
            data = yaml.safe_load(videos_file.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except Exception:
            return []
    return []


def main():
    print("AI Pulse Video Discovery")
    print("=" * 40)

    DATA_DIR.mkdir(exist_ok=True)

    existing = load_existing_videos()
    existing_ids = {v["video_id"] for v in existing}
    print(f"Existing videos: {len(existing)}")

    all_videos = []
    seen_ids = set()

    for channel_id, channel_name in CHANNELS.items():
        print(f"Fetching: {channel_name}...")
        videos = fetch_channel_videos(channel_id, channel_name)
        for v in videos:
            vid = v["video_id"]
            if vid not in seen_ids:
                seen_ids.add(vid)
                all_videos.append(v)
        print(f"  Found {len(videos)} AI videos")

    # Merge with existing, preferring new data for duplicates
    merged = {}
    for v in existing:
        merged[v["video_id"]] = v
    for v in all_videos:
        merged[v["video_id"]] = v

    # Sort by date (newest first) and limit
    sorted_videos = sorted(
        merged.values(),
        key=lambda x: x.get("published", ""),
        reverse=True,
    )[:MAX_VIDEOS]

    # Save to _data/videos.yml
    videos_file = DATA_DIR / "videos.yml"
    videos_file.write_text(
        yaml.dump(sorted_videos, default_flow_style=False, allow_unicode=True),
        encoding="utf-8",
    )

    new_count = len([v for v in sorted_videos if v["video_id"] not in existing_ids])
    print(f"\nSaved {len(sorted_videos)} videos ({new_count} new) to _data/videos.yml")


if __name__ == "__main__":
    main()
