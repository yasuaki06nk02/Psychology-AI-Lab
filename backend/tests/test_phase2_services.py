from app.application.services.benchmark_service import BenchmarkService
from app.application.services.dataset_service import DatasetService
from app.application.services.experiment_service import ExperimentService
from app.application.services.model_service import ModelService
from app.application.services.provider_service import ProviderService
from app.application.services.result_service import ResultService
from app.infrastructure.repositories.in_memory_repositories import (
    InMemoryBenchmarkRepository,
    InMemoryDatasetRepository,
    InMemoryExperimentRepository,
    InMemoryModelRepository,
    InMemoryProviderRepository,
    InMemoryResultRepository,
)


def test_phase2_services_create_and_list_entities() -> None:
    provider_service = ProviderService(InMemoryProviderRepository())
    model_service = ModelService(InMemoryModelRepository())
    dataset_service = DatasetService(InMemoryDatasetRepository())
    benchmark_service = BenchmarkService(InMemoryBenchmarkRepository())
    result_service = ResultService(InMemoryResultRepository())
    experiment_service = ExperimentService(InMemoryExperimentRepository())

    provider = provider_service.create(name="openai", display_name="OpenAI")
    model = model_service.create(provider_id=provider.id, model_name="gpt-5", version="2026-07")
    dataset = dataset_service.create(dataset_name="cbt-benchmark", version="v1", question_count=10)
    benchmark = benchmark_service.create(name="baseline", dataset_id=dataset.id, benchmark_version="v1")
    result = result_service.create(benchmark_id=benchmark.id, model_id=model.id, score=0.91)
    experiment = experiment_service.create(name="exp-1", description="baseline run")

    assert provider_service.get(provider.id) == provider
    assert model_service.get(model.id) == model
    assert dataset_service.get(dataset.id) == dataset
    assert benchmark_service.get(benchmark.id) == benchmark
    assert result_service.get(result.id) == result
    assert experiment_service.get(experiment.id) == experiment

    assert len(provider_service.list()) == 1
    assert len(model_service.list()) == 1
    assert len(dataset_service.list()) == 1
    assert len(benchmark_service.list()) == 1
    assert len(result_service.list()) == 1
    assert len(experiment_service.list()) == 1
