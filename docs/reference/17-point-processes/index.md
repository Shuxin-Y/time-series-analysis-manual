# 17. Point Processes

Poisson, renewal, Cox and Hawkes processes; marked and neural point processes.

## Branch sub-diagram

**Part 1: event intensity.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B2["B2 Event times"] --> B2_EVENT_EDA["Event-time diagnostics<br/>intensity, inter-event distributions"]
    B2_EVENT_EDA --> B2_QUESTION{"Object of interest?"}
    B2_QUESTION -->|"Event intensity"| B2_CLUSTERING{"Self-exciting?"}
    B2_QUESTION -->|"Durations or time to failure"| B2_TO_PART_2(["Continue in part 2"])
    B2_CLUSTERING -->|"No"| B2_BASELINE{"Intensity?"}
    B2_CLUSTERING -->|"Yes"| B2_EXCITATION{"Excitation model?"}
    B2_BASELINE -->|"Deterministic"| B2_POISSON["Poisson and renewal processes"]
    B2_BASELINE -->|"Random"| B2_COX["Cox processes"]
    B2_EXCITATION -->|"Parametric kernel"| B2_HAWKES["Hawkes self-exciting processes"]
    B2_EXCITATION -->|"Marks or several streams"| B2_MARKED["Marked and multivariate point processes"]
    B2_EXCITATION -->|"Learned intensity"| B2_NEURAL_PP["Neural point processes"]
    B2_POISSON & B2_COX & B2_HAWKES & B2_MARKED & B2_NEURAL_PP --> P7_RESCALING[["Time-rescaling check of event-time residuals"]]
    P7_RESCALING --> P8[["P8: Estimation"]]
    class B2_TO_PART_2 terminator
    class B2_QUESTION,B2_CLUSTERING,B2_BASELINE,B2_EXCITATION decision
    class B2,B2_EVENT_EDA,B2_POISSON,B2_COX,B2_HAWKES,B2_MARKED,B2_NEURAL_PP process
    class P7_RESCALING,P8 ref
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
    B2_PART_2_IN(["From part 1"]) --> B2_QUESTION_2{"Object of interest?"}
    B2_QUESTION_2 -->|"Durations"| B2_ACD["Autoregressive conditional duration"]
    B2_QUESTION_2 -->|"Time to failure"| B2_FAILURE{"Data?"}
    B2_FAILURE -->|"Failure times"| B2_SURVIVAL["Survival and hazard models<br/>Cox proportional hazards"]
    B2_FAILURE -->|"Degradation signal"| B2_DEGRADATION["Degradation processes and remaining useful life<br/>Wiener and gamma processes"]
    B2_ACD & B2_SURVIVAL & B2_DEGRADATION --> P7_RESCALING[["Time-rescaling check of event-time residuals"]]
    P7_RESCALING --> P8[["P8: Estimation"]]
    class B2_PART_2_IN terminator
    class B2_QUESTION_2,B2_FAILURE decision
    class B2_ACD,B2_SURVIVAL,B2_DEGRADATION process
    class P7_RESCALING,P8 ref
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

## Intensity misspecification

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_INTENSITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Event-time diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_EVENT_EDA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Poisson and renewal processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_POISSON`). Write this section following the content rules in `.claude/rules/writing.md`.

## Cox processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_COX`). Write this section following the content rules in `.claude/rules/writing.md`.

## Hawkes self-exciting processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_HAWKES`). Write this section following the content rules in `.claude/rules/writing.md`.

## Marked and multivariate point processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_MARKED`). Write this section following the content rules in `.claude/rules/writing.md`.

## Neural point processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_NEURAL_PP`). Write this section following the content rules in `.claude/rules/writing.md`.

## Survival and hazard models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_SURVIVAL`). Write this section following the content rules in `.claude/rules/writing.md`.
