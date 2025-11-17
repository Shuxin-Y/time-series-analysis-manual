/**
 * Mermaid Initialization for MkDocs Material
 * Ensures Mermaid diagrams render properly with Material theme
 */

// Wait for both DOMContentLoaded and Mermaid library to be available
(function() {
  function initMermaid() {
    if (typeof mermaid === 'undefined') {
      console.log('Waiting for Mermaid to load...');
      setTimeout(initMermaid, 100);
      return;
    }

    // Initialize Mermaid with configuration
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose',
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
      }
    });

    // Function to render diagrams
    function renderDiagrams() {
      const diagrams = document.querySelectorAll('.mermaid');
      if (diagrams.length > 0) {
        diagrams.forEach((element, index) => {
          const id = `mermaid-${index}`;
          if (!element.hasAttribute('data-processed')) {
            element.setAttribute('data-processed', 'true');
            try {
              const graphDefinition = element.textContent;
              mermaid.render(id, graphDefinition).then(result => {
                element.innerHTML = result.svg;
              });
            } catch (error) {
              console.error('Mermaid rendering error:', error);
            }
          }
        });
      }
    }

    // Initial render
    renderDiagrams();

    // Re-render on navigation (Material theme SPA)
    if (typeof document$ !== 'undefined') {
      document$.subscribe(() => {
        setTimeout(renderDiagrams, 100);
      });
    }
  }

  // Start initialization
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMermaid);
  } else {
    initMermaid();
  }
})();
