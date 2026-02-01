---
layout: default
title: "About Sinan Koparan"
description: "Learn about Sinan Koparan, PhD Candidate in Sports Data Science & AI, creator of AI Pulse."
permalink: /author/
---

<article class="author-page" itemscope itemtype="https://schema.org/Person">
  <header class="author-header">
    <div class="author-avatar-large">
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

  <section class="author-section">
    <h2>About</h2>
    <p itemprop="description">{{ site.author.full_bio }}</p>
  </section>

  <section class="author-section">
    <h2>Areas of Expertise</h2>
    <ul class="author-expertise-list">
      {% for skill in site.author.expertise %}
      <li itemprop="knowsAbout">{{ skill }}</li>
      {% endfor %}
    </ul>
  </section>

  <section class="author-section">
    <h2>Connect</h2>
    <div class="author-social-links">
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

  <section class="author-section">
    <h2>Latest Articles</h2>
    <div class="author-articles-list">
      {% for post in site.posts limit:10 %}
      <article class="author-article-card">
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
  padding: var(--space-xl) 0;
}

.author-header {
  display: flex;
  align-items: center;
  gap: var(--space-xl);
  margin-bottom: var(--space-2xl);
  padding: var(--space-xl);
  background: var(--card);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
}

.author-avatar-large img,
.author-avatar-large .author-avatar-placeholder {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--border);
}

.author-avatar-large .author-avatar-placeholder {
  background: var(--gradient-primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  font-weight: 700;
}

.author-info h1 {
  margin: 0 0 var(--space-xs) 0;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: var(--dark);
}

.author-title {
  color: var(--text-light);
  margin: 0;
  font-size: 1.1rem;
}

.author-section {
  margin-bottom: var(--space-xl);
  padding: var(--space-lg);
  background: var(--card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}

.author-section h2 {
  font-size: 1.1rem;
  margin: 0 0 var(--space-md) 0;
  padding-bottom: var(--space-sm);
  border-bottom: 2px solid var(--border);
  color: var(--dark);
  position: relative;
}

.author-section h2::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 50px;
  height: 2px;
  background: var(--gradient-primary);
}

.author-section p {
  color: var(--text);
  line-height: 1.7;
  margin: 0;
}

.author-expertise-list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm);
  list-style: none;
  padding: 0;
  margin: 0;
}

.author-expertise-list li {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
  color: var(--primary);
  padding: var(--space-sm) var(--space-md);
  border-radius: var(--radius-full);
  font-size: 0.9rem;
  font-weight: 500;
  border: 1px solid rgba(99, 102, 241, 0.15);
}

.author-social-links {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm);
}

.author-social-links a {
  display: inline-flex;
  align-items: center;
  gap: var(--space-sm);
  padding: var(--space-sm) var(--space-md);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  text-decoration: none;
  color: var(--text);
  font-weight: 500;
  transition: all var(--transition-fast);
  min-height: 44px;
}

.author-social-links a:hover {
  background: var(--primary);
  border-color: var(--primary);
  color: white;
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.author-articles-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.author-article-card a {
  display: block;
  padding: var(--space-md);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: all var(--transition-fast);
}

.author-article-card a:hover {
  border-color: var(--primary);
  transform: translateX(4px);
}

.author-article-card h3 {
  margin: 0 0 var(--space-xs) 0;
  font-size: 1rem;
  font-weight: 600;
  color: var(--dark);
}

.author-article-card a:hover h3 {
  color: var(--primary);
}

.author-article-card time {
  font-size: 0.85rem;
  color: var(--text-muted);
}

@media (max-width: 600px) {
  .author-header {
    flex-direction: column;
    text-align: center;
    gap: var(--space-md);
  }

  .author-avatar-large img,
  .author-avatar-large .author-avatar-placeholder {
    width: 100px;
    height: 100px;
  }

  .author-social-links {
    justify-content: center;
  }
}
</style>
