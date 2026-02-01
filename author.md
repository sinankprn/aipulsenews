---
layout: default
title: "About Sinan Koparan"
description: "Learn about Sinan Koparan, PhD Candidate in Sports Data Science & AI, creator of AI Pulse."
permalink: /author/
---

<article class="author-page" itemscope itemtype="https://schema.org/Person">
  <header class="author-header">
    <div class="author-avatar">
      {% if site.author.image %}
      <img src="{{ site.author.image | relative_url }}" alt="{{ site.author.name }}" itemprop="image" loading="lazy">
      {% else %}
      <div class="author-avatar-placeholder">{{ site.author.name | slice: 0 }}</div>
      {% endif %}
    </div>
    <div class="author-info">
      <h1 itemprop="name">{{ site.author.name }}</h1>
      <p class="author-title" itemprop="jobTitle">{{ site.author.bio }}</p>
    </div>
  </header>

  <section class="author-bio">
    <h2>About</h2>
    <p itemprop="description">{{ site.author.full_bio }}</p>
  </section>

  <section class="author-expertise">
    <h2>Areas of Expertise</h2>
    <ul class="expertise-list">
      {% for skill in site.author.expertise %}
      <li itemprop="knowsAbout">{{ skill }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="author-social">
    <h2>Connect</h2>
    <div class="social-links">
      {% if site.author.url %}
      <a href="{{ site.author.url }}" target="_blank" rel="noopener" itemprop="url">
        <span aria-hidden="true">&#127760;</span> Website
      </a>
      {% endif %}
      {% if site.author.github %}
      <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener" itemprop="sameAs">
        <span aria-hidden="true">&#128187;</span> GitHub
      </a>
      {% endif %}
      {% if site.author.twitter %}
      <a href="https://twitter.com/{{ site.author.twitter }}" target="_blank" rel="noopener" itemprop="sameAs">
        <span aria-hidden="true">&#128038;</span> Twitter
      </a>
      {% endif %}
      {% if site.author.linkedin %}
      <a href="https://linkedin.com/in/{{ site.author.linkedin }}" target="_blank" rel="noopener" itemprop="sameAs">
        <span aria-hidden="true">&#128188;</span> LinkedIn
      </a>
      {% endif %}
    </div>
  </section>

  <section class="author-articles">
    <h2>Latest Articles</h2>
    <div class="articles-list">
      {% for post in site.posts limit:10 %}
      <article class="article-card">
        <a href="{{ post.url | relative_url }}">
          <h3>{{ post.title }}</h3>
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
        </a>
      </article>
      {% endfor %}
    </div>
  </section>
</article>

<style>
.author-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 0;
}

.author-header {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 3rem;
}

.author-avatar img,
.author-avatar-placeholder {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
}

.author-avatar-placeholder {
  background: var(--primary, #6366f1);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 700;
}

.author-info h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2rem;
}

.author-title {
  color: var(--text-muted, #666);
  margin: 0;
}

.author-bio,
.author-expertise,
.author-social,
.author-articles {
  margin-bottom: 2.5rem;
}

.author-bio h2,
.author-expertise h2,
.author-social h2,
.author-articles h2 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--border, #e5e7eb);
}

.expertise-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.expertise-list li {
  background: var(--surface, #f3f4f6);
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-size: 0.9rem;
}

.social-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.social-links a {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: var(--surface, #f3f4f6);
  border-radius: 0.5rem;
  text-decoration: none;
  color: inherit;
  transition: background 0.2s;
}

.social-links a:hover {
  background: var(--primary, #6366f1);
  color: white;
}

.articles-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.article-card a {
  display: block;
  padding: 1rem;
  background: var(--surface, #f3f4f6);
  border-radius: 0.5rem;
  text-decoration: none;
  color: inherit;
  transition: background 0.2s;
}

.article-card a:hover {
  background: var(--border, #e5e7eb);
}

.article-card h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
}

.article-card time {
  font-size: 0.85rem;
  color: var(--text-muted, #666);
}

@media (max-width: 600px) {
  .author-header {
    flex-direction: column;
    text-align: center;
  }
}
</style>
