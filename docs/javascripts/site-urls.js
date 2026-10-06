/**
 * Site URL helpers shared by flowchart-links.js and glossary.js; loaded before both.
 *
 * Inventory sections and glossary references are docs-relative source paths
 * (path/file.md#anchor). mkdocs.yml sets use_directory_urls, so `a/b.md` is served at
 * `a/b/`, `a/index.md` at `a/`, and the root `index.md` at the site root.
 */

(function() {
  'use strict';

  function base() {
    return window.__md_scope || new URL('/', window.location.href);
  }

  function docUrl(section) {
    const [file, anchor] = section.split('#');
    const page = file.replace(/\.md$/, '');
    const path = page === 'index' ? '' : page.endsWith('/index') ? page.slice(0, -'index'.length) : page + '/';
    return new URL(path, base()).href + (anchor ? '#' + anchor : '');
  }

  // Fetch a site file as text; a failed request is logged with its URL and rejects.
  async function fetchText(path) {
    const url = new URL(path, base()).href;
    const response = await fetch(url);
    if (!response.ok) {
      console.error(`Could not load ${url}: HTTP ${response.status}`);
      throw new Error(`HTTP ${response.status} for ${url}`);
    }
    return response.text();
  }

  window.tsamSite = { base, docUrl, fetchText };
})();
