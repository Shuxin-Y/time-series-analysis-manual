# 20. Spatio-Temporal Models

Spatial econometrics with time, geostatistics, graph-based and network time series.

## Branch sub-diagram

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    B5["B5 Spatial and network"] --> B5_SPATIAL_AUTOCORRELATION["Spatial autocorrelation<br/>Moran's I"]
    B5_SPATIAL_AUTOCORRELATION --> B5_INDEX{"Index?"}
    B5_INDEX -->|"Regions or panels"| B5_SPATIAL_PANEL_VAR["Spatial panel VAR and spatial error and lag models"]
    B5_INDEX -->|"Continuous space"| B5_KRIGING["Spatio-temporal kriging and Gaussian processes"]
    B5_INDEX -->|"Graph"| B5_GRAPH_SIGNAL["Graph signal processing"]
    B5_INDEX -->|"Events in space"| B5_ST_POINT_PROCESS["Spatio-temporal point processes"]
    B5_GRAPH_SIGNAL --> B5_STGNN["Spatio-temporal graph neural networks"]
    B5_STGNN --> B5_NETWORK_AR["Network autoregression"]
    B5_SPATIAL_PANEL_VAR & B5_KRIGING & B5_NETWORK_AR & B5_ST_POINT_PROCESS --> P8[["P8: Estimation"]]
    class B5_INDEX decision
    class B5,B5_SPATIAL_AUTOCORRELATION,B5_SPATIAL_PANEL_VAR,B5_KRIGING,B5_GRAPH_SIGNAL,B5_ST_POINT_PROCESS,B5_STGNN,B5_NETWORK_AR process
    class P8 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## B5 Spatial and network

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5`). Write this section following the content rules in `.claude/rules/writing.md`.

## Spatial autocorrelation

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_SPATIAL_AUTOCORRELATION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Spatial panel VAR and spatial error and lag models

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_SPATIAL_PANEL_VAR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Spatio-temporal kriging and Gaussian processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_KRIGING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Graph signal processing

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_GRAPH_SIGNAL`). Write this section following the content rules in `.claude/rules/writing.md`.

## Spatio-temporal graph neural networks

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_STGNN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Network autoregression

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_NETWORK_AR`). Write this section following the content rules in `.claude/rules/writing.md`.

## Spatio-temporal point processes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `B5_ST_POINT_PROCESS`). Write this section following the content rules in `.claude/rules/writing.md`.
