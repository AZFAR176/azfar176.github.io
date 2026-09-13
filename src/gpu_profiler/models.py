from __future__ import annotations

from typing import Dict, List

from pydantic import BaseModel, Field


class MetricSample(BaseModel):
    ts_ms: int
    name: str
    value: float
    rank: int = 0


class WorkloadSample(BaseModel):
    ts_ms: int
    step_id: int
    tokens_per_sec: float | None = None
    step_latency_ms: float | None = None
    batch_size: int | None = None
    seq_len: int | None = None


class TelemetryBundle(BaseModel):
    gpu_metrics: List[MetricSample] = Field(default_factory=list)
    workload_metrics: List[WorkloadSample] = Field(default_factory=list)


class WorkloadProfile(BaseModel):
    feature_values: Dict[str, float] = Field(default_factory=dict)
    notes: List[str] = Field(default_factory=list)


class Diagnosis(BaseModel):
    labels: List[str] = Field(default_factory=list)
    confidence: float = 0.0
    evidence: List[str] = Field(default_factory=list)


class Recommendation(BaseModel):
    title: str
    why: str
    expected_impact: str


class ProfilerOutput(BaseModel):
    diagnosis: Diagnosis
    explanation: str
    recommendations: List[Recommendation] = Field(default_factory=list)
