# 14. Functional and High-Frequency

The B4 branch (series as curves, basis smoothing, sparse curves, curve registration, functional principal components, functional regression) and autoregressive conditional durations. Ultra-high-frequency (tick) data is irregularly sampled (B3, area 15) and summarised by realised measures (area 10); survival models live in area 17. The page also hosts: sparse curves by pooled covariance estimation.

## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B4["B4 Functional"] --> B4_CURVES["Series as curves<br/>when functional data analysis applies"]
    B4_CURVES --> P5[["P5: Representation selection"]]
    P5 --> P5_FN_DENSE[["Dense sampling per curve?"]]
    P5_FN_DENSE -->|"Yes"| P5_FN_BASIS[["Basis representation and smoothing of curves"]]
    P5_FN_DENSE -->|"No"| P5_FN_PACE[["Sparse curves by pooled covariance estimation"]]
    P5_FN_BASIS & P5_FN_PACE --> B4_PHASE{"Phase variation present, and a nuisance?"}
    B4_PHASE -->|"Yes"| B4_INTRADAY["Curve registration<br/>warping after smoothing; intraday seasonality as a domain case"]
    B4_PHASE -->|"No: timing carries information"| P6[["P6: Conditional-mean model class"]]
    B4_INTRADAY --> P6
    P6 --> P6_KIND_FLAG[["Set flag: model kind"]]
    P6_KIND_FLAG --> B4_OUT(["Continue on the spine at P7"])
    class P6_KIND_FLAG ref
    class B4_OUT terminator
    class B4_PHASE decision
    class B4,B4_CURVES,B4_INTRADAY process
    class P5,P5_FN_DENSE,P5_FN_BASIS,P5_FN_PACE,P6 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## B4 Functional

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B4`). Write this section following the content rules in `.claude/rules/writing.md`.

## Series as curves

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B4_CURVES`). Write this section following the content rules in `.claude/rules/writing.md`.

## Basis representation and smoothing of curves

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_BASIS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Sparse curves by pooled covariance estimation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_PACE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Curve registration

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B4_INTRADAY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Functional principal components

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_FPCA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Functional regression and functional autoregression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_REGRESSION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Autoregressive conditional duration

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_ACD`). Write this section following the content rules in `.claude/rules/writing.md`.
