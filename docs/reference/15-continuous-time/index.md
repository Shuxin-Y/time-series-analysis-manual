# 15. Continuous-Time Models

Diffusions, CARMA, Levy processes, jump diffusions and numerical methods for SDEs.

## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B3["B3 Irregular sampling and continuous time"] --> B3_ROUTE{"Route?"}
    B3_ROUTE -.->|"Resample"| P0_RESAMPLE[["Resample and anti-alias"]]
    B3_ROUTE -->|"Keep the grid"| B3_IRREGULAR_KALMAN["Kalman filtering on an irregular grid"]
    B3_ROUTE -->|"Continuous time"| B3_OU["Ornstein-Uhlenbeck process and exact discretisation"]
    B3_IRREGULAR_KALMAN --> P5_FD_LOMB_SCARGLE[["Lomb-Scargle periodogram"]]
    P5_FD_LOMB_SCARGLE --> P5[["P5: Representation selection"]]
    B3_OU --> B3_CARMA["CARMA processes"]
    B3_CARMA --> B3_SDE["Diffusions and SDE discretisation<br/>Euler-Maruyama, Milstein"]
    B3_SDE --> B3_JUMPS{"Jumps?"}
    B3_JUMPS -->|"Yes"| P7_JUMPS[["Jump diffusion"]]
    B3_JUMPS -->|"No"| B3_SDE_INFERENCE
    P7_JUMPS --> B3_SDE_INFERENCE["Likelihood inference for diffusions<br/>signature methods"]
    B3_SDE_INFERENCE --> P8[["P8: Estimation"]]
    class B3_ROUTE,B3_JUMPS decision
    class B3,B3_IRREGULAR_KALMAN,B3_OU,B3_CARMA,B3_SDE,B3_SDE_INFERENCE process
    class P0_RESAMPLE,P5_FD_LOMB_SCARGLE,P5,P7_JUMPS,P8 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## B3 Irregular sampling and continuous time

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3`). Write this section following the content rules in `.claude/rules/writing.md`.

## Jump diffusion

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_JUMPS`). Write this section following the content rules in `.claude/rules/writing.md`.


## Kalman filtering on an irregular grid

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_IRREGULAR_KALMAN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Ornstein-Uhlenbeck process and exact discretisation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_OU`). Write this section following the content rules in `.claude/rules/writing.md`.

## CARMA processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_CARMA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Diffusions and SDE discretisation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_SDE`). Write this section following the content rules in `.claude/rules/writing.md`.


## Likelihood inference for diffusions

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_SDE_INFERENCE`). Write this section following the content rules in `.claude/rules/writing.md`.
