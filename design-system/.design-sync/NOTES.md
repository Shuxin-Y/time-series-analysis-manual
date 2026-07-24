# design-sync notes — @tsam/design-system

This package is the React implementation of the book's design system
(`DESIGN-SYSTEM.md` at the repo root is the authoritative catalog). It exists so
the brand can be synced to claude.ai/design. It is NOT imported by the MkDocs
site — the site uses the CSS/JS under `docs/`.

## Environment gotchas

- **No system Node.** This machine has no `node`/`npm`/`brew`. A local Node was
  installed by extracting the official darwin-arm64 tarball into the session
  scratchpad and prepending its `bin/` to `PATH`. That scratchpad lives under
  `/tmp` and is periodically cleaned — on a fresh session, reinstall Node the
  same way (or install a persistent Node) before doing anything.
- **npm can break independently of node.** During this sync the scratchpad's
  `npm` lost its own `lib/cli.js` to tmp cleanup while `node` and installed
  packages survived. Workaround: call tools directly instead of via `npm run`,
  e.g. `node node_modules/tsup/dist/cli-default.js` to build the package.
- Build the package with `tsup` (config in `tsup.config.ts`): emits
  `dist/index.js` + `dist/index.css` + copied fonts. `cfg.buildCmd` is
  `npm run build`; if npm is broken, run tsup directly as above.

## Converter invocation (from `design-system/`)

```
node .ds-sync/package-build.mjs --config .design-sync/config.json \
  --node-modules ./node_modules --entry ./dist/index.js --out ./ds-bundle
node .ds-sync/package-validate.mjs ./ds-bundle
```

Re-sync driver: `node .ds-sync/resync.mjs --config .design-sync/config.json --node-modules ./node_modules --entry ./dist/index.js --out ./ds-bundle --remote .design-sync/.cache/remote-sync.json`

## Design decisions

- **Theme via `data-theme` on any element, not just `:root`.** The dark/light
  token overrides in `styles.css` use bare `[data-theme="dark"]` /
  `[data-theme="light"]` selectors so the `Root` wrapper (which stamps
  `data-theme` on a `<div>`) actually themes its subtree. Scoping them to
  `:root[data-theme]` (the first attempt) left `Root theme="dark"` rendering on a
  white background — fixed. Do not re-scope these to `:root`.
- Styling idiom is CSS custom-property tokens (mirrors the book's own idiom), not
  a utility-class system. Tokens live in `_ds_bundle.css`, `@import`ed by
  `styles.css`.

## Known render warns

None. All 12 components render cleanly (0 bad, 0 thin, 0 fallback).

## Re-sync risks (what can silently go stale)

- **Local Node is ephemeral** (scratchpad under `/tmp`). Every re-sync must
  re-establish a working `node` first; npm may need bypassing (see above).
- **Source Serif 4 fonts were fetched from GitHub** (`adobe-fonts/source-serif`
  release branch) into `fonts/`. They are committed, so re-sync does not refetch
  — but if `fonts/` is ever cleaned, refetch from that source. Inter came from
  the repo's own `assets/fonts/inter/`.
- **Playwright chromium** lives in `~/Library/Caches/ms-playwright` (persists
  across sessions, unlike the scratchpad). If the render check reports
  `[RENDER_SKIPPED]`, reinstall with `node .ds-sync/node_modules/playwright/cli.js install chromium`.
- The conventions header (`conventions.md`) enumerates token and component names
  validated against the build. If components/tokens are added or renamed, re-run
  the conventions validation and update the header.
