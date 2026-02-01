(function() {
  'use strict';

  var searchInput = document.getElementById('search-input');
  var resultsContainer = document.getElementById('search-results');
  var searchIndex = null;
  var searchData = null;

  // Load search data
  fetch('/search.json')
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      searchData = data;
      searchIndex = lunr(function() {
        this.ref('url');
        this.field('title', { boost: 10 });
        this.field('description', { boost: 5 });
        this.field('content');
        this.field('tags', { boost: 3 });

        data.forEach(function(doc) {
          this.add({
            url: doc.url,
            title: doc.title,
            description: doc.description,
            content: doc.content,
            tags: doc.tags ? doc.tags.join(' ') : ''
          });
        }, this);
      });

      // Check for query parameter
      var urlParams = new URLSearchParams(window.location.search);
      var query = urlParams.get('q');
      if (query) {
        searchInput.value = query;
        performSearch(query);
      }
    })
    .catch(function(error) {
      console.error('Error loading search index:', error);
      resultsContainer.innerHTML = '<p class="search-no-results">Error loading search. Please try again.</p>';
    });

  // Search input handler
  var debounceTimer;
  searchInput.addEventListener('input', function(e) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function() {
      performSearch(e.target.value);
    }, 200);
  });

  function performSearch(query) {
    if (!searchIndex || !query || query.trim().length < 2) {
      resultsContainer.innerHTML = query && query.trim().length < 2
        ? '<p class="search-no-results">Please enter at least 2 characters to search.</p>'
        : '';
      return;
    }

    try {
      // Add wildcards for partial matching
      var searchQuery = query.trim().split(/\s+/).map(function(term) {
        return term + '*';
      }).join(' ');

      var results = searchIndex.search(searchQuery);

      if (results.length === 0) {
        resultsContainer.innerHTML = '<p class="search-no-results">No results found for "' + escapeHtml(query) + '"</p>';
        return;
      }

      var html = results.map(function(result) {
        var doc = searchData.find(function(d) { return d.url === result.ref; });
        if (!doc) return '';

        var excerpt = highlightMatches(doc.description, query);

        return '<article class="search-result">' +
          '<h2 class="search-result-title"><a href="' + doc.url + '">' + escapeHtml(doc.title) + '</a></h2>' +
          '<p class="search-result-excerpt">' + excerpt + '</p>' +
          '<div class="search-result-meta">' +
            '<time>' + doc.date + '</time>' +
            (doc.tags && doc.tags.length ? ' &middot; ' + doc.tags.join(', ') : '') +
          '</div>' +
        '</article>';
      }).join('');

      resultsContainer.innerHTML = html;
    } catch (e) {
      // Fallback for invalid search queries
      resultsContainer.innerHTML = '<p class="search-no-results">Invalid search query. Try simpler terms.</p>';
    }
  }

  function highlightMatches(text, query) {
    if (!text) return '';
    var escaped = escapeHtml(text);
    var terms = query.trim().split(/\s+/);

    terms.forEach(function(term) {
      if (term.length >= 2) {
        var regex = new RegExp('(' + escapeRegex(term) + ')', 'gi');
        escaped = escaped.replace(regex, '<mark>$1</mark>');
      }
    });

    return escaped;
  }

  function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
})();
