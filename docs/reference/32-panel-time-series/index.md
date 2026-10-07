# 32. Panel Time Series

Panel unit roots and cointegration, dynamic panel GMM, heterogeneous panels and cross-sectional dependence.

## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B6["B6 Wide panel"] --> B6_PANEL_UNIT_ROOT["Panel unit-root and cointegration tests"]
    B6_PANEL_UNIT_ROOT --> B6_DYNAMIC{"Lagged dependent variable?"}
    B6_DYNAMIC -->|"No"| B6_STATIC_PANEL["Fixed and random effects"]
    B6_DYNAMIC -->|"Yes"| B6_DYNAMIC_PANEL["Dynamic panel GMM<br/>Arellano-Bond"]
    B6_STATIC_PANEL & B6_DYNAMIC_PANEL --> B6_HETERO{"Heterogeneous slopes?"}
    B6_HETERO -->|"Yes"| B6_HETEROGENEOUS["Heterogeneous panels<br/>mean group, pooled mean group"]
    B6_HETERO -->|"No"| B6_CROSS_SECTION_DEPENDENCE
    B6_HETEROGENEOUS --> B6_CROSS_SECTION_DEPENDENCE["Cross-sectional dependence<br/>CD test, common correlated effects"]
    B6_CROSS_SECTION_DEPENDENCE --> P8[["P8: Estimation"]]
    B6_CROSS_SECTION_DEPENDENCE --> P10[["P10: Inference and interpretation"]]
    class B6_DYNAMIC,B6_HETERO decision
    class B6,B6_PANEL_UNIT_ROOT,B6_STATIC_PANEL,B6_DYNAMIC_PANEL,B6_HETEROGENEOUS,B6_CROSS_SECTION_DEPENDENCE process
    class P8,P10 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## B6 Wide panel

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B6`). Write this section following the content rules in `.claude/rules/writing.md`.

## Panel unit-root and cointegration tests

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B6_PANEL_UNIT_ROOT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Fixed and random effects

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B6_STATIC_PANEL`). Write this section following the content rules in `.claude/rules/writing.md`.

## Dynamic panel GMM

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B6_DYNAMIC_PANEL`). Write this section following the content rules in `.claude/rules/writing.md`.

## Heterogeneous panels

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B6_HETEROGENEOUS`). Write this section following the content rules in `.claude/rules/writing.md`.

## Cross-sectional dependence

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B6_CROSS_SECTION_DEPENDENCE`). Write this section following the content rules in `.claude/rules/writing.md`.
