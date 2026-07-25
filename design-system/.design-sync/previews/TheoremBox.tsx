import React from "react";
import { TheoremBox } from "@tsam/design-system";

export const Assumption = () => (
  <TheoremBox title="Assumption 1: Zero Conditional Mean">
    The innovations have zero mean conditional on the regressors:
    E[εₜ | X] = 0. This is the identifying restriction for the OLS estimator.
  </TheoremBox>
);

export const Theorem = () => (
  <TheoremBox title="Theorem 4.1 (Gauss–Markov)">
    Under the classical assumptions, the OLS estimator is the best linear
    unbiased estimator: no other linear unbiased estimator has smaller
    variance.
  </TheoremBox>
);
