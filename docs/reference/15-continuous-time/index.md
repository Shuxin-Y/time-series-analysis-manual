# 15. Continuous-Time Models

The B3 branch (informative sampling times, sampling-pattern diagnostics, the Ornstein-Uhlenbeck process, CARMA, fractional processes in continuous time, SDE discretisation, Kalman filtering on an irregular grid, likelihood inference for diffusions) and jump diffusion. Brownian motion and Levy processes are a Part 0 foundation. The branch chart is an index over the spine for a series that keeps its irregular times: the process type is chosen first, its exact discretisation over each interval defines the Kalman filter, and the filter gives the prediction-error likelihood.

## Branch sub-diagram

**Part 1: sampling times, diagnostics and representation.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B3["B3 Irregular sampling and continuous time"] --> B3_INFORMATIVE{"Sampling times informative?"}
    B3_INFORMATIVE -->|"Yes: times depend on the process"| B3_JOINT_SAMPLING["Joint model of the observation times<br/>marked point process, inverse-intensity weighting"]
    B3_INFORMATIVE -->|"No"| B3_ROUTE{"Resample to a regular grid?"}
    B3_JOINT_SAMPLING --> B3_ROUTE
    B3_ROUTE -.->|"Yes, purpose allows: interpolation lowers high-frequency power"| P1_RESAMPLE[["Resample and anti-alias"]]
    B3_ROUTE -->|"No: keep the irregular times"| P3[["P3: Exploratory diagnostics"]]
    P3 --> B3_DIAGNOSTICS["Sampling-pattern and trend diagnostics<br/>interval distribution, window function, variogram"]
    B3_DIAGNOSTICS --> P5[["P5: Representation selection"]]
    P5 --> P5_FD_LOMB_SCARGLE[["Lomb-Scargle periodogram<br/>exploratory; window function, false-alarm probability"]]
    P5_FD_LOMB_SCARGLE --> B3_TO_PART_2(["Continue in part 2"])
    class B3_TO_PART_2 terminator
    class B3_INFORMATIVE,B3_ROUTE decision
    class B3,B3_JOINT_SAMPLING,B3_DIAGNOSTICS process
    class P1_RESAMPLE,P3,P5,P5_FD_LOMB_SCARGLE ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: process type, discretisation and estimation.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B3_PART_2_IN(["From part 1"]) --> P6[["P6: Conditional-mean model class"]]
    P6 --> B3_PROCESS{"Process type?"}
    B3_PROCESS -->|"Mean-reverting Gaussian"| B3_OU["Ornstein-Uhlenbeck process and exact discretisation"]
    B3_PROCESS -->|"Higher-order linear"| B3_CARMA["CARMA processes"]
    B3_PROCESS -->|"Long memory"| B3_FBM["Fractional processes in continuous time<br/>fBm, fractional OU, CARFIMA at the observed times"]
    B3_PROCESS -->|"Nonlinear diffusion"| B3_SDE["Diffusions and SDE discretisation<br/>Euler-Maruyama, Milstein"]
    B3_OU & B3_CARMA & B3_FBM & B3_SDE --> P7[["P7: Error-process specification"]]
    P7 --> B3_JUMPS{"Jumps in a diffusion?"}
    B3_JUMPS -->|"Yes"| P7_JUMPS[["Jump diffusion"]]
    B3_JUMPS -->|"No"| P8
    P7_JUMPS --> P8[["P8: Estimation"]]
    P8 --> B3_ESTIMATOR{"Model?"}
    B3_ESTIMATOR -->|"OU or CARMA"| B3_IRREGULAR_KALMAN["Kalman filtering on an irregular grid<br/>transition from the exact discretisation over each interval"]
    B3_ESTIMATOR -->|"Fractional: exact Gaussian likelihood at the observed times"| P9
    B3_ESTIMATOR -->|"Nonlinear diffusion"| B3_SDE_INFERENCE["Likelihood inference for diffusions<br/>Euler pseudo-likelihood and its bias, Ait-Sahalia expansions, simulated likelihood, MCMC"]
    B3_IRREGULAR_KALMAN & B3_SDE_INFERENCE --> P9[["P9: In-sample diagnostics"]]
    P9 --> B3_OUT(["Continue on the spine at P10"])
    class B3_PART_2_IN,B3_OUT terminator
    class B3_PROCESS,B3_JUMPS,B3_ESTIMATOR decision
    class B3_OU,B3_CARMA,B3_FBM,B3_SDE,B3_IRREGULAR_KALMAN,B3_SDE_INFERENCE process
    class P6,P7,P7_JUMPS,P8,P9 ref
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

## Joint model of the observation times

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_JOINT_SAMPLING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Sampling-pattern and trend diagnostics

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_DIAGNOSTICS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Ornstein-Uhlenbeck process and exact discretisation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_OU`). Write this section following the content rules in `.claude/rules/writing.md`.

## CARMA processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_CARMA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Fractional processes in continuous time

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_FBM`). Write this section following the content rules in `.claude/rules/writing.md`.

## Diffusions and SDE discretisation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_SDE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Jump diffusion

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P7_JUMPS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Kalman filtering on an irregular grid

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_IRREGULAR_KALMAN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Likelihood inference for diffusions

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B3_SDE_INFERENCE`). Write this section following the content rules in `.claude/rules/writing.md`.
