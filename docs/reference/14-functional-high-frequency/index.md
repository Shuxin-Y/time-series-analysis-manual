# 14. Functional and High-Frequency

The B4 branch (series as curves, intraday curve alignment, basis smoothing, functional principal components, functional regression) and autoregressive conditional durations. Survival models live in area 17 and realised volatility in area 10.

## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B4["B4 Functional"] --> B4_CURVES["Series as curves<br/>when functional data analysis applies"]
    B4_CURVES --> B4_INTRADAY["Intraday seasonality and curve alignment"]
    B4_INTRADAY --> P5_FN_BASIS[["Basis representation and smoothing of curves"]]
    P5_FN_BASIS --> P5[["P5: Representation selection"]]
    class B4,B4_CURVES,B4_INTRADAY process
    class P5_FN_BASIS,P5 ref
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

## Basis representation and smoothing of curves

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_BASIS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Functional principal components

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_FPCA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Functional regression and functional autoregression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P5_FN_REGRESSION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Autoregressive conditional duration

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B2_ACD`). Write this section following the content rules in `.claude/rules/writing.md`.


## Series as curves

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B4_CURVES`). Write this section following the content rules in `.claude/rules/writing.md`.

## Intraday seasonality and curve alignment

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B4_INTRADAY`). Write this section following the content rules in `.claude/rules/writing.md`.
