# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Pulse is a Jekyll-based AI news blog hosted on GitHub Pages. Content is discovered automatically from news sources and generated via a Gemini AI pipeline. The full pipeline runs twice daily via GitHub Actions.

## Commands

```bash
# Local development
bundle install              # Install Ruby dependencies
bundle exec jekyll serve    # Run local server at http://localhost:4000

# Full automated pipeline (discover + generate + images)
pip install -r scripts/requirements.txt
python scripts/update-site.py

# Individual pipeline steps
python scripts/discover-news.py       # Find trending AI news, create queue files
python scripts/generate-posts.py      # Generate articles from queue (auto-publishes to _posts/)
python scripts/generate-posts.py --drafts-only  # Generate to _drafts/ instead
python scripts/generate-images.py     # Create branded images for posts missing them
```

## Content Pipeline

1. **Discover**: `discover-news.py` fetches trending AI news from Google News RSS, Hacker News, and Reddit. Creates 2-3 queue files automatically.
2. **Generate**: `generate-posts.py` uses Gemini to write articles from queue files. Auto-publishes to `_posts/`.
3. **Images**: `generate-images.py` creates branded placeholder images (gradient + title) for posts missing images.
4. **Orchestrate**: `update-site.py` runs all three steps in sequence.
5. **Deploy**: GitHub Actions commits changes and triggers deploy to GitHub Pages.

Manual topic creation is also supported: copy `_content-queue/TEMPLATE.md`, fill in headline, sources, angle, tags.

## Architecture

```
_content-queue/     # Topic briefs waiting for generation
  _processed/       # Topics that have been generated
_posts/             # Published articles (auto-published by pipeline)
_drafts/            # Articles awaiting manual review (--drafts-only mode)
_layouts/
  default.html      # Base layout (header, footer, newsletter)
  post.html         # Single article layout
  tag.html          # Tag archive pages
_includes/
  seo-structured-data.html  # Schema.org JSON-LD (NewsArticle, Person, WebSite, BreadcrumbList)
  social-share.html         # Social sharing buttons (with UTM tracking)
  related-posts.html        # Related articles component
  breadcrumbs.html          # Visible breadcrumb navigation
  faq-schema.html           # FAQ structured data + visible FAQ section
  newsletter-cta.html       # Scroll-triggered newsletter popup
  ads.html                  # AdSense integration
scripts/
  update-site.py            # Full pipeline orchestrator
  discover-news.py          # News discovery from RSS/APIs
  generate-posts.py         # Gemini-powered article generator
  generate-images.py        # Branded placeholder image generator
```

## Key Configuration (_config.yml)

- `adsense.enabled`: Toggle ad display
- `newsletter.popup_enabled`: Toggle newsletter popup
- `enable_search_action`: Enables SearchAction schema for Google sitelinks
- `pagination.per_page`: Posts per page on homepage (default: 12)
- `author.*`: Populates Person schema and author page
- `keywords`: Site-wide SEO keywords

## Writing Guidelines

- Do not use emdashes in content (use commas instead)
- Posts require: title, date, author, tags, description, sources
- Posts support optional `faq` frontmatter for FAQ schema
- Images go in `/assets/images/posts/` (optimal: 1200x630px)

## GitHub Actions

- `generate-content.yml`: Twice-daily content pipeline (9 AM and 6 PM UTC) - discovers news, generates articles, creates images
- `deploy.yml`: Deploys to GitHub Pages on push
