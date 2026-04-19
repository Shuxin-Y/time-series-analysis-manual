/**
 * Interactive Glossary System for Time Series Analysis Manual
 *
 * Recognizes technical terms in the content and makes them clickable.
 * When clicked, displays a drawer panel from the right with:
 * - Definition
 * - Mathematical formulation
 * - Historical context
 * - Reference link
 *
 * Note: Applies to all chapters (00–07) and appendices
 */

(function() {
  'use strict';

  // Configuration — resolve glossary path relative to the site root so it
  // works both on localhost (root = /) and GitHub Pages (root = /repo-name/).
  const GLOSSARY_URL = new URL('glossary.yml', window.__md_scope || '/').href;
  const ENABLED_PATHS = [
    '/00-introduction/',
    '/01-master-flowchart/',
    '/02-data-preparation/',
    '/03-exploratory-analysis/',
    '/04-frequency-domain/',
    '/05-modelling/',
    '/06-feature-extraction/',
    '/07-validation-deployment/',
    '/appendices/'
  ];

  // Check if glossary should be enabled on current page
  function isGlossaryEnabled() {
    const path = window.location.pathname;
    return ENABLED_PATHS.some(enabledPath => path.includes(enabledPath));
  }

  // Load glossary data
  async function loadGlossary() {
    try {
      const response = await fetch(GLOSSARY_URL);
      const yamlText = await response.text();
      const glossary = jsyaml.load(yamlText);
      return glossary.terms || [];
    } catch (error) {
      console.warn('Could not load glossary:', error);
      return [];
    }
  }

  // Escape regex special characters
  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Find and mark glossary terms in content
  function highlightTerms(terms) {
    const content = document.querySelector('.md-content__inner');
    if (!content) return;

    // Build regex pattern for all terms
    // Sort by length (longest first) to match "Unit Root Test" before "Unit Root"
    const sortedTerms = [...terms].sort((a, b) => b.term.length - a.term.length);
    const termPattern = sortedTerms
      .map(t => escapeRegex(t.term))
      .join('|');

    const regex = new RegExp(`\\b(${termPattern})\\b`, 'gi');

    // Process text nodes only (not already marked, not in code blocks)
    const walker = document.createTreeWalker(
      content,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function(node) {
          // Skip if parent is already a glossary term
          if (node.parentElement.classList.contains('glossary-term')) {
            return NodeFilter.FILTER_REJECT;
          }
          // Skip code blocks
          if (node.parentElement.closest('code, pre, .highlight')) {
            return NodeFilter.FILTER_REJECT;
          }
          // Skip if no text content
          if (!node.textContent.trim()) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    const nodesToProcess = [];
    let node;
    while (node = walker.nextNode()) {
      nodesToProcess.push(node);
    }

    // Process nodes
    nodesToProcess.forEach(textNode => {
      const text = textNode.textContent;
      if (!regex.test(text)) return;

      // Create a temporary container
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = text.replace(regex, match => {
        // Find the actual term (preserve case)
        const matchedTerm = sortedTerms.find(t =>
          t.term.toLowerCase() === match.toLowerCase()
        );
        if (!matchedTerm) return match;

        return `<span class="glossary-term" data-term="${matchedTerm.term}">${match}</span>`;
      });

      // Replace the text node with marked up content
      const parent = textNode.parentNode;
      while (tempDiv.firstChild) {
        parent.insertBefore(tempDiv.firstChild, textNode);
      }
      parent.removeChild(textNode);
    });
  }

  // Add click handlers to glossary terms
  function addClickHandlers(terms) {
    document.querySelectorAll('.glossary-term').forEach(element => {
      element.addEventListener('click', function(e) {
        e.preventDefault();
        const termName = this.dataset.term;
        const termData = terms.find(t => t.term === termName);
        if (termData) {
          showDrawer(termData);
        }
      });
    });
  }

  // Show the glossary drawer
  function showDrawer(termData) {
    // Remove existing drawer if any
    const existingDrawer = document.querySelector('.glossary-drawer');
    if (existingDrawer) {
      existingDrawer.remove();
    }

    // Create drawer element
    const drawer = document.createElement('div');
    drawer.className = 'glossary-drawer';
    drawer.innerHTML = `
      <div class="glossary-drawer-content">
        <div class="glossary-drawer-header">
          <h3>${termData.term}</h3>
          <button class="close-drawer" aria-label="Close">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            </svg>
          </button>
        </div>

        <div class="glossary-drawer-body">
          <section class="glossary-section">
            <h4>Definition</h4>
            <p>${termData.definition}</p>
          </section>

          ${termData.mathematical ? `
            <section class="glossary-section">
              <h4>Mathematical Formulation</h4>
              <div class="math-block arithmatex">
                ${termData.mathematical}
              </div>
            </section>
          ` : ''}

          ${termData.historical ? `
            <section class="glossary-section">
              <h4>Historical Context</h4>
              <div class="historical-note">
                ${termData.historical}
              </div>
            </section>
          ` : ''}

          ${termData.reference ? `
            <section class="glossary-section">
              <a href="${termData.reference}" class="reference-link">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                  <path d="M13.25 10.75L16.5 14l-3.25 3.25V15H9V9h4.25v-1.75zM21 11v2h-7v7h-2v-7H5v-2h7V4h2v7h7z"/>
                </svg>
                Read more in documentation
              </a>
            </section>
          ` : ''}
        </div>
      </div>

      <div class="glossary-drawer-overlay"></div>
    `;

    document.body.appendChild(drawer);

    // Trigger reflow for animation
    drawer.offsetHeight;

    // Add open class for animation
    setTimeout(() => {
      drawer.classList.add('open');
    }, 10);

    // Render math in the drawer if MathJax is available
    if (window.MathJax && termData.mathematical) {
      MathJax.typesetPromise([drawer]).catch(err => {
        console.warn('MathJax rendering in drawer failed:', err);
      });
    }

    // Close handlers
    const closeBtn = drawer.querySelector('.close-drawer');
    const overlay = drawer.querySelector('.glossary-drawer-overlay');

    function closeDrawer() {
      drawer.classList.remove('open');
      setTimeout(() => {
        drawer.remove();
      }, 300); // Match CSS transition duration
    }

    closeBtn.addEventListener('click', closeDrawer);
    overlay.addEventListener('click', closeDrawer);

    // Close on Escape key
    function handleEscape(e) {
      if (e.key === 'Escape') {
        closeDrawer();
        document.removeEventListener('keydown', handleEscape);
      }
    }
    document.addEventListener('keydown', handleEscape);
  }

  // Initialize glossary system
  async function initGlossary() {
    if (!isGlossaryEnabled()) {
      console.log('Glossary not enabled on this page');
      return;
    }

    console.log('Initializing glossary system...');

    const terms = await loadGlossary();
    if (terms.length === 0) {
      console.warn('No glossary terms loaded');
      return;
    }

    console.log(`Loaded ${terms.length} glossary terms`);

    highlightTerms(terms);
    addClickHandlers(terms);

    console.log('Glossary system initialized');
  }

  // Run on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlossary);
  } else {
    initGlossary();
  }

  // Re-run when navigating in SPA mode (Material for MkDocs)
  if (typeof document$ !== 'undefined') {
    document$.subscribe(() => {
      setTimeout(initGlossary, 100); // Small delay for content to load
    });
  }

})();
