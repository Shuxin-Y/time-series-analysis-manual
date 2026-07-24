import React from "react";
import { Table } from "@tsam/design-system";

export const NotationTable = () => (
  <Table
    caption="Table 2.1 — Notation for the AR(1) process"
    columns={[
      { header: "Symbol" },
      { header: "Meaning" },
      { header: "First use" }
    ]}
    rows={[
      ["y_t", "Observation at time t", "§2.1"],
      ["φ", "Autoregressive coefficient", "§2.2"],
      ["ε_t", "White-noise innovation", "§2.2"]
    ]}
  />
);

export const ResultsTable = () => (
  <Table
    caption="Table 5.3 — OLS estimates with HAC standard errors"
    columns={[
      { header: "Term" },
      { header: "Estimate", numeric: true },
      { header: "Std. error", numeric: true },
      { header: "p-value", numeric: true }
    ]}
    rows={[
      ["Intercept", "0.014", "0.006", "0.021"],
      ["Trend", "0.002", "0.001", "0.088"],
      ["Lag 1", "0.631", "0.045", "<0.001"]
    ]}
  />
);
