# 14_SCORING_ENGINE.md

# Scoring Engine

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

The Scoring Engine is responsible for objectively evaluating AI responses generated during benchmark execution.

It converts raw AI responses into standardized, reproducible evaluation scores that can be compared across AI models, prompts, RAG configurations, and counseling strategies.

The Scoring Engine is designed to support both traditional knowledge-based evaluation (e.g., public psychologist examinations) and future counseling quality evaluation using multidimensional psychological metrics.

The Scoring Engine evaluates responses but never generates them.

---

# Responsibilities

The Scoring Engine is responsible for

 Evaluating benchmark responses
 Applying scoring rules
 Calculating category scores
 Calculating overall benchmark scores
 Recording detailed evaluation results
 Supporting multiple evaluation methods
 Producing reproducible scores
 Supporting future ACS evaluation

The Scoring Engine is not responsible for

 Benchmark execution
 AI communication
 Prompt generation
 Dataset authoring
 Experiment management
 Report visualization

---

# Functional Requirements

## FR-001 Response Evaluation

The engine shall evaluate every response produced by the Benchmark Engine.

Evaluation shall occur after benchmark execution has completed.

---

## FR-002 Multiple Evaluation Methods

The engine shall support multiple scoring strategies.

Examples include

 Exact Match
 Multiple Choice Accuracy
 Partial Credit
 Rule-Based Evaluation
 Rubric-Based Evaluation
 LLM-as-a-Judge
 Human Evaluation (Future)

Each benchmark specifies its evaluation strategy.

---

## FR-003 Category Scoring

The engine shall calculate scores for individual evaluation categories.

Examples

Knowledge

 Psychology Knowledge
 CBT Knowledge
 Clinical Knowledge

Communication

 Empathy
 Reflection
 Emotional Validation

Reasoning

 Case Formulation
 Clinical Reasoning
 Intervention Planning

Safety

 Risk Assessment
 Ethical Response
 Boundary Awareness

Each benchmark may define different categories.

---

## FR-004 Overall Score

The engine shall calculate an overall benchmark score.

The overall score shall be reproducible.

Weighting rules shall be configurable.

---

## FR-005 Explanation

Every evaluation shall include an explanation.

Examples

 Correct Answer
 Expected Reasoning
 Score Breakdown
 Evaluation Comments

Evaluation explanations support research and model improvement.

---

## FR-006 Evaluation Metadata

Every evaluation shall record

 Evaluation Method
 Evaluation Version
 Evaluator
 Timestamp
 Configuration

Metadata is required for reproducibility.

---

## FR-007 Batch Scoring

The engine shall support

 Single Response
 Batch Evaluation
 Parallel Evaluation

Batch scoring improves benchmark performance.

---

# Non-Functional Requirements

## Reproducibility

Identical benchmark inputs shall produce identical scores.

---

## Transparency

Every score shall be explainable.

No score shall be treated as a black box.

---

## Extensibility

New evaluation methods shall be added without modifying existing scoring logic.

---

## Reliability

Scoring failures shall never corrupt benchmark data.

Failed evaluations shall be logged separately.

---

# Architecture

```text
              Benchmark Engine
                     │
                     ▼
              Response Repository
                     │
                     ▼
               Scoring Engine
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Rule Engine   LLM Judge     Score Calculator
      │              │              │
      └──────────────┼──────────────┘
                     ▼
             Benchmark Result
```

The Scoring Engine receives completed benchmark responses and transforms them into standardized evaluation results.

---

# Internal Components

## Rule Engine

Responsible for deterministic scoring.

Examples

 Multiple Choice
 Exact Match
 Numerical Answer

---

## Rubric Engine

Evaluates responses using predefined rubrics.

Suitable for

 Essays
 Clinical Cases
 Reflection
 Counseling Dialogue

---

## LLM Judge

Future component.

Uses an independent AI model to evaluate benchmark responses.

Judge models shall be version controlled.

---

## Score Calculator

Calculates

 Category Scores
 Weighted Scores
 Overall Score

Supports configurable weighting.

---

## Evaluation Logger

Stores

 Evaluation Details
 Rule Versions
 Judge Version
 Execution Metadata

---

# Scoring Pipeline

```text
Response

↓

Evaluation Method

↓

Category Scores

↓

Weighting

↓

Overall Score

↓

Evaluation Report
```

---

# Score Categories

Version 1 primarily focuses on objective evaluation.

Examples

 Accuracy
 Correct Answer Rate
 Category Accuracy
 Completion Rate

Future versions expand evaluation.

---

# Future Counseling Categories

Future benchmark categories include

## Psychological Knowledge

Measures

 CBT
 ACT
 Schema Therapy
 Clinical Psychology
 Public Psychologist Examination

---

## Therapeutic Alliance

Measures

 Trust Building
 Collaboration
 Rapport
 User Engagement

---

## Empathy

Measures

 Emotional Validation
 Compassion
 Acceptance
 Warmth

---

## Reflection

Measures

 Active Listening
 Summarization
 Clarification
 Emotional Reflection

---

## Case Formulation

Measures

 Problem Identification
 Cognitive Patterns
 Behavioral Patterns
 Psychological Understanding

---

## Treatment Planning

Measures

 Goal Setting
 Intervention Selection
 Homework Suggestions
 Follow-up Planning

---

## Safety

Measures

 Crisis Detection
 Ethical Boundaries
 Risk Assessment
 Appropriate Referral

---

## Long-Term Consistency

Future versions evaluate

 Session Continuity
 Memory Usage
 Counseling Progress
 Longitudinal Quality

---

# ACS (AIMindary Counseling Score)

Future versions introduce ACS.

ACS integrates multiple dimensions into one composite score.

Example dimensions

 Knowledge
 Empathy
 Reflection
 Therapeutic Alliance
 Case Formulation
 Intervention
 Treatment Planning
 Safety
 Consistency

ACS is designed specifically for AI counseling evaluation.

---

# Error Handling

Possible scoring errors include

 Missing Response
 Invalid Evaluation Rule
 Judge Failure
 Weight Configuration Error
 Unsupported Question Type

Errors shall be recorded without affecting completed benchmark runs.

---

# Logging

The Scoring Engine shall log

 Evaluation Method
 Evaluation Duration
 Category Scores
 Overall Score
 Rule Version
 Judge Version
 Error Information

Logs shall be immutable.

---

# Versioning

Every evaluation shall record

 Scoring Version
 Evaluation Rule Version
 Rubric Version
 Judge Model Version
 ACS Version (Future)

Version history shall never be overwritten.

---

# Future Extension

Future versions may support

 Human Expert Review
 Multi-Judge Consensus
 Judge Calibration
 Confidence Scores
 Inter-Rater Reliability
 Benchmark Certification
 Psychological Safety Certification
 Continuous Regression Evaluation

These extensions shall integrate without changing the Scoring Engine's core responsibility.

---

# Dependencies

Depends on

 Benchmark Engine
 Dataset Manager

Provides data to

 Result Engine
 Experiment Engine
 Dashboard

---

# Summary

The Scoring Engine transforms benchmark responses into objective, reproducible evaluation results.

By separating response generation from response evaluation, the Scoring Engine enables fair comparison between AI models while supporting increasingly sophisticated assessment methods, from traditional examination scoring to multidimensional counseling evaluation through the future AIMindary Counseling Score (ACS).
