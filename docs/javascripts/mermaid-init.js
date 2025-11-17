/**
 * Mermaid Initialization for MkDocs Material
 *
 * Configures and initializes Mermaid diagrams with proper
 * integration for Material theme and SPA navigation.
 */

// Wait for Mermaid to load
document.addEventListener('DOMContentLoaded', function() {
  if (typeof mermaid !== 'undefined') {
    // Configure Mermaid
    mermaid.initialize({
      startOnLoad: true,
      theme: 'default',
      themeVariables: {
        primaryColor: '#3f51b5',
        primaryTextColor: '#fff',
        primaryBorderColor: '#303f9f',
        lineColor: '#5c6bc0',
        secondaryColor: '#7986cb',
        tertiaryColor: '#9fa8da'
      },
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true,
        curve: 'basis'
      },
      sequence: {
        diagramMarginX: 50,
        diagramMarginY: 10,
        actorMargin: 50,
        width: 150,
        height: 65,
        boxMargin: 10,
        boxTextMargin: 5,
        noteMargin: 10,
        messageMargin: 35,
        mirrorActors: true,
        bottomMarginAdj: 1,
        useMaxWidth: true
      },
      gantt: {
        titleTopMargin: 25,
        barHeight: 20,
        barGap: 4,
        topPadding: 50,
        leftPadding: 75,
        gridLineStartPadding: 35,
        fontSize: 11,
        numberSectionStyles: 4,
        axisFormat: '%Y-%m-%d'
      }
    });

    console.log('Mermaid initialized successfully');
  } else {
    console.warn('Mermaid library not loaded');
  }
});

// Re-render diagrams on SPA navigation (MkDocs Material)
if (typeof document$ !== 'undefined') {
  document$.subscribe(function() {
    if (typeof mermaid !== 'undefined') {
      // Find all mermaid code blocks
      const mermaidBlocks = document.querySelectorAll('.mermaid');

      if (mermaidBlocks.length > 0) {
        // Re-initialize Mermaid for new content
        mermaid.init(undefined, mermaidBlocks);
        console.log(`Rendered ${mermaidBlocks.length} Mermaid diagram(s)`);
      }
    }
  });
}
