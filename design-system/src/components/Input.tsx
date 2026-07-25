import type { InputHTMLAttributes } from "react";

export interface InputProps
  extends Omit<InputHTMLAttributes<HTMLInputElement>, "size"> {
  label?: string;
  hint?: string;
  /** Marks the field invalid (Burgundy border). */
  invalid?: boolean;
}

/**
 * Text input with an optional label and hint. When `invalid` is set the border
 * takes the brand Burgundy to signal an error. Focus shows a Cerulean ring.
 */
export function Input({
  label,
  hint,
  invalid,
  className,
  id,
  ...rest
}: InputProps) {
  const input = (
    <input
      id={id}
      className={[
        "tsam-input",
        invalid ? "tsam-input--invalid" : "",
        className
      ]
        .filter(Boolean)
        .join(" ")}
      aria-invalid={invalid || undefined}
      {...rest}
    />
  );

  if (!label && !hint) return input;

  return (
    <div className="tsam-field">
      {label && (
        <label className="tsam-field__label" htmlFor={id}>
          {label}
        </label>
      )}
      {input}
      {hint && <span className="tsam-field__hint">{hint}</span>}
    </div>
  );
}

export default Input;
