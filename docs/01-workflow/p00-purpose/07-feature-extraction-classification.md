# Purpose 7: Feature extraction, classification and clustering

**Goal:** Turn series into feature vectors and learn labels or groups.

## Sub-chart

**Part 1: hand-crafted features.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_FE_IN(["Labelling or grouping question"]) --> P0_FE_FEATURE_Q{"Feature family?"}
    P0_FE_FEATURE_Q -->|"Hand-crafted features"| P0_FE_HANDCRAFTED{"Domain?"}
    P0_FE_FEATURE_Q -->|"Representations"| P0_FE_TO_PART_2
    P0_FE_HANDCRAFTED -->|"Time"| P0_FE_TIME_FEATURES["Time-domain features<br/>moments, autocorrelation, rolling statistics"]
    P0_FE_HANDCRAFTED -->|"Frequency"| P0_FE_FREQ_FEATURES["Frequency-domain features<br/>band power, spectral entropy, spectral centroid"]
    P0_FE_HANDCRAFTED -->|"Time-frequency"| P0_FE_TF_FEATURES["Time-frequency features<br/>STFT and wavelet coefficients"]
    P0_FE_HANDCRAFTED -->|"Nonlinear dynamics"| P0_FE_NONLINEAR_FEATURES["Nonlinear dynamics features<br/>entropy, recurrence quantification; chaos indicators from P3"]
    P0_FE_HANDCRAFTED -->|"Automated"| P0_FE_AUTOMATED["Automated feature extraction<br/>tsfresh, catch22"]
    P0_FE_TIME_FEATURES & P0_FE_FREQ_FEATURES & P0_FE_TF_FEATURES & P0_FE_NONLINEAR_FEATURES & P0_FE_AUTOMATED --> P0_FE_TO_PART_2(["Continue in part 2"])
    class P0_FE_IN,P0_FE_TO_PART_2 terminator
    class P0_FE_FEATURE_Q,P0_FE_HANDCRAFTED decision
    class P0_FE_TIME_FEATURES,P0_FE_FREQ_FEATURES,P0_FE_TF_FEATURES,P0_FE_NONLINEAR_FEATURES,P0_FE_AUTOMATED process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: representations, learners and evaluation.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P0_FE_FROM_PART_1(["From part 1"]) --> P0_FE_FEATURE_Q_2{"Feature family?"}
    P0_FE_FEATURE_Q_2 -->|"Representations"| P0_FE_REPRESENTATION{"Representation?"}
    P0_FE_FEATURE_Q_2 -->|"Hand-crafted features"| P0_FE_LEARNER
    P0_FE_REPRESENTATION -->|"Symbolic"| P0_FE_SYMBOLIC["Symbolic representations<br/>SAX, SFA"]
    P0_FE_REPRESENTATION -->|"Learned"| P0_FE_REPRESENTATION_LEARNING["Self-supervised representation learning"]
    P0_FE_REPRESENTATION -->|"Topological"| P0_FE_TDA["Topological data analysis"]
    P0_FE_SYMBOLIC & P0_FE_REPRESENTATION_LEARNING & P0_FE_TDA --> P0_FE_LEARNER{"Task?"}
    P0_FE_LEARNER -->|"Classification"| P0_FE_CLASSIFIER{"Classifier family?"}
    P0_FE_CLASSIFIER -->|"Distance-based"| P0_FE_DISTANCES["Distance measures<br/>dynamic time warping, edit distances, kernels"]
    P0_FE_CLASSIFIER -->|"Shapelets or random kernels"| P0_FE_SHAPELETS["Shapelets and ROCKET"]
    P0_FE_CLASSIFIER -->|"Deep networks"| P0_FE_DEEP_CLASSIFIERS["Deep classifiers<br/>InceptionTime"]
    P0_FE_LEARNER -->|"Clustering"| P0_FE_CLUSTERING["Clustering<br/>k-means with DTW, spectral clustering"]
    P0_FE_LEARNER -->|"Regression"| P6[["P6: Conditional-mean model class"]]
    P6 --> P6_TREE_ENSEMBLES[["Tree ensembles on lag features"]]
    P0_FE_DISTANCES & P0_FE_SHAPELETS & P0_FE_DEEP_CLASSIFIERS & P0_FE_CLUSTERING --> P0_FE_AUGMENTATION["Data augmentation<br/>slicing, warping, synthetic oversampling"]
    P0_FE_AUGMENTATION --> P11[["P11: Inference and interpretation"]]
    P6_TREE_ENSEMBLES --> P8[["P8: Estimation"]]
    P8 --> P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]]
    P8_HYPERPARAMETERS --> P11
    P11 --> P11_INTERPRETABILITY[["Interpretability"]]
    P11_INTERPRETABILITY --> P10[["P10: Out-of-sample evaluation and selection"]]
    P10 --> P10_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    class P0_FE_FROM_PART_1 terminator
    class P0_FE_FEATURE_Q_2,P0_FE_REPRESENTATION,P0_FE_LEARNER,P0_FE_CLASSIFIER decision
    class P0_FE_SYMBOLIC,P0_FE_REPRESENTATION_LEARNING,P0_FE_TDA,P0_FE_DISTANCES,P0_FE_SHAPELETS,P0_FE_DEEP_CLASSIFIERS,P0_FE_CLUSTERING,P0_FE_AUGMENTATION process
    class P6,P6_TREE_ENSEMBLES,P11,P8,P8_HYPERPARAMETERS,P11_INTERPRETABILITY,P10,P10_CLASSIFICATION_METRICS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P11 inference for this purpose

[Interpretability](../../reference/18-machine-learning/index.md#interpretability).

## P10 metrics for this purpose

[Classification and anomaly metrics](../../reference/19-classification-anomaly/index.md#classification-and-anomaly-metrics).
