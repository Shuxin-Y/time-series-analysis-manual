import type { ReactNode } from "react";

export interface HypothesisTestProps {
  /** Test name, e.g. "Augmented Dickey–Fuller Test". */
  title: ReactNode;
  /** Null hypothesis statement. An automatic "H₀:" label is prepended. */
  nullHypothesis: ReactNode;
  /** Alternative hypothesis statement. An automatic "H₁:" label is prepended. */
  altHypothesis: ReactNode;
  /** Reject/retain rule. Rendered in the accent-bordered decision-rule block. */
  decisionRule?: ReactNode;
  className?: string;
}

/**
 * Cerulean-bordered box laying out a hypothesis test. The null and alternative
 * are auto-labelled "H₀:" and "H₁:"; the optional decision rule renders in an
 * accent-bordered block below. Do not type the H₀/H₁ labels yourself.
 */
export function HypothesisTest({
  title,
  nullHypothesis,
  altHypothesis,
  decisionRule,
  className
}: HypothesisTestProps) {
  return (
    <div
      className={["tsam-hypothesis-test", className]
        .filter(Boolean)
        .join(" ")}
    >
      <div className="tsam-hypothesis-test__title">{title}</div>
      <div className="tsam-hypothesis tsam-hypothesis--null">
        {nullHypothesis}
      </div>
      <div className="tsam-hypothesis tsam-hypothesis--alt">
        {altHypothesis}
      </div>
      {decisionRule != null && (
        <div className="tsam-decision-rule">
          <strong>Decision rule: </strong>
          {decisionRule}
        </div>
      )}
    </div>
  );
}

export default HypothesisTest;
