import React from "react";
import { DefinitionBox } from "@tsam/design-system";

export const Term = () => (
  <DefinitionBox title="Stationarity">
    A series is covariance-stationary if its mean, variance, and
    autocovariances do not change over time. Only the lag between two
    observations matters, not their absolute position.
  </DefinitionBox>
);

export const Estimator = () => (
  <DefinitionBox title="Autocovariance function">
    The autocovariance at lag k is the covariance between yₜ and yₜ₋ₖ,
    γ(k) = Cov(yₜ, yₜ₋ₖ). For a stationary series it depends only on k.
  </DefinitionBox>
);
