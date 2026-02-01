---
layout: default
title: "Privacy Policy"
description: "Privacy Policy for AI Pulse - how we collect, use, and protect your information."
permalink: /privacy/
---

<article class="legal-page">
  <h1>Privacy Policy</h1>
  <p class="legal-updated">Last updated: {{ site.time | date: "%B %d, %Y" }}</p>

  <section>
    <h2>Introduction</h2>
    <p>AI Pulse ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, and safeguard your information when you visit our website at {{ site.url }}.</p>
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
    <h2>Cookies and Tracking Technologies</h2>
    <p>Our website uses cookies and similar tracking technologies. These include:</p>

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
    <p>We use Google AdSense to display advertisements. Google, as a third-party vendor, uses cookies to serve ads on our site. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to our site and other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>.</p>
    <p>For more information about how Google uses data, please visit <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">Google's Privacy & Terms</a>.</p>

    <h3>Buttondown (Newsletter)</h3>
    <p>If you subscribe to our newsletter, your email address is stored and processed by Buttondown. Please review <a href="https://buttondown.email/legal/privacy" target="_blank" rel="noopener">Buttondown's Privacy Policy</a> for more information.</p>

    <h3>GitHub Pages</h3>
    <p>This website is hosted on GitHub Pages. GitHub may collect technical information from visitors. Please review <a href="https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement" target="_blank" rel="noopener">GitHub's Privacy Statement</a> for more information.</p>
  </section>

  <section>
    <h2>Data Retention</h2>
    <p>We retain your personal information only for as long as necessary to fulfill the purposes outlined in this Privacy Policy, unless a longer retention period is required by law.</p>
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
    <p>Our website is not intended for children under 13 years of age. We do not knowingly collect personal information from children under 13. If you believe we have collected information from a child under 13, please contact us immediately.</p>
  </section>

  <section>
    <h2>Changes to This Policy</h2>
    <p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last updated" date.</p>
  </section>

  <section>
    <h2>Contact Us</h2>
    <p>If you have any questions about this Privacy Policy, please contact us:</p>
    <ul>
      <li>Website: <a href="{{ site.author.url }}" target="_blank" rel="noopener">{{ site.author.url }}</a></li>
      <li>GitHub: <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener">github.com/{{ site.author.github }}</a></li>
    </ul>
  </section>
</article>

<style>
.legal-page {
  max-width: 800px;
  margin: 0 auto;
  padding: var(--space-xl) 0;
}

.legal-page h1 {
  font-size: clamp(1.75rem, 5vw, 2.5rem);
  color: var(--dark);
  margin: 0 0 var(--space-sm) 0;
}

.legal-updated {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin: 0 0 var(--space-xl) 0;
  padding-bottom: var(--space-lg);
  border-bottom: 2px solid var(--border);
}

.legal-page section {
  margin-bottom: var(--space-xl);
}

.legal-page h2 {
  font-size: 1.25rem;
  color: var(--dark);
  margin: 0 0 var(--space-md) 0;
}

.legal-page h3 {
  font-size: 1rem;
  color: var(--dark);
  margin: var(--space-md) 0 var(--space-sm) 0;
}

.legal-page p {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
}

.legal-page ul {
  color: var(--text);
  line-height: 1.7;
  margin: 0 0 var(--space-md) 0;
  padding-left: var(--space-lg);
}

.legal-page li {
  margin-bottom: var(--space-xs);
}

.legal-page a {
  color: var(--primary);
  text-decoration: underline;
  text-underline-offset: 2px;
}

.legal-page a:hover {
  color: var(--primary-dark);
}
</style>
