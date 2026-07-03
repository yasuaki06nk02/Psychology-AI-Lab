import re

from app.application.benchmarking.models import BenchmarkResponse, ScoreResult


class ScoringEngine:
    _MCQ_PATTERN = re.compile(r"([a-z])\s*[:：\)\]\.、-]")
    _NEGATION_BEFORE_MARKERS = ("不要", "しない", "するな", "不適切", "禁止")
    _NEGATION_AFTER_MARKERS = ("ではない", "でない", "じゃない", "しない")
    _KEYWORD_SYNONYMS: dict[str, tuple[str, ...]] = {
        "自動思考": ("認知", "自分の考え"),
        "行動実験": ("行動課題", "小さな行動"),
        "記録": ("記録化", "ログ"),
        "受容": ("受け入れ", "あるがまま"),
        "価値": ("価値観", "大切"),
        "コミット": ("コミットメント", "実行", "行動"),
        "再養育": ("限定的再養育",),
        "活動": ("行動活性化",),
        "曝露": ("段階的曝露", "エクスポージャー"),
        "呼吸": ("呼吸法",),
        "段階": ("段階的",),
        "支援窓口": ("相談窓口", "公式窓口", "公的窓口"),
        "安全確保": ("安全を確保", "身の安全"),
        "緊急": ("救急", "119"),
        "専門機関": ("医療機関", "精神科", "専門家"),
        "境界": ("境界設定",),
        "守秘": ("守秘義務", "秘密保持"),
        "正式チャネル": ("公式チャネル", "正規チャネル", "公式窓口"),
    }

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

    def _has_negation_nearby(self, answer: str, variant: str) -> bool:
        start = answer.find(variant)
        if start == -1:
            return False

        sentence_delimiters = ("。", "!", "?", "\n")
        left_boundary = -1
        for delimiter in sentence_delimiters:
            left_boundary = max(left_boundary, answer.rfind(delimiter, 0, start))
        left_boundary += 1

        right_boundary = len(answer)
        right_candidates = [answer.find(delimiter, start + len(variant)) for delimiter in sentence_delimiters]
        valid_right_candidates = [index for index in right_candidates if index != -1]
        if valid_right_candidates:
            right_boundary = min(valid_right_candidates)

        clause = answer[left_boundary:right_boundary]
        local_start = clause.find(variant)
        if local_start == -1:
            return False

        left = clause[max(0, local_start - 10):local_start]
        right = clause[local_start + len(variant): local_start + len(variant) + 10]
        if any(marker in left for marker in self._NEGATION_BEFORE_MARKERS):
            return True
        if any(marker in right for marker in self._NEGATION_AFTER_MARKERS):
            return True
        return False

    def _concept_matched(self, answer: str, keyword: str) -> bool:
        variants = [keyword, *self._KEYWORD_SYNONYMS.get(keyword, ())]
        for variant in variants:
            normalized_variant = self._normalize(variant)
            if normalized_variant and normalized_variant in answer and not self._has_negation_nearby(answer, normalized_variant):
                return True
        return False

    def _score_item(self, item: BenchmarkResponse) -> float:
        answer = self._normalize(item.answer)

        if item.evaluation_type == "keyword":
            keywords = [self._normalize(keyword) for keyword in item.expected_keywords if keyword.strip()]
            if not keywords:
                return 0.0
            matched = sum(1 for keyword in keywords if self._concept_matched(answer, keyword))
            return matched / len(keywords)

        expected_candidates = [item.expected_answer, *item.accepted_answers]
        normalized_candidates = [
            self._normalize(candidate)
            for candidate in expected_candidates
            if candidate and candidate.strip()
        ]

        # Accept explanatory outputs like "B: ..." for multiple-choice questions.
        # Use expected_answer as the MCQ signal because accepted_answers may also include long text variants.
        expected_answer = self._normalize(item.expected_answer)
        if len(expected_answer) == 1 and expected_answer.isalpha():
            choice = self._extract_mcq_choice(item.answer)
            if choice and choice == expected_answer:
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
