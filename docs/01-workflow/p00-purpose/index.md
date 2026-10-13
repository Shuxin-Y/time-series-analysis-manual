## Reserve the final hold-out

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P0_HOLDOUT`). Write this section following the content rules in `.claude/rules/writing.md`.

# P0: Purpose and evaluation plan

**Question this phase answers:** What is the question, how will the answer be judged, and what must the data keep?

The purpose comes first because it decides what cleaning may remove, what transformations may destroy and how the answer will be judged. Fixing these choices before looking at the data is pre-specification. Ten purposes are distinguished. Methods that belong to a purpose rather than to the standard pipeline (change-point algorithms, anomaly methods, component analysis, feature extraction, classification, clustering, simulation) are leaves of this phase.

## Purpose selector

**Part 1: the future, causes and structure in the series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_IN(["Question and raw time-stamped data"]) --> P0_QUESTION{"Question about?"}
    P0_QUESTION -->|"The future"| P0_FUTURE{"Values or events?"}
    P0_QUESTION -->|"Causes"| P0_CAUSAL["Purpose 2: Causal and structural inference"]
    P0_QUESTION -->|"Structure in the series"| P0_STRUCTURE{"Which structure?"}
    P0_QUESTION -->|"Events or other outputs"| P0_TO_PART_2(["Continue in part 2"])
    P0_FUTURE -->|"Future values"| P0_FORECASTING["Purpose 1: Forecasting"]
    P0_FUTURE -->|"An event in a future window"| P0_FEATURES[["Purpose 7: Feature extraction, classification and clustering"]]
    P0_STRUCTURE -->|"Signal versus noise"| P0_SIGNAL["Purpose 3: Signal extraction and denoising"]
    P0_STRUCTURE -->|"Components"| P0_DECOMPOSITION["Purpose 6: Decomposition"]
    P0_STRUCTURE -->|"Frequencies"| P0_SPECTRAL["Purpose 8: Spectral analysis"]
    P0_FORECASTING & P0_CAUSAL & P0_SIGNAL & P0_DECOMPOSITION & P0_SPECTRAL & P0_FEATURES --> P0_PURPOSE_FLAG["Set flag: purpose"]
    P0_PURPOSE_FLAG --> P0_TO_PART_3(["Continue in part 3"])
    B2_SURVIVAL[["Survival and hazard models"]] -.- P0_FEATURES
    class P0_IN,P0_TO_PART_2,P0_TO_PART_3 terminator
    class P0_QUESTION,P0_FUTURE,P0_STRUCTURE decision
    class P0_FORECASTING,P0_CAUSAL,P0_SIGNAL,P0_DECOMPOSITION,P0_SPECTRAL,P0_PURPOSE_FLAG process
    class P0_FEATURES,B2_SURVIVAL ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: events and other outputs.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_PART_2_IN(["From part 1"]) --> P0_QUESTION_2{"Question about?"}
    P0_QUESTION_2 -->|"Events"| P0_EVENTS{"Which events?"}
    P0_QUESTION_2 -->|"Other outputs"| P0_OUTPUTS{"Which output?"}
    P0_EVENTS -->|"Changes"| P0_CHANGE_POINT["Purpose 4: Change-point detection"]
    P0_EVENTS -->|"Anomalies or regimes"| P0_ANOMALY["Purpose 5: Anomaly and regime detection"]
    P0_OUTPUTS -->|"Features and labels"| P0_FEATURES["Purpose 7: Feature extraction, classification and clustering"]
    P0_OUTPUTS -->|"A system model"| P0_SYSTEM_ID["Purpose 9: System identification"]
    P0_OUTPUTS -->|"Simulated paths"| P0_SIMULATION["Purpose 10: Simulation and scenario generation"]
    P0_CHANGE_POINT & P0_ANOMALY & P0_FEATURES & P0_SYSTEM_ID & P0_SIMULATION --> P0_PURPOSE_FLAG[["Set flag: purpose"]]
    P0_PURPOSE_FLAG --> P0_PART_2_OUT(["Continue in part 3"])
    class P0_PART_2_IN,P0_PART_2_OUT terminator
    class P0_QUESTION_2,P0_EVENTS,P0_OUTPUTS decision
    class P0_CHANGE_POINT,P0_ANOMALY,P0_FEATURES,P0_SYSTEM_ID,P0_SIMULATION process
    class P0_PURPOSE_FLAG ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: evaluation plan.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_PART_3_IN(["From parts 1 and 2"]) --> P0_PLAN{"Purpose flag?"}
    P0_PLAN -->|"Forecasting"| P0_FORECAST_TASK["Specify the forecasting task<br/>horizons, functional, loss"]
    P0_PLAN -->|"Change points, anomalies"| P0_DETECTION_TASK["Specify the detection task<br/>online or offline, delay, false alarms"]
    P0_PLAN -->|"Causes, system model"| P0_ESTIMAND["Specify the estimand<br/>effect, its horizon, or system property"]
    P0_PLAN -->|"Features, labels, clusters"| P0_SPLIT_UNIT["Choose the split unit<br/>unit, time, or both"]
    P0_PLAN -->|"Other purposes"| P0_PART_3_OUT(["Continue in part 4"])
    P0_FORECAST_TASK --> P0_FC_BASELINES["Baselines for comparison<br/>naive, seasonal naive, Theta; Croston once P1 finds intermittent counts"]
    P0_FC_BASELINES --> P0_FORECAST_FLAG["Set flag: forecast task and baselines"]
    P0_FORECAST_FLAG --> P0_COVARIATES["Covariates and their availability<br/>known, forecast, lagged, co-forecast"]
    P0_ESTIMAND --> P0_COVARIATES
    P0_COVARIATES --> P0_COVARIATE_FLAG["Set flag: covariates"]
    P0_DETECTION_TASK --> P0_LABELS{"Labels available?"}
    P0_LABELS -->|"Many: supervised learning"| P0_FEATURES[["Purpose 7: Feature extraction, classification and clustering"]]
    P0_FEATURES --> P0_PURPOSE_FLAG[["Set flag: purpose"]]
    P0_PURPOSE_FLAG --> P0_SPLIT_UNIT
    P0_LABELS -->|"Few or none"| P0_DETECTION_FLAG["Set flag: labels"]
    P0_SPLIT_UNIT --> P0_SPLIT_FLAG["Set flag: split unit"]
    P0_COVARIATE_FLAG & P0_DETECTION_FLAG & P0_SPLIT_FLAG --> P0_HOLDOUT["Reserve the final hold-out<br/>the last stretch, or held-out units; touched by no phase before P10"]
    P0_HOLDOUT --> P0_HOLDOUT_FLAG["Set flag: hold-out"]
    P0_HOLDOUT_FLAG --> P0_PART_3_OUT
    class P0_PART_3_IN,P0_PART_3_OUT terminator
    class P0_PLAN,P0_LABELS decision
    class P0_FORECAST_TASK,P0_DETECTION_TASK,P0_ESTIMAND,P0_SPLIT_UNIT,P0_FC_BASELINES,P0_COVARIATES,P0_FORECAST_FLAG,P0_COVARIATE_FLAG,P0_DETECTION_FLAG,P0_SPLIT_FLAG,P0_HOLDOUT,P0_HOLDOUT_FLAG process
    class P0_FEATURES,P0_PURPOSE_FLAG ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: what the data must keep, and when the output is used.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_PART_4_IN(["From part 3"]) --> P0_KEEP_ANOMALIES{"Anomalies or changes are the target?"}
    P0_KEEP_ANOMALIES -->|"Yes: purposes 4 and 5"| P0_KEEP_ANOMALIES_FLAG["Set flag: keep anomalies"]
    P0_KEEP_ANOMALIES -->|"No"| P0_KEEP_LEVELS{"Levels needed?"}
    P0_KEEP_ANOMALIES_FLAG --> P0_KEEP_LEVELS
    P0_KEEP_LEVELS -->|"Yes: signal, changes, components, frequencies"| P0_KEEP_LEVELS_FLAG["Set flag: keep levels"]
    P0_KEEP_LEVELS -->|"No"| P0_TIMING{"Output used in real time?"}
    P0_KEEP_LEVELS_FLAG --> P0_TIMING
    P0_TIMING -->|"Yes, or forecast or learner features"| P0_REAL_TIME_FLAG["Set flag: timing, real time"]
    P0_TIMING -->|"No: offline"| P1[["P1: Data acquisition and cleaning"]]
    P0_REAL_TIME_FLAG --> P1
    class P0_PART_4_IN terminator
    class P0_KEEP_ANOMALIES,P0_KEEP_LEVELS,P0_TIMING decision
    class P0_KEEP_ANOMALIES_FLAG,P0_KEEP_LEVELS_FLAG,P0_REAL_TIME_FLAG process
    class P1 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

The timing flag is set here once. Real time applies to live outputs, learner features and real-time detection: every two-sided step on their route (STL, X-13, gap filling by a smoother, centred windows) is replaced by its one-sided version. A statistical forecasting model fitted to adjusted data may keep the two-sided adjustment, because [P10](../p10-evaluation-selection.md#rolling-origin-backtesting) refits it inside each training window, where it sees only data before the origin; a learner's features stay one-sided, because a centred window at time s contains the targets after s.

## Quick navigation

Emphasised phases are the phases after P0 whose leaves the purpose's sub-chart routes through (dotted pointers excluded).

| Purpose | Emphasised phases | Key leaves |
|---|---|---|
| [1. Forecasting](01-forecasting.md) | P1, P6, P10, P11 | Baselines for comparison; Complete forecast product per origin; Reproduction number and SIR fitting |
| [2. Causal and structural inference](02-causal-inference.md) | P3, P6, P11 | Identification strategy and exogeneity; Placebo and falsification tests; Sensitivity analysis across specifications |
| [3. Signal extraction and denoising](03-signal-extraction.md) | P4, P5, P8, P10 | Characterise the noise; Wavelet denoising; Evaluate the signal-to-noise ratio |
| [4. Change-point detection](04-change-point-detection.md) | P3, P6, P10, P11 | Dependence-aware detection; Calibrate the threshold; Offline segmentation |
| [5. Anomaly and regime detection](05-anomaly-regime-detection.md) | P4, P6, P10, P12 | Statistical outlier scores; Matrix profile and discord discovery; Set thresholds by the cost of errors |
| [6. Decomposition](06-decomposition.md) | P3, P4, P5, P6 | Analyse and interpret the components; Decomposition diagnostics; Revision stability of real-time decompositions |
| [7. Feature extraction, classification and clustering](07-feature-extraction-classification.md) | P10, P11 | Time-domain features; Shapelets and ROCKET; Tabular learners on feature vectors |
| [8. Spectral analysis](08-spectral-analysis.md) | P5, P11 | Interpret the spectral shape; Peak significance; Cross-spectrum, coherence and phase |
| [9. System identification](09-system-identification.md) | P6 | Closed-loop identification; Nonparametric analysis of the system; Poles, zeros and stability |
| [10. Simulation and scenario generation](10-simulation.md) | P6, P11 | Monte Carlo simulation from a fitted model; Check distribution and dependence matching; Train on synthetic, test on real |

## Specify the forecasting task

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P0_FORECAST_TASK`). Write this section following the content rules in `.claude/rules/writing.md`.

## Specify the detection task

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P0_DETECTION_TASK`). Write this section following the content rules in `.claude/rules/writing.md`.

## Specify the estimand

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P0_ESTIMAND`). Write this section following the content rules in `.claude/rules/writing.md`.

## Choose the split unit

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P0_SPLIT_UNIT`). Write this section following the content rules in `.claude/rules/writing.md`.

## Covariates and their availability

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P0_COVARIATES`). Write this section following the content rules in `.claude/rules/writing.md`.
