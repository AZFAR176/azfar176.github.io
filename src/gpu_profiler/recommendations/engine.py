from __future__ import annotations

from gpu_profiler.models import Diagnosis, Recommendation


class RecommendationEngine:
    def recommend(self, diagnosis: Diagnosis) -> list[Recommendation]:
        label = diagnosis.labels[0] if diagnosis.labels else "mixed_or_unknown"

        if label == "communication_bound":
            return [
                Recommendation(
                    title="Improve communication overlap",
                    why="Collectives consume a high fraction of step time.",
                    expected_impact="Higher scaling efficiency and lower step latency.",
                ),
                Recommendation(
                    title="Revisit TP/FSDP sharding configuration",
                    why="Communication volume may be too high for current parallelism plan.",
                    expected_impact="Reduced NCCL pressure.",
                ),
            ]
        if label == "gpu_underfeeding":
            return [
                Recommendation(
                    title="Increase effective batching and prefetch",
                    why="GPU idle ratio indicates insufficient work supply.",
                    expected_impact="Higher utilization and tokens/sec.",
                ),
                Recommendation(
                    title="Profile host data pipeline",
                    why="CPU/input stalls may be throttling device work.",
                    expected_impact="Fewer execution gaps on GPU timeline.",
                ),
            ]
        if label == "memory_bandwidth_bound":
            return [
                Recommendation(
                    title="Use fused kernels / FlashAttention",
                    why="Memory traffic appears to dominate over compute.",
                    expected_impact="Lower memory pressure and better MFU.",
                ),
                Recommendation(
                    title="Reduce redundant memory movement",
                    why="Bandwidth saturation limits arithmetic throughput.",
                    expected_impact="Lower step time at same model quality.",
                ),
            ]

        return [
            Recommendation(
                title="Collect deeper trace and segment by phase",
                why="No dominant single bottleneck was identified.",
                expected_impact="Higher diagnosis confidence on next run.",
            )
        ]
