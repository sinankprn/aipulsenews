(function() {
  'use strict';

  var tocList = document.getElementById('toc-list');
  var postContent = document.querySelector('.post-content');

  if (!tocList || !postContent) return;

  // Generate TOC from h2 and h3 headings
  var headings = postContent.querySelectorAll('h2, h3');
  if (headings.length === 0) {
    // Hide TOC if no headings
    var tocWrapper = document.querySelector('.toc-wrapper');
    if (tocWrapper) tocWrapper.style.display = 'none';
    return;
  }

  var tocItems = [];
  var html = '';

  headings.forEach(function(heading, index) {
    // Ensure heading has an ID
    if (!heading.id) {
      heading.id = 'heading-' + index;
    }

    var level = heading.tagName.toLowerCase();
    var text = heading.textContent;
    var id = heading.id;

    tocItems.push({ element: heading, id: id });

    if (level === 'h2') {
      html += '<li><a href="#' + id + '">' + escapeHtml(text) + '</a></li>';
    } else {
      html += '<li class="toc-h3"><a href="#' + id + '">' + escapeHtml(text) + '</a></li>';
    }
  });

  tocList.innerHTML = html;

  // TOC toggle functionality for mobile
  var tocToggle = document.querySelector('.toc-toggle');
  var tocContent = document.querySelector('.toc-content');

  if (tocToggle && tocContent) {
    tocToggle.addEventListener('click', function() {
      var isExpanded = tocToggle.getAttribute('aria-expanded') === 'true';
      tocToggle.setAttribute('aria-expanded', !isExpanded);
      tocContent.classList.toggle('open');
    });
  }

  // Scroll spy for TOC
  var tocLinks = tocList.querySelectorAll('a');
  var ticking = false;

  function updateActiveLink() {
    var windowHeight = window.innerHeight;
    var activeIndex = 0;

    // Find the heading that's currently in view
    for (var i = 0; i < tocItems.length; i++) {
      var rect = tocItems[i].element.getBoundingClientRect();
      if (rect.top <= windowHeight * 0.3) {
        activeIndex = i;
      }
    }

    // Update active class
    tocLinks.forEach(function(link) {
      link.classList.remove('active');
    });
    if (tocLinks[activeIndex]) {
      tocLinks[activeIndex].classList.add('active');
    }

    ticking = false;
  }

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(updateActiveLink);
      ticking = true;
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  updateActiveLink();

  // Smooth scroll to headings
  tocLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      var href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        var target = document.getElementById(href.slice(1));
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          history.pushState(null, null, href);

          // Close mobile TOC
          if (tocToggle && window.innerWidth < 1200) {
            tocToggle.setAttribute('aria-expanded', 'false');
            tocContent.classList.remove('open');
          }
        }
      }
    });
  });

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
})();
