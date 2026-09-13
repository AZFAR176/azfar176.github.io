from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field


class RunConfig(BaseModel):
    input_path: Path = Field(description="Path to telemetry/workload input directory")
    mode: str = Field(default="train", description="train or infer")
