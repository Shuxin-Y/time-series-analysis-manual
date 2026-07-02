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
      // Do not inject Mermaid's "bomb" error SVG into the DOM on a parse error.
      // Without this, mermaid.render() appends the error graphic to <body>
      // (outside the content container), so it lands at the page bottom. Errors
      // are still thrown to the catch handler below and logged to the console.
      suppressErrorRendering: true,
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
      }
    });

    // Remove any orphaned Mermaid artifacts left directly on <body> by a prior
    // failed render (the error SVG / temp measurement node). Real diagrams live
    // inside .mermaid-container within the content, never as a direct body child,
    // so this selector cannot touch them.
    function clearOrphanedArtifacts() {
      document
        .querySelectorAll('body > svg[id^="mermaid-"], body > [id^="dmermaid-"]')
        .forEach(node => node.remove());
    }

    // Function to render diagrams
    function renderDiagrams() {
      clearOrphanedArtifacts();

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
