import type { ReactNode } from "react";
import { Admonition } from "./Admonition";

export interface TheoremBoxProps {
  /** Full title, e.g. "Assumption 1: Zero Mean" or "Theorem 3.2". */
  title: ReactNode;
  children: ReactNode;
  className?: string;
}

/**
 * Burgundy-accented box for a formal result — a theorem, lemma, proposition, or
 * assumption. Convenience wrapper over `Admonition type="theorem"`.
 */
export function TheoremBox({ title, children, className }: TheoremBoxProps) {
  return (
    <Admonition type="theorem" title={title} className={className}>
      {children}
    </Admonition>
  );
}

export default TheoremBox;
