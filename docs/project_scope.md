# Project Scope

## Objective

Build an automated profiler that converts low-level hardware/runtime telemetry into:
- bottleneck diagnosis,
- plain-language root-cause explanation,
- and prioritized optimization recommendations.

This system targets both **training** and **inference** workloads.

## Inputs

### Hardware/runtime telemetry
- GPU utilization
- SM/Tensor Core utilization
- achieved FLOPs / MFU
- HBM bandwidth + memory usage
- kernel launch timings
- NCCL communication timing and volume
- GPU idle gaps
- CPU utilization and host-side stalls
- power and thermals (optional early)

### Workload telemetry
- batch size / microbatch size
- sequence length distribution
- tokens/sec
- step latency and variance
- per-rank throughput and wait time

## Outputs

1. **Bottleneck label(s)**:
   - compute bound
   - memory bandwidth bound
   - communication bound
   - CPU/data pipeline bound
   - synchronization bound
   - underfeeding/poor batching
   - load imbalance / straggler

2. **Evidence bundle**:
   - top supporting metrics
   - confidence score
   - timeline snippets where issue appears

3. **Action plan**:
   - 3 to 5 ranked recommendations
   - expected impact (throughput/latency/MFU)
   - risk or trade-off notes

## Non-goals for MVP

- Full root-cause certainty in all cases
- Auto-tuning across every framework out of the box
- Perfect support for all vendor-specific telemetry formats

## Success Criteria

- Diagnose at least one dominant bottleneck for most runs.
- Explanations are understandable by engineers without profiling specialization.
- Recommendations are testable and lead to measurable improvement in a subset of cases.

## Evaluation

- **Diagnosis quality**: agreement with expert diagnosis on curated traces.
- **Practical utility**: fraction of recommendations that improve target metric.
- **Speed**: analysis latency after run completion.
- **Coverage**: percentage of runs producing actionable output.
