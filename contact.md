---
layout: default
title: "Contact"
description: "Get in touch with AI Pulse. We welcome tips, feedback, and corrections."
permalink: /contact/
---

<div class="contact-page">
  <article class="contact-card">
    <header class="contact-header">
      <h1>Contact Us</h1>
      <p>We welcome your feedback, story tips, and corrections.</p>
    </header>

    <div class="contact-content">
      <section class="contact-section">
        <h2>Get in Touch</h2>
        <p>AI Pulse is committed to accurate, timely reporting on artificial intelligence news and developments. If you have a tip, correction, or feedback, we want to hear from you.</p>

        <div class="contact-methods">
          <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener" class="contact-method">
            <span class="contact-icon">&#128187;</span>
            <span class="contact-label">GitHub</span>
            <span class="contact-value">@{{ site.author.github }}</span>
          </a>

          <a href="https://twitter.com/{{ site.author.twitter }}" target="_blank" rel="noopener" class="contact-method">
            <span class="contact-icon">&#128038;</span>
            <span class="contact-label">Twitter/X</span>
            <span class="contact-value">@{{ site.author.twitter }}</span>
          </a>

          <a href="https://linkedin.com/in/{{ site.author.linkedin }}" target="_blank" rel="noopener" class="contact-method">
            <span class="contact-icon">&#128188;</span>
            <span class="contact-label">LinkedIn</span>
            <span class="contact-value">{{ site.author.name }}</span>
          </a>

          <a href="{{ site.author.url }}" target="_blank" rel="noopener" class="contact-method">
            <span class="contact-icon">&#127760;</span>
            <span class="contact-label">Website</span>
            <span class="contact-value">{{ site.author.url | remove: 'https://' }}</span>
          </a>
        </div>
      </section>

      <section class="contact-section">
        <h2>Story Tips</h2>
        <p>Have a breaking AI story or insider information? We protect our sources and investigate all credible tips. Reach out via any channel above.</p>
      </section>

      <section class="contact-section">
        <h2>Corrections</h2>
        <p>Accuracy is our priority. If you spot an error in any of our articles, please let us know immediately. We review all correction requests and update articles promptly when warranted. See our <a href="{{ '/editorial/' | relative_url }}">Editorial Standards</a> for our corrections policy.</p>
      </section>

      <section class="contact-section">
        <h2>Press & Partnerships</h2>
        <p>For media inquiries, partnership opportunities, or interview requests, please reach out via LinkedIn or Twitter with details about your proposal.</p>
      </section>
    </div>
  </article>
</div>

<style>
.contact-page {
  padding: var(--space-lg) 0 var(--space-2xl);
}

.contact-card {
  background: var(--card);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.contact-header {
  background: var(--gradient-primary);
  padding: var(--space-xl) var(--space-lg);
  position: relative;
}

.contact-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  opacity: 0.5;
}

.contact-header h1 {
  position: relative;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: #fff;
  margin: 0 0 var(--space-xs) 0;
}

.contact-header p {
  position: relative;
  color: rgba(255, 255, 255, 0.85);
  margin: 0;
  font-size: 1.05rem;
}

.contact-content {
  padding: var(--space-xl) var(--space-lg);
}

.contact-section {
  margin-bottom: var(--space-xl);
  padding-bottom: var(--space-xl);
  border-bottom: 1px solid var(--border);
}

.contact-section:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.contact-section h2 {
  font-size: 1.15rem;
  color: var(--dark);
  margin: 0 0 var(--space-sm) 0;
}

.contact-section p {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
}

.contact-section a {
  color: var(--primary);
  text-decoration: none;
}

.contact-section a:hover {
  text-decoration: underline;
}

.contact-methods {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: var(--space-md);
  margin-top: var(--space-lg);
}

.contact-method {
  display: flex;
  align-items: center;
  gap: var(--space-md);
  padding: var(--space-md);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  text-decoration: none;
  color: inherit;
  transition: all var(--transition-fast);
}

.contact-method:hover {
  border-color: var(--primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
  text-decoration: none;
}

.contact-icon {
  font-size: 1.5rem;
  width: 40px;
  text-align: center;
}

.contact-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: block;
}

.contact-value {
  font-weight: 600;
  color: var(--dark);
  display: block;
}

@media (min-width: 600px) {
  .contact-header,
  .contact-content {
    padding: var(--space-2xl);
  }
}
</style>
