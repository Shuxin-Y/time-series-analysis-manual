# Purpose 7: Feature extraction, classification and clustering

**Goal:** Turn series into feature vectors and learn labels or groups.

## Sub-chart

**Part 1: task and hand-crafted features.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P2_FE_IN(["Labelling or grouping question"]) --> P2_FE_TASK["Classification, clustering or regression task"]
    P2_FE_TASK --> P2_FE_FEATURE_Q{"Feature family?"}
    P2_FE_FEATURE_Q -->|"Hand-crafted features"| P2_FE_HANDCRAFTED{"Domain?"}
    P2_FE_FEATURE_Q -->|"Representations"| P2_FE_TO_PART_2
    P2_FE_HANDCRAFTED -->|"Time"| P2_FE_TIME_FEATURES["Time-domain features<br/>moments, autocorrelation, rolling statistics"]
    P2_FE_HANDCRAFTED -->|"Frequency"| P2_FE_FREQ_FEATURES["Frequency-domain features<br/>band power, spectral entropy, spectral centroid"]
    P2_FE_HANDCRAFTED -->|"Time-frequency"| P2_FE_TF_FEATURES["Time-frequency features<br/>STFT and wavelet coefficients"]
    P2_FE_HANDCRAFTED -->|"Nonlinear dynamics"| P2_FE_NONLINEAR_FEATURES["Nonlinear dynamics features<br/>entropy, Lyapunov exponents, recurrence quantification"]
    P2_FE_HANDCRAFTED -->|"Automated"| P2_FE_AUTOMATED["Automated feature extraction<br/>tsfresh, catch22"]
    P2_FE_TIME_FEATURES & P2_FE_FREQ_FEATURES & P2_FE_TF_FEATURES & P2_FE_NONLINEAR_FEATURES & P2_FE_AUTOMATED --> P2_FE_TO_PART_2(["Continue in part 2"])
    class P2_FE_IN,P2_FE_TO_PART_2 terminator
    class P2_FE_FEATURE_Q,P2_FE_HANDCRAFTED decision
    class P2_FE_TASK,P2_FE_TIME_FEATURES,P2_FE_FREQ_FEATURES,P2_FE_TF_FEATURES,P2_FE_NONLINEAR_FEATURES,P2_FE_AUTOMATED process
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
    P2_FE_FROM_PART_1(["From part 1"]) -->|"Representations"| P2_FE_REPRESENTATION{"Representation?"}
    P2_FE_FROM_PART_1 -->|"Hand-crafted features"| P2_FE_LEARNER
    P2_FE_REPRESENTATION -->|"Symbolic"| P2_FE_SYMBOLIC["Symbolic representations<br/>SAX, SFA"]
    P2_FE_REPRESENTATION -->|"Learned"| P2_FE_REPRESENTATION_LEARNING["Self-supervised representation learning"]
    P2_FE_REPRESENTATION -->|"Topological"| P2_FE_TDA["Topological data analysis"]
    P2_FE_SYMBOLIC & P2_FE_REPRESENTATION_LEARNING & P2_FE_TDA --> P2_FE_LEARNER{"Task?"}
    P2_FE_LEARNER -->|"Classification"| P2_FE_DISTANCES["Distance measures<br/>dynamic time warping, edit distances, kernels"]
    P2_FE_LEARNER -->|"Clustering"| P2_FE_CLUSTERING["Clustering<br/>k-means with DTW, spectral clustering"]
    P2_FE_LEARNER -->|"Regression"| P6_TREE_ENSEMBLES[["Tree ensembles on lag features"]]
    P2_FE_DISTANCES --> P2_FE_SHAPELETS["Shapelets and ROCKET"]
    P2_FE_SHAPELETS --> P2_FE_DEEP_CLASSIFIERS["Deep classifiers<br/>InceptionTime"]
    P2_FE_DEEP_CLASSIFIERS & P2_FE_CLUSTERING & P6_TREE_ENSEMBLES --> P2_FE_AUGMENTATION["Data augmentation<br/>slicing, warping, synthetic oversampling"]
    P2_FE_AUGMENTATION --> P8_HYPERPARAMETERS[["Time-aware hyperparameter tuning"]]
    P8_HYPERPARAMETERS --> P11_CLASSIFICATION_METRICS[["Classification and anomaly metrics"]]
    P11_CLASSIFICATION_METRICS --> P2_FE_OUT(["Labels or groups assigned"])
    class P2_FE_FROM_PART_1,P2_FE_OUT terminator
    class P2_FE_REPRESENTATION,P2_FE_LEARNER decision
    class P2_FE_SYMBOLIC,P2_FE_REPRESENTATION_LEARNING,P2_FE_TDA,P2_FE_DISTANCES,P2_FE_CLUSTERING,P2_FE_SHAPELETS,P2_FE_DEEP_CLASSIFIERS,P2_FE_AUGMENTATION process
    class P6_TREE_ENSEMBLES,P8_HYPERPARAMETERS,P11_CLASSIFICATION_METRICS ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## P10 inference for this purpose

Feature importance, prototypes.

## P11 metrics for this purpose

Downstream cross-validation, F1, silhouette.
