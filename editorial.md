---
layout: default
title: "Editorial Standards"
description: "AI Pulse editorial standards, ethics policy, and commitment to accurate AI journalism."
permalink: /editorial/
---

<div class="editorial-page">
  <article class="editorial-card">
    <header class="editorial-header">
      <h1>Editorial Standards</h1>
      <p>Our commitment to accuracy, transparency, and ethical AI journalism.</p>
    </header>

    <div class="editorial-content">
      <section class="editorial-section">
        <h2>Our Mission</h2>
        <p>AI Pulse delivers timely, accurate, and accessible news about artificial intelligence to help readers understand the rapidly evolving AI landscape. We aim to cut through hype and provide balanced coverage of breakthroughs, industry developments, and the societal implications of AI technology.</p>
      </section>

      <section class="editorial-section">
        <h2>Editorial Independence</h2>
        <p>AI Pulse maintains complete editorial independence. Our coverage decisions are based solely on newsworthiness and reader interest. We do not accept payment for coverage, and advertising does not influence our editorial content.</p>
      </section>

      <section class="editorial-section">
        <h2>Accuracy Standards</h2>
        <p>We are committed to accuracy in all our reporting:</p>
        <ul>
          <li><strong>Source verification:</strong> We verify information through multiple credible sources before publication when possible.</li>
          <li><strong>Expert consultation:</strong> For technical topics, we consult primary sources and official documentation.</li>
          <li><strong>Clear attribution:</strong> All articles include source links so readers can verify information independently.</li>
          <li><strong>Distinction of fact and analysis:</strong> We clearly distinguish between factual reporting and analysis or opinion.</li>
        </ul>
      </section>

      <section class="editorial-section">
        <h2>Corrections Policy</h2>
        <p>When we make errors, we correct them promptly and transparently:</p>
        <ul>
          <li><strong>Minor corrections:</strong> Typos, grammatical errors, and minor factual clarifications are corrected in place.</li>
          <li><strong>Significant corrections:</strong> Material errors that affect the meaning or accuracy of an article are corrected with a visible correction notice at the top of the article.</li>
          <li><strong>Retractions:</strong> In rare cases where an article contains fundamental errors, we will retract the article and publish an explanation.</li>
        </ul>
        <p>To report an error, please <a href="{{ '/contact/' | relative_url }}">contact us</a>.</p>
      </section>

      <section class="editorial-section">
        <h2>AI-Assisted Content</h2>
        <p>AI Pulse uses AI tools in our editorial process:</p>
        <ul>
          <li><strong>Research assistance:</strong> AI tools help gather and summarize information from multiple sources.</li>
          <li><strong>Draft generation:</strong> Initial article drafts may be AI-assisted based on verified source material.</li>
          <li><strong>Human oversight:</strong> All content is reviewed, edited, and approved by human editors before publication.</li>
          <li><strong>Fact-checking:</strong> Claims and data points are verified against primary sources regardless of how the draft was generated.</li>
        </ul>
        <p>We believe in transparency about AI's role in journalism while maintaining human accountability for accuracy and editorial judgment.</p>
      </section>

      <section class="editorial-section">
        <h2>Conflicts of Interest</h2>
        <p>We disclose relevant conflicts of interest:</p>
        <ul>
          <li>If we cover a company or product in which our staff has a financial interest, we disclose this in the article.</li>
          <li>We do not accept gifts, travel, or other compensation from companies we cover.</li>
          <li>Sponsored content, if any, is clearly labeled as such and separated from editorial content.</li>
        </ul>
      </section>

      <section class="editorial-section">
        <h2>Source Protection</h2>
        <p>We protect confidential sources. If you share information with us on a confidential basis, we will not reveal your identity without your explicit consent. See our <a href="{{ '/contact/' | relative_url }}">Contact page</a> for secure ways to reach us.</p>
      </section>

      <section class="editorial-section">
        <h2>Content Updates</h2>
        <p>AI news moves fast. We update articles when significant new information becomes available:</p>
        <ul>
          <li>Updated articles show a "Last updated" timestamp.</li>
          <li>Major updates include an editor's note explaining what changed.</li>
          <li>We preserve the original publication date for reference.</li>
        </ul>
      </section>

      <section class="editorial-section">
        <h2>Questions or Concerns</h2>
        <p>If you have questions about our editorial standards or concerns about our coverage, please <a href="{{ '/contact/' | relative_url }}">contact us</a>. We take reader feedback seriously and respond to all substantive inquiries.</p>
      </section>
    </div>
  </article>
</div>

<style>
.editorial-page {
  padding: var(--space-lg) 0 var(--space-2xl);
}

.editorial-card {
  background: var(--card);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.editorial-header {
  background: var(--gradient-primary);
  padding: var(--space-xl) var(--space-lg);
  position: relative;
}

.editorial-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  opacity: 0.5;
}

.editorial-header h1 {
  position: relative;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: #fff;
  margin: 0 0 var(--space-xs) 0;
}

.editorial-header p {
  position: relative;
  color: rgba(255, 255, 255, 0.85);
  margin: 0;
  font-size: 1.05rem;
}

.editorial-content {
  padding: var(--space-xl) var(--space-lg);
}

.editorial-section {
  margin-bottom: var(--space-xl);
  padding-bottom: var(--space-xl);
  border-bottom: 1px solid var(--border);
}

.editorial-section:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.editorial-section h2 {
  font-size: 1.15rem;
  color: var(--dark);
  margin: 0 0 var(--space-sm) 0;
}

.editorial-section p {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
}

.editorial-section ul {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
  padding-left: var(--space-lg);
}

.editorial-section li {
  margin-bottom: var(--space-sm);
}

.editorial-section a {
  color: var(--primary);
  text-decoration: none;
}

.editorial-section a:hover {
  text-decoration: underline;
}

@media (min-width: 600px) {
  .editorial-header,
  .editorial-content {
    padding: var(--space-2xl);
  }
}
</style>
