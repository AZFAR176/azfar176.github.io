from __future__ import annotations

from gpu_profiler.models import Diagnosis, WorkloadProfile


class BottleneckClassifier:
    """Rule-based diagnosis baseline."""

    def classify(self, profile: WorkloadProfile) -> Diagnosis:
        mfu = profile.feature_values.get("mfu", 0.0)
        hbm = profile.feature_values.get("hbm_util", 0.0)
        nccl = profile.feature_values.get("nccl_wait_ratio", 0.0)
        idle = profile.feature_values.get("gpu_idle_ratio", 0.0)

        if mfu < 0.4 and hbm > 0.8:
            return Diagnosis(
                labels=["memory_bandwidth_bound"],
                confidence=0.75,
                evidence=["Low MFU with high HBM utilization"],
            )
        if mfu < 0.4 and hbm < 0.5 and nccl < 0.3 and idle > 0.1:
            return Diagnosis(
                labels=["gpu_underfeeding"],
                confidence=0.72,
                evidence=["Low MFU + low HBM/NCCL with measurable idle gaps"],
            )
        if nccl > 0.5:
            return Diagnosis(
                labels=["communication_bound"],
                confidence=0.8,
                evidence=["NCCL wait ratio dominates step time"],
            )

        return Diagnosis(
            labels=["mixed_or_unknown"],
            confidence=0.35,
            evidence=["No dominant rule strongly triggered"],
        )
