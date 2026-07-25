import type { ReactNode } from "react";
import { Admonition } from "./Admonition";

export interface DefinitionBoxProps {
  /** The term being defined, e.g. "Estimator". */
  title: ReactNode;
  children: ReactNode;
  className?: string;
}

/**
 * Thistle-accented box for the first formal statement of a term. Convenience
 * wrapper over `Admonition type="definition"`.
 */
export function DefinitionBox({ title, children, className }: DefinitionBoxProps) {
  return (
    <Admonition type="definition" title={title} className={className}>
      {children}
    </Admonition>
  );
}

export default DefinitionBox;
