from app.application.benchmarking.models import BenchmarkResponse
from app.application.benchmarking.scoring_engine import ScoringEngine


def _response(answer: str, expected: str, categories: list[str] | None = None) -> BenchmarkResponse:
    return BenchmarkResponse(
        question_id="q1",
        prompt="question",
        answer=answer,
        expected_answer=expected,
        evaluation_type="exact_match",
        categories=categories or ["accuracy"],
        accepted_answers=[],
        expected_keywords=[],
        latency_ms=1,
        input_tokens=1,
        output_tokens=1,
    )


def test_exact_match_accepts_mcq_answer_with_explanation() -> None:
    engine = ScoringEngine()

    result = engine.score(
        [
            _response(
                answer="**B: 守秘義務の説明**\n\n理由: ...",
                expected="B",
                categories=["level_foundation"],
            )
        ]
    )

    assert result.overall_score == 1.0
    assert result.category_scores["level_foundation"] == 1.0


def test_exact_match_rejects_wrong_mcq_answer_with_explanation() -> None:
    engine = ScoringEngine()

    result = engine.score(
        [
            _response(
                answer="A: 情報収集",
                expected="B",
                categories=["level_foundation"],
            )
        ]
    )

    assert result.overall_score == 0.0
    assert result.category_scores["level_foundation"] == 0.0


def test_exact_match_accepts_mcq_with_explanation_and_textual_candidates() -> None:
    engine = ScoringEngine()

    response = BenchmarkResponse(
        question_id="q1",
        prompt="question",
        answer="B: 情報収集と主訴の整理",
        expected_answer="B",
        evaluation_type="exact_match",
        categories=["level_foundation"],
        accepted_answers=["b", "B", "情報収集と主訴の整理"],
        expected_keywords=[],
        latency_ms=1,
        input_tokens=1,
        output_tokens=1,
    )

    result = engine.score([response])

    assert result.overall_score == 1.0
    assert result.category_scores["level_foundation"] == 1.0
