from app.application.benchmarking.models import BenchmarkResponse, ScoreResult


class ScoringEngine:
    def score(self, responses: list[BenchmarkResponse]) -> ScoreResult:
        total = len(responses)
        if total == 0:
            return ScoreResult(category_scores={"accuracy": 0.0}, overall_score=0.0)

        correct = 0
        for item in responses:
            if item.answer.strip().lower() == item.expected_answer.strip().lower():
                correct += 1

        accuracy = correct / total
        return ScoreResult(category_scores={"accuracy": accuracy}, overall_score=accuracy)
