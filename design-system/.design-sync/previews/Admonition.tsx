import React from "react";
import { Admonition } from "@tsam/design-system";

export const Note = () => (
  <Admonition type="note" title="Remark">
    The lag operator L shifts a series back one step, so that L·yₜ = yₜ₋₁.
    Polynomials in L factor exactly like ordinary polynomials.
  </Admonition>
);

export const Theorem = () => (
  <Admonition type="theorem" title="Theorem 3.2 (Wold Decomposition)">
    Every covariance-stationary process admits a unique representation as the
    sum of a deterministic component and an infinite moving average of
    white-noise innovations.
  </Admonition>
);

export const Definition = () => (
  <Admonition type="definition" title="Estimator">
    An estimator is a procedure that maps observed data to parameter values
    within a chosen model class.
  </Admonition>
);

export const Abstract = () => (
  <Admonition type="abstract" title="Chapter overview">
    This chapter bridges the time and frequency domains, showing how the
    autocovariance function and the spectral density carry the same
    information.
  </Admonition>
);

export const Warning = () => (
  <Admonition type="warning" title="Look-ahead bias">
    Never fit a scaler on the full series before splitting. Standardize using
    training-set statistics only, or the backtest is optimistic.
  </Admonition>
);

export const Tip = () => (
  <Admonition type="tip" title="Practical guidance">
    When ADF and KPSS disagree, inspect the series for a structural break
    before differencing.
  </Admonition>
);

export const Question = () => (
  <Admonition type="question" title="Open question">
    Does the series contain a deterministic trend, a stochastic trend, or
    both?
  </Admonition>
);
