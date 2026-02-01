---
layout: default
title: "Privacy Policy"
description: "Privacy Policy for AI Pulse - how we collect, use, and protect your information."
permalink: /privacy/
---

<div class="privacy-page">
  <article class="privacy-card">
    <header class="privacy-header">
      <h1>Privacy Policy</h1>
      <p class="privacy-updated">Last updated: {{ site.time | date: "%B %d, %Y" }}</p>
    </header>

    <div class="privacy-content">
      <section>
        <h2>Introduction</h2>
        <p>AI Pulse ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, and safeguard your information when you visit our website.</p>
      </section>

      <section>
        <h2>Information We Collect</h2>
        <h3>Information You Provide</h3>
        <p>We may collect information you voluntarily provide, including:</p>
        <ul>
          <li>Email address (if you subscribe to our newsletter)</li>
          <li>Any information you submit through contact forms</li>
        </ul>

        <h3>Automatically Collected Information</h3>
        <p>When you visit our website, certain information may be collected automatically:</p>
        <ul>
          <li>IP address</li>
          <li>Browser type and version</li>
          <li>Operating system</li>
          <li>Pages visited and time spent</li>
          <li>Referring website</li>
          <li>Device information</li>
        </ul>
      </section>

      <section>
        <h2>How We Use Your Information</h2>
        <p>We use the collected information to:</p>
        <ul>
          <li>Provide and maintain our website</li>
          <li>Send newsletters and updates (only if you subscribe)</li>
          <li>Analyze website traffic and usage patterns</li>
          <li>Improve our content and user experience</li>
          <li>Comply with legal obligations</li>
        </ul>
      </section>

      <section>
        <h2>Cookies and Tracking</h2>
        <p>Our website uses cookies and similar tracking technologies:</p>

        <h3>Essential Cookies</h3>
        <p>Required for the website to function properly. These cannot be disabled.</p>

        <h3>Analytics Cookies</h3>
        <p>We may use analytics services to understand how visitors interact with our website. This helps us improve our content and user experience.</p>

        <h3>Advertising Cookies</h3>
        <p>We use Google AdSense to display advertisements. Google may use cookies to serve ads based on your prior visits to our website or other websites. You can opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>.</p>
      </section>

      <section>
        <h2>Third-Party Services</h2>

        <h3>Google AdSense</h3>
        <p>We use Google AdSense to display advertisements. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to our site and other sites on the Internet.</p>
        <p>For more information, visit <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">Google's Privacy & Terms</a>.</p>

        <h3>Buttondown (Newsletter)</h3>
        <p>If you subscribe to our newsletter, your email address is stored and processed by Buttondown. Please review <a href="https://buttondown.email/legal/privacy" target="_blank" rel="noopener">Buttondown's Privacy Policy</a> for more information.</p>

        <h3>GitHub Pages</h3>
        <p>This website is hosted on GitHub Pages. GitHub may collect technical information from visitors. Please review <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener">GitHub's Privacy Statement</a> for more information.</p>
      </section>

      <section>
        <h2>Your Rights</h2>
        <p>Depending on your location, you may have the following rights:</p>
        <ul>
          <li>Access the personal information we hold about you</li>
          <li>Request correction of inaccurate information</li>
          <li>Request deletion of your information</li>
          <li>Opt out of marketing communications</li>
          <li>Withdraw consent where applicable</li>
        </ul>
        <p>To exercise any of these rights, please contact us using the information below.</p>
      </section>

      <section>
        <h2>Children's Privacy</h2>
        <p>Our website is not intended for children under 13 years of age. We do not knowingly collect personal information from children under 13.</p>
      </section>

      <section>
        <h2>Changes to This Policy</h2>
        <p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last updated" date.</p>
      </section>

      <section>
        <h2>Contact Us</h2>
        <p>If you have any questions about this Privacy Policy, please contact us:</p>
        <div class="contact-links">
          <a href="{{ site.author.url }}" target="_blank" rel="noopener">{{ site.author.url }}</a>
          <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener">github.com/{{ site.author.github }}</a>
        </div>
      </section>
    </div>
  </article>
</div>

<style>
.privacy-page {
  padding: var(--space-lg) 0 var(--space-2xl);
}

.privacy-card {
  background: var(--card);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.privacy-header {
  background: var(--gradient-primary);
  padding: var(--space-xl) var(--space-lg);
  position: relative;
}

.privacy-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  opacity: 0.5;
}

.privacy-header h1 {
  position: relative;
  font-size: clamp(1.5rem, 5vw, 2rem);
  color: #fff;
  margin: 0 0 var(--space-xs) 0;
  font-weight: 700;
}

.privacy-updated {
  position: relative;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  margin: 0;
}

.privacy-content {
  padding: var(--space-xl) var(--space-lg);
}

.privacy-content section {
  margin-bottom: var(--space-xl);
  padding-bottom: var(--space-xl);
  border-bottom: 1px solid var(--border);
}

.privacy-content section:last-child {
  margin-bottom: 0;
  padding-bottom: 0;
  border-bottom: none;
}

.privacy-content h2 {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--dark);
  margin: 0 0 var(--space-md) 0;
}

.privacy-content h3 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--dark);
  margin: var(--space-lg) 0 var(--space-sm) 0;
}

.privacy-content h3:first-of-type {
  margin-top: 0;
}

.privacy-content p {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-sm) 0;
}

.privacy-content ul {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
  padding-left: var(--space-lg);
}

.privacy-content li {
  margin-bottom: var(--space-xs);
}

.privacy-content a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}

.privacy-content a:hover {
  text-decoration: underline;
}

.contact-links {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm);
  margin-top: var(--space-md);
}

.contact-links a {
  display: inline-flex;
  align-items: center;
  padding: var(--space-sm) var(--space-md);
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  font-size: 0.9rem;
  transition: all var(--transition-fast);
}

.contact-links a:hover {
  border-color: var(--primary);
  text-decoration: none;
}

@media (min-width: 600px) {
  .privacy-header {
    padding: var(--space-2xl);
  }

  .privacy-content {
    padding: var(--space-2xl);
  }
}
</style>
