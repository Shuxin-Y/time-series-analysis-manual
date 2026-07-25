import type { ReactNode } from "react";

export type Verdict = "good" | "escalate" | "problem";

export interface DecisionCell {
  content: ReactNode;
  /**
   * Semantic verdict colouring the cell. `good` (sufficient), `escalate`
   * (inspect), `problem` (replace). Omit for a plain cell. The verdict text is
   * still the content, so colour is never the sole signal.
   */
  verdict?: Verdict;
}

export interface DecisionMatrixProps {
  headers: ReactNode[];
  /** Rows of cells. A cell may be a plain node or a `DecisionCell` with a verdict. */
  rows: (ReactNode | DecisionCell)[][];
  className?: string;
}

function isDecisionCell(cell: ReactNode | DecisionCell): cell is DecisionCell {
  return (
    typeof cell === "object" &&
    cell !== null &&
    !Array.isArray(cell) &&
    "content" in cell
  );
}

/**
 * Colour-coded decision matrix mapping combined test outcomes to a verdict.
 * Verdict cells use the brand `good`/`escalate`/`problem` fills; the verdict is
 * also written as text so colour is never the sole signal (WCAG 1.4.1).
 */
export function DecisionMatrix({ headers, rows, className }: DecisionMatrixProps) {
  return (
    <table
      className={["tsam-decision-matrix", className]
        .filter(Boolean)
        .join(" ")}
    >
      <thead>
        <tr>
          {headers.map((h, i) => (
            <th key={i}>{h}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, r) => (
          <tr key={r}>
            {row.map((cell, c) => {
              if (isDecisionCell(cell)) {
                return (
                  <td
                    key={c}
                    className={cell.verdict ? `tsam-${cell.verdict}` : undefined}
                  >
                    {cell.content}
                  </td>
                );
              }
              return <td key={c}>{cell}</td>;
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default DecisionMatrix;
