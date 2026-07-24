import type { ReactNode } from "react";

export type AdmonitionType =
  | "note"
  | "info"
  | "abstract"
  | "summary"
  | "theorem"
  | "danger"
  | "error"
  | "failure"
  | "definition"
  | "example"
  | "tip"
  | "success"
  | "warning"
  | "caution"
  | "question"
  | "quote";

export interface AdmonitionProps {
  /**
   * Semantic type. Selects the accent colour family: note/info → Cerulean,
   * abstract/summary → Navajo, theorem/danger/error → Burgundy,
   * failure → soft Burgundy, definition/example → Thistle,
   * tip/success → Sage, warning/caution → Amber, question → Sunset,
   * quote → neutral grey.
   */
  type?: AdmonitionType;
  /** Box title, rendered in the accent colour above an underrule. */
  title: ReactNode;
  children: ReactNode;
  className?: string;
}

/**
 * Branded callout box: a 2px accent outline, rounded corners, and an
 * accent-coloured title separated from the body by an underrule. This is the
 * book's signature admonition. Choose `type` by meaning, not by colour.
 */
export function Admonition({
  type = "note",
  title,
  children,
  className
}: AdmonitionProps) {
  return (
    <div
      className={["tsam-admonition", `tsam-admonition--${type}`, className]
        .filter(Boolean)
        .join(" ")}
      role="note"
    >
      <div className="tsam-admonition__title">{title}</div>
      <div className="tsam-admonition__body">{children}</div>
    </div>
  );
}

export default Admonition;
