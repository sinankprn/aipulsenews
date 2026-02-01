(function() {
  'use strict';

  var progressBar = document.querySelector('.progress-bar');
  if (!progressBar) return;

  var article = document.querySelector('.post-content');
  if (!article) return;

  var ticking = false;

  function updateProgress() {
    var articleRect = article.getBoundingClientRect();
    var articleTop = articleRect.top + window.scrollY;
    var articleHeight = article.offsetHeight;
    var windowHeight = window.innerHeight;
    var scrollY = window.scrollY;

    // Calculate progress based on article position
    var start = articleTop - windowHeight;
    var end = articleTop + articleHeight;
    var current = scrollY;

    var progress = ((current - start) / (end - start)) * 100;
    progress = Math.max(0, Math.min(100, progress));

    progressBar.style.width = progress + '%';

    // Show/hide based on scroll position
    if (scrollY > 100) {
      progressBar.classList.add('visible');
    } else {
      progressBar.classList.remove('visible');
    }

    ticking = false;
  }

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(updateProgress);
      ticking = true;
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  updateProgress();
})();
