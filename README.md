# GPU Profiler: Intelligent Performance Diagnosis for Model Workloads

An automated profiling system that reads GPU/workload telemetry during training or inference, diagnoses performance bottlenecks, explains root causes, and recommends concrete optimizations.

## What We Want To Do (First)

1. **Collect telemetry continuously** from GPU, CPU, communication stack, and workload runtime.
2. **Build a time-aligned workload profile** instead of isolated metric snapshots.
3. **Diagnose bottlenecks automatically** (compute, memory, communication, CPU/data, sync, underfeeding, imbalance).
4. **Generate plain-language explanations** that map signals to likely root causes.
5. **Recommend actionable optimizations** tied to each diagnosis.
6. **Close the loop experimentally**: apply recommendation, rerun, and measure improvement.

## One-line Pitch

> Intelligent GPU profiling for model workloads: observe, diagnose, explain, and optimize.

## End-to-End Pipeline

```text
Collect telemetry
  -> Analyze behavior over time
  -> Detect bottleneck class
  -> Explain likely cause
  -> Recommend optimization
  -> Validate by A/B rerun
```

## Example Signal Patterns

- `Low MFU + High HBM BW` -> likely memory-bandwidth bottleneck
- `Low MFU + Low HBM + Low NCCL + GPU idle gaps` -> likely GPU underfeeding
- `High NCCL wait + near-saturated network` -> likely communication bottleneck
- `High step-time variance across ranks` -> likely load imbalance/straggler issue

## Repository Layout

```text
gpu-profiler-project/
  README.md
  docs/
    project_scope.md
    roadmap.md
  src/gpu_profiler/
    main.py
    config.py
    models.py
    pipeline.py
    telemetry/
      collector.py
    profiling/
      analyzer.py
    diagnosis/
      classifier.py
    recommendations/
      engine.py
```

## MVP Milestones

1. **M1 Telemetry ingestion**: parse logs/exports (Nsight/NVML/DCGM/NCCL traces, workload stats).
2. **M2 Profile builder**: create per-step/per-rank aligned timeline and aggregate features.
3. **M3 Bottleneck diagnosis**: rule-based baseline classifier with confidence scores.
4. **M4 Insight generation**: explain bottleneck in human-readable terms.
5. **M5 Recommendation engine**: map bottleneck -> ranked optimization actions.
6. **M6 Optimization loop**: compare config A vs B and quantify gains.

## Quick Start (Scaffold)

```bash
python -m gpu_profiler.main --input ./sample_data --mode train
```

## Next Step

Implement the first vertical slice:
`telemetry collection -> feature extraction -> bottleneck diagnosis -> explanation`.
