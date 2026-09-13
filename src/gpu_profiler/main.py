from __future__ import annotations

import argparse
import json
from pathlib import Path

from gpu_profiler.config import RunConfig
from gpu_profiler.pipeline import ProfilerPipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GPU profiler project scaffold CLI")
    parser.add_argument("--input", type=Path, required=True, help="Telemetry input directory")
    parser.add_argument("--mode", type=str, default="train", choices=["train", "infer"])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RunConfig(input_path=args.input, mode=args.mode)
    output = ProfilerPipeline().run(cfg)
    print(json.dumps(output.model_dump(), indent=2))


if __name__ == "__main__":
    main()
