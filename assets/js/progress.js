(function() {
  'use strict';

  var progressBar = document.querySelector('.progress-bar');
  if (!progressBar) return;

  var article = document.querySelector('.post-content');
  if (!article) return;

  var ticking = false;
  var STORAGE_PREFIX = 'reading-progress-';
  var pageKey = STORAGE_PREFIX + window.location.pathname;
  var saveTimeout = null;
  var toastShown = false;

  function getStoredProgress() {
    try {
      var stored = localStorage.getItem(pageKey);
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (e) {}
    return null;
  }

  function saveProgress(scrollY, progress) {
    if (progress >= 95) {
      // Article completed, clear saved position
      localStorage.removeItem(pageKey);
      return;
    }
    try {
      localStorage.setItem(pageKey, JSON.stringify({
        scrollY: scrollY,
        progress: progress,
        timestamp: Date.now()
      }));
    } catch (e) {}
  }

  function showContinueToast(savedData) {
    if (toastShown) return;
    toastShown = true;

    var toast = document.getElementById('continue-reading-toast');
    if (!toast) return;

    var progressPercent = Math.round(savedData.progress);
    var progressText = toast.querySelector('.toast-progress');
    if (progressText) {
      progressText.textContent = progressPercent + '% read';
    }

    toast.classList.add('visible');

    var continueBtn = toast.querySelector('.toast-continue');
    var dismissBtn = toast.querySelector('.toast-dismiss');

    if (continueBtn) {
      continueBtn.addEventListener('click', function() {
        window.scrollTo({ top: savedData.scrollY, behavior: 'smooth' });
        hideToast();
      });
    }

    if (dismissBtn) {
      dismissBtn.addEventListener('click', function() {
        localStorage.removeItem(pageKey);
        hideToast();
      });
    }

    // Auto-hide after 8 seconds
    setTimeout(hideToast, 8000);
  }

  function hideToast() {
    var toast = document.getElementById('continue-reading-toast');
    if (toast) {
      toast.classList.remove('visible');
    }
  }

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

    // Debounce saving progress
    if (saveTimeout) clearTimeout(saveTimeout);
    saveTimeout = setTimeout(function() {
      saveProgress(scrollY, progress);
    }, 500);

    ticking = false;
  }

  function onScroll() {
    if (!ticking) {
      requestAnimationFrame(updateProgress);
      ticking = true;
    }
  }

  // Check for saved progress on load
  var savedProgress = getStoredProgress();
  if (savedProgress && savedProgress.progress > 10 && savedProgress.progress < 95) {
    // Only show toast if saved within last 7 days
    var sevenDaysAgo = Date.now() - (7 * 24 * 60 * 60 * 1000);
    if (savedProgress.timestamp > sevenDaysAgo) {
      setTimeout(function() {
        showContinueToast(savedProgress);
      }, 1000);
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  updateProgress();
})();
