# Counselor Skill Assessment v2

## Qualification Notice

- This benchmark is a custom internal research benchmark.
- Passing this benchmark does not grant, replace, or imply eligibility for national qualifications such as Licensed/Public Psychologist credentials.
- The benchmark is intended for model comparison and quality improvement only.

## Alignment Policy

- When public exam blueprints and public guidance are available, question domains should be aligned to those published domains.
- Items must not claim to be official past questions unless their provenance is explicitly documented and legally reusable.
- Every dataset version should include metadata for origin, alignment status, and references.

## Purpose

This benchmark measures practical counselor skill across both:

- public psychologist style competency (ethics, safety, institutional response)
- clinical psychology style competency (case formulation, CBT, ACT, schema-oriented response)

It is designed to make level differences visible in benchmark output.

## Dataset File

- backend/datasets/counselor_skill_assessment_v2.json

## Result JSON Guide

- docs/benchmarks/BENCHMARK_RESULT_JSON_GUIDE.md

## Evaluation Axes

- Domain split:
  - domain_public_psychologist
  - domain_clinical_psychology
- Skill split:
  - cbt
  - act
  - schema_therapy
  - depression
  - anxiety
  - workplace_mental_health
  - risk_assessment
  - ethics
  - boundary_awareness
  - formulation
- Proficiency level split:
  - level_foundation
  - level_practitioner
  - level_advanced

## Question Design

- Foundation level uses exact_match questions for baseline professional knowledge.
- Practitioner and Advanced levels use keyword evaluation for structured clinical response quality.
- Safety and ethical boundary handling are included as mandatory capability checks.

## How to Run

```powershell
python scripts/run_benchmark.py --provider openai --model "<model>" --pass-threshold 0.8 --report-file .\reports\counselor_skill_v2.json
```

Use `--provider mock` for deterministic pipeline checks.

## Interpreting Scores

- Compare `domain_public_psychologist` vs `domain_clinical_psychology` to see orientation differences.
- Compare `level_foundation`, `level_practitioner`, `level_advanced` to estimate capability stage.
- Check `safety`, `risk_assessment`, and `ethics` as minimum deployment gates.

Recommended gate example:

- overall_score >= 0.75
- safety >= 0.80
- ethics >= 0.80
- level_advanced >= 0.65
