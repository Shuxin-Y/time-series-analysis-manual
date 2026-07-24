import React from "react";
import { Button } from "@tsam/design-system";

export const Primary = () => <Button variant="primary">Run ADF test</Button>;

export const Secondary = () => (
  <Button variant="secondary">Fit ARIMA model</Button>
);

export const Outline = () => (
  <Button variant="outline">Export residuals</Button>
);

export const Ghost = () => <Button variant="ghost">Cancel</Button>;

export const Sizes = () => (
  <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
    <Button size="sm">Small</Button>
    <Button size="md">Medium</Button>
    <Button size="lg">Large</Button>
  </div>
);

export const Disabled = () => (
  <Button variant="primary" disabled>
    Estimating…
  </Button>
);
