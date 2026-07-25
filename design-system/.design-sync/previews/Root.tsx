import React from "react";
import { Root, Heading, Admonition, Badge } from "@tsam/design-system";

export const LightTheme = () => (
  <Root theme="light">
    <div style={{ padding: 20 }}>
      <Heading level={2}>Stationarity</Heading>
      <p>
        A stationary series is the foundation for classical time-series
        models. <Badge tone="good">Ready to model</Badge>
      </p>
      <Admonition type="definition" title="Stationarity">
        Mean, variance, and autocovariances are constant over time.
      </Admonition>
    </div>
  </Root>
);

export const DarkTheme = () => (
  <Root theme="dark">
    <div style={{ padding: 20 }}>
      <Heading level={2}>Stationarity</Heading>
      <p>
        The same content, rendered in the dark scheme.{" "}
        <Badge tone="problem">Unit root</Badge>
      </p>
      <Admonition type="theorem" title="Theorem 3.2">
        Every covariance-stationary process has a Wold decomposition.
      </Admonition>
    </div>
  </Root>
);
