# P9: Diagnostics and model selection

**Question this phase answers:** Does the fitted model hold up?

Residual tests on the complete model, volatility and count diagnostics, information criteria, bootstrap inference, and forecast-comparison tests; failures loop back to P6 or P7.

## Sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P9_IN(["Estimated joint model"]) --> P9_RESIDUAL_AUTOCORRELATION["Residual autocorrelation tests<br/>Ljung-Box, Breusch-Godfrey, Durbin-Watson"]
    P9_RESIDUAL_AUTOCORRELATION --> P9_AC{"Autocorrelation left?"}
    P9_AC -.->|"Yes"| P6[["P6: Conditional-mean model class"]]
    P9_AC -->|"No"| P9_RESIDUAL_ARCH["Residual heteroskedasticity tests<br/>ARCH-LM, McLeod-Li"]
    P9_RESIDUAL_ARCH --> P9_ARCH{"ARCH left?"}
    P9_ARCH -.->|"Yes"| P7[["P7: Error-process specification"]]
    P9_ARCH -->|"No"| P9_RESIDUAL_NORMALITY["Residual normality tests<br/>Jarque-Bera"]
    P9_RESIDUAL_NORMALITY --> P9_RESIDUAL_NONLINEARITY["Remaining nonlinearity<br/>BDS on residuals"]
    P9_RESIDUAL_NONLINEARITY --> P9_MODEL_KIND{"Model kind?"}
    P9_MODEL_KIND -->|"Volatility"| P9_VOLATILITY_DIAGNOSTICS["Volatility model diagnostics<br/>standardised residuals, sign-bias test, news impact curve"]
    P9_MODEL_KIND -->|"Counts"| P9_COUNT_DIAGNOSTICS["Count model diagnostics<br/>overdispersion, zero inflation"]
    P9_MODEL_KIND -->|"Other"| P9_INFORMATION_CRITERIA
    P9_VOLATILITY_DIAGNOSTICS & P9_COUNT_DIAGNOSTICS --> P9_INFORMATION_CRITERIA["Information criteria<br/>AIC, BIC, HQIC, WAIC, LOO"]
    P9_INFORMATION_CRITERIA --> P9_INFERENCE_NEEDED{"Finite-sample inference?"}
    P9_INFERENCE_NEEDED -->|"Yes"| P9_BOOTSTRAP["Bootstrap inference<br/>block, stationary, sieve"]
    P9_INFERENCE_NEEDED -->|"No"| P9_FORECAST_COMPARISON
    P9_BOOTSTRAP --> P9_FORECAST_COMPARISON["Forecast comparison tests<br/>Diebold-Mariano, Clark-West, reality check, model confidence set"]
    P9_FORECAST_COMPARISON --> P9_ENCOMPASSING["Forecast encompassing"]
    P9_ENCOMPASSING --> P9_PASS{"All diagnostics pass?"}
    P9_PASS -->|"Yes"| P9_OUT(["To P10 Inference"])
    P9_PASS -.->|"No"| P6
    class P9_IN,P9_OUT terminator
    class P9_AC,P9_ARCH,P9_MODEL_KIND,P9_INFERENCE_NEEDED,P9_PASS decision
    class P9_RESIDUAL_AUTOCORRELATION,P9_RESIDUAL_ARCH,P9_RESIDUAL_NORMALITY,P9_RESIDUAL_NONLINEARITY,P9_VOLATILITY_DIAGNOSTICS,P9_COUNT_DIAGNOSTICS,P9_INFORMATION_CRITERIA,P9_BOOTSTRAP,P9_FORECAST_COMPARISON,P9_ENCOMPASSING process
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

## Residual autocorrelation tests

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_RESIDUAL_AUTOCORRELATION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Residual heteroskedasticity tests

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_RESIDUAL_ARCH`). Write this section following the content rules in `.claude/rules/writing.md`.

## Residual normality tests

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_RESIDUAL_NORMALITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Remaining nonlinearity

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_RESIDUAL_NONLINEARITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Volatility model diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_VOLATILITY_DIAGNOSTICS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Count model diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P9_COUNT_DIAGNOSTICS`). Write this section following the content rules in `.claude/rules/writing.md`.
