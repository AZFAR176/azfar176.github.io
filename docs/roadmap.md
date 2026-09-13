# Roadmap

## Phase 0: Setup and Data Contracts
- Define common telemetry schema (timestamps, rank id, metric name, value).
- Define workload event schema (step begin/end, batch metadata, tokens).
- Create adapter interface for telemetry sources.

Deliverable: schema docs + parser stubs.

## Phase 1: Telemetry Ingestion
- Implement ingestion adapters for baseline sources (CSV/JSON exports first).
- Normalize timestamps and align per-rank timelines.
- Store unified trace in simple local format.

Deliverable: one command to load and normalize a run.

## Phase 2: Behavioral Profiling
- Build feature extraction over windows and full steps:
  - utilization moments,
  - idle/wait fractions,
  - NCCL-to-compute ratio,
  - memory pressure indicators,
  - inter-rank skew metrics.
- Segment runs into phases (warmup/steady-state/spikes).

Deliverable: profile report object.

## Phase 3: Bottleneck Diagnosis Engine (Rule-Based MVP)
- Encode first-pass diagnostic rules with confidence.
- Support multi-label diagnoses where needed.
- Add contradiction checks to prevent overconfident wrong labels.

Deliverable: bottleneck classifier with evidence traces.

## Phase 4: Insight and Recommendation Generation
- Convert diagnosis + evidence into human-readable explanation.
- Rank recommendations by likely impact and effort.
- Add guardrails for recommendation quality.

Deliverable: actionable text report + JSON output.

## Phase 5: Comparative Optimization Loop
- Analyze baseline run A and candidate run B.
- Quantify improvement or regression on key KPIs.
- Feed delta back into recommendation ranking.

Deliverable: "did this fix help?" report.

## Phase 6: Productionization
- Streaming mode for near-real-time signals.
- Dashboard integration and alerting.
- Experiment tracking integration.

Deliverable: service mode + CI quality checks.

## Initial Tech Stack
- Python 3.11+
- `pydantic` for typed schemas
- `numpy`/`pandas` for feature aggregation
- optional `networkx` for dependency/rank-flow analysis

## Key Risks
- Metric availability differs by platform.
- Telemetry clocks can be misaligned.
- One symptom can map to multiple causes.

## Mitigations
- confidence and uncertainty reporting
- layered diagnosis (dominant + secondary factors)
- calibration with expert-labeled traces
