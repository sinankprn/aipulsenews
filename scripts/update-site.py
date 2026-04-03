#!/usr/bin/env python3
"""
Full pipeline orchestrator for AI Pulse.
Discovers news, generates articles, and creates images.
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent


def run_step(name: str, script: str, extra_args: list[str] = None):
    """Run a pipeline step and report results."""
    print(f"\n{'=' * 50}")
    print(f"STEP: {name}")
    print(f"{'=' * 50}\n")

    cmd = [sys.executable, str(SCRIPTS_DIR / script)]
    if extra_args:
        cmd.extend(extra_args)

    result = subprocess.run(cmd, capture_output=False)

    if result.returncode != 0:
        print(f"\nWarning: {name} exited with code {result.returncode}")
    else:
        print(f"\n{name} completed successfully.")

    return result.returncode


def main():
    print("AI Pulse Full Pipeline")
    print("=" * 50)
    print("This script runs the complete content pipeline:")
    print("  1. Discover trending AI news")
    print("  2. Discover trending AI videos")
    print("  3. Generate articles from queue")
    print("  4. Generate images for posts missing them")
    print()

    # Step 1: Discover news
    run_step("News Discovery", "discover-news.py")

    # Step 2: Discover videos
    run_step("Video Discovery", "discover-videos.py")

    # Step 3: Generate posts (auto-publish)
    import os
    if not os.environ.get("GEMINI_API_KEY"):
        print("\nSkipping article generation: GEMINI_API_KEY not set.")
    else:
        extra = []
        if "--drafts-only" in sys.argv:
            extra.append("--drafts-only")
        run_step("Article Generation", "generate-posts.py", extra)

    # Step 4: Generate images
    run_step("Image Generation", "generate-images.py")

    print(f"\n{'=' * 50}")
    print("PIPELINE COMPLETE")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
