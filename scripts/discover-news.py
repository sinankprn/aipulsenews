#!/usr/bin/env python3
"""
AI news discovery script for AI Pulse.
Fetches trending AI news from free sources and creates queue files.
"""

import os
import re
import json
import time
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
from difflib import SequenceMatcher

import feedparser
import requests
import yaml

# Configuration
QUEUE_DIR = Path(__file__).parent.parent / "_content-queue"
POSTS_DIR = Path(__file__).parent.parent / "_posts"
PROCESSED_DIR = QUEUE_DIR / "_processed"
MAX_STORIES = 4

# AI-related keywords for filtering
AI_KEYWORDS = [
    "artificial intelligence", "machine learning", "deep learning",
    "neural network", "llm", "large language model", "gpt", "openai",
    "anthropic", "claude", "gemini", "google ai", "meta ai", "mistral",
    "transformer", "diffusion", "generative ai", "chatbot", "ai model",
    "ai agent", "autonomous", "reinforcement learning", "computer vision",
    "natural language", "nlp", "ai safety", "alignment", "ai regulation",
    "copilot", "ai chip", "nvidia", "ai startup", "foundation model",
]

# User-Agent for requests
HEADERS = {
    "User-Agent": "AI-Pulse-News-Bot/1.0 (AI news aggregator)"
}


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:50]


def is_ai_related(title: str, description: str = "") -> bool:
    """Check if a story is AI-related based on keywords."""
    text = (title + " " + description).lower()
    return any(kw in text for kw in AI_KEYWORDS)


def title_similarity(a: str, b: str) -> float:
    """Fuzzy title comparison."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def get_existing_titles() -> list[str]:
    """Collect titles from existing posts and queue files."""
    titles = []
    for d in [POSTS_DIR, QUEUE_DIR, PROCESSED_DIR]:
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            if f.name.startswith((".", "TEMPLATE", "_")):
                continue
            try:
                content = f.read_text(encoding="utf-8")
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        fm = yaml.safe_load(parts[1])
                        if fm and (fm.get("headline") or fm.get("title")):
                            titles.append(fm.get("headline") or fm.get("title"))
            except Exception:
                continue
    return titles


def is_duplicate(title: str, existing_titles: list[str]) -> bool:
    """Check if a story title is too similar to existing content."""
    for existing in existing_titles:
        if title_similarity(title, existing) > 0.65:
            return True
    return False


def fetch_google_news() -> list[dict]:
    """Fetch AI news from Google News RSS feeds."""
    stories = []
    queries = [
        "artificial intelligence",
        "AI LLM",
        "OpenAI OR Anthropic OR Google AI",
        "AI startup funding OR AI acquisition",
        "AI regulation OR AI policy",
    ]

    for query in queries:
        url = f"https://news.google.com/rss/search?q={requests.utils.quote(query)}&hl=en&gl=US&ceid=US:en"
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                title = entry.get("title", "")
                # Google News appends " - Source" to titles
                clean_title = re.sub(r"\s*-\s*[^-]+$", "", title)
                link = entry.get("link", "")
                published = entry.get("published", "")

                if clean_title and link:
                    stories.append({
                        "title": clean_title,
                        "url": link,
                        "source": "google_news",
                        "published": published,
                    })
        except Exception as e:
            print(f"  Error fetching Google News for '{query}': {e}")
            continue

    return stories


def fetch_hacker_news() -> list[dict]:
    """Fetch AI-related stories from Hacker News."""
    stories = []
    try:
        resp = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            headers=HEADERS,
            timeout=10,
        )
        top_ids = resp.json()[:50]

        for story_id in top_ids:
            try:
                item_resp = requests.get(
                    f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json",
                    headers=HEADERS,
                    timeout=5,
                )
                item = item_resp.json()
                if not item:
                    continue

                title = item.get("title", "")
                url = item.get("url", f"https://news.ycombinator.com/item?id={story_id}")
                score = item.get("score", 0)

                if title and is_ai_related(title) and score >= 20:
                    stories.append({
                        "title": title,
                        "url": url,
                        "source": "hacker_news",
                        "score": score,
                    })
            except Exception:
                continue

    except Exception as e:
        print(f"  Error fetching Hacker News: {e}")

    return stories


def fetch_reddit() -> list[dict]:
    """Fetch AI news from Reddit."""
    stories = []
    subreddits = ["artificial", "MachineLearning", "LocalLLaMA"]

    for sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/hot/.json?limit=15&t=day"
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            data = resp.json()

            for post in data.get("data", {}).get("children", []):
                pd = post.get("data", {})
                title = pd.get("title", "")
                link = pd.get("url", "")
                score = pd.get("score", 0)

                if title and link and score >= 50:
                    stories.append({
                        "title": title,
                        "url": link,
                        "source": f"reddit_r/{sub}",
                        "score": score,
                    })
        except Exception as e:
            print(f"  Error fetching r/{sub}: {e}")
            continue

    return stories


def rank_stories(stories: list[dict]) -> list[dict]:
    """Rank and deduplicate stories."""
    # Group by similar titles
    grouped = {}
    for story in stories:
        title = story["title"]
        found = False
        for key in grouped:
            if title_similarity(title, key) > 0.6:
                grouped[key]["sources"].append(story["url"])
                grouped[key]["count"] += 1
                grouped[key]["score"] = max(
                    grouped[key].get("score", 0),
                    story.get("score", 0)
                )
                found = True
                break
        if not found:
            grouped[title] = {
                "title": title,
                "sources": [story["url"]],
                "count": 1,
                "score": story.get("score", 0),
            }

    # Sort by source count (coverage), then score
    ranked = sorted(
        grouped.values(),
        key=lambda x: (x["count"], x["score"]),
        reverse=True,
    )
    return ranked


def determine_tags(title: str) -> list[str]:
    """Determine relevant tags based on title."""
    title_lower = title.lower()
    tags = ["AI"]

    tag_keywords = {
        "OpenAI": ["openai", "gpt", "chatgpt", "dall-e", "sora"],
        "Google": ["google", "gemini", "deepmind", "bard"],
        "Anthropic": ["anthropic", "claude"],
        "Meta": ["meta ai", "llama"],
        "LLM": ["llm", "language model", "gpt", "claude", "gemini"],
        "Research": ["paper", "research", "study", "arxiv", "benchmark"],
        "Open Source": ["open source", "open-source", "hugging face", "llama"],
        "Regulation": ["regulation", "policy", "law", "ban", "govern"],
        "Robotics": ["robot", "humanoid", "autonomous"],
        "Computer Vision": ["image", "vision", "video", "diffusion", "dall-e"],
        "AI Safety": ["safety", "alignment", "risk", "existential"],
        "Startups": ["startup", "funding", "raised", "valuation", "series"],
    }

    for tag, keywords in tag_keywords.items():
        if any(kw in title_lower for kw in keywords):
            tags.append(tag)

    return tags[:4]  # Limit to 4 tags


def generate_angle(title: str) -> str:
    """Generate an article angle/focus based on the headline."""
    title_lower = title.lower()

    if any(w in title_lower for w in ["launch", "release", "announce", "unveil", "introduce"]):
        return "Cover the announcement, what it means for the industry, and how it compares to competitors."
    elif any(w in title_lower for w in ["research", "paper", "study", "discover"]):
        return "Explain the research findings in accessible terms, their significance, and potential real-world applications."
    elif any(w in title_lower for w in ["regulation", "policy", "ban", "law"]):
        return "Analyze the regulatory development, industry reactions, and implications for AI development."
    elif any(w in title_lower for w in ["funding", "acquire", "invest", "raise"]):
        return "Cover the business development and what it signals about the AI market landscape."
    else:
        return "Provide comprehensive coverage with context, analysis, and implications for the AI industry."


def create_queue_file(story: dict, existing_titles: list[str]) -> bool:
    """Create a queue file for a story."""
    title = story["title"]

    if is_duplicate(title, existing_titles):
        print(f"  Skipping duplicate: {title[:60]}...")
        return False

    slug = slugify(title)
    filename = f"{slug}.md"
    filepath = QUEUE_DIR / filename

    if filepath.exists():
        print(f"  Queue file already exists: {filename}")
        return False

    tags = determine_tags(title)
    angle = generate_angle(title)
    sources = story["sources"][:5]  # Limit to 5 sources

    frontmatter = {
        "headline": title,
        "sources": sources,
        "angle": angle,
        "tags": tags,
        "image": f"/assets/images/posts/{slug}.png",
    }

    content = "---\n"
    content += yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
    content += "---\n\n"
    content += f"Auto-discovered trending AI news story. Found across {story['count']} source(s).\n"

    filepath.write_text(content, encoding="utf-8")
    print(f"  Created queue file: {filename}")
    return True


def main():
    """Main discovery pipeline."""
    print("AI Pulse News Discovery")
    print("=" * 40)

    QUEUE_DIR.mkdir(exist_ok=True)
    PROCESSED_DIR.mkdir(exist_ok=True)

    existing_titles = get_existing_titles()
    print(f"Found {len(existing_titles)} existing titles to check against.\n")

    # Fetch from all sources
    print("Fetching from Google News...")
    google_stories = fetch_google_news()
    print(f"  Found {len(google_stories)} stories")

    print("Fetching from Hacker News...")
    hn_stories = fetch_hacker_news()
    print(f"  Found {len(hn_stories)} stories")

    print("Fetching from Reddit...")
    reddit_stories = fetch_reddit()
    print(f"  Found {len(reddit_stories)} stories")

    # Combine and rank
    all_stories = google_stories + hn_stories + reddit_stories
    print(f"\nTotal stories collected: {len(all_stories)}")

    ranked = rank_stories(all_stories)
    print(f"After deduplication: {len(ranked)} unique stories")

    # Create queue files for top stories
    created = 0
    print(f"\nCreating queue files (max {MAX_STORIES})...")
    for story in ranked:
        if created >= MAX_STORIES:
            break
        if create_queue_file(story, existing_titles):
            existing_titles.append(story["title"])
            created += 1

    print(f"\nDone! Created {created} new queue file(s).")


if __name__ == "__main__":
    main()
