import type { ReactNode } from "react";

export interface TableColumn {
  /** Column header text. */
  header: ReactNode;
  /** Set true for numeric columns (right-aligned, tabular figures). */
  numeric?: boolean;
}

export interface TableProps {
  columns: TableColumn[];
  /** Row data as arrays of cells, in column order. */
  rows: ReactNode[][];
  /** Self-contained caption, e.g. "Table 3.1 — ADF results". */
  caption?: ReactNode;
  className?: string;
}

/**
 * Data table following the book's table standard: mandatory header row,
 * left-aligned text, right-aligned numerics with tabular figures, and a
 * self-contained caption.
 */
export function Table({ columns, rows, caption, className }: TableProps) {
  return (
    <table
      className={["tsam-table", className].filter(Boolean).join(" ")}
    >
      {caption != null && <caption>{caption}</caption>}
      <thead>
        <tr>
          {columns.map((col, i) => (
            <th key={i} className={col.numeric ? "tsam-num" : undefined}>
              {col.header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, r) => (
          <tr key={r}>
            {row.map((cell, c) => (
              <td key={c} className={columns[c]?.numeric ? "tsam-num" : undefined}>
                {cell}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Table;
