# P6: Conditional-mean model class

**Question this phase answers:** Which family describes the mean?

P6 reads the value type and the structure first: counts and categories, event times, curves, wide panels and spatial or network data continue in the P6 part of their branch chart, and a deliverable that is no conditional-mean model goes to its purpose chart (part 12) and then to P10. For continuous and compositional series P6 reads the pooling, mixed-frequency and structure flags to choose a route, then the family on that route: linear, long memory, smoothing, periodic and intermittent for one series; VAR, VECM and ADL for a few related series; factor, shrinkage and graphical models for many variables; nonlinear, time-varying and latent-component, input-output, and learner families. Covariates, intervention terms and deterministic regressors are read after the family, because every family can carry them. The first question has answer No when the deliverable is a component, a filtered signal, a spectrum, a classifier, a detector, a segmentation or a resampled path; state-space smoothing, regime switching and residual-based detection fit a model, so their answer is Yes. P6 can emit several candidates (for example a local ETS and a global gradient-boosting model); each passes P7 to P9 and meets the P0 baselines in P10.

## Sub-diagram

**Part 1: routing on the value type and the structure.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_IN(["Transformed series, representation, flags"]) --> P6_MODEL_NEEDED{"Is a conditional-mean model the deliverable?"}
    P6_MODEL_NEEDED -->|"No"| P6_TO_PART_12(["Continue in part 12"])
    P6_MODEL_NEEDED -->|"Yes"| P6_VALUE_TYPE{"Value-type flag?"}
    P6_VALUE_TYPE -->|"Counts or categorical"| B1[["B1 Counts and categorical<br/>its P6 part: count and categorical families"]]
    P6_VALUE_TYPE -->|"Event times"| B2[["B2 Event times<br/>its P6 part: intensity families"]]
    P6_VALUE_TYPE -->|"Curves"| B4[["B4 Functional<br/>its P6 part: functional families"]]
    P6_VALUE_TYPE -->|"Continuous or compositional"| P6_PANEL_Q{"Structure flag?"}
    P6_PANEL_Q -->|"Wide panel"| B6[["B6 Wide panel<br/>its P6 part: panel families"]]
    P6_PANEL_Q -->|"Spatial or network"| B5[["B5 Spatial and network<br/>its P6 part: spatio-temporal families"]]
    P6_PANEL_Q -->|"Single, few related or many similar"| P6_TO_PART_2(["Continue in part 2"])
    class P6_IN,P6_TO_PART_12,P6_TO_PART_2 terminator
    class P6_MODEL_NEEDED,P6_VALUE_TYPE,P6_PANEL_Q decision
    class B1,B2,B4,B6,B5 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 2: routing on the pooling, mixed-frequency and structure flags.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_2_IN(["From part 1"]) --> P6_POOLING{"Pooling flag?"}
    P6_POOLING -->|"Global"| P6_GLOBAL_MODELS["Global models across many series<br/>one learner trained on all series"]
    P6_POOLING -->|"Compare: both routes"| P6_GLOBAL_MODELS
    P6_POOLING -->|"Compare: both routes"| P6_MIXED_Q
    P6_POOLING -->|"Local, or cluster then local"| P6_MIXED_Q{"Mixed-frequency flag?"}
    P6_POOLING -->|"Partial"| P6_PARTIAL_POOLING["Hierarchical models with partial pooling<br/>series parameters drawn from a common distribution"]
    P6_GLOBAL_MODELS --> P6_TO_PART_9(["Continue in part 9"])
    P6_MIXED_Q -->|"Yes"| P6_MIXED_FREQUENCY["Mixed-frequency models<br/>MIDAS, mixed-frequency VAR"]
    P6_MIXED_Q -->|"No"| P6_STRUCTURE_Q{"Structure flag?"}
    P6_STRUCTURE_Q -->|"Single, or many similar fitted one by one"| P6_TO_PART_5(["Continue in part 5"])
    P6_STRUCTURE_Q -->|"A few related"| P6_TO_PART_3(["Continue in part 3"])
    P6_STRUCTURE_Q -->|"Many variables"| P6_TO_PART_4(["Continue in part 4"])
    P6_MIXED_FREQUENCY & P6_PARTIAL_POOLING --> P6_PART_2_OUT(["Continue in part 11"])
    class P6_GLOBAL_MODELS,P6_PARTIAL_POOLING,P6_MIXED_FREQUENCY escalate
    class P6_PART_2_IN,P6_TO_PART_9,P6_TO_PART_5,P6_TO_PART_3,P6_TO_PART_4,P6_PART_2_OUT terminator
    class P6_POOLING,P6_MIXED_Q,P6_STRUCTURE_Q decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 3: a few related series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_3_IN(["From part 2: a few related series"]) --> P6_COINTEGRATED{"Cointegration flag?"}
    P6_COINTEGRATED -->|"Rank r of at least 1"| P6_VECM["VECM<br/>rank r from P3; fractional cointegration (FCVAR)"]
    P6_COINTEGRATED -->|"Mixed orders, one equation, weakly exogenous regressors"| P6_DYNAMIC_REGRESSION[["Distributed-lag and ADL models"]]
    P6_COINTEGRATED -->|"Mixed orders with feedback, or no cointegration"| P6_VAR["VAR<br/>in levels for mixed orders; in differences when r = 0 and all series are I(1)"]
    P6_VAR -->|"Structural question"| P6_SVAR["SVAR<br/>identification schemes in P11"]
    P6_VAR -->|"Time-varying"| P6_TVP_VAR["Time-varying parameter VAR"]
    P6_VAR -->|"Reduced form"| P6_PART_3_OUT
    P6_VECM & P6_SVAR & P6_TVP_VAR & P6_DYNAMIC_REGRESSION --> P6_PART_3_OUT(["Continue in part 11"])
    class P6_VECM,P6_VAR,P6_SVAR,P6_TVP_VAR escalate
    class P6_PART_3_IN,P6_PART_3_OUT terminator
    class P6_COINTEGRATED decision
    class P6_DYNAMIC_REGRESSION ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 4: many variables.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_4_IN(["From part 2: many variables"]) --> P6_DIMENSION{"Dimension reduction?"}
    P6_DIMENSION -->|"Factors"| P6_FACTOR_MODELS["Static and dynamic factor models"]
    P6_DIMENSION -->|"Shrinkage"| P6_REGULARISED_VAR["Regularised VAR<br/>LASSO, ridge, elastic net"]
    P6_DIMENSION -->|"Bayesian shrinkage"| P6_BVAR["Bayesian VAR<br/>Minnesota and conjugate priors"]
    P6_DIMENSION -->|"Graph"| P6_GRAPHICAL_MODELS["Graphical models and sparse precision matrices"]
    P6_DIMENSION -->|"Tensor"| P6_TENSOR_AR["Matrix and tensor autoregression"]
    P6_DIMENSION -->|"Learn from data"| P6_PART_4_TO_PART_9(["Continue in part 9"])
    P6_FACTOR_MODELS -->|"Factors in a VAR"| P6_FAVAR["FAVAR and GVAR"]
    P6_FACTOR_MODELS -->|"Factors alone"| P6_PART_4_OUT
    P6_FAVAR & P6_REGULARISED_VAR & P6_BVAR & P6_GRAPHICAL_MODELS & P6_TENSOR_AR --> P6_PART_4_OUT(["Continue in part 11"])
    class P6_FACTOR_MODELS,P6_REGULARISED_VAR,P6_BVAR,P6_GRAPHICAL_MODELS,P6_TENSOR_AR,P6_FAVAR escalate
    class P6_PART_4_IN,P6_PART_4_TO_PART_9,P6_PART_4_OUT terminator
    class P6_DIMENSION decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: one series, and its linear families.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_5_IN(["From part 2: one series"]) --> P6_DEPENDENCE{"Dependence type?"}
    P6_DEPENDENCE -->|"Linear"| P6_LINEAR{"Fractional remainder flag?"}
    P6_DEPENDENCE -->|"Nonlinear flag"| P6_TO_PART_6(["Continue in part 6"])
    P6_DEPENDENCE -->|"Time-varying or latent components"| P6_TO_PART_7(["Continue in part 7"])
    P6_DEPENDENCE -->|"Input-output system"| P6_TO_PART_8(["Continue in part 8"])
    P6_DEPENDENCE -->|"Learn from data, long series"| P6_PART_5_TO_PART_9(["Continue in part 9"])
    P6_LINEAR -->|"Yes"| P6_ARFIMA["ARFIMA<br/>exact ML of d - k after differencing, or CSS on the levels"]
    P6_LINEAR -->|"No"| P6_LINEAR_FAMILY{"Family?"}
    P6_LINEAR_FAMILY -->|"Autoregressive"| P6_AR_MA_ARMA["AR, MA and ARMA"]
    P6_LINEAR_FAMILY -->|"Smoothing"| P6_SMOOTHING{"Smoothing method?"}
    P6_LINEAR_FAMILY -->|"Periodic"| P6_PERIODIC_AR["Periodic autoregression"]
    P6_LINEAR_FAMILY -->|"Intermittent"| P6_INTERMITTENT["Intermittent demand<br/>Croston, TSB"]
    P6_SMOOTHING -->|"State-space ETS"| P6_ETS["Exponential smoothing and ETS<br/>on the levels"]
    P6_SMOOTHING -->|"Theta decomposition"| P6_THETA["Theta method<br/>on the levels"]
    P6_AR_MA_ARMA --> P6_ARIMA_SARIMA["ARIMA and SARIMA<br/>ARMA after P4 differencing or ARIMA on the levels, not both"]
    P6_ARFIMA & P6_ARIMA_SARIMA & P6_ETS --> P6_PART_5_OUT
    P6_THETA & P6_PERIODIC_AR & P6_INTERMITTENT --> P6_PART_5_OUT(["Continue in part 11"])
    F_LAG_OPERATOR[["Lag operator, difference equations and characteristic roots"]] -.- P6_AR_MA_ARMA
    class P6_ARFIMA,P6_AR_MA_ARMA,P6_PERIODIC_AR,P6_INTERMITTENT,P6_ETS,P6_THETA,P6_ARIMA_SARIMA escalate
    class P6_PART_5_IN,P6_TO_PART_6,P6_TO_PART_7,P6_TO_PART_8,P6_PART_5_TO_PART_9,P6_PART_5_OUT terminator
    class P6_DEPENDENCE,P6_LINEAR,P6_LINEAR_FAMILY,P6_SMOOTHING decision
    class F_LAG_OPERATOR ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 6: nonlinear families.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_6_IN(["From part 5: nonlinear flag"]) --> P6_NONLINEAR_FAMILY{"Regime mechanism?"}
    P6_NONLINEAR_FAMILY -->|"Threshold"| P6_THRESHOLD["Threshold models<br/>TAR, SETAR, MTAR"]
    P6_NONLINEAR_FAMILY -->|"Smooth"| P6_SMOOTH_TRANSITION["Smooth-transition models<br/>STAR, LSTAR, ESTAR"]
    P6_NONLINEAR_FAMILY -->|"Hidden state"| P6_MARKOV_SWITCHING["Markov-switching models"]
    P6_NONLINEAR_FAMILY -->|"Bilinear"| P6_BILINEAR["Bilinear models"]
    P6_NONLINEAR_FAMILY -->|"Unknown form"| P6_NONPARAMETRIC["Nonparametric and additive regression<br/>kernels, local polynomials, GAM"]
    P6_THRESHOLD & P6_SMOOTH_TRANSITION & P6_MARKOV_SWITCHING & P6_BILINEAR & P6_NONPARAMETRIC --> P6_PART_6_OUT(["Continue in part 11"])
    class P6_THRESHOLD,P6_SMOOTH_TRANSITION,P6_MARKOV_SWITCHING,P6_BILINEAR,P6_NONPARAMETRIC escalate
    class P6_PART_6_IN,P6_PART_6_OUT terminator
    class P6_NONLINEAR_FAMILY decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 7: time-varying and latent-component families.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_7_IN(["From part 5"]) --> P6_STRUCTURED{"Structure?"}
    P6_STRUCTURED -->|"Time-varying coefficients"| P6_TVP_REGRESSION["Time-varying parameter regression"]
    P6_STRUCTURED -->|"Latent components"| P6_LATENT_MODEL{"Latent model?"}
    P6_LATENT_MODEL -->|"Components"| P6_STRUCTURAL_TS["Structural time-series models<br/>on the levels: local level, local linear trend, seasonal, cycle"]
    P6_LATENT_MODEL -->|"General linear Gaussian"| P6_DLM["Dynamic linear models<br/>linear Gaussian state space; ARIMA as a special case"]
    P6_LATENT_MODEL -->|"Bayesian, many candidate regressors"| P6_BSTS["Bayesian structural time series<br/>on the levels; spike-and-slab regressor selection"]
    P6_TVP_REGRESSION & P6_STRUCTURAL_TS & P6_DLM & P6_BSTS --> P6_PART_7_OUT(["Continue in part 11"])
    class P6_TVP_REGRESSION,P6_STRUCTURAL_TS,P6_DLM,P6_BSTS escalate
    class P6_PART_7_IN,P6_PART_7_OUT terminator
    class P6_STRUCTURED,P6_LATENT_MODEL decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 8: input-output systems.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_8_IN(["From part 5: input-output system"]) --> P6_IO_STRUCTURE{"Structure?"}
    P6_IO_STRUCTURE -->|"Noise shares the system poles"| P6_ARX_ARMAX["ARX and ARMAX input-output models"]
    P6_IO_STRUCTURE -->|"State space"| P6_SUBSPACE["Subspace identification<br/>N4SID"]
    P6_IO_STRUCTURE -->|"Block-oriented"| P6_HAMMERSTEIN_WIENER["Hammerstein-Wiener models"]
    P6_IO_STRUCTURE -->|"Sparse nonlinear"| P6_SINDY["Sparse identification of nonlinear dynamics"]
    P6_IO_STRUCTURE -->|"Independent noise model"| P6_TRANSFER_FUNCTION[["Transfer-function and intervention models"]]
    P6_IO_STRUCTURE -->|"No noise model"| P6_OUTPUT_ERROR["Output-error models"]
    P6_ARX_ARMAX & P6_OUTPUT_ERROR & P6_SUBSPACE & P6_HAMMERSTEIN_WIENER & P6_SINDY & P6_TRANSFER_FUNCTION --> P6_PART_8_OUT(["Continue in part 11"])
    class P6_ARX_ARMAX,P6_OUTPUT_ERROR,P6_SUBSPACE,P6_HAMMERSTEIN_WIENER,P6_SINDY escalate
    class P6_PART_8_IN,P6_PART_8_OUT terminator
    class P6_IO_STRUCTURE decision
    class P6_TRANSFER_FUNCTION ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 9: learners: multi-step strategy, then classical, pretrained or generative, and hybrid.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_9_IN(["From parts 2, 4 and 5"]) --> P6_FD_Q{"Fractional remainder flag?"}
    P6_FD_Q -->|"Yes"| P6_FRACTIONAL_DIFFERENCE["Fractional differencing for learners<br/>d estimated inside each training window"]
    P6_FD_Q -->|"No"| P6_HORIZON_Q
    P6_FRACTIONAL_DIFFERENCE --> P6_HORIZON_Q{"Horizon beyond one step?"}
    P6_HORIZON_Q -->|"Yes"| P6_MULTISTEP["Multi-step strategies<br/>recursive, direct, MIMO; direct uses lags of at least h"]
    P6_HORIZON_Q -->|"No"| P6_ML_FAMILY
    P6_MULTISTEP --> P6_ML_FAMILY{"Model family?"}
    P6_ML_FAMILY -->|"Classical ML"| P6_ML_CLASSICAL{"Learner?"}
    P6_ML_FAMILY -->|"Neural sequence models"| P6_TO_PART_10(["Continue in part 10"])
    P6_ML_FAMILY -->|"Pretrained"| P6_FOUNDATION_MODELS["Foundation models<br/>Chronos, Lag-Llama, Moirai, TimesFM, MOMENT"]
    P6_ML_FAMILY -->|"Generative"| P6_GENERATIVE["Generative models for time series<br/>diffusion models"]
    P6_ML_FAMILY -->|"Hybrid"| P6_HYBRID["Hybrid models<br/>ARIMA with neural residuals"]
    P6_ML_CLASSICAL -->|"Pooled linear"| P6_POOLED_AR["Pooled linear autoregression"]
    P6_ML_CLASSICAL -->|"Trees"| P6_TREE_ENSEMBLES["Tree ensembles on lag features<br/>random forests, XGBoost, LightGBM"]
    P6_ML_CLASSICAL -->|"Kernel"| P6_GAUSSIAN_PROCESS["Gaussian-process regression"]
    P6_POOLED_AR & P6_TREE_ENSEMBLES & P6_GAUSSIAN_PROCESS --> P6_PART_9_OUT
    P6_FOUNDATION_MODELS & P6_GENERATIVE & P6_HYBRID --> P6_PART_9_OUT(["Continue in part 11"])
    class P6_HYBRID,P6_POOLED_AR,P6_TREE_ENSEMBLES,P6_GAUSSIAN_PROCESS,P6_FOUNDATION_MODELS,P6_GENERATIVE escalate
    class P6_PART_9_IN,P6_TO_PART_10,P6_PART_9_OUT terminator
    class P6_FD_Q,P6_HORIZON_Q,P6_ML_FAMILY,P6_ML_CLASSICAL decision
    class P6_FRACTIONAL_DIFFERENCE,P6_MULTISTEP process
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 10: neural sequence models.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_10_IN(["From part 9: neural sequence models"]) --> P6_ML_NEURAL{"Architecture?"}
    P6_ML_NEURAL -->|"Recurrent"| P6_RNN["Recurrent networks<br/>RNN, LSTM, GRU, DeepAR"]
    P6_ML_NEURAL -->|"Convolutional"| P6_TCN["Temporal convolutional networks"]
    P6_ML_NEURAL -->|"Attention"| P6_TRANSFORMERS["Transformers for time series<br/>Informer, Autoformer, PatchTST"]
    P6_ML_NEURAL -->|"State-space sequence"| P6_SSM_SEQUENCE["State-space sequence models<br/>S4, S5, Mamba"]
    P6_ML_NEURAL -->|"MLP forecasters"| P6_NEURAL_FORECASTERS["Neural forecasters<br/>N-BEATS, N-HiTS, TiDE"]
    P6_ML_NEURAL -->|"Fixed random recurrence"| P6_RESERVOIR["Reservoir computing<br/>echo state networks"]
    P6_RNN & P6_TCN & P6_TRANSFORMERS & P6_SSM_SEQUENCE & P6_NEURAL_FORECASTERS & P6_RESERVOIR --> P6_PART_10_OUT(["Continue in part 11"])
    class P6_RNN,P6_TCN,P6_TRANSFORMERS,P6_SSM_SEQUENCE,P6_NEURAL_FORECASTERS,P6_RESERVOIR escalate
    class P6_PART_10_IN,P6_PART_10_OUT terminator
    class P6_ML_NEURAL decision
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 11: terms every family can carry, model kind and the candidate set.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_11_IN(["From the family parts"]) --> P6_COVARIATE_Q{"Covariates flag?"}
    P6_COVARIATE_Q -->|"None, or already inside the family: VAR, learners, TVP regression"| P6_INTERVENTION_Q
    P6_COVARIATE_Q -->|"Known future, external forecast, or lagged"| P6_EXOG_FORM{"How do covariates enter?"}
    P6_EXOG_FORM -->|"Marginal effect, dependent errors"| P6_REGRESSION_FLAG["Set flag: regression with dependent errors"]
    P6_EXOG_FORM -->|"Inside the recursion"| P6_ARIMAX["ARIMAX and SARIMAX<br/>beta is an impact; long-run effect beta / phi(1)"]
    P6_EXOG_FORM -->|"Distributed lags"| P6_DYNAMIC_REGRESSION["Distributed-lag and ADL models<br/>ARDL bounds test, single-equation ECM"]
    P6_EXOG_FORM -->|"Rational lag with a noise model"| P6_TRANSFER_FUNCTION["Transfer-function and intervention models<br/>Chen-Liu outlier types: additive, innovation, level shift, temporary change"]
    P6_REGRESSION_FLAG & P6_ARIMAX & P6_DYNAMIC_REGRESSION --> P6_INTERVENTION_Q{"Intervention-terms flag?"}
    P6_INTERVENTION_Q -->|"Yes: candidate-outlier mask"| P6_TRANSFER_FUNCTION
    P6_INTERVENTION_Q -->|"No"| P6_DETERMINISTIC_Q
    P6_TRANSFER_FUNCTION --> P6_DETERMINISTIC_Q{"Trend, drift, seasonality or calendar flags?"}
    P6_DETERMINISTIC_Q -->|"Yes"| P6_DETERMINISTIC["Deterministic regressors<br/>trend, a drift constant in the differenced model, seasonal dummies or Fourier terms, calendar and holiday effects"]
    P6_DETERMINISTIC_Q -->|"No"| P6_PRIOR_Q
    P6_DETERMINISTIC --> P6_PRIOR_Q{"Prior specified?"}
    P6_PRIOR_Q -->|"Yes: Bayesian family or Bayesian estimation"| P6_PRIOR_FLAG["Set flag: prior specified"]
    P6_PRIOR_Q -->|"No"| P6_KIND_FLAG
    P6_PRIOR_FLAG --> P6_KIND_FLAG["Set flag: model kind<br/>likelihood, loss minimisation, Bayesian"]
    P6_KIND_FLAG --> P6_CANDIDATE_SET["Candidate set<br/>each family and pooling regime passes P7 to P9; P0 baselines join in P10"]
    P6_CANDIDATE_SET --> P7[["P7: Error-process specification"]]
    class P6_ARIMAX,P6_DYNAMIC_REGRESSION,P6_TRANSFER_FUNCTION,P6_DETERMINISTIC escalate
    class P6_PART_11_IN terminator
    class P6_COVARIATE_Q,P6_EXOG_FORM,P6_INTERVENTION_Q,P6_DETERMINISTIC_Q,P6_PRIOR_Q decision
    class P6_REGRESSION_FLAG,P6_PRIOR_FLAG,P6_KIND_FLAG,P6_CANDIDATE_SET process
    class P7 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 12: routes that fit no conditional-mean model.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_12_IN(["From part 1: no conditional-mean model"]) --> P6_NO_MODEL{"Purpose flag?"}
    P6_NO_MODEL -->|"Components, signal or spectrum"| P10[["P10: Out-of-sample evaluation and selection<br/>the method was chosen in P4 and P5"]]
    P6_NO_MODEL -->|"Detection, labels, clusters or resampled paths"| P0[["P0: Purpose and evaluation plan<br/>the method part of the purpose chart, then P10"]]
    class P6_PART_12_IN terminator
    class P6_NO_MODEL decision
    class P10,P0 ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

## Phase guide

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P6`). Write this section following the content rules in `.claude/rules/writing.md`.

## Candidate set

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P6_CANDIDATE_SET`). Write this section following the content rules in `.claude/rules/writing.md`.
