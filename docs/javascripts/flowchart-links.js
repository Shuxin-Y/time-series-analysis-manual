/**
 * Flowchart node linking.
 *
 * Mermaid diagrams carry no URLs. After mermaid-init.js inserts a rendered diagram it
 * dispatches `mermaid:rendered`; diagrams rendered before this script loaded are picked up
 * by a scan of `.mermaid-container` at load. The script loads docs/flowcharts/inventory.yml once and,
 * for every SVG node whose id matches an inventory row, attaches navigation to the row's
 * section and a hover title with the label and area numbers. The inventory is the single
 * source of link targets (see planning/2026-10-06-flowchart-framework-design.md, section 10.5).
 */

(function() {
  'use strict';

  const NODE_ID_RE = /^flowchart-(.+)-\d+$/;
  let inventoryPromise = null;

  function loadInventory() {
    if (!inventoryPromise) {
      inventoryPromise = window.tsamSite.fetchText('flowcharts/inventory.yml')
        .then(text => {
          const rows = ((jsyaml.load(text) || {}).nodes) || [];
          const byId = new Map();
          rows.forEach(row => byId.set(row.id, row));
          return byId;
        })
        .catch(error => {
          console.error('flowchart-links: inventory unavailable, nodes stay unlinked', error);
          return new Map();
        });
    }
    return inventoryPromise;
  }

  async function decorate(container) {
    const inventory = await loadInventory();
    container.querySelectorAll('g.node[id]').forEach(group => {
      const match = NODE_ID_RE.exec(group.id);
      if (!match) return;
      const row = inventory.get(match[1]);
      if (!row || group.classList.contains('flowchart-link')) return;

      group.classList.add('flowchart-link');
      group.setAttribute('role', 'link');
      group.setAttribute('tabindex', '0');
      const title = document.createElementNS('http://www.w3.org/2000/svg', 'title');
      const areas = Array.isArray(row.areas) && row.areas.length ? ` (areas ${row.areas.join(', ')})` : '';
      title.textContent = `${row.label}${areas}`;
      group.prepend(title);

      const go = () => { window.location.href = window.tsamSite.docUrl(row.section); };
      group.addEventListener('click', go);
      group.addEventListener('keydown', event => { if (event.key === 'Enter') go(); });
    });
  }

  document.addEventListener('mermaid:rendered', event => decorate(event.detail.container));
  document.querySelectorAll('.mermaid-container').forEach(decorate);
})();
