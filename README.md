# AI Pulse

AI news blog powered by Jekyll, GitHub Pages, and Gemini AI.

## Quick Start

### Local Development

1. Install Ruby and Bundler
2. Run `bundle install`
3. Run `bundle exec jekyll serve`
4. Open http://localhost:4000

### Adding Content

1. Copy `_content-queue/TEMPLATE.md` and rename it
2. Fill in: headline, sources, angle, tags
3. Add any notes or context in the body
4. Commit and push

The daily automation will generate a draft from your input.

### Manual Generation

```bash
export GEMINI_API_KEY='your-key'
pip install -r scripts/requirements.txt
python scripts/generate-posts.py
```

### Publishing Drafts

1. Check `_drafts/` for generated posts
2. Review and edit as needed
3. Move to `_posts/` to publish
4. Commit and push

## Setup

### 1. Create GitHub Repository

Create a new repo and push this code.

### 2. Add Gemini API Key

Go to Settings > Secrets > Actions and add:
- Name: `GEMINI_API_KEY`
- Value: Your Gemini API key

### 3. Enable GitHub Pages

Go to Settings > Pages and set:
- Source: GitHub Actions

### 4. Update Config

Edit `_config.yml`:
- Set `url` to `https://yourusername.github.io`
- Set `baseurl` to `/your-repo-name`

## Workflows

- **generate-content.yml** - Runs daily at 9 AM UTC, generates posts from queue
- **deploy.yml** - Deploys to GitHub Pages on push to main
