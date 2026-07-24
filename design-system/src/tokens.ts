/**
 * Design tokens for the Time Series Analysis Manual.
 *
 * These values mirror the brand palette and typography defined in
 * `DESIGN-SYSTEM.md` (repo root) and `docs/stylesheets/extra.css`. They are the
 * single JS-side home for the tokens; components read the matching CSS custom
 * properties declared in `styles.css`, so this object and that stylesheet must
 * stay in sync.
 */

export const colors = {
  // Cerulean — primary cool hue, body links
  cerulean: "#007BA7",
  ceruleanLight: "#4DA8C9",
  ceruleanDark: "#005A7A",
  ceruleanDeep: "#003D5C",
  // Burgundy — accent, theorem, danger
  burgundy: "#800020",
  burgundyLight: "#A33548",
  burgundyLighter: "#C97A86",
  burgundyDark: "#5A0017",
  // Thistle — definition, blockquote
  thistle: "#D8BFD8",
  thistleDark: "#9B7FA7",
  // Navajo — abstract, text selection
  navajo: "#FFDEAD",
  navajoDark: "#C9A55E",
  // Sunset — site header (primary)
  sunset: "#B87D6C",
  sunsetDark: "#9E6657",
  sunsetLight: "#D5A496",
  // Sage — tip, success
  sage: "#7FA98A",
  sageDark: "#4F7A5E",
  // Amber — caution, warning
  amber: "#E0A458",
  amberDark: "#B07A2E",
  // Semantic outcome fills (flowcharts, decision matrices)
  good: "#DCEFD8",
  escalate: "#FFE9C2",
  problem: "#F2D9DE"
} as const;

export const fonts = {
  /** Serif display face for content headings H1–H3 (academic gravitas). */
  display: '"Source Serif 4", Georgia, "Times New Roman", serif',
  /** Body and chrome face. */
  body: 'Inter, "Helvetica Neue", Arial, sans-serif'
} as const;

export const fontWeights = {
  regular: 400,
  semibold: 600,
  bold: 700
} as const;

/** Spacing scale, matching the book's utility classes (0.5rem steps). */
export const spacing = {
  xs: "0.25rem",
  sm: "0.5rem",
  md: "1rem",
  lg: "1.5rem",
  xl: "2rem"
} as const;

export const radii = {
  box: "0.5rem",
  control: "0.375rem",
  pill: "999px"
} as const;

export const typography = {
  bodyLineHeight: 1.75,
  bodySize: "max(0.8rem, 14px)"
} as const;

export type ColorToken = keyof typeof colors;

export const tokens = {
  colors,
  fonts,
  fontWeights,
  spacing,
  radii,
  typography
} as const;

export default tokens;
