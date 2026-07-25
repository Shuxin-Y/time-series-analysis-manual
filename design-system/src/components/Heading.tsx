import type { ReactNode } from "react";

export interface HeadingProps {
  /** Heading level 1–4. Levels 1–3 use the Source Serif 4 display face. */
  level?: 1 | 2 | 3 | 4;
  children: ReactNode;
  id?: string;
  className?: string;
}

/**
 * Content heading. Levels 1–3 render in the serif display face (academic
 * gravitas); level 4 stays in the body sans face. Level 2 carries a bottom
 * underrule, matching the book's section headings.
 */
export function Heading({ level = 2, children, id, className }: HeadingProps) {
  const Tag = `h${level}` as "h1" | "h2" | "h3" | "h4";
  return (
    <Tag
      id={id}
      className={["tsam-heading", `tsam-heading--${level}`, className]
        .filter(Boolean)
        .join(" ")}
    >
      {children}
    </Tag>
  );
}

export default Heading;
