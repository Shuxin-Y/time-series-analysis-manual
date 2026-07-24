import type { ReactNode } from "react";

export interface BadgeProps {
  /**
   * Semantic tone. `good`/`escalate`/`problem` reuse the book's decision-outcome
   * fills so status reads consistently with flowcharts and decision matrices.
   */
  tone?: "neutral" | "primary" | "good" | "escalate" | "problem";
  children: ReactNode;
  className?: string;
}

/**
 * Small status label. The `good`, `escalate`, and `problem` tones map to the
 * brand's semantic outcome colours.
 */
export function Badge({ tone = "neutral", children, className }: BadgeProps) {
  return (
    <span
      className={["tsam-badge", `tsam-badge--${tone}`, className]
        .filter(Boolean)
        .join(" ")}
    >
      {children}
    </span>
  );
}

export default Badge;
