from __future__ import annotations

from pathlib import Path

from gpu_profiler.models import TelemetryBundle


class TelemetryCollector:
    """Loads telemetry/workload data into a unified in-memory bundle."""

    def collect(self, input_path: Path) -> TelemetryBundle:
        # TODO: Replace with real parsers for Nsight/NVML/DCGM/NCCL exports.
        if not input_path.exists():
            raise FileNotFoundError(f"Input path does not exist: {input_path}")
        return TelemetryBundle()
