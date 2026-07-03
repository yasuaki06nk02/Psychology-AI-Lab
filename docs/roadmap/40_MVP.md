# 40_MVP.md

# Minimum Viable Product (MVP)

Project Psychology AI Lab

Version 1.0.0

Status Design

---

# Purpose

This document defines the Minimum Viable Product (MVP) for Psychology AI Lab.

The MVP focuses on one objective

 Objectively evaluate how capable current AI models are at psychological counseling before introducing any custom RAG, memory, or fine-tuning.

This establishes a scientific baseline that all future improvements can be compared against.

---

# MVP Goals

The MVP must answer the following questions

 Which AI model performs best for counseling
 Which provider performs best
 What are each model's strengths and weaknesses
 How reproducible are benchmark results
 How much improvement does RAG provide
 Which packages should eventually be deployed into AIMindary

---

# Scope

The MVP includes only the minimum components required to benchmark AI models.

Included

 AI Provider Management
 Model Management
 Benchmark Execution
 Dataset Management
 Prompt Management
 Scoring
 Result Comparison
 Dashboard

Excluded

 User Authentication
 Multi-user Support
 Session Memory
 Long-term Memory
 Knowledge Learning
 Production Counseling
 AIMindary Integration
 Automatic Package Publishing

---

# MVP Architecture

```text
Flutter Web

↓

FastAPI

↓

Benchmark Engine

↓

Provider Manager

↓

AI Providers

↓

Scoring Engine

↓

Result Engine

↓

PostgreSQL
```

No RAG is required for the first benchmark baseline.

---

# Supported Providers

Version 1

 OpenAI
 Gemini
 Claude
 OpenRouter

Future

 Ollama
 Bedrock
 Azure OpenAI
 NVIDIA NIM
 Groq

---

# Supported Models

The MVP should benchmark as many available models as practical.

Examples

OpenAI

 GPT-5
 GPT-5 Mini

Google

 Gemini 2.5 Pro
 Gemini 2.5 Flash

Anthropic

 Claude Opus
 Claude Sonnet

OpenRouter

 Configurable Models

The model list shall remain dynamic.

---

# MVP Modules

The MVP consists of

```text
Provider Manager

↓

Model Manager

↓

Dataset Manager

↓

Benchmark Engine

↓

Scoring Engine

↓

Result Engine

↓

Dashboard
```

---

# Dataset Requirements

Initial benchmark datasets should include

 CBT
 Cognitive Distortions
 Active Listening
 Empathy
 Reflection
 Psychoeducation

Recommended size

 100–300 benchmark questions

Datasets shall be version-controlled.

---

# Prompt Strategy

Prompt structure

```text
System Prompt

↓

Developer Prompt

↓

User Prompt
```

Context and RAG are intentionally excluded from the baseline.

---

# Benchmark Workflow

```text
Select Dataset

↓

Select Models

↓

Run Benchmark

↓

Collect Responses

↓

Score Responses

↓

Store Results

↓

Compare Models
```

---

# Scoring

The MVP supports

Objective Scores

 Accuracy
 Completeness
 Consistency

Counseling Scores

 Empathy
 Reflection
 CBT Adherence
 Psychological Safety

Overall Score

Weighted total across all categories.

---

# Dashboard

The dashboard shall display

 Models
 Providers
 Benchmark Runs
 Leaderboard
 Average Scores
 Response Time
 Token Usage

---

# Result Comparison

Users should be able to compare

 Model A vs Model B
 Provider A vs Provider B
 Prompt Version A vs B

Side-by-side comparison is required.

---

# Database

The MVP requires

 PostgreSQL

Development

 SQLite

No vector database is required.

---

# API

Required endpoints

 Providers
 Models
 Datasets
 Benchmarks
 Scores
 Results

Package APIs are optional.

---

# Testing

The MVP shall include

 Unit Tests
 API Tests
 Integration Tests

Benchmark reproducibility shall be verified.

---

# Success Criteria

The MVP is considered complete when it can

✓ Register providers

✓ Discover available models

✓ Load benchmark datasets

✓ Execute benchmarks

✓ Evaluate responses

✓ Rank AI models

✓ Compare benchmark results

✓ Export benchmark reports

---

# Deliverables

Version 1 produces

 Benchmark Database
 Benchmark Reports
 Leaderboards
 Score History
 Experiment Logs

No production counseling packages are generated.

---

# Out of Scope

The following are intentionally postponed

 RAG
 Knowledge Packages
 Persona Packages
 Memory Engine
 Continuous Learning
 AI Self-Improvement
 Human Reviewer Workflow
 AIMindary Deployment

These features belong to later milestones.

---

# Roadmap

## Phase 1 — Baseline Benchmark (MVP)

 Provider integration
 Model comparison
 Dataset evaluation
 Scoring
 Dashboard

Deliverable

Baseline benchmark of standard AI models

---

## Phase 2 — RAG Evaluation

Add

 Knowledge Packages
 Embedding Models
 Qdrant
 Retrieval Evaluation

Deliverable

Measure performance gains from RAG

---

## Phase 3 — Persona Evaluation

Add

 Persona Packages
 Therapist Styles
 Communication Strategies

Deliverable

Identify optimal counseling personas

---

## Phase 4 — Production Packages

Add

 Package Builder
 Validation
 Package Export

Deliverable

Deploy validated packages into AIMindary

---

# Relationship with AIMindary

The MVP is completely independent of AIMindary.

Its sole purpose is to establish a reliable benchmark for AI counseling performance. Only after standard models, RAG configurations, personas, and prompts have been scientifically evaluated should validated packages be transferred into AIMindary for production use.

---

# Summary

The MVP of Psychology AI Lab establishes the research foundation for the entire project.

By benchmarking standard AI models under controlled and reproducible conditions, it creates an objective baseline against which all future enhancements—such as RAG, personas, memory systems, and package generation—can be measured. This evidence-first approach ensures that every improvement introduced into AIMindary is supported by measurable gains in counseling quality rather than subjective impressions.
