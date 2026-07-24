import { defineConfig } from "tsup";

export default defineConfig({
  entry: ["src/index.ts"],
  format: ["esm"],
  dts: true,
  clean: true,
  sourcemap: false,
  external: ["react", "react-dom", "react/jsx-runtime"],
  // Bundle the imported stylesheet to dist/index.css and copy referenced
  // font files (.ttf) alongside it, so the package is self-contained.
  loader: {
    ".ttf": "file"
  },
  injectStyle: false
});
