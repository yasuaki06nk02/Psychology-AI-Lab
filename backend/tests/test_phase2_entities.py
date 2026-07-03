from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

import pytest

from app.domain.entities.benchmark import Benchmark
from app.domain.entities.dataset import Dataset
from app.domain.entities.experiment import Experiment
from app.domain.entities.model import AIModel
from app.domain.entities.provider import Provider
from app.domain.entities.result import BenchmarkResult


def test_phase2_entities_are_immutable() -> None:
    now = datetime.now(UTC)

    provider = Provider(id="p1", name="openai", display_name="OpenAI", created_at=now)
    model = AIModel(
        id="m1",
        provider_id="p1",
        model_name="gpt-5",
        version="2026-07",
        created_at=now,
    )
    dataset = Dataset(
        id="d1",
        dataset_name="cbt-benchmark",
        version="v1",
        question_count=10,
        created_at=now,
    )
    benchmark = Benchmark(
        id="b1",
        name="baseline",
        dataset_id="d1",
        benchmark_version="v1",
        created_at=now,
    )
    result = BenchmarkResult(
        id="r1",
        benchmark_id="b1",
        model_id="m1",
        score=0.85,
        created_at=now,
    )
    experiment = Experiment(
        id="e1",
        name="experiment-1",
        description="baseline comparison",
        created_at=now,
    )

    assert provider.name == "openai"
    assert model.model_name == "gpt-5"
    assert dataset.question_count == 10
    assert benchmark.dataset_id == "d1"
    assert result.score == 0.85
    assert experiment.name == "experiment-1"

    with pytest.raises(FrozenInstanceError):
        provider.name = "changed"
