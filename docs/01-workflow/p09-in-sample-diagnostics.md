# P9: In-sample diagnostics

**Question this phase answers:** Does the fitted model hold up?

P9 reads the model kind first: a learner is checked by its validation loss from the P8 tuning windows and by pooled residual diagnostics, because a loss-minimisation fit has no likelihood and per-series tests on thousands of residual series are a multiple-testing exercise. A likelihood or Bayesian fit re-runs the P7 tests on the complete model with the corrections that estimated parameters require (Li-Mak for squared standardised residuals, bootstrap critical values for BDS, probability integral transforms against the fitted law), then checks parameter stability, roots and parameter redundancy, and compares information criteria within one model class, one transform and one differencing order. Forecast comparison and encompassing belong to P10, because they need out-of-sample errors.

What a failed diagnostic triggers depends on the purpose. The outputs of inference purposes, model-based extraction, decomposition and spectra, and simulation from a fitted model are valid only under the fitted model, so a failure loops back. Forecasting, detection and collections judge candidates out of sample, so a failure is an improvement signal and the candidate stays in the comparison set. Routes that fit no model do not pass P9.

## Sub-diagram

**Part 1: model kind, value type, mean and variance re-tests.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_IN(["Estimated candidates from P8"]) --> P9_KIND{"Model-kind flag?"}
    P9_KIND -->|"Loss minimisation"| P9_LEARNER_DIAGNOSTICS["Validation loss and pooled residual diagnostics<br/>from the P8 tuning windows"]
    P9_KIND -->|"Likelihood or Bayesian"| P9_TYPE{"Value-type flag?"}
    P9_LEARNER_DIAGNOSTICS --> P9_LEARNER_TO_PART_4(["Continue in part 4"])
    P9_TYPE -->|"Continuous"| P7_MEAN_TESTS[["Test residual autocorrelation"]]
    P9_TYPE -->|"Counts"| P7_COUNT_TESTS[["Test overdispersion of count innovations"]]
    P9_TYPE -->|"Event times"| P7_RESCALING[["Time-rescaling check of event-time residuals"]]
    P7_MEAN_TESTS --> P9_AC{"Autocorrelation left?"}
    P9_AC -.->|"Yes: mean misspecified"| P6[["P6: Conditional-mean model class"]]
    P9_AC -->|"No"| P7_VAR_TESTS[["Test conditional heteroskedasticity<br/>Li-Mak correction on standardised residuals"]]
    P7_VAR_TESTS --> P9_ARCH{"ARCH left?"}
    P9_ARCH -.->|"Yes"| P7[["P7: Error-process specification"]]
    P9_ARCH -->|"No"| P9_TO_PART_2(["Continue in part 2"])
    P7_COUNT_TESTS --> P9_COUNT{"Dispersion misspecified?"}
    P9_COUNT -.->|"Yes"| P7
    P9_COUNT -->|"No"| P9_COUNTS_TO_PART_3
    P7_RESCALING --> P9_INTENSITY{"Intensity misspecified?"}
    P9_INTENSITY -.->|"Yes"| P7
    P9_INTENSITY -->|"No"| P9_COUNTS_TO_PART_3(["Continue in part 3"])
    class P9_IN,P9_LEARNER_TO_PART_4,P9_TO_PART_2,P9_COUNTS_TO_PART_3 terminator
    class P9_KIND,P9_TYPE,P9_AC,P9_ARCH,P9_COUNT,P9_INTENSITY decision
    class P9_LEARNER_DIAGNOSTICS process
    class P7_MEAN_TESTS,P7_COUNT_TESTS,P7_RESCALING,P6,P7_VAR_TESTS,P7 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: distribution, regimes, correlation and nonlinearity.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_PART_2_IN(["From part 1"]) --> P9_QMLE_Q{"Estimated by QMLE?"}
    P9_QMLE_Q -->|"Yes: no law assumed, sandwich standard errors"| P7_REGIME_TESTS
    P9_QMLE_Q -->|"No"| P9_DIST_FIT["Test the assumed innovation distribution<br/>PIT against the fitted law; parametric bootstrap or Bai's test"]
    P9_DIST_FIT --> P9_DIST{"Fitted law rejected?"}
    P9_DIST -.->|"Yes"| P7[["P7: Error-process specification"]]
    P9_DIST -->|"No"| P7_REGIME_TESTS[["Test for variance regimes"]]
    P7_REGIME_TESTS --> P9_REGIME{"Regimes left?"}
    P9_REGIME -.->|"Yes"| P7
    P9_REGIME -->|"No"| P9_MULTI{"Multivariate flag?"}
    P9_MULTI -->|"Yes"| P7_CORR_TESTS[["Test innovation correlation structure"]]
    P9_MULTI -->|"No"| P9_RESIDUAL_NONLINEARITY
    P7_CORR_TESTS --> P9_CORR{"Correlation misspecified?"}
    P9_CORR -.->|"Yes"| P7
    P9_CORR -->|"No"| P9_RESIDUAL_NONLINEARITY["Remaining nonlinearity<br/>BDS with bootstrap critical values"]
    P9_RESIDUAL_NONLINEARITY --> P9_NONLINEAR{"Nonlinearity left?"}
    P9_NONLINEAR -.->|"Yes, from variance asymmetry"| P7
    P9_NONLINEAR -.->|"Yes, in the mean"| P6[["P6: Conditional-mean model class"]]
    P9_NONLINEAR -->|"No"| P9_TO_PART_3(["Continue in part 3"])
    class P9_PART_2_IN,P9_TO_PART_3 terminator
    class P9_QMLE_Q,P9_DIST,P9_REGIME,P9_MULTI,P9_CORR,P9_NONLINEAR decision
    class P9_DIST_FIT,P9_RESIDUAL_NONLINEARITY process
    class P7,P7_REGIME_TESTS,P7_CORR_TESTS,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: Bayesian and volatility checks, stability, roots and information criteria.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_PART_3_IN(["From parts 1 and 2"]) --> P9_BAYESIAN_Q{"Bayesian fit?"}
    P9_BAYESIAN_Q -->|"Yes"| P9_POSTERIOR_PREDICTIVE["Posterior predictive checks<br/>replicated data, Bayesian p-values, LOO-PIT"]
    P9_BAYESIAN_Q -->|"No"| P9_VOLATILITY_Q
    P9_POSTERIOR_PREDICTIVE --> P9_PPC_VERDICT{"Replicated data match?"}
    P9_PPC_VERDICT -->|"Yes"| P9_VOLATILITY_Q{"Variance model?"}
    P9_PPC_VERDICT -.->|"No: revise the model or priors"| P6[["P6: Conditional-mean model class"]]
    P9_VOLATILITY_Q -->|"Yes"| P9_VOLATILITY_DIAGNOSTICS["Volatility model diagnostics<br/>standardised residuals, sign-bias test, news impact curve"]
    P9_VOLATILITY_Q -->|"No"| P9_STABILITY
    P9_VOLATILITY_DIAGNOSTICS --> P9_STABILITY["Parameter-stability tests<br/>recursive estimates, CUSUM, CUSUMSQ, Nyblom, Hansen, Andrews sup-F; VAR stability"]
    P9_STABILITY --> P9_STABLE{"Parameters stable?"}
    P9_STABLE -.->|"No: breaks"| P4_BREAK_HANDLING[["Handle breaks and explosive episodes"]]
    P9_STABLE -.->|"No: drifting or switching"| P6
    P9_STABLE -->|"Yes"| P9_ROOTS["Roots, invertibility and parameter redundancy<br/>MA root near -1, AR root near 1, cancelling roots, companion eigenvalues"]
    P9_ROOTS --> P9_ROOTS_OK{"Roots and orders adequate?"}
    P9_ROOTS_OK -.->|"No: integration order or transform"| P3[["P3: Exploratory diagnostics"]]
    P9_ROOTS_OK -.->|"No: redundant parameters"| P6
    P9_ROOTS_OK -->|"Yes"| P9_INFORMATION_CRITERIA["Information criteria<br/>within one model class, one transform and one differencing order"]
    P9_INFORMATION_CRITERIA --> P9_INFERENCE_NEEDED{"Finite-sample inference?"}
    P9_INFERENCE_NEEDED -->|"Yes"| P9_BOOTSTRAP["Bootstrap inference<br/>block, stationary, sieve"]
    P9_INFERENCE_NEEDED -->|"No"| P9_TO_PART_4
    P9_BOOTSTRAP --> P9_TO_PART_4(["Continue in part 4"])
    class P9_PART_3_IN,P9_TO_PART_4 terminator
    class P9_BAYESIAN_Q,P9_PPC_VERDICT,P9_VOLATILITY_Q,P9_STABLE,P9_ROOTS_OK,P9_INFERENCE_NEEDED decision
    class P9_POSTERIOR_PREDICTIVE,P9_VOLATILITY_DIAGNOSTICS,P9_STABILITY,P9_ROOTS,P9_INFORMATION_CRITERIA,P9_BOOTSTRAP process
    class P6,P4_BREAK_HANDLING,P3 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: the gate, by purpose.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_PART_4_IN(["From parts 1 and 3"]) --> P9_PASS{"All diagnostics pass?"}
    P9_PASS -->|"Yes"| P9_OUT(["To P10 Out-of-sample evaluation and selection"])
    P9_PASS -->|"No"| P9_GATE{"Purpose flag?"}
    P9_GATE -->|"Forecasting, detection, collections: keep as candidate"| P9_OUT
    P9_GATE -->|"Inference, model-based extraction, decomposition or spectra, simulation"| P9_WHERE{"Which part is misspecified?"}
    P9_WHERE -.->|"Mean"| P6[["P6: Conditional-mean model class"]]
    P9_WHERE -.->|"Innovations"| P7[["P7: Error-process specification"]]
    P9_WHERE -.->|"Integration order or transform"| P3[["P3: Exploratory diagnostics"]]
    class P9_PART_4_IN,P9_OUT terminator
    class P9_PASS,P9_GATE,P9_WHERE decision
    class P6,P7,P3 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Phase guide

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9`). Write this section following the content rules in `.claude/rules/writing.md`.

## Test the assumed innovation distribution

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_DIST_FIT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Remaining nonlinearity

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_RESIDUAL_NONLINEARITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Posterior predictive checks

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_POSTERIOR_PREDICTIVE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Volatility model diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_VOLATILITY_DIAGNOSTICS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Parameter-stability tests

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_STABILITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Roots, invertibility and parameter redundancy

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_ROOTS`). Write this section following the content rules in `.claude/rules/writing.md`.
