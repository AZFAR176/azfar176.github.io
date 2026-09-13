# PR Title

Initialize GPU profiler project scaffold (telemetry -> diagnosis -> recommendation loop)

# PR Body

## What this PR adds

- creates a new `gpu-profiler-project` scaffold with a clear project goal and first milestones
- adds end-to-end pipeline framing:
  - collect telemetry
  - analyze workload behavior
  - detect bottlenecks
  - explain likely causes
  - recommend optimizations
  - validate improvements with comparative reruns
- adds project planning docs:
  - `docs/project_scope.md`
  - `docs/roadmap.md`
- adds starter Python package structure under `src/gpu_profiler/`:
  - telemetry collector stub
  - workload analyzer stub
  - bottleneck classifier (rule-based baseline)
  - recommendation engine
  - pipeline orchestrator
  - CLI entrypoint
- adds packaging and repo basics:
  - `pyproject.toml`
  - `.gitignore`

## Why

This establishes a practical baseline for building an intelligent profiling system that turns low-level training/inference telemetry into actionable optimization guidance.

## Validation

- Python syntax compiled successfully:
  - `python3 -m compileall src`
- Basic lint diagnostics: no issues reported in the created files.

## Next steps

- implement telemetry parsers for real sources (Nsight/NVML/DCGM/NCCL traces)
- add feature extraction from aligned per-step/per-rank timelines
- improve diagnosis confidence calibration and multi-label handling
- add evaluation harness to measure recommendation impact (A/B run comparisons)
