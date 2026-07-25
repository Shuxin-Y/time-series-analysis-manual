import React from "react";
import { Badge } from "@tsam/design-system";

export const Tones = () => (
  <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
    <Badge tone="neutral">Draft</Badge>
    <Badge tone="primary">Chapter 05</Badge>
    <Badge tone="good">Stationary</Badge>
    <Badge tone="escalate">Inconclusive</Badge>
    <Badge tone="problem">Unit root</Badge>
  </div>
);

export const Outcomes = () => (
  <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
    <span>ADF + KPSS verdict:</span>
    <Badge tone="good">Difference not required</Badge>
  </div>
);
