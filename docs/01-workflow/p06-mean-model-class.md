# P6: Conditional-mean model class

**Question this phase answers:** Which family describes the mean?

Routing on the multivariate, global and exogenous-variable flags, then the model families: univariate linear, periodic and intermittent, long memory, nonlinear, time-varying parameter, multivariate, structural state-space, system identification, count and categorical, machine learning and deep learning, and global models.

## Sub-diagram

**Part 1: routing on the flags.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_IN(["Transformed series, representation, flags"]) --> P6_EXOGENOUS{"Exogenous variables?"}
    P6_EXOGENOUS -->|"Future known"| P6_EXOG_FLAG["Set flag: exogenous regressors"]
    P6_EXOGENOUS -->|"Co-forecast"| P6_MULTI_FLAG["Set flag: multivariate"]
    P6_EXOGENOUS -->|"None"| P6_GLOBAL_Q
    P6_EXOG_FLAG & P6_MULTI_FLAG --> P6_GLOBAL_Q{"Global flag?"}
    P6_GLOBAL_Q -->|"Yes"| P6_GLOBAL_MODELS["Global models across many series"]
    P6_GLOBAL_Q -->|"No"| P6_MIXED_Q{"Mixed-frequency flag?"}
    P6_MIXED_Q -->|"Yes"| P6_MIXED_FREQUENCY["Mixed-frequency models<br/>MIDAS, mixed-frequency VAR"]
    P6_MIXED_Q -->|"No"| P6_MULTI_Q{"Multivariate flag?"}
    P6_MULTI_Q -->|"Yes"| P6_MANY_Q{"Many variables?"}
    P6_MULTI_Q -->|"No"| P6_TO_PART_4(["Continue in part 4"])
    P6_MANY_Q -->|"No"| P6_TO_PART_2(["Continue in part 2"])
    P6_MANY_Q -->|"Yes"| P6_TO_PART_3(["Continue in part 3"])
    P6_GLOBAL_MODELS & P6_MIXED_FREQUENCY --> P7[["P7: Error-process specification"]]
    class P6_IN,P6_TO_PART_4,P6_TO_PART_2,P6_TO_PART_3 terminator
    class P6_EXOGENOUS,P6_GLOBAL_Q,P6_MIXED_Q,P6_MULTI_Q,P6_MANY_Q decision
    class P6_EXOG_FLAG,P6_MULTI_FLAG,P6_GLOBAL_MODELS,P6_MIXED_FREQUENCY process
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

**Part 2: a few related series.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_2_IN(["From part 1: a few related series"]) --> P6_COINTEGRATED{"Cointegrated?"}
    P6_COINTEGRATED -->|"Yes"| P6_VECM["VECM"]
    P6_COINTEGRATED -->|"No"| P6_VAR["VAR"]
    P6_VAR -->|"Structural question"| P6_SVAR["SVAR<br/>identification schemes in P10"]
    P6_VAR -->|"Time-varying"| P6_TVP_VAR["Time-varying parameter VAR"]
    P6_VAR -->|"Reduced form"| P7
    P6_VECM & P6_SVAR & P6_TVP_VAR --> P7[["P7: Error-process specification"]]
    class P6_PART_2_IN terminator
    class P6_COINTEGRATED decision
    class P6_VECM,P6_VAR,P6_SVAR,P6_TVP_VAR process
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

**Part 3: many variables.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_3_IN(["From part 1: many variables"]) --> P6_DIMENSION{"Dimension reduction?"}
    P6_DIMENSION -->|"Factors"| P6_FACTOR_MODELS["Static and dynamic factor models"]
    P6_DIMENSION -->|"Shrinkage"| P6_REGULARISED_VAR["Regularised VAR<br/>LASSO, ridge, elastic net"]
    P6_DIMENSION -->|"Bayesian shrinkage"| P6_BVAR["Bayesian VAR<br/>Minnesota and conjugate priors"]
    P6_DIMENSION -->|"Graph"| P6_GRAPHICAL_MODELS["Graphical models and sparse precision matrices"]
    P6_DIMENSION -->|"Tensor"| P6_TENSOR_AR["Matrix and tensor autoregression"]
    P6_FACTOR_MODELS -->|"Factors in a VAR"| P6_FAVAR["FAVAR and global VAR"]
    P6_FACTOR_MODELS -->|"Factors alone"| P7
    P6_FAVAR & P6_REGULARISED_VAR & P6_BVAR & P6_GRAPHICAL_MODELS & P6_TENSOR_AR --> P7[["P7: Error-process specification"]]
    class P6_PART_3_IN terminator
    class P6_DIMENSION decision
    class P6_FACTOR_MODELS,P6_REGULARISED_VAR,P6_BVAR,P6_GRAPHICAL_MODELS,P6_TENSOR_AR,P6_FAVAR process
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

**Part 4: one series, and its linear families.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_4_IN(["From part 1: one series"]) --> P6_DEPENDENCE{"Dependence type?"}
    P6_DEPENDENCE -->|"Linear"| P6_LINEAR{"Long memory flag?"}
    P6_DEPENDENCE -->|"Nonlinear flag"| P6_TO_PART_6(["Continue in part 6"])
    P6_DEPENDENCE -->|"Time-varying, latent or Bayesian"| P6_TO_PART_7(["Continue in part 7"])
    P6_DEPENDENCE -->|"Input-output system"| P6_TO_PART_8(["Continue in part 8"])
    P6_DEPENDENCE -->|"Learn from data"| P6_TO_PART_9(["Continue in part 9"])
    P6_LINEAR -->|"Yes"| P6_ARFIMA["ARFIMA"]
    P6_LINEAR -->|"No"| P6_LINEAR_FAMILY{"Family?"}
    P6_LINEAR_FAMILY -->|"Autoregressive"| P6_AR_MA_ARMA["AR, MA and ARMA"]
    P6_LINEAR_FAMILY -->|"Exogenous flag"| P6_TO_PART_5(["Continue in part 5"])
    P6_LINEAR_FAMILY -->|"Smoothing"| P6_SMOOTHING{"Smoothing method?"}
    P6_LINEAR_FAMILY -->|"Periodic"| P6_PERIODIC_AR["Periodic autoregression"]
    P6_LINEAR_FAMILY -->|"Intermittent"| P6_INTERMITTENT["Intermittent demand<br/>Croston, TSB"]
    P6_SMOOTHING -->|"State-space ETS"| P6_ETS["Exponential smoothing and ETS"]
    P6_SMOOTHING -->|"Theta decomposition"| P6_THETA["Theta method"]
    P6_AR_MA_ARMA --> P6_ARIMA_SARIMA["ARIMA and SARIMA"]
    P6_ARFIMA & P6_ARIMA_SARIMA & P6_ETS --> P7
    P6_THETA & P6_PERIODIC_AR & P6_INTERMITTENT --> P7[["P7: Error-process specification"]]
    F_LAG_OPERATOR[["Lag operator, difference equations and characteristic roots"]] -.- P6_AR_MA_ARMA
    class P6_PART_4_IN,P6_TO_PART_6,P6_TO_PART_7,P6_TO_PART_8,P6_TO_PART_9,P6_TO_PART_5 terminator
    class P6_DEPENDENCE,P6_LINEAR,P6_LINEAR_FAMILY,P6_SMOOTHING decision
    class P6_ARFIMA,P6_AR_MA_ARMA,P6_PERIODIC_AR,P6_INTERMITTENT,P6_ETS,P6_THETA,P6_ARIMA_SARIMA process
    class P7,F_LAG_OPERATOR ref
    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef data fill:#FFF4E0,stroke:#C9A55E,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
    classDef escalate fill:#FFE9C2,stroke:#C9A55E,color:#1A1A1A;
    classDef problem fill:#F2D9DE,stroke:#800020,color:#1A1A1A;
    classDef ref fill:#F7F7F7,stroke:#5A6B73,color:#1A1A1A,stroke-dasharray:4 3;
```

**Part 5: exogenous regressors.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_5_IN(["From part 4: exogenous flag"]) --> P6_EXOG_FORM{"Exogenous form?"}
    P6_EXOG_FORM -->|"Inputs in the ARMA recursion"| P6_ARIMAX["ARIMAX and SARIMAX"]
    P6_EXOG_FORM -->|"Distributed lags"| P6_DYNAMIC_REGRESSION["Distributed-lag and ADL models"]
    P6_EXOG_FORM -->|"Transfer function or intervention"| P6_TRANSFER_FUNCTION["Transfer-function and intervention models"]
    P6_ARIMAX & P6_DYNAMIC_REGRESSION & P6_TRANSFER_FUNCTION --> P7[["P7: Error-process specification"]]
    class P6_PART_5_IN terminator
    class P6_EXOG_FORM decision
    class P6_ARIMAX,P6_DYNAMIC_REGRESSION,P6_TRANSFER_FUNCTION process
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

**Part 6: nonlinear families.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_6_IN(["From part 4: nonlinear flag"]) --> P6_NONLINEAR_FAMILY{"Regime mechanism?"}
    P6_NONLINEAR_FAMILY -->|"Threshold"| P6_THRESHOLD["Threshold models<br/>TAR, SETAR, MTAR"]
    P6_NONLINEAR_FAMILY -->|"Smooth"| P6_SMOOTH_TRANSITION["Smooth-transition models<br/>STAR, LSTAR, ESTAR"]
    P6_NONLINEAR_FAMILY -->|"Hidden state"| P6_MARKOV_SWITCHING["Markov-switching models"]
    P6_NONLINEAR_FAMILY -->|"Bilinear"| P6_BILINEAR["Bilinear models"]
    P6_NONLINEAR_FAMILY -->|"Unknown form"| P6_NONPARAMETRIC["Nonparametric and additive regression<br/>kernels, local polynomials, GAM"]
    P6_THRESHOLD & P6_SMOOTH_TRANSITION & P6_MARKOV_SWITCHING & P6_BILINEAR & P6_NONPARAMETRIC --> P7[["P7: Error-process specification"]]
    class P6_PART_6_IN terminator
    class P6_NONLINEAR_FAMILY decision
    class P6_THRESHOLD,P6_SMOOTH_TRANSITION,P6_MARKOV_SWITCHING,P6_BILINEAR,P6_NONPARAMETRIC process
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

**Part 7: time-varying, latent-component and Bayesian families.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_7_IN(["From part 4"]) --> P6_STRUCTURED{"Structure?"}
    P6_STRUCTURED -->|"Time-varying coefficients"| P6_TVP_REGRESSION["Time-varying parameter regression"]
    P6_STRUCTURED -->|"Latent components"| P6_LATENT_MODEL{"Latent model?"}
    P6_STRUCTURED -->|"Bayesian priors"| P6_DLM & P6_BSTS
    P6_LATENT_MODEL -->|"Components"| P6_STRUCTURAL_TS["Structural time-series models<br/>local level, local linear trend, seasonal, cycle"]
    P6_LATENT_MODEL -->|"General linear Gaussian"| P6_DLM["Dynamic linear models"]
    P6_LATENT_MODEL -->|"Bayesian with regressors"| P6_BSTS["Bayesian structural time series"]
    P6_TVP_REGRESSION & P6_STRUCTURAL_TS & P6_DLM & P6_BSTS --> P7[["P7: Error-process specification"]]
    class P6_PART_7_IN terminator
    class P6_STRUCTURED,P6_LATENT_MODEL decision
    class P6_TVP_REGRESSION,P6_STRUCTURAL_TS,P6_DLM,P6_BSTS process
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

**Part 8: input-output systems.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_8_IN(["From part 4: input-output system"]) --> P6_IO_STRUCTURE{"Structure?"}
    P6_IO_STRUCTURE -->|"Polynomial"| P6_ARX_ARMAX["ARX and ARMAX input-output models"]
    P6_IO_STRUCTURE -->|"State space"| P6_SUBSPACE["Subspace identification<br/>N4SID"]
    P6_IO_STRUCTURE -->|"Block-oriented"| P6_HAMMERSTEIN_WIENER["Hammerstein-Wiener models"]
    P6_IO_STRUCTURE -->|"Sparse nonlinear"| P6_SINDY["Sparse identification of nonlinear dynamics"]
    P6_ARX_ARMAX & P6_SUBSPACE & P6_HAMMERSTEIN_WIENER & P6_SINDY --> P7[["P7: Error-process specification"]]
    class P6_PART_8_IN terminator
    class P6_IO_STRUCTURE decision
    class P6_ARX_ARMAX,P6_SUBSPACE,P6_HAMMERSTEIN_WIENER,P6_SINDY process
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

**Part 9: machine-learning families: classical, pretrained or generative, and hybrid.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_9_IN(["From part 4: learn from data"]) --> P6_ML_FAMILY{"Model family?"}
    P6_ML_FAMILY -->|"Classical ML"| P6_ML_CLASSICAL{"Learner?"}
    P6_ML_FAMILY -->|"Neural sequence models"| P6_TO_PART_10(["Continue in part 10"])
    P6_ML_FAMILY -->|"Pretrained or generative"| P6_ML_PRETRAINED{"Approach?"}
    P6_ML_FAMILY -->|"Hybrid"| P6_HYBRID["Hybrid models<br/>ARIMA with neural residuals"]
    P6_ML_CLASSICAL -->|"Trees"| P6_TREE_ENSEMBLES["Tree ensembles on lag features<br/>random forests, XGBoost, LightGBM"]
    P6_ML_CLASSICAL -->|"Kernel"| P6_GAUSSIAN_PROCESS["Gaussian-process regression"]
    P6_ML_CLASSICAL -->|"Reservoir"| P6_RESERVOIR["Reservoir computing<br/>echo state networks"]
    P6_ML_PRETRAINED -->|"Pretrained"| P6_FOUNDATION_MODELS["Foundation models<br/>Chronos, Lag-Llama, Moirai, TimesFM, MOMENT"]
    P6_ML_PRETRAINED -->|"Generative"| P6_GENERATIVE["Generative models for time series<br/>diffusion models"]
    P6_TREE_ENSEMBLES & P6_GAUSSIAN_PROCESS & P6_RESERVOIR --> P7
    P6_FOUNDATION_MODELS & P6_GENERATIVE & P6_HYBRID --> P7[["P7: Error-process specification"]]
    class P6_PART_9_IN,P6_TO_PART_10 terminator
    class P6_ML_FAMILY,P6_ML_CLASSICAL,P6_ML_PRETRAINED decision
    class P6_HYBRID,P6_TREE_ENSEMBLES,P6_GAUSSIAN_PROCESS,P6_RESERVOIR,P6_FOUNDATION_MODELS,P6_GENERATIVE process
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

**Part 10: neural sequence models.**

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    P6_PART_10_IN(["From part 9: neural sequence models"]) --> P6_ML_NEURAL{"Architecture?"}
    P6_ML_NEURAL -->|"Recurrent"| P6_RNN["Recurrent networks<br/>RNN, LSTM, GRU"]
    P6_ML_NEURAL -->|"Convolutional"| P6_TCN["Temporal convolutional networks"]
    P6_ML_NEURAL -->|"Attention"| P6_TRANSFORMERS["Transformers for time series<br/>Informer, Autoformer, PatchTST"]
    P6_ML_NEURAL -->|"State-space sequence"| P6_SSM_SEQUENCE["State-space sequence models<br/>S4, S5, Mamba"]
    P6_ML_NEURAL -->|"MLP forecasters"| P6_NEURAL_FORECASTERS["Neural forecasters<br/>N-BEATS, N-HiTS, TiDE"]
    P6_RNN & P6_TCN & P6_TRANSFORMERS & P6_SSM_SEQUENCE & P6_NEURAL_FORECASTERS --> P7[["P7: Error-process specification"]]
    class P6_PART_10_IN terminator
    class P6_ML_NEURAL decision
    class P6_RNN,P6_TCN,P6_TRANSFORMERS,P6_SSM_SEQUENCE,P6_NEURAL_FORECASTERS process
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

## Phase guide

!!! note "Section pending"
    To-do item created from the flowchart inventory (node `P6`). Write this section following the content rules in `.claude/rules/writing.md`.
