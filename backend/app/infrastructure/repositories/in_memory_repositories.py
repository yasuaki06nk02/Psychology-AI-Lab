from app.domain.entities.benchmark import Benchmark
from app.domain.entities.dataset import Dataset
from app.domain.entities.experiment import Experiment
from app.domain.entities.model import AIModel
from app.domain.entities.provider import Provider
from app.domain.entities.result import BenchmarkResult


class InMemoryProviderRepository:
    def __init__(self) -> None:
        self._items: dict[str, Provider] = {}

    def save(self, provider: Provider) -> Provider:
        self._items[provider.id] = provider
        return provider

    def get_by_id(self, provider_id: str) -> Provider | None:
        return self._items.get(provider_id)

    def list_all(self) -> list[Provider]:
        return list(self._items.values())


class InMemoryModelRepository:
    def __init__(self) -> None:
        self._items: dict[str, AIModel] = {}

    def save(self, model: AIModel) -> AIModel:
        self._items[model.id] = model
        return model

    def get_by_id(self, model_id: str) -> AIModel | None:
        return self._items.get(model_id)

    def list_all(self) -> list[AIModel]:
        return list(self._items.values())


class InMemoryDatasetRepository:
    def __init__(self) -> None:
        self._items: dict[str, Dataset] = {}

    def save(self, dataset: Dataset) -> Dataset:
        self._items[dataset.id] = dataset
        return dataset

    def get_by_id(self, dataset_id: str) -> Dataset | None:
        return self._items.get(dataset_id)

    def list_all(self) -> list[Dataset]:
        return list(self._items.values())


class InMemoryBenchmarkRepository:
    def __init__(self) -> None:
        self._items: dict[str, Benchmark] = {}

    def save(self, benchmark: Benchmark) -> Benchmark:
        self._items[benchmark.id] = benchmark
        return benchmark

    def get_by_id(self, benchmark_id: str) -> Benchmark | None:
        return self._items.get(benchmark_id)

    def list_all(self) -> list[Benchmark]:
        return list(self._items.values())


class InMemoryResultRepository:
    def __init__(self) -> None:
        self._items: dict[str, BenchmarkResult] = {}

    def save(self, result: BenchmarkResult) -> BenchmarkResult:
        self._items[result.id] = result
        return result

    def get_by_id(self, result_id: str) -> BenchmarkResult | None:
        return self._items.get(result_id)

    def list_all(self) -> list[BenchmarkResult]:
        return list(self._items.values())


class InMemoryExperimentRepository:
    def __init__(self) -> None:
        self._items: dict[str, Experiment] = {}

    def save(self, experiment: Experiment) -> Experiment:
        self._items[experiment.id] = experiment
        return experiment

    def get_by_id(self, experiment_id: str) -> Experiment | None:
        return self._items.get(experiment_id)

    def list_all(self) -> list[Experiment]:
        return list(self._items.values())
