from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class BenchmarkQuestion:
    id: str
    prompt: str
    expected_answer: str
    evaluation_type: str = "exact_match"
    categories: list[str] = field(default_factory=lambda: ["accuracy"])
    accepted_answers: list[str] = field(default_factory=list)
    expected_keywords: list[str] = field(default_factory=list)


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
    evaluation_type: str
    categories: list[str]
    accepted_answers: list[str]
    expected_keywords: list[str]
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
