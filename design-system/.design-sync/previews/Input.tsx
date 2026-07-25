import React from "react";
import { Input } from "@tsam/design-system";

export const WithLabel = () => (
  <div style={{ maxWidth: 320 }}>
    <Input
      id="series"
      label="Series name"
      hint="The column to model, e.g. log_returns"
      placeholder="gdp_growth"
    />
  </div>
);

export const Invalid = () => (
  <div style={{ maxWidth: 320 }}>
    <Input
      id="alpha"
      label="Significance level"
      invalid
      hint="Must be between 0 and 1"
      defaultValue="1.5"
    />
  </div>
);

export const Plain = () => (
  <div style={{ maxWidth: 320 }}>
    <Input placeholder="Search glossary…" />
  </div>
);
