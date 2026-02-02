(function() {
  'use strict';

  var STORAGE_KEY = 'theme-preference';

  function getColorPreference() {
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      return stored;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setPreference(theme) {
    localStorage.setItem(STORAGE_KEY, theme);
    reflectPreference(theme);
  }

  function reflectPreference(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    var toggle = document.querySelector('.theme-toggle');
    if (toggle) {
      toggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      updateToggleIcon(toggle, theme);
    }
  }

  function updateToggleIcon(toggle, theme) {
    var sunIcon = toggle.querySelector('.theme-icon-sun');
    var moonIcon = toggle.querySelector('.theme-icon-moon');
    if (sunIcon && moonIcon) {
      if (theme === 'dark') {
        sunIcon.style.display = 'block';
        moonIcon.style.display = 'none';
      } else {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'block';
      }
    }
  }

  // Set theme immediately to prevent flash
  var theme = getColorPreference();
  reflectPreference(theme);

  // Wait for DOM
  window.addEventListener('DOMContentLoaded', function() {
    var toggle = document.querySelector('.theme-toggle');
    if (toggle) {
      reflectPreference(getColorPreference());

      toggle.addEventListener('click', function() {
        var currentTheme = document.documentElement.getAttribute('data-theme') || getColorPreference();
        var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setPreference(newTheme);
      });
    }
  });

  // Sync with system changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
    if (!localStorage.getItem(STORAGE_KEY)) {
      reflectPreference(e.matches ? 'dark' : 'light');
    }
  });
})();
