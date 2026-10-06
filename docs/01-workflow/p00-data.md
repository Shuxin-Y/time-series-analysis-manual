# P0: Data acquisition and cleaning

**Question this phase answers:** Is the series fit to analyse?

Sampling rate and resolution; timestamp alignment, time zones, daylight-saving transitions, duplicate stamps; missing-value imputation; the time-series outlier taxonomy (additive, innovation, level shift, temporary change); robust filtering; unit and metadata consistency; cumulative-to-flow conversion; anti-aliasing when downsampling; calendar effects; temporal disaggregation; data revisions and vintages.

## Sub-diagram

!!! note "Diagram pending"
    To-do item from the flowchart inventory (node `P0`): draw the P0 sub-diagram following the decision-flowchart notation in `DESIGN-SYSTEM.md`; its leaf nodes get rows in `docs/flowcharts/inventory.yml`.

## Phase guide

!!! note "Section pending"
    Procedural guide to this phase: which tests to run, in which order, and where each outcome leads.

### Topics carried over from the previous outline

- Inspection and sampling: data quality, sampling rates, alignment
- Missing data: imputation strategies and segmentation
- Outlier detection: statistical methods for identifying and treating outliers
- Transformations: variance stabilisation, detrending, normalisation
