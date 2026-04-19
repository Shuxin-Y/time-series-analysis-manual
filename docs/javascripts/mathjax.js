/**
 * MathJax Configuration for Time Series Analysis Manual
 *
 * Enables mathematical notation rendering with equation numbering
 * and proper integration with MkDocs Material theme.
 */

window.MathJax = {
  tex: {
    // Inline math delimiters
    inlineMath: [['\\(', '\\)'], ['$', '$']],

    // Display math delimiters
    displayMath: [['\\[', '\\]'], ['$$', '$$']],

    // Process escape sequences
    processEscapes: true,
    processEnvironments: true,

    // Equation numbering (AMS style)
    tags: 'ams',
    tagSide: 'right',
    tagIndent: '0.8em',

    // Allow \begin{align}, \begin{equation}, etc.
    packages: {'[+]': ['ams', 'newcommand', 'configmacros', 'boldsymbol']},

    // Custom macros for consistent notation
    macros: {
      // Time series notation
      RR: "\\mathbb{R}",
      EE: "\\mathbb{E}",
      Var: "\\text{Var}",
      Cov: "\\text{Cov}",
      Corr: "\\text{Corr}",

      // Operators
      argmin: "\\operatorname{argmin}",
      argmax: "\\operatorname{argmax}",

      // Common symbols
      iid: "\\text{i.i.d.}",
      as: "\\text{a.s.}",

      // Vectors and matrices
      bm: ["\\boldsymbol{#1}", 1],

      // Differential
      dd: "\\mathrm{d}",

      // Probability
      Prob: "\\mathbb{P}",

      // Convergence
      plim: "\\text{plim}",
      convd: "\\xrightarrow{d}",
      convp: "\\xrightarrow{p}",
      convas: "\\xrightarrow{a.s.}"
    }
  },

  options: {
    // Ignore elements without arithmatex class
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },

  // Startup configuration
  startup: {
    // Ensure MathJax is ready
    ready() {
      MathJax.startup.defaultReady();
      console.log('MathJax is loaded and ready!');
    }
  },

  // SVG output configuration (recommended for web)
  svg: {
    fontCache: 'global',
    displayAlign: 'left',
    displayIndent: '2em'
  }
};

// Re-render math when page content changes (for SPA navigation)
document$.subscribe(() => {
  MathJax.typesetPromise()
    .then(() => {
      console.log('MathJax typesetting complete');
    })
    .catch((err) => console.log('MathJax typesetting failed: ' + err.message));
});
