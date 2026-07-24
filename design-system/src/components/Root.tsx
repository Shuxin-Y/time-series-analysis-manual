import type { ReactNode } from "react";

export interface RootProps {
  children: ReactNode;
  /**
   * Force a colour scheme. When omitted, the system follows the viewer's
   * `prefers-color-scheme`. Setting this stamps `data-theme` so the token
   * overrides in `styles.css` resolve deterministically.
   */
  theme?: "light" | "dark";
  className?: string;
}

/**
 * Root wrapper for the design system. Establishes the brand typography,
 * foreground, and background, and carries the theme flag that the token
 * stylesheet reads. Wrap an application (or a preview) in `Root` so every
 * component inside inherits the brand tokens.
 */
export function Root({ children, theme, className }: RootProps) {
  return (
    <div
      className={["tsam-root", className].filter(Boolean).join(" ")}
      data-theme={theme}
    >
      {children}
    </div>
  );
}

export default Root;
