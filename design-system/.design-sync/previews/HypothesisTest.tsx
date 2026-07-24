import React from "react";
import { HypothesisTest } from "@tsam/design-system";

export const ADF = () => (
  <HypothesisTest
    title="Augmented Dickey–Fuller Test"
    nullHypothesis="The series has a unit root (non-stationary): γ = 0."
    altHypothesis="The series is stationary: γ < 0."
    decisionRule="reject when the p-value falls below α = 0.05."
  />
);

export const LjungBox = () => (
  <HypothesisTest
    title="Ljung–Box Test"
    nullHypothesis="The residual autocorrelations up to lag m are jointly zero."
    altHypothesis="At least one autocorrelation up to lag m is non-zero."
    decisionRule="reject when Q exceeds the χ² critical value at α = 0.05."
  />
);

export const NoRule = () => (
  <HypothesisTest
    title="KPSS Test"
    nullHypothesis="The series is trend-stationary."
    altHypothesis="The series has a unit root."
  />
);
