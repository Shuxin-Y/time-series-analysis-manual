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
      // Handle multiple possible selectors:
      // - <code class="mermaid">
      // - <div class="mermaid">
      // - <pre class="mermaid"><code>
      const codeBlocks = document.querySelectorAll('code.mermaid');
      const divBlocks = document.querySelectorAll('div.mermaid');
      const preBlocks = document.querySelectorAll('pre.mermaid');

      const allBlocks = [...codeBlocks, ...divBlocks, ...preBlocks];

      if (allBlocks.length > 0) {
        allBlocks.forEach((element, index) => {
          const id = `mermaid-${Date.now()}-${index}`;
          if (!element.hasAttribute('data-processed')) {
            element.setAttribute('data-processed', 'true');
            try {
              const graphDefinition = element.textContent;
              mermaid.render(id, graphDefinition).then(result => {
                const container = document.createElement('div');
                container.className = 'mermaid-container';
                container.innerHTML = result.svg;
                element.replaceWith(container);
              }).catch(error => {
                console.error('Mermaid rendering error:', error);
                element.innerHTML = `<pre>Error rendering diagram: ${error.message}</pre>`;
              });
            } catch (error) {
              console.error('Mermaid rendering error:', error);
              element.innerHTML = `<pre>Error rendering diagram: ${error.message}</pre>`;
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
