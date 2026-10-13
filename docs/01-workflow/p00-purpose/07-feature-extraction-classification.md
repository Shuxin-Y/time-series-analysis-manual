# Purpose 7: Feature extraction, classification and clustering

**Goal:** Turn series into feature vectors and learn labels or groups.

## Sub-chart

**Part 1: split unit, data and the learner input.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_FE_IN(["Labelling or grouping question"]) --> P0_SPLIT_UNIT[["Choose the split unit"]]
    P0_SPLIT_UNIT --> P1[["P1: Data acquisition and cleaning"]]
    P1 --> P3[["P3: Exploratory diagnostics"]]
    P3 --> P4[["P4: Transformations"]]
    P4 --> P5[["P5: Representation selection"]]
    P5 --> P0_FE_INPUT{"Learner input?"}
    P0_FE_INPUT -->|"Raw series"| P0_FE_TO_PART_3(["Continue in part 3"])
    P0_FE_INPUT -->|"Representations"| P0_FE_TO_PART_2(["Continue in part 2"])
    P0_FE_INPUT -->|"Hand-crafted features"| P0_FE_HANDCRAFTED{"Domain?"}
    P0_FE_HANDCRAFTED -->|"Time"| P0_FE_TIME_FEATURES["Time-domain features<br/>moments, autocorrelation, rolling statistics"]
    P0_FE_HANDCRAFTED -->|"Frequency"| P0_FE_FREQ_FEATURES["Frequency-domain features<br/>band power, spectral entropy, spectral centroid"]
    P0_FE_HANDCRAFTED -->|"Time-frequency"| P0_FE_TF_FEATURES["Time-frequency features<br/>STFT and wavelet coefficients"]
    P0_FE_HANDCRAFTED -->|"Nonlinear dynamics"| P0_FE_NONLINEAR_FEATURES["Nonlinear dynamics features<br/>entropy, recurrence quantification, chaos indicators"]
    P0_FE_HANDCRAFTED -->|"Automated"| P0_FE_AUTOMATED["Automated feature extraction<br/>tsfresh, catch22"]
    P0_FE_TIME_FEATURES & P0_FE_FREQ_FEATURES & P0_FE_TF_FEATURES & P0_FE_NONLINEAR_FEATURES & P0_FE_AUTOMATED --> P0_FE_FEATURES_TO_PART_2(["Continue in part 2"])
    class P0_FE_IN,P0_FE_TO_PART_3,P0_FE_TO_PART_2,P0_FE_FEATURES_TO_PART_2 terminator
    class P0_FE_INPUT,P0_FE_HANDCRAFTED decision
    class P0_FE_TIME_FEATURES,P0_FE_FREQ_FEATURES,P0_FE_TF_FEATURES,P0_FE_NONLINEAR_FEATURES,P0_FE_AUTOMATED process
    class P0_SPLIT_UNIT,P1,P3,P4,P5 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: representations and learners on feature vectors.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_FE_PART_2_IN(["From part 1: features or representations"]) --> P0_FE_REPRESENTATION{"Representation?"}
    P0_FE_REPRESENTATION -->|"Hand-crafted features"| P0_FE_TASK
    P0_FE_REPRESENTATION -->|"Symbolic"| P0_FE_SYMBOLIC["Symbolic representations<br/>SAX, SFA"]
    P0_FE_REPRESENTATION -->|"Learned"| P0_FE_REPRESENTATION_LEARNING["Self-supervised representation learning"]
    P0_FE_REPRESENTATION -->|"Topological"| P0_FE_TDA["Topological data analysis"]
    P0_FE_SYMBOLIC & P0_FE_REPRESENTATION_LEARNING & P0_FE_TDA --> P0_FE_TASK{"Task?"}
    P0_FE_TASK -->|"Classification or regression"| P0_FE_TABULAR["Tabular learners on feature vectors<br/>tree ensembles, ridge, logistic regression"]
    P0_FE_TASK -->|"Clustering"| P0_FE_CLUSTERING["Clustering<br/>k-means, spectral clustering; validated by internal indices and stability"]
    P0_FE_TABULAR --> P0_FE_PART_2_OUT(["Continue in part 4"])
    P0_FE_CLUSTERING --> P0_FE_CLUSTER_TO_PART_4(["Continue in part 4"])
    class P0_FE_PART_2_IN,P0_FE_PART_2_OUT,P0_FE_CLUSTER_TO_PART_4 terminator
    class P0_FE_REPRESENTATION,P0_FE_TASK decision
    class P0_FE_SYMBOLIC,P0_FE_REPRESENTATION_LEARNING,P0_FE_TDA,P0_FE_TABULAR,P0_FE_CLUSTERING process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: learners on raw series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_FE_PART_3_IN(["From part 1: raw series"]) --> P0_FE_CLASSIFIER{"Classifier or regressor family?"}
    P0_FE_CLASSIFIER -->|"Distance-based"| P0_FE_DISTANCES["Distance measures<br/>dynamic time warping, edit distances, kernels"]
    P0_FE_CLASSIFIER -->|"Shapelets or random kernels"| P0_FE_SHAPELETS["Shapelets and ROCKET<br/>ROCKET with ridge for regression"]
    P0_FE_CLASSIFIER -->|"Deep networks"| P0_FE_DEEP_CLASSIFIERS["Deep classifiers<br/>InceptionTime, also as a regressor"]
    P0_FE_DISTANCES & P0_FE_SHAPELETS & P0_FE_DEEP_CLASSIFIERS --> P0_FE_PART_3_OUT(["Continue in part 4"])
    class P0_FE_PART_3_IN,P0_FE_PART_3_OUT terminator
    class P0_FE_CLASSIFIER decision
    class P0_FE_DISTANCES,P0_FE_SHAPELETS,P0_FE_DEEP_CLASSIFIERS process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: training, evaluation and interpretation.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_FE_PART_4_IN(["From parts 2 and 3: supervised learners"]) --> P0_FE_AUGMENTATION["Data augmentation<br/>slicing, warping, synthetic oversampling, inside training folds"]
    P0_FE_AUGMENTATION --> P10[["P10: Out-of-sample evaluation and selection"]]
    P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]] -.- P0_FE_AUGMENTATION
    P0_FE_CLUSTER_IN(["From part 2: clustering"]) --> P10
    P10 --> P10_GROUPED_SPLITS[["Grouped and temporal splits"]]
    P10_GROUPED_SPLITS --> P10_COLLECTION_TASK[["Task?"]]
    P10_COLLECTION_TASK -->|"Supervised"| P10_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    P10_COLLECTION_TASK -->|"Clustering"| P10_CLUSTER_VALIDATION[["Cluster validation"]]
    P10_CLASSIFICATION_METRICS & P10_CLUSTER_VALIDATION --> P11[["P11: Inference and interpretation"]]
    P11 --> P11_INTERPRETABILITY[["Interpretability"]]
    P11_INTERPRETABILITY --> P12[["P12: Deployment and monitoring"]]
    class P0_FE_PART_4_IN,P0_FE_CLUSTER_IN terminator
    class P0_FE_AUGMENTATION process
    class P8_HYPERPARAMETERS,P10,P10_GROUPED_SPLITS,P10_COLLECTION_TASK,P10_CLASSIFICATION_METRICS,P10_CLUSTER_VALIDATION,P11,P11_INTERPRETABILITY,P12 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P10 metrics for this purpose

[Grouped and temporal splits](../../reference/19-classification-anomaly/index.md#grouped-and-temporal-splits), [Classification and anomaly metrics](../../reference/19-classification-anomaly/index.md#classification-and-anomaly-metrics).

## P11 inference for this purpose

[Interpretability](../../reference/18-machine-learning/index.md#interpretability).
