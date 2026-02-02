---
layout: default
title: "Terms of Service"
description: "Terms of Service for AI Pulse - rules and guidelines for using our website."
permalink: /terms/
---

<div class="terms-page">
  <article class="terms-card">
    <header class="terms-header">
      <h1>Terms of Service</h1>
      <p>Last updated: {{ site.time | date: "%B %d, %Y" }}</p>
    </header>

    <div class="terms-content">
      <section class="terms-section">
        <h2>Agreement to Terms</h2>
        <p>By accessing and using AI Pulse ("the Website"), you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use the Website.</p>
      </section>

      <section class="terms-section">
        <h2>Description of Service</h2>
        <p>AI Pulse is a news and information website focused on artificial intelligence developments, breakthroughs, and industry news. We provide articles, analysis, and commentary on AI-related topics.</p>
      </section>

      <section class="terms-section">
        <h2>AI Training and Scraping</h2>
        <p>We permit the use of our content for AI and machine learning purposes:</p>
        <ul>
          <li>You may use our content to train AI models</li>
          <li>You may scrape our website for AI research and development</li>
          <li>We encourage the advancement of AI technology and welcome its use of our content</li>
        </ul>
        <p>We only ask that you respect our server resources by implementing reasonable rate limits in automated requests.</p>
      </section>

      <section class="terms-section">
        <h2>User Conduct</h2>
        <p>When using the Website, you agree not to:</p>
        <ul>
          <li>Use the Website for any unlawful purpose</li>
          <li>Attempt to gain unauthorized access to any part of the Website</li>
          <li>Interfere with or disrupt the Website's operation</li>
        </ul>
      </section>

      <section class="terms-section">
        <h2>Comments and User Content</h2>
        <p>If we enable comments or other user-generated content features:</p>
        <ul>
          <li>You retain ownership of content you submit, but grant us a license to display it on the Website</li>
          <li>You are responsible for the content you post</li>
          <li>We reserve the right to remove any content that violates these terms or is otherwise objectionable</li>
          <li>Do not post content that is defamatory, obscene, threatening, or infringes on others' rights</li>
        </ul>
      </section>

      <section class="terms-section">
        <h2>Newsletter</h2>
        <p>If you subscribe to our newsletter:</p>
        <ul>
          <li>You consent to receive periodic emails about AI news and updates</li>
          <li>You can unsubscribe at any time using the link in each email</li>
          <li>We will not sell or share your email address with third parties for marketing purposes</li>
        </ul>
      </section>

      <section class="terms-section">
        <h2>Disclaimer of Warranties</h2>
        <p>The Website and its content are provided "as is" without warranties of any kind, either express or implied. We do not warrant that:</p>
        <ul>
          <li>The Website will be uninterrupted or error-free</li>
          <li>All information on the Website is accurate, complete, or current</li>
          <li>The Website is free of viruses or harmful components</li>
        </ul>
        <p>Our articles are for informational purposes only and should not be considered professional advice. Always conduct your own research and consult appropriate professionals before making decisions based on our content.</p>
      </section>

      <section class="terms-section">
        <h2>Limitation of Liability</h2>
        <p>To the fullest extent permitted by law, AI Pulse and its operators shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising from your use of the Website or reliance on any information provided.</p>
      </section>

      <section class="terms-section">
        <h2>Third-Party Links</h2>
        <p>The Website may contain links to third-party websites. We are not responsible for the content, privacy policies, or practices of these external sites. Clicking on third-party links is at your own risk.</p>
      </section>

      <section class="terms-section">
        <h2>Advertising</h2>
        <p>The Website may display advertisements from third-party ad networks. These advertisements may use cookies and similar technologies. See our <a href="{{ '/privacy/' | relative_url }}">Privacy Policy</a> for more information about advertising and tracking.</p>
      </section>

      <section class="terms-section">
        <h2>Changes to Terms</h2>
        <p>We reserve the right to modify these Terms of Service at any time. Changes will be effective immediately upon posting to the Website. Your continued use of the Website after changes constitutes acceptance of the new terms.</p>
      </section>

      <section class="terms-section">
        <h2>Termination</h2>
        <p>We reserve the right to restrict or terminate your access to the Website at any time, without notice, for any reason, including violation of these Terms of Service.</p>
      </section>

      <section class="terms-section">
        <h2>Governing Law</h2>
        <p>These Terms of Service shall be governed by and construed in accordance with applicable laws, without regard to conflict of law principles.</p>
      </section>

      <section class="terms-section">
        <h2>Contact</h2>
        <p>If you have questions about these Terms of Service, please <a href="{{ '/contact/' | relative_url }}">contact us</a>.</p>
      </section>
    </div>
  </article>
</div>

<style>
.terms-page {
  padding: var(--space-lg) 0 var(--space-2xl);
}

.terms-card {
  background: var(--card);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.terms-header {
  background: var(--gradient-primary);
  padding: var(--space-xl) var(--space-lg);
  position: relative;
}

.terms-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  opacity: 0.5;
}

.terms-header h1 {
  position: relative;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: #fff;
  margin: 0 0 var(--space-xs) 0;
}

.terms-header p {
  position: relative;
  color: rgba(255, 255, 255, 0.8);
  margin: 0;
  font-size: 0.9rem;
}

.terms-content {
  padding: var(--space-xl) var(--space-lg);
}

.terms-section {
  margin-bottom: var(--space-xl);
  padding-bottom: var(--space-xl);
  border-bottom: 1px solid var(--border);
}

.terms-section:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.terms-section h2 {
  font-size: 1.15rem;
  color: var(--dark);
  margin: 0 0 var(--space-sm) 0;
}

.terms-section p {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
}

.terms-section ul {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
  padding-left: var(--space-lg);
}

.terms-section li {
  margin-bottom: var(--space-sm);
}

.terms-section a {
  color: var(--primary);
  text-decoration: none;
}

.terms-section a:hover {
  text-decoration: underline;
}

@media (min-width: 600px) {
  .terms-header,
  .terms-content {
    padding: var(--space-2xl);
  }
}
</style>
