# 17. Point Processes

The B2 branch: Poisson, renewal and Cox processes, Hawkes, marked and neural point processes, survival and hazard models, and intensity misspecification. Durations live in area 14 and degradation models in area 26. The branch chart is an index over the spine: clustering of events can come from self-excitation or from a random intensity, so every candidate intensity model is fitted and the candidates are compared in P10, and every model is checked after estimation. The page also hosts: fit every candidate intensity, check the degradation increments.

## Branch sub-diagram

**Part 1: event intensity.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B2["B2 Event times"] --> P3[["P3: Exploratory diagnostics"]]
    P3 --> B2_EVENT_EDA["Event-time diagnostics<br/>intensity, inter-event distributions, time-varying baseline"]
    B2_EVENT_EDA --> B2_QUESTION{"Object of interest?"}
    B2_QUESTION -->|"Event intensity"| P6[["P6: Conditional-mean model class"]]
    B2_QUESTION -->|"Durations or time to failure"| B2_TO_PART_2(["Continue in part 2"])
    P6 --> B2_MARKS{"Marks or several streams?"}
    B2_MARKS -->|"Yes"| B2_MARKED["Marked and multivariate point processes<br/>Poisson, Cox or Hawkes with marks"]
    B2_MARKS -->|"No"| B2_FIT_ALL["Fit every candidate intensity<br/>deterministic, random, self-exciting, learned; compared in P10"]
    B2_FIT_ALL --> B2_POISSON["Poisson and renewal processes<br/>inhomogeneous Poisson; renewal through the hazard of the age"]
    B2_FIT_ALL --> B2_COX["Doubly stochastic (Cox) processes"]
    B2_FIT_ALL --> B2_HAWKES["Hawkes self-exciting processes<br/>with a time-varying baseline"]
    B2_FIT_ALL --> B2_NEURAL_PP["Neural point processes"]
    B2_MARKED & B2_POISSON & B2_COX & B2_HAWKES & B2_NEURAL_PP --> P6_KIND_FLAG[["Set flag: model kind"]]
    P6_KIND_FLAG --> P7[["P7: Error-process specification"]]
    class P6_KIND_FLAG ref
    P7 --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> P7_RESCALING[["Time-rescaling check of event-time residuals"]]
    P7_RESCALING --> B2_OUT(["Continue on the spine at P10, comparing the candidates"])
    class B2_TO_PART_2,B2_OUT terminator
    class B2_QUESTION,B2_MARKS decision
    class B2,B2_EVENT_EDA,B2_FIT_ALL,B2_MARKED,B2_POISSON,B2_COX,B2_HAWKES,B2_NEURAL_PP process
    class P3,P6,P7,P8,P9,P7_RESCALING ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: durations and time to failure.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B2_PART_2_IN(["From part 1"]) --> P6[["P6: Conditional-mean model class"]]
    P6 --> B2_QUESTION_2{"Object of interest?"}
    B2_QUESTION_2 -->|"Durations"| B2_ACD["Autoregressive conditional duration"]
    B2_QUESTION_2 -->|"Time to failure"| B2_FAILURE{"Data?"}
    B2_FAILURE -->|"Failure times"| B2_SURVIVAL["Survival and hazard models<br/>Cox proportional hazards"]
    B2_FAILURE -->|"Degradation signal"| B2_DEGRADATION["Degradation processes and remaining useful life<br/>Wiener and gamma processes"]
    B2_ACD & B2_SURVIVAL & B2_DEGRADATION --> P6_KIND_FLAG[["Set flag: model kind"]]
    P6_KIND_FLAG --> P7[["P7: Error-process specification"]]
    class P6_KIND_FLAG ref
    P7 --> P8[["P8: Estimation"]]
    P8 --> P9[["P9: In-sample diagnostics"]]
    P9 --> B2_CHECK{"Residual check?"}
    B2_CHECK -->|"Durations, failure times"| P7_RESCALING[["Time-rescaling check of event-time residuals<br/>standardised durations, Cox-Snell residuals"]]
    B2_CHECK -->|"Degradation paths"| B2_INCREMENT_CHECK["Check the degradation increments<br/>independence, Gaussian or gamma increments"]
    P7_RESCALING & B2_INCREMENT_CHECK --> B2_PART_2_OUT(["Continue on the spine at P10"])
    class B2_PART_2_IN,B2_PART_2_OUT terminator
    class B2_QUESTION_2,B2_FAILURE,B2_CHECK decision
    class B2_ACD,B2_SURVIVAL,B2_DEGRADATION,B2_INCREMENT_CHECK process
    class P6,P7,P8,P9,P7_RESCALING ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## B2 Event times

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2`). Write this section following the content rules in `.claude/rules/writing.md`.

## Event-time diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_EVENT_EDA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Fit every candidate intensity

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_FIT_ALL`). Write this section following the content rules in `.claude/rules/writing.md`.

## Marked and multivariate point processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_MARKED`). Write this section following the content rules in `.claude/rules/writing.md`.

## Poisson and renewal processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_POISSON`). Write this section following the content rules in `.claude/rules/writing.md`.

## Doubly stochastic (Cox) processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_COX`). Write this section following the content rules in `.claude/rules/writing.md`.

## Hawkes self-exciting processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_HAWKES`). Write this section following the content rules in `.claude/rules/writing.md`.

## Neural point processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_NEURAL_PP`). Write this section following the content rules in `.claude/rules/writing.md`.

## Intensity misspecification

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_INTENSITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Survival and hazard models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_SURVIVAL`). Write this section following the content rules in `.claude/rules/writing.md`.

## Check the degradation increments

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_INCREMENT_CHECK`). Write this section following the content rules in `.claude/rules/writing.md`.
