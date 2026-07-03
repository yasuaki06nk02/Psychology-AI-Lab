# Benchmark Result JSON Guide

This document explains how to interpret benchmark result files such as:

- backend/reports/gemini_trial.json
- backend/reports/gemini_trial_insight.md

## Purpose

Benchmark result JSON is for model quality comparison and tracking.

- It is not a legal qualification certificate.
- It does not grant professional licenses.

Model insight markdown is generated from the same result to summarize strengths, weaknesses, and risk points.

## Top-Level Fields

- generated_at:
  - UTC timestamp when this report was generated.
- exam_name:
  - Human-readable exam title used in this run.
- benchmark_origin:
  - Origin of the benchmark definition.
  - Example: custom_internal_benchmark.
- alignment_status:
  - How closely the benchmark is aligned to publicly available domain standards.
  - Example: partial_alignment_with_publicly_available_exam_domains.
- qualification_equivalence:
  - Whether this benchmark is qualification-equivalent.
  - Expected to be false for internal research benchmarks.
- qualification_disclaimer:
  - Plain-language warning that this result is not equivalent to national qualification.
- source_references:
  - List of source references used when designing benchmark domains.
- provider_name:
  - Provider adapter used for generation (mock, openai, gemini).
- model_name:
  - Model ID used in this run.
- benchmark_id:
  - Internal benchmark identifier.
- benchmark_version:
  - Version of benchmark definition.
- dataset_name:
  - Dataset identifier used in this run.
- dataset_version:
  - Dataset version string.
- prompt_version:
  - Prompt template version.
- overall_score:
  - Final mean score across all questions after scoring rules are applied.
  - Typical range: 0.0 to 1.0.
- category_scores:
  - Per-category mean scores.
  - Each key is a category label, each value is 0.0 to 1.0.
- duration_seconds:
  - End-to-end runtime in seconds.
- pass_threshold:
  - Required minimum overall_score for pass=true.
- passed:
  - True when overall_score >= pass_threshold.

## How To Read Scores

1. Check passed first.
2. Check overall_score against pass_threshold.
3. Inspect category_scores to find weak areas.

Example interpretation:

- overall_score = 0.6667, pass_threshold = 0.8, passed = false
- Means the model passed many items but does not meet required quality gate.
- Use low categories (for example act, boundary_awareness) to guide prompt/model improvements.

## Category Score Notes

- category_scores are means over only questions tagged with that category.
- Different categories can have different question counts.
- A low category can occur even when foundation categories are high.

## Fairness and Limits

Current text scoring:

- Uses keyword-based partial credit with conservative synonym handling.
- Includes negation guard (for example, keyword appears in a negated context).
- Still rule-based, not full semantic understanding.

Therefore:

- High score means strong alignment with current rubric.
- Low score does not always mean clinically wrong; it can reflect rubric mismatch.

## Operational Recommendation

For production gating, combine:

- overall_score threshold
- critical category thresholds (for example safety, ethics)
- manual review for borderline cases

This yields better fairness than a single pass/fail value alone.
