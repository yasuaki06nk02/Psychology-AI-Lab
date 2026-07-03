from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BenchmarkQuestion:
    id: str
    prompt: str
    expected_answer: str


@dataclass(frozen=True, slots=True)
class PromptTemplate:
    version: str
    system_prompt: str
    developer_prompt: str
    user_template: str


@dataclass(frozen=True, slots=True)
class BenchmarkDefinition:
    benchmark_id: str
    benchmark_version: str
    provider_name: str
    model_name: str
    model_version: str
    dataset_name: str
    dataset_version: str
    questions: list[BenchmarkQuestion]
    prompt_template: PromptTemplate


@dataclass(frozen=True, slots=True)
class BenchmarkResponse:
    question_id: str
    prompt: str
    answer: str
    expected_answer: str
    latency_ms: int
    input_tokens: int
    output_tokens: int


@dataclass(frozen=True, slots=True)
class ScoreResult:
    category_scores: dict[str, float]
    overall_score: float


@dataclass(frozen=True, slots=True)
class BenchmarkRunResult:
    benchmark_id: str
    benchmark_version: str
    dataset_name: str
    dataset_version: str
    provider_name: str
    model_name: str
    model_version: str
    prompt_version: str
    responses: list[BenchmarkResponse]
    score: ScoreResult
