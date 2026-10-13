# 16. Count and Categorical

The B1 branch: count diagnostics, INAR, Poisson and negative-binomial autoregression, GLARMA, zero-inflated and hurdle counts, Poisson hidden Markov models, Markov chains, autoregressive logit and probit, compositional series, and the choice of count innovations. The branch chart is an index over the spine: it draws the phases a count, categorical or compositional series passes, with this chapter's leaves inside them, and returns to the spine at P10.

## Branch sub-diagram

**Part 1: diagnostics and value type.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1["B1 Counts and categorical"] --> P3[["P3: Exploratory diagnostics"]]
    P3 --> B1_VALUE{"Value type?"}
    B1_VALUE -->|"Counts or categorical"| B1_COUNT_EDA["Count-data diagnostics<br/>zeros, dispersion, trend, seasonality, covariates"]
    B1_VALUE -->|"Compositional"| B1_COMPOSITIONAL["Compositional series<br/>log-ratio transforms; every later test runs on the log-ratios"]
    B1_COUNT_EDA --> B1_TO_PART_2(["Continue in part 2"])
    B1_COMPOSITIONAL --> B1_MULTIVARIATE_FLAG["Set flag: multivariate"]
    B1_MULTIVARIATE_FLAG --> B1_COMPOSITIONAL_OUT(["Continue on the spine at P3, as log-ratios"])
    class B1_TO_PART_2,B1_COMPOSITIONAL_OUT terminator
    class B1_VALUE decision
    class B1,B1_COUNT_EDA,B1_COMPOSITIONAL,B1_MULTIVARIATE_FLAG process
    class P3 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: count models with dynamics in the mean.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1_PART_2_IN(["From part 1"]) --> P6[["P6: Conditional-mean model class"]]
    P6 --> B1_KIND{"Counts or categories?"}
    B1_KIND -->|"Categories"| B1_TO_PART_5(["Continue in part 5"])
    B1_KIND -->|"Counts"| B1_POOLING{"Pooling flag?"}
    B1_POOLING -->|"Global, or compare"| P6_GLOBAL_MODELS[["Global models across many series<br/>count loss: Poisson, Tweedie, negative binomial"]]
    B1_POOLING -->|"Local"| B1_COUNT_FAMILY{"Count model family?"}
    B1_COUNT_FAMILY -->|"Zeros, states or intermittency"| B1_TO_PART_3(["Continue in part 3"])
    B1_COUNT_FAMILY -->|"Thinning"| B1_INAR["INAR models"]
    B1_COUNT_FAMILY -->|"Intensity"| B1_POISSON_AR["Poisson and negative-binomial autoregression<br/>INGARCH"]
    B1_COUNT_FAMILY -->|"GLM"| B1_GLARMA["GLARMA and dynamic generalised linear models"]
    B1_INAR & B1_POISSON_AR & B1_GLARMA & P6_GLOBAL_MODELS --> B1_TO_PART_4(["Continue in part 4"])
    class B1_PART_2_IN,B1_TO_PART_3,B1_TO_PART_4,B1_TO_PART_5 terminator
    class B1_KIND,B1_POOLING,B1_COUNT_FAMILY decision
    class B1_INAR,B1_POISSON_AR,B1_GLARMA process
    class P6,P6_GLOBAL_MODELS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: excess zeros, hidden states and intermittent demand.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1_PART_3_IN(["From part 2"]) --> B1_ZEROS{"Feature?"}
    B1_ZEROS -->|"Excess zeros"| B1_ZERO_INFLATED["Zero-inflated and hurdle count models"]
    B1_ZEROS -->|"Hidden states"| B1_POISSON_HMM["Poisson hidden Markov models"]
    B1_ZEROS -->|"Intermittent demand"| P6_INTERMITTENT[["Intermittent demand"]]
    B1_ZERO_INFLATED & B1_POISSON_HMM & P6_INTERMITTENT --> B1_PART_3_OUT(["Continue in part 4"])
    class B1_PART_3_IN,B1_PART_3_OUT terminator
    class B1_ZEROS decision
    class B1_ZERO_INFLATED,B1_POISSON_HMM process
    class P6_INTERMITTENT ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: count innovations, estimation and diagnostics.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1_PART_4_IN(["From parts 2 and 3"]) --> P7[["P7: Error-process specification"]]
    P7 --> P7_COUNT_TESTS[["Test overdispersion of count innovations"]]
    P7_COUNT_TESTS --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> B1_OUT(["Continue on the spine at P10"])
    class B1_PART_4_IN,B1_OUT terminator
    class P7,P7_COUNT_TESTS,P8,P9 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: categorical series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1_PART_5_IN(["From part 2"]) --> B1_CATEGORICAL_Q{"State count and covariates?"}
    B1_CATEGORICAL_Q -->|"Few states, no covariates"| B1_MARKOV_CHAIN["Markov chains for categorical series"]
    B1_CATEGORICAL_Q -->|"Covariates or ordered states"| B1_AR_LOGIT["Autoregressive logit, probit and multinomial series"]
    B1_MARKOV_CHAIN & B1_AR_LOGIT --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> B1_PART_5_OUT(["Continue on the spine at P10"])
    F_MARKOV[["Markov chains"]] -.- B1_MARKOV_CHAIN
    class B1_PART_5_IN,B1_PART_5_OUT terminator
    class B1_CATEGORICAL_Q decision
    class B1_MARKOV_CHAIN,B1_AR_LOGIT process
    class P8,P9,F_MARKOV ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## B1 Counts and categorical

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1`). Write this section following the content rules in `.claude/rules/writing.md`.

## Count-data diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_COUNT_EDA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Compositional series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_COMPOSITIONAL`). Write this section following the content rules in `.claude/rules/writing.md`.

## INAR models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_INAR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Poisson and negative-binomial autoregression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_POISSON_AR`). Write this section following the content rules in `.claude/rules/writing.md`.

## GLARMA and dynamic generalised linear models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_GLARMA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Zero-inflated and hurdle count models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_ZERO_INFLATED`). Write this section following the content rules in `.claude/rules/writing.md`.

## Poisson hidden Markov models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_POISSON_HMM`). Write this section following the content rules in `.claude/rules/writing.md`.

## Markov chains for categorical series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_MARKOV_CHAIN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Autoregressive logit, probit and multinomial series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_AR_LOGIT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Count innovations: Poisson or negative binomial

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_INGARCH`). Write this section following the content rules in `.claude/rules/writing.md`.
