/**
 * Interactive Glossary System for Time Series Analysis Manual
 *
 * Recognises glossary terms in the page and makes them clickable. A click opens a
 * right-hand drawer with the term's definition, mathematical formulation, derivation
 * chain ("Why it holds"), upstream terms ("Rests on", clickable chips that open the
 * upstream drawer, with a back stack), historical context, and a link to the section
 * where the term is first developed.
 *
 * Term files are listed in glossary/index.yml, generated at build time by
 * scripts/mkdocs_hooks.py. Paths in `reference` are docs-relative source paths
 * (path/file.md#anchor); tsamSite.docUrl() (site-urls.js) converts them to site URLs.
 */

(function() {
  'use strict';

  // Pages where the glossary is switched off: the home page and the design showcase.
  const DISABLED_PATHS = ['/design-system-showcase/'];

  let termsPromise = null;
  let allTerms = [];
  let drawerStack = [];

  function isGlossaryEnabled() {
    const path = window.location.pathname;
    const base = new URL(window.tsamSite.base(), window.location.origin).pathname;
    if (path === base || path === base + 'index.html') return false;
    return !DISABLED_PATHS.some(disabled => path.includes(disabled));
  }

  // Fetched once per page load; a failed file is logged by tsamSite.fetchText and contributes no terms.
  function loadGlossary() {
    if (!termsPromise) {
      termsPromise = (async () => {
        let files = [];
        try {
          files = ((jsyaml.load(await window.tsamSite.fetchText('glossary/index.yml')) || {}).files) || [];
        } catch (error) {
          console.error('glossary: file list unusable', error);
          return [];
        }
        const fetches = files.map(async name => {
          try {
            const data = jsyaml.load(await window.tsamSite.fetchText(`glossary/${name}`));
            return (data && data.terms) || [];
          } catch (error) {
            console.error(`glossary: ${name} unusable`, error);
            return [];
          }
        });
        return (await Promise.all(fetches)).flat();
      })();
    }
    return termsPromise;
  }

  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function escapeHtml(string) {
    return String(string)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // Find and mark glossary terms in content
  function highlightTerms(terms) {
    const content = document.querySelector('.md-content__inner');
    if (!content) return;

    const sortedTerms = [...terms].sort((a, b) => b.term.length - a.term.length);
    const regex = new RegExp(`\\b(${sortedTerms.map(t => escapeRegex(t.term)).join('|')})\\b`, 'gi');

    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, {
      acceptNode: function(node) {
        if (node.parentElement.classList.contains('glossary-term')) return NodeFilter.FILTER_REJECT;
        if (node.parentElement.closest('a, code, pre, .highlight, .mermaid-container, .arithmatex')) return NodeFilter.FILTER_REJECT;
        if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    const nodesToProcess = [];
    let node;
    while ((node = walker.nextNode())) nodesToProcess.push(node);

    nodesToProcess.forEach(textNode => {
      const text = textNode.textContent;
      regex.lastIndex = 0;
      if (!regex.test(text)) return;
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = escapeHtml(text).replace(regex, match => {
        const matched = sortedTerms.find(t => t.term.toLowerCase() === match.toLowerCase());
        if (!matched) return match;
        return `<span class="glossary-term" data-term="${escapeHtml(matched.term)}">${match}</span>`;
      });
      const parent = textNode.parentNode;
      while (tempDiv.firstChild) parent.insertBefore(tempDiv.firstChild, textNode);
      parent.removeChild(textNode);
    });
  }

  function addClickHandlers() {
    document.querySelectorAll('.glossary-term').forEach(element => {
      if (element.dataset.bound) return;
      element.dataset.bound = 'true';
      element.addEventListener('click', function(e) {
        e.preventDefault();
        openTerm(this.dataset.term, { reset: true });
      });
    });
  }

  function findTerm(name) {
    return allTerms.find(t => t.term === name);
  }

  function openTerm(name, options) {
    const termData = findTerm(name);
    if (!termData) return;
    if (options && options.reset) drawerStack = [];
    drawerStack.push(termData);
    showDrawer(termData);
  }

  // Math spans ($$...$$, $...$, \(...\), \[...\]) pass through to MathJax untouched by the transforms below.
  const MATH_SPAN_RE = /(\$\$[\s\S]+?\$\$|\$[^$\n]+\$|\\\([\s\S]+?\\\)|\\\[[\s\S]+?\\\])/;

  // Inline markdown on escaped text: **bold**, *italic*; odd split indices are math spans.
  function inlineMarkdownToHtml(text) {
    return text.split(MATH_SPAN_RE).map((part, i) => {
      const safe = escapeHtml(part);
      if (i % 2) return safe;
      return safe
        .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(?!\s)([^*\n]+?)(?<!\s)\*/g, '<em>$1</em>');
    }).join('');
  }

  // Block markdown: paragraphs, "- " bullets, "1. " numbered steps. Math left for MathJax.
  function renderMarkdown(text) {
    if (!text) return '';
    const output = [];
    let open = null; // 'ul' | 'ol' | null
    const close = () => { if (open) { output.push(`</${open}>`); open = null; } };
    for (const raw of text.split('\n')) {
      const line = raw.trim();
      if (!line) { close(); continue; }
      const bullet = line.match(/^- (.*)$/);
      const numbered = line.match(/^\d+\.\s+(.*)$/);
      if (bullet) {
        if (open !== 'ul') { close(); output.push('<ul>'); open = 'ul'; }
        output.push(`<li class="arithmatex">${inlineMarkdownToHtml(bullet[1])}</li>`);
      } else if (numbered) {
        if (open !== 'ol') { close(); output.push('<ol>'); open = 'ol'; }
        output.push(`<li class="arithmatex">${inlineMarkdownToHtml(numbered[1])}</li>`);
      } else {
        close();
        output.push(`<p class="arithmatex">${inlineMarkdownToHtml(line)}</p>`);
      }
    }
    close();
    return output.join('');
  }

  function section(title, bodyHtml, extraClass) {
    if (!bodyHtml) return '';
    return `<section class="glossary-section ${extraClass || ''}"><h4>${title}</h4>${bodyHtml}</section>`;
  }

  function showDrawer(termData) {
    const existing = document.querySelector('.glossary-drawer');
    if (existing) existing.remove();

    const crumbs = drawerStack.map(t => escapeHtml(t.term)).join(' › ');
    const backButton = drawerStack.length > 1
      ? `<button class="glossary-back" aria-label="Back to ${escapeHtml(drawerStack[drawerStack.length - 2].term)}">‹ Back</button>`
      : '';
    const chips = (termData.depends_on || []).map(name => {
      const known = !!findTerm(name);
      return known
        ? `<button class="glossary-chip" data-term="${escapeHtml(name)}">${escapeHtml(name)}</button>`
        : `<span class="glossary-chip glossary-chip--missing" title="No glossary entry yet">${escapeHtml(name)}</span>`;
    }).join('');
    const reference = termData.reference
      ? `<p><a href="${window.tsamSite.docUrl(termData.reference)}">${escapeHtml(termData.reference.split('#')[0])}</a></p>`
      : '';

    const drawer = document.createElement('div');
    drawer.className = 'glossary-drawer';
    drawer.innerHTML = `
      <div class="glossary-drawer-content">
        <div class="glossary-drawer-header">
          <div>
            ${backButton}
            <h3>${escapeHtml(termData.term)}${termData.foundation === true ? ' <span class="glossary-root" title="Foundation: root of derivation chains">root</span>' : ''}</h3>
            ${drawerStack.length > 1 ? `<div class="glossary-crumbs">${crumbs}</div>` : ''}
          </div>
          <button class="close-drawer" aria-label="Close">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
              <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
            </svg>
          </button>
        </div>
        <div class="glossary-drawer-body">
          ${section('Definition', `<p>${escapeHtml(termData.definition || '')}</p>`)}
          ${section('Mathematical Formulation', termData.mathematical ? `<div class="math-block">${renderMarkdown(termData.mathematical)}</div>` : '')}
          ${section('Why it holds', termData.derivation ? `<div class="derivation">${renderMarkdown(termData.derivation)}</div>` : '')}
          ${section('Rests on', chips ? `<div class="glossary-chips">${chips}</div>` : '')}
          ${section('Historical Context', termData.historical ? `<div class="historical-note">${renderMarkdown(termData.historical)}</div>` : '')}
          ${section('First developed in', reference)}
        </div>
      </div>
      <div class="glossary-drawer-overlay"></div>
    `;
    document.body.appendChild(drawer);
    drawer.offsetHeight;
    setTimeout(() => drawer.classList.add('open'), 10);

    if (window.MathJax) {
      const mathBlocks = Array.from(drawer.querySelectorAll('.arithmatex'));
      if (mathBlocks.length > 0) {
        MathJax.typesetPromise(mathBlocks).catch(err => console.warn('MathJax rendering in drawer failed:', err));
      }
    }

    function closeDrawer() {
      drawer.classList.remove('open');
      drawerStack = [];
      setTimeout(() => drawer.remove(), 300);
      document.removeEventListener('keydown', handleEscape);
    }
    function handleEscape(e) {
      if (e.key === 'Escape') closeDrawer();
    }

    drawer.querySelector('.close-drawer').addEventListener('click', closeDrawer);
    drawer.querySelector('.glossary-drawer-overlay').addEventListener('click', closeDrawer);
    document.addEventListener('keydown', handleEscape);

    drawer.querySelectorAll('.glossary-chip[data-term]').forEach(chip => {
      chip.addEventListener('click', () => {
        document.removeEventListener('keydown', handleEscape);
        openTerm(chip.dataset.term);
      });
    });
    const back = drawer.querySelector('.glossary-back');
    if (back) {
      back.addEventListener('click', () => {
        document.removeEventListener('keydown', handleEscape);
        drawerStack.pop();
        showDrawer(drawerStack[drawerStack.length - 1]);
      });
    }
  }

  async function initGlossary() {
    if (!isGlossaryEnabled()) return;
    allTerms = await loadGlossary();
    if (allTerms.length === 0) { console.error('No glossary terms loaded'); return; }
    highlightTerms(allTerms);
    addClickHandlers();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGlossary);
  } else {
    initGlossary();
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(() => setTimeout(initGlossary, 100));
  }
})();
