# P4: Transformations

**Question this phase answers:** What must change before modelling, given the purpose and the P3 flags?

Structure the model class will not represent (variance scaling, integration when the class works on differences, breaks) is removed here. Structure the class represents is left for P6: integration carried by an ARIMA-type model, exponential smoothing, Theta, a structural model, a VECM, a VAR in levels or an ARDL, and the deterministic trend, seasonal and calendar regressors. Purposes that study levels keep them: decomposition works on the (log) level, spectral analysis prewhitens and recolours instead of differencing, and change-point detection and signal extraction read the integration flag on their own route instead of differencing; for them the outlier question runs only for signal extraction with impulsive noise, and readers whose target is the anomalies or changes keep them. Decomposition is asked only of readers who want components; readers who keep levels for changes or a signal keep seasonality that is not their target out of it in part 6. Differencing asks which unit roots the model class carries: the regular ones, the seasonal ones too, or none. Compositional series arrive as log-ratios from P3. Counts skip the continuous transforms, event times, categories and curves skip P4, and irregular series skip differencing.

## Sub-diagram

**Part 1: value type, scale and outliers.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P4_IN(["Flags from P3"]) --> P4_TYPE{"Value-type flag?"}
    P4_TYPE -->|"Events or categories"| P5[["P5: Representation selection"]]
    P4_TYPE -->|"Curves"| P5
    P4_TYPE -->|"Counts"| P4_COUNT_POOLING{"Global pooling?"}
    P4_TYPE -->|"Continuous, or log-ratios"| P4_VARIANCE{"Variance flag?"}
    P4_COUNT_POOLING -->|"Yes"| P4_FEATURES[["Calendar features and per-series scaling"]]
    P4_COUNT_POOLING -->|"No: trend and season enter the count model"| P5
    P4_FEATURES --> P5
    P4_VARIANCE -->|"Transform"| P4_LOG_BOXCOX["Variance-stabilising transforms<br/>log, Box-Cox, Yeo-Johnson; lambda by Guerrero"]
    P4_VARIANCE -->|"None"| P4_OUTLIER_GATE
    P4_LOG_BOXCOX --> P4_OUTLIER_GATE{"Keep-anomalies or keep-levels flag?"}
    P4_OUTLIER_GATE -->|"Keep anomalies: they are the target"| P4_TO_PART_2
    P4_OUTLIER_GATE -->|"Keep levels: signal with impulsive noise"| P4_OUTLIERS{"Candidate outliers: treatment?"}
    P4_OUTLIER_GATE -->|"Keep levels: otherwise"| P4_TO_PART_2
    P4_OUTLIER_GATE -->|"Neither"| P4_OUTLIERS
    P4_OUTLIERS -->|"Prefilter"| P4_ROBUST_PREFILTER["Robust prefiltering<br/>median and Hampel filters on the level; breaks excluded"]
    P4_OUTLIERS -->|"Model them in P6"| P4_INTERVENTION_FLAG["Set flag: intervention terms"]
    P4_OUTLIERS -->|"Keep them, or none"| P4_TO_PART_2
    P4_ROBUST_PREFILTER & P4_INTERVENTION_FLAG --> P4_TO_PART_2(["Continue in part 2"])
    class P4_IN,P4_TO_PART_2 terminator
    class P4_TYPE,P4_COUNT_POOLING,P4_VARIANCE,P4_OUTLIER_GATE,P4_OUTLIERS decision
    class P4_LOG_BOXCOX,P4_ROBUST_PREFILTER,P4_INTERVENTION_FLAG process
    class P5,P4_FEATURES ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: the keep-levels routes, and decomposition on the levels.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P4_PART_2_IN(["From part 1"]) --> P4_KEEP_LEVELS{"Keep-levels flag?"}
    P4_KEEP_LEVELS -->|"Yes: components"| P4_DECOMP{"Decomposition method?"}
    P4_KEEP_LEVELS -->|"Yes: frequencies"| P4_TO_PART_5(["Continue in part 5"])
    P4_KEEP_LEVELS -->|"Yes: signal or changes"| P4_TO_PART_6(["Continue in part 6"])
    P4_KEEP_LEVELS -->|"No"| P4_TO_PART_3(["Continue in part 3"])
    P4_DECOMP -->|"Filter-based"| P4_FILTER_DECOMPOSITION["Filter-based decomposition<br/>HP, Baxter-King, Christiano-Fitzgerald, Hamilton"]
    P4_DECOMP -->|"Model-based"| P4_MODEL_DECOMPOSITION["Model-based decomposition<br/>Beveridge-Nelson, unobserved components"]
    P4_DECOMP -->|"Nonparametric"| P4_SSA["Singular spectrum analysis"]
    P4_DECOMP -->|"Seasonal: STL, X-13, classical"| P4_SEASONAL_ADJUSTMENT[["Seasonal adjustment"]]
    P4_DECOMP -->|"Several seasonal periods"| P4_MULTIPLE_SEASONALITY[["Multiple seasonality"]]
    P4_FILTER_DECOMPOSITION & P4_MODEL_DECOMPOSITION & P4_SSA --> P4_COMPONENTS_TO_PART_4
    P4_SEASONAL_ADJUSTMENT & P4_MULTIPLE_SEASONALITY --> P4_COMPONENTS_TO_PART_4
    P4_COMPONENTS_TO_PART_4(["Continue in part 4"])
    class P4_PART_2_IN,P4_TO_PART_5,P4_TO_PART_6,P4_COMPONENTS_TO_PART_4,P4_TO_PART_3 terminator
    class P4_DECOMP,P4_KEEP_LEVELS decision
    class P4_FILTER_DECOMPOSITION,P4_MODEL_DECOMPOSITION,P4_SSA process
    class P4_SEASONAL_ADJUSTMENT,P4_MULTIPLE_SEASONALITY ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: the integration filter and seasonal treatment.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P4_PART_3_IN(["From part 2"]) --> P4_GRID{"Sampling flag?"}
    P4_GRID -->|"Irregular, kept"| P4_SEASON
    P4_GRID -->|"Regular, resampled or mixed"| P4_INTEGRATION{"Integration flag?"}
    P4_INTEGRATION -->|"k at least 1, or a seasonal filter"| P4_CLASS{"Unit roots the model carries?"}
    P4_CLASS -->|"None: ARMA, learners"| P4_DIFFERENCE["Regular differencing<br/>each series, covariates included, to its own order k<br/>none when k = 0"]
    P4_CLASS -->|"All: SARIMA, ETS, structural"| P4_SEASON
    P4_CLASS -->|"Regular only: Theta, VECM,<br/>levels VAR, ARDL to I(1)"| P4_CARRIED_SEASONAL{"Seasonal filter flag?"}
    P4_CARRIED_SEASONAL -->|"Yes"| P4_SEASONAL_DIFFERENCE
    P4_CARRIED_SEASONAL -->|"No"| P4_SEASON
    P4_INTEGRATION -->|"k = 0, no seasonal filter"| P4_SEASON
    P4_DIFFERENCE --> P4_SEASONAL_FILTER{"Seasonal filter too?"}
    P4_SEASONAL_FILTER -->|"Yes"| P4_SEASONAL_DIFFERENCE["Seasonal differencing<br/>full or partial seasonal filter"]
    P4_SEASONAL_FILTER -->|"No"| P4_OVERDIFFERENCING
    P4_SEASONAL_DIFFERENCE --> P4_OVERDIFFERENCING["Check for over-differencing<br/>after the whole filter"]
    P4_OVERDIFFERENCING --> P4_DIFF_VERDICT{"After the filter?"}
    P4_DIFF_VERDICT -->|"Short memory"| P4_SEASON
    P4_DIFF_VERDICT -->|"Trend-stationary"| P4_TREND_FLAG["Update flags: k reduced, deterministic trend<br/>the regular difference is undone"]
    P4_DIFF_VERDICT -->|"Seasonal over-difference"| P4_SEASON_FLAG["Update flags: no seasonal filter,<br/>deterministic seasonality"]
    P4_DIFF_VERDICT -->|"Antipersistent"| P4_FRACTIONAL_FLAG["Update flag: fractional remainder for P6"]
    P4_TREND_FLAG & P4_SEASON_FLAG & P4_FRACTIONAL_FLAG --> P4_SEASON{"Seasonal treatment?"}
    P4_SEASON -->|"None, or regressors in P6"| P4_PART_3_OUT(["Continue in part 4"])
    P4_SEASON -->|"Adjusted series needed"| P4_SEASONAL_ADJUSTMENT["Seasonal adjustment<br/>classical decomposition, STL, X-13 and SEATS"]
    P4_SEASON -->|"Multiple seasonality"| P4_MULTIPLE_SEASONALITY["Multiple seasonality<br/>MSTL, TBATS, Fourier terms"]
    P4_SEASONAL_ADJUSTMENT & P4_MULTIPLE_SEASONALITY --> P4_PART_3_OUT
    class P4_PART_3_IN,P4_PART_3_OUT terminator
    class P4_GRID,P4_INTEGRATION,P4_CLASS,P4_CARRIED_SEASONAL,P4_SEASONAL_FILTER,P4_DIFF_VERDICT,P4_SEASON decision
    class P4_DIFFERENCE,P4_SEASONAL_DIFFERENCE,P4_OVERDIFFERENCING,P4_TREND_FLAG,P4_SEASON_FLAG,P4_FRACTIONAL_FLAG,P4_SEASONAL_ADJUSTMENT,P4_MULTIPLE_SEASONALITY process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: breaks, features and the retest.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P4_PART_4_IN(["From parts 2, 3, 5 and 6"]) --> P4_BREAKS{"Break or explosive flag?"}
    P4_BREAKS -->|"Yes, and changes are not the target"| P4_BREAK_HANDLING["Handle breaks and explosive episodes<br/>segmenting, regime dummies, time-varying parameters, dated episodes"]
    P4_BREAKS -->|"No, or changes are the target"| P4_POOLING
    P4_BREAK_HANDLING --> P4_POOLING{"Global pooling?"}
    P4_POOLING -->|"Yes, or compare local and global"| P4_FEATURES["Calendar features and per-series scaling<br/>computed from data before each origin"]
    P4_POOLING -->|"No"| P4_RETEST
    P4_FEATURES --> P4_RETEST["Retest stationarity around the model's deterministic terms<br/>trend, seasonal, break and calendar regressors"]
    P4_RETEST --> P4_STATIONARY{"Stationary now?"}
    P4_STATIONARY -->|"Yes, or explained: integration carried by the class, fractional remainder, cointegrated levels, dated episode, kept levels"| P4_OUT(["To P5 Representation"])
    P4_STATIONARY -.->|"No, unexplained: re-diagnose"| P3[["P3: Exploratory diagnostics"]]
    class P4_PART_4_IN,P4_OUT terminator
    class P4_BREAKS,P4_POOLING,P4_STATIONARY decision
    class P4_BREAK_HANDLING,P4_FEATURES,P4_RETEST process
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

**Part 5: spectral analysis on levels.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P4_PART_5_IN(["From part 2: keep levels, frequencies"]) --> P4_SPECTRAL_ORDER{"Integration flag?"}
    P4_SPECTRAL_ORDER -->|"k = 0, trend-stationary, or none: irregular, kept"| P4_DETREND["Detrending by regression on time<br/>mean or low-order trend removal"]
    P4_SPECTRAL_ORDER -->|"k at least 1"| P4_PREWHITEN["Prewhiten and recolour<br/>difference, divide by the filter's squared gain; pseudo-spectrum"]
    P4_DETREND & P4_PREWHITEN --> P4_PART_5_OUT(["Continue in part 4"])
    class P4_PART_5_IN,P4_PART_5_OUT terminator
    class P4_SPECTRAL_ORDER decision
    class P4_DETREND,P4_PREWHITEN process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 6: signal extraction and change points on levels.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P4_PART_6_IN(["From part 2: keep levels, signal or changes"]) --> P4_LEVELS_SEASON{"Seasonal flags?"}
    P4_LEVELS_SEASON -->|"Set, and seasonality is not the target"| P4_LEVELS_SEASONALITY["Seasonality on the levels routes<br/>changes: seasonal terms in the segmentation cost; signal: a seasonal component modelled with it"]
    P4_LEVELS_SEASON -->|"Not set, or seasonality is the target"| P4_LEVELS_ORDER{"Integration flag?"}
    P4_LEVELS_SEASONALITY --> P4_LEVELS_ORDER
    P4_LEVELS_ORDER -->|"k = 0, or none: irregular, kept"| P4_PART_6_OUT
    P4_LEVELS_ORDER -->|"k at least 1"| P4_INTEGRATED_LEVELS["Integrated series kept in levels<br/>signal: state-space or Wiener-Kolmogorov extraction, unit gain at frequency zero; changes: drift changes on the differences, or a stochastic-level model"]
    P4_INTEGRATED_LEVELS --> P4_PART_6_OUT(["Continue in part 4"])
    class P4_PART_6_IN,P4_PART_6_OUT terminator
    class P4_LEVELS_SEASON,P4_LEVELS_ORDER decision
    class P4_LEVELS_SEASONALITY,P4_INTEGRATED_LEVELS process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

Every two-sided step here (STL, X-13, centred Hampel windows) has a one-sided version, used where the timing flag requires it (see [rolling-origin backtesting](p10-evaluation-selection.md#rolling-origin-backtesting) for the forecaster's case).

## Phase guide

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4`). Write this section following the content rules in `.claude/rules/writing.md`.

## Variance-stabilising transforms

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_LOG_BOXCOX`). Write this section following the content rules in `.claude/rules/writing.md`.

## Robust prefiltering

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_ROBUST_PREFILTER`). Write this section following the content rules in `.claude/rules/writing.md`.

## Filter-based decomposition

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_FILTER_DECOMPOSITION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Model-based decomposition

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_MODEL_DECOMPOSITION`). Write this section following the content rules in `.claude/rules/writing.md`.

## Singular spectrum analysis

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_SSA`). Write this section following the content rules in `.claude/rules/writing.md`.

## Regular differencing

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_DIFFERENCE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Seasonal differencing

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_SEASONAL_DIFFERENCE`). Write this section following the content rules in `.claude/rules/writing.md`.

## Check for over-differencing

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_OVERDIFFERENCING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Seasonal adjustment

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_SEASONAL_ADJUSTMENT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Multiple seasonality

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_MULTIPLE_SEASONALITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Handle breaks and explosive episodes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_BREAK_HANDLING`). Write this section following the content rules in `.claude/rules/writing.md`.

## Calendar features and per-series scaling

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_FEATURES`). Write this section following the content rules in `.claude/rules/writing.md`.

## Retest stationarity around the model's deterministic terms

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_RETEST`). Write this section following the content rules in `.claude/rules/writing.md`.

## Detrending by regression on time

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_DETREND`). Write this section following the content rules in `.claude/rules/writing.md`.

## Prewhiten and recolour

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_PREWHITEN`). Write this section following the content rules in `.claude/rules/writing.md`.

## Seasonality on the levels routes

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_LEVELS_SEASONALITY`). Write this section following the content rules in `.claude/rules/writing.md`.

## Integrated series kept in levels

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P4_INTEGRATED_LEVELS`). Write this section following the content rules in `.claude/rules/writing.md`.
