import type { ButtonHTMLAttributes, ReactNode } from "react";

export interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Visual weight. `primary` uses the brand Sunset; `secondary` uses Cerulean. */
  variant?: "primary" | "secondary" | "outline" | "ghost";
  size?: "sm" | "md" | "lg";
  children: ReactNode;
}

/**
 * Brand button. `primary` is the Sunset call-to-action, `secondary` the
 * Cerulean action, `outline` the accent-bordered variant, and `ghost` a
 * low-emphasis text button.
 */
export function Button({
  variant = "primary",
  size = "md",
  className,
  children,
  type = "button",
  ...rest
}: ButtonProps) {
  return (
    <button
      type={type}
      className={[
        "tsam-btn",
        `tsam-btn--${variant}`,
        size !== "md" ? `tsam-btn--${size}` : "",
        className
      ]
        .filter(Boolean)
        .join(" ")}
      {...rest}
    >
      {children}
    </button>
  );
}

export default Button;
