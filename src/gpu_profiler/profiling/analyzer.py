from __future__ import annotations

from gpu_profiler.models import TelemetryBundle, WorkloadProfile


class WorkloadAnalyzer:
    """Builds a time-aggregated behavior profile from telemetry."""

    def analyze(self, bundle: TelemetryBundle) -> WorkloadProfile:
        # Placeholder features for MVP wiring.
        feature_values = {
            "mfu": 0.0,
            "hbm_util": 0.0,
            "nccl_wait_ratio": 0.0,
            "gpu_idle_ratio": 0.0,
        }
        notes = [f"Samples loaded: gpu={len(bundle.gpu_metrics)}, workload={len(bundle.workload_metrics)}"]
        return WorkloadProfile(feature_values=feature_values, notes=notes)
