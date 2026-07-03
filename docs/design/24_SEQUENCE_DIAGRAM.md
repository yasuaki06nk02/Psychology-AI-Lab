# 24_SEQUENCE_DIAGRAM.md

# Sequence Diagrams

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the major runtime sequences of Psychology AI Lab.

The purpose of these sequence diagrams is to describe how the system components collaborate during benchmarking, experimentation, RAG evaluation, scoring, and package generation.

These diagrams represent the logical flow of the system and are implementation-independent.

---

# Sequence 1 — Benchmark Execution

## Overview

A researcher executes a benchmark against one or more AI models.

```text
Researcher

    │
    ▼

Frontend

    │
    ▼

REST API

    │
    ▼

Benchmark Engine

    │
    ▼

Model Manager

    │
    ▼

Provider Manager

    │
    ▼

AI Provider

    │
    ▼

Response

    │
    ▼

Scoring Engine

    │
    ▼

Result Engine

    │
    ▼

Database

    │
    ▼

Frontend
```

### Flow

1. User selects Benchmark.
2. User selects AI Model.
3. Benchmark Engine loads benchmark configuration.
4. Model Manager resolves the target model.
5. Provider Manager invokes the provider API.
6. AI generates responses.
7. Responses are scored.
8. Results are stored.
9. Dashboard updates.

---

# Sequence 2 — Experiment Execution

## Overview

An experiment executes multiple benchmark runs under controlled conditions.

```text
Researcher

    │
    ▼

Experiment Engine

    │

    ├──────────────┐
    ▼              ▼

Benchmark A   Benchmark B

    │              │

    ▼              ▼

Scoring Engine

    │

    ▼

Result Engine

    │

    ▼

Statistics

    │

    ▼

Experiment Summary
```

### Flow

1. Researcher creates experiment.
2. Variables are configured.
3. Benchmark runs are generated.
4. Each benchmark executes independently.
5. Scores are calculated.
6. Statistics are aggregated.
7. Experiment report is produced.

---

# Sequence 3 — RAG Benchmark

## Overview

A benchmark is executed using Retrieval-Augmented Generation.

```text
Question

    │
    ▼

RAG Engine

    │
    ▼

Embedding Model

    │
    ▼

Vector Database

    │
    ▼

Retrieved Documents

    │
    ▼

Prompt Augmentation

    │
    ▼

Benchmark Engine

    │
    ▼

AI Provider

    │
    ▼

Scoring Engine

    │
    ▼

Result Engine
```

### Flow

1. Benchmark begins.
2. Question is embedded.
3. Relevant knowledge is retrieved.
4. Prompt is augmented.
5. AI generates response.
6. Benchmark proceeds normally.
7. Scores are recorded.

---

# Sequence 4 — Model Comparison

## Overview

Multiple AI models are benchmarked using the same dataset.

```text
Dataset

     │

     ▼

Benchmark Engine

     │

 ┌───┼───────────────┐

 ▼   ▼               ▼

GPT Claude Gemini

 │    │       │

 ▼    ▼       ▼

Responses

 │

 ▼

Scoring Engine

 │

 ▼

Comparison

 │

 ▼

Leaderboard
```

### Flow

1. Dataset is fixed.
2. Benchmark runs for each model.
3. Responses are evaluated.
4. Scores are normalized.
5. Comparison report is generated.

---

# Sequence 5 — Package Generation

## Overview

Validated benchmark results are converted into production packages.

```text
Experiment

    │
    ▼

Validation

    │
    ▼

Package Builder

    │
    ▼

Manifest Builder

    │
    ▼

Package Archive

    │
    ▼

Package Repository

    │
    ▼

AIMindary
```

### Flow

1. Experiment completes.
2. Validation succeeds.
3. Package Builder creates package.
4. Manifest is generated.
5. Package is verified.
6. Package is published.
7. AIMindary imports package.

---

# Sequence 6 — Dataset Import

## Overview

Researchers import a new benchmark dataset.

```text
Researcher

    │
    ▼

Frontend

    │
    ▼

Dataset Manager

    │
    ▼

Validator

    │
    ▼

Database

    │
    ▼

Dataset Published
```

### Flow

1. Dataset selected.
2. Validation begins.
3. Metadata generated.
4. Dataset stored.
5. Version assigned.
6. Dataset published.

---

# Sequence 7 — Scoring Pipeline

## Overview

AI responses are transformed into benchmark scores.

```text
AI Response

      │
      ▼

Scoring Engine

      │

 ┌────┼──────────┐

 ▼    ▼          ▼

Rules Rubric LLM Judge

      │

      ▼

Category Scores

      │

      ▼

Overall Score

      │

      ▼

Result Engine
```

### Flow

1. Response received.
2. Evaluation method selected.
3. Category scores calculated.
4. Overall score computed.
5. Results stored.

---

# Sequence 8 — Research Workflow

## Overview

Overall research lifecycle.

```text
Research Question

        │

        ▼

Dataset

        │

        ▼

Experiment

        │

        ▼

Benchmark

        │

        ▼

Scoring

        │

        ▼

Results

        │

        ▼

Analysis

        │

        ▼

Validated Package

        │

        ▼

AIMindary
```

This sequence represents the complete evidence-based research pipeline.

---

# Sequence 9 — Psychology AI Lab → AIMindary

## Overview

Knowledge flows from the research platform into the production counseling system.

```text
Psychology AI Lab

       │

Validated Packages

       │

       ▼

Knowledge Package

Persona Package

Prompt Package

Evaluation Package

       │

       ▼

Package Builder

       │

       ▼

AIMindary Import

       │

       ▼

Counseling Engine

       │

       ▼

End User
```

Only validated assets are deployed into production.

---

# Future Sequence

Future versions may include

 Human Evaluation
 Multi-Agent Benchmarking
 Continuous Benchmark Runner
 Automatic Regression Detection
 Package Marketplace
 Collaborative Research
 AI-generated Experiment Planning
 Continuous Knowledge Learning
 Memory Evaluation Workflow
 Counseling Session Evaluation

---

# Summary

These sequence diagrams define the primary interactions between the major components of Psychology AI Lab.

They illustrate how benchmarking, experimentation, RAG evaluation, scoring, result management, and package deployment collaborate to create a reproducible, evidence-based research platform. By clearly separating research workflows from production deployment, the architecture ensures that only scientifically validated improvements are transferred into AIMindary.
