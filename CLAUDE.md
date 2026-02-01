# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Pulse is a Jekyll-based AI news blog hosted on GitHub Pages. Content is generated via a Gemini AI pipeline that transforms topic briefs in `_content-queue/` into full articles.

## Commands

```bash
# Local development
bundle install              # Install Ruby dependencies
bundle exec jekyll serve    # Run local server at http://localhost:4000

# Content generation (requires GEMINI_API_KEY env var)
pip install -r scripts/requirements.txt
python scripts/generate-posts.py
```

## Content Pipeline

1. **Add topic**: Copy `_content-queue/TEMPLATE.md`, fill in headline, sources, angle, tags
2. **Generate**: Run `generate-posts.py` or wait for daily GitHub Action (9 AM UTC)
3. **Review**: Check `_drafts/` for generated articles
4. **Publish**: Move from `_drafts/` to `_posts/` and commit

## Architecture

```
_content-queue/     # Topic briefs waiting for generation
  _processed/       # Topics that have been generated
_drafts/            # Generated articles awaiting review
_posts/             # Published articles
_layouts/
  default.html      # Base layout (header, footer, newsletter)
  post.html         # Single article layout
  tag.html          # Tag archive pages
_includes/
  seo-structured-data.html  # Schema.org JSON-LD (NewsArticle, Person, WebSite, BreadcrumbList)
  social-share.html         # Social sharing buttons
  related-posts.html        # Related articles component
  toc.html                  # Table of contents
  ads.html                  # AdSense integration
scripts/
  generate-posts.py         # Gemini-powered article generator
```

## Key Configuration (_config.yml)

- `adsense.enabled`: Toggle ad display
- `enable_search_action`: Enables SearchAction schema for Google sitelinks
- `author.*`: Populates Person schema and author page
- `keywords`: Site-wide SEO keywords

## Writing Guidelines

- Do not use emdashes in content (use commas instead)
- Posts require: title, date, author, tags, description, sources
- Images go in `/assets/images/posts/` (optimal: 1200x630px)

## GitHub Actions

- `generate-content.yml`: Daily content generation from queue
- `deploy.yml`: Deploys to GitHub Pages on push
