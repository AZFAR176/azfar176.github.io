from __future__ import annotations

from gpu_profiler.config import RunConfig
from gpu_profiler.diagnosis.classifier import BottleneckClassifier
from gpu_profiler.models import ProfilerOutput
from gpu_profiler.profiling.analyzer import WorkloadAnalyzer
from gpu_profiler.recommendations.engine import RecommendationEngine
from gpu_profiler.telemetry.collector import TelemetryCollector


def build_explanation(labels: list[str], evidence: list[str]) -> str:
    if not labels:
        return "No confident bottleneck detected."
    primary = labels[0].replace("_", " ")
    evidence_txt = "; ".join(evidence) if evidence else "limited evidence"
    return f"Primary bottleneck appears to be {primary}. Evidence: {evidence_txt}."


class ProfilerPipeline:
    def __init__(self) -> None:
        self.collector = TelemetryCollector()
        self.analyzer = WorkloadAnalyzer()
        self.classifier = BottleneckClassifier()
        self.recommender = RecommendationEngine()

    def run(self, cfg: RunConfig) -> ProfilerOutput:
        bundle = self.collector.collect(cfg.input_path)
        profile = self.analyzer.analyze(bundle)
        diagnosis = self.classifier.classify(profile)
        explanation = build_explanation(diagnosis.labels, diagnosis.evidence)
        recommendations = self.recommender.recommend(diagnosis)
        return ProfilerOutput(
            diagnosis=diagnosis,
            explanation=explanation,
            recommendations=recommendations,
        )
