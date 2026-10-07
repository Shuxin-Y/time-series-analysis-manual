# 16. Count and Categorical

Integer-valued, categorical and compositional time series.

## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B1["B1 Counts and categorical"] --> B1_COUNT_EDA["Count-data diagnostics<br/>dispersion, zeros"]
    B1_COUNT_EDA --> B1_VALUE{"Value type?"}
    B1_VALUE -->|"Counts"| B1_DISPERSION{"Overdispersed?"}
    B1_VALUE -->|"Categorical"| B1_MARKOV_CHAIN["Markov chains for categorical series"]
    B1_VALUE -->|"Compositional"| B1_COMPOSITIONAL["Compositional series<br/>log-ratio transforms, Dirichlet regression"]
    B1_DISPERSION -->|"No"| B1_INAR["INAR models"]
    B1_DISPERSION -->|"Yes"| B1_NEGATIVE_BINOMIAL["Negative-binomial autoregression"]
    B1_INAR --> B1_POISSON_AR["Poisson autoregression and INGARCH"]
    B1_NEGATIVE_BINOMIAL --> B1_GLARMA["GLARMA and dynamic generalised linear models"]
    B1_MARKOV_CHAIN --> B1_AR_LOGIT["Autoregressive logit, probit and multinomial series"]
    B1_POISSON_AR & B1_GLARMA & B1_AR_LOGIT & B1_COMPOSITIONAL --> P7_COUNT_TESTS[["Test overdispersion of count innovations"]]
    P7_COUNT_TESTS --> P8[["P8: Estimation"]]
    F_MARKOV[["Markov chains"]] -.- B1_MARKOV_CHAIN
    class B1_VALUE,B1_DISPERSION decision
    class B1,B1_COUNT_EDA,B1_MARKOV_CHAIN,B1_COMPOSITIONAL,B1_INAR,B1_NEGATIVE_BINOMIAL,B1_POISSON_AR,B1_GLARMA,B1_AR_LOGIT process
    class P7_COUNT_TESTS,P8,F_MARKOV ref
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

## INGARCH and negative-binomial innovations

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_INGARCH`). Write this section following the content rules in `.claude/rules/writing.md`.

## Count-data diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_COUNT_EDA`). Write this section following the content rules in `.claude/rules/writing.md`.

## INAR models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_INAR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Poisson autoregression and INGARCH

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_POISSON_AR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Negative-binomial autoregression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_NEGATIVE_BINOMIAL`). Write this section following the content rules in `.claude/rules/writing.md`.

## GLARMA and dynamic generalised linear models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_GLARMA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Markov chains for categorical series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_MARKOV_CHAIN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Autoregressive logit, probit and multinomial series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_AR_LOGIT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Compositional series

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B1_COMPOSITIONAL`). Write this section following the content rules in `.claude/rules/writing.md`.
