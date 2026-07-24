import type { HTMLAttributes, ReactNode } from "react";

export interface CardProps extends Omit<HTMLAttributes<HTMLDivElement>, "title"> {
  /** Optional heading rendered in the serif display face. */
  title?: ReactNode;
  children: ReactNode;
}

/**
 * Surface container with a hairline border and rounded corners. Use to group
 * related content. An optional `title` renders in the brand display face.
 */
export function Card({ title, children, className, ...rest }: CardProps) {
  return (
    <div
      className={["tsam-card", className].filter(Boolean).join(" ")}
      {...rest}
    >
      {title != null && <div className="tsam-card__title">{title}</div>}
      <div className="tsam-card__body">{children}</div>
    </div>
  );
}

export default Card;
