# P9: Diagnostics and model selection

**Question this phase answers:** Does the fitted model hold up?

Residual tests on the complete model, volatility and count diagnostics, information criteria, bootstrap inference, and forecast-comparison tests; failures loop back to P6 or P7.

## Sub-diagram

**Part 1: innovation tests re-run on the complete model.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_IN(["Estimated joint model"]) --> P9_TYPE{"Innovation type?"}
    P9_TYPE -->|"Continuous"| P7_MEAN_TESTS[["Test residual autocorrelation"]]
    P9_TYPE -->|"Counts"| P7_COUNT_TESTS[["Test overdispersion of count innovations"]]
    P9_TYPE -->|"Event times"| P7_RESCALING[["Time-rescaling check of event-time residuals"]]
    P7_MEAN_TESTS --> P9_AC{"Autocorrelation left?"}
    P9_AC -.->|"Yes: mean misspecified"| P6[["P6: Conditional-mean model class"]]
    P9_AC -->|"No"| P7_VAR_TESTS[["Test conditional heteroskedasticity"]]
    P7_VAR_TESTS --> P9_ARCH{"ARCH left?"}
    P9_ARCH -.->|"Yes"| P7[["P7: Error-process specification"]]
    P9_ARCH -->|"No"| P7_DIST_TESTS[["Test the distribution of standardised innovations"]]
    P7_DIST_TESTS --> P9_DIST{"Distribution rejected?"}
    P9_DIST -.->|"Yes"| P7
    P9_DIST -->|"No"| P7_REGIME_TESTS[["Test for variance regimes"]]
    P7_REGIME_TESTS --> P9_REGIME{"Regimes left?"}
    P9_REGIME -.->|"Yes"| P7
    P9_REGIME -->|"No"| P9_MULTI{"Multivariate flag?"}
    P9_MULTI -->|"Yes"| P7_CORR_TESTS[["Test innovation correlation structure"]]
    P9_MULTI -->|"No"| P9_RESIDUAL_NONLINEARITY
    P7_CORR_TESTS --> P9_CORR{"Correlation misspecified?"}
    P9_CORR -.->|"Yes"| P7
    P9_CORR -->|"No"| P9_RESIDUAL_NONLINEARITY["Remaining nonlinearity<br/>BDS on residuals"]
    P9_RESIDUAL_NONLINEARITY --> P9_NONLINEAR{"Nonlinearity left?"}
    P9_NONLINEAR -.->|"Yes"| P6
    P9_NONLINEAR -->|"No"| P9_TO_PART_2
    P7_COUNT_TESTS --> P9_COUNT{"Dispersion misspecified?"}
    P9_COUNT -.->|"Yes"| P7
    P9_COUNT -->|"No"| P9_TO_PART_2
    P7_RESCALING --> P9_INTENSITY{"Intensity misspecified?"}
    P9_INTENSITY -.->|"Yes"| P7
    P9_INTENSITY -->|"No"| P9_TO_PART_2(["Continue in part 2"])
    class P9_IN,P9_TO_PART_2 terminator
    class P9_TYPE,P9_AC,P9_ARCH,P9_DIST,P9_REGIME,P9_MULTI,P9_CORR,P9_NONLINEAR,P9_COUNT,P9_INTENSITY decision
    class P9_RESIDUAL_NONLINEARITY process
    class P7_MEAN_TESTS,P7_COUNT_TESTS,P7_RESCALING,P6,P7_VAR_TESTS,P7,P7_DIST_TESTS,P7_REGIME_TESTS,P7_CORR_TESTS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: model-specific checks, selection and comparison.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_PART_2_IN(["From part 1"]) --> P9_MODEL_KIND{"Model kind?"}
    P9_MODEL_KIND -->|"Volatility"| P9_VOLATILITY_DIAGNOSTICS["Volatility model diagnostics<br/>standardised residuals, sign-bias test, news impact curve"]
    P9_MODEL_KIND -->|"Other"| P9_INFORMATION_CRITERIA
    P9_VOLATILITY_DIAGNOSTICS --> P9_INFORMATION_CRITERIA["Information criteria<br/>AIC, BIC, HQIC, WAIC, LOO"]
    P9_INFORMATION_CRITERIA --> P9_INFERENCE_NEEDED{"Finite-sample inference?"}
    P9_INFERENCE_NEEDED -->|"Yes"| P9_BOOTSTRAP["Bootstrap inference<br/>block, stationary, sieve"]
    P9_INFERENCE_NEEDED -->|"No"| P9_FORECAST_COMPARISON
    P9_BOOTSTRAP --> P9_FORECAST_COMPARISON["Forecast comparison tests<br/>Diebold-Mariano, Clark-West, reality check, model confidence set"]
    P9_FORECAST_COMPARISON --> P9_ENCOMPASSING["Forecast encompassing"]
    P9_ENCOMPASSING --> P9_PASS{"All diagnostics pass?"}
    P9_PASS -->|"Yes"| P9_OUT(["To P10 Inference"])
    P9_PASS -.->|"Mean misspecified"| P6[["P6: Conditional-mean model class"]]
    P9_PASS -.->|"Innovations misspecified"| P7[["P7: Error-process specification"]]
    class P9_PART_2_IN,P9_OUT terminator
    class P9_MODEL_KIND,P9_INFERENCE_NEEDED,P9_PASS decision
    class P9_VOLATILITY_DIAGNOSTICS,P9_INFORMATION_CRITERIA,P9_BOOTSTRAP,P9_FORECAST_COMPARISON,P9_ENCOMPASSING process
    class P6,P7 ref
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




## Remaining nonlinearity

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_RESIDUAL_NONLINEARITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Volatility model diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_VOLATILITY_DIAGNOSTICS`). Write this section following the content rules in `.claude/rules/writing.md`.

