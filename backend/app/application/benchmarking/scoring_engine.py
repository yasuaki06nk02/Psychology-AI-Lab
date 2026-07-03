import re

from app.application.benchmarking.models import BenchmarkResponse, ScoreResult


class ScoringEngine:
    _MCQ_PATTERN = re.compile(r"([a-z])\s*[:：\)\]\.、-]")

    @staticmethod
    def _normalize(text: str) -> str:
        return " ".join(text.strip().lower().split())

    def _extract_mcq_choice(self, text: str) -> str | None:
        head = text.strip().lower()[:120]
        match = self._MCQ_PATTERN.search(head)
        if match:
            return match.group(1)

        token_match = re.search(r"\b([a-d])\b", head)
        if token_match:
            return token_match.group(1)
        return None

    def _score_item(self, item: BenchmarkResponse) -> float:
        answer = self._normalize(item.answer)

        if item.evaluation_type == "keyword":
            keywords = [self._normalize(keyword) for keyword in item.expected_keywords if keyword.strip()]
            if not keywords:
                return 0.0
            matched = sum(1 for keyword in keywords if keyword in answer)
            return matched / len(keywords)

        expected_candidates = [item.expected_answer, *item.accepted_answers]
        normalized_candidates = [
            self._normalize(candidate)
            for candidate in expected_candidates
            if candidate and candidate.strip()
        ]

        # Accept explanatory outputs like "B: ..." for multiple-choice questions.
        if normalized_candidates and all(len(candidate) == 1 and candidate.isalpha() for candidate in normalized_candidates):
            choice = self._extract_mcq_choice(item.answer)
            if choice and choice in normalized_candidates:
                return 1.0

        return 1.0 if answer in normalized_candidates else 0.0

    def score(self, responses: list[BenchmarkResponse]) -> ScoreResult:
        total = len(responses)
        if total == 0:
            return ScoreResult(category_scores={"accuracy": 0.0}, overall_score=0.0)

        total_score = 0.0
        category_totals: dict[str, float] = {}
        category_counts: dict[str, int] = {}

        for item in responses:
            item_score = self._score_item(item)
            total_score += item_score

            categories = item.categories if item.categories else ["accuracy"]
            for category in categories:
                category_totals[category] = category_totals.get(category, 0.0) + item_score
                category_counts[category] = category_counts.get(category, 0) + 1

        category_scores = {
            category: (category_totals[category] / category_counts[category])
            for category in category_totals
        }

        # Keep a baseline accuracy metric for compatibility.
        if "accuracy" not in category_scores:
            category_scores["accuracy"] = total_score / total

        overall_score = total_score / total
        return ScoreResult(category_scores=category_scores, overall_score=overall_score)
