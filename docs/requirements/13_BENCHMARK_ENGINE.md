# 13_BENCHMARK_ENGINE.md

# Benchmark Engine

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

The Benchmark Engine is the core execution engine of Psychology AI Lab.

Its responsibility is to execute standardized psychological benchmarks against one or more AI models under controlled and reproducible conditions.

The Benchmark Engine coordinates the complete benchmark workflow, including question selection, prompt generation, AI execution, response collection, and execution logging. It does not evaluate responses or calculate scores.

---

# Responsibilities

The Benchmark Engine is responsible for

 Executing benchmark runs
 Coordinating benchmark workflows
 Loading benchmark datasets
 Generating prompts
 Invoking AI models
 Collecting responses
 Recording execution metadata
 Managing retries
 Managing execution order
 Supporting batch benchmarking

The Benchmark Engine is not responsible for

 Score calculation
 Result evaluation
 Dataset authoring
 AI provider management
 Report generation

---

# Functional Requirements

## FR-001 Benchmark Execution

The engine shall execute one benchmark using

 One Benchmark Definition
 One Dataset Version
 One Prompt Template Version
 One AI Model

Each execution produces one Benchmark Run.

---

## FR-002 Multi-Model Benchmark

The engine shall support executing the same benchmark against multiple AI models.

Example

```text
Dataset
      │
      ▼
Psychologist Exam

      │
 ┌────┼────┬────┐
 ▼    ▼    ▼    ▼
GPT Gemini Claude Qwen

      │
      ▼

Responses
```

All models shall receive identical benchmark conditions.

---

## FR-003 Prompt Generation

The engine shall generate prompts using the Prompt Template.

Prompt generation combines

 System Prompt
 Developer Prompt
 User Prompt
 Question
 Configuration

Prompt generation must be deterministic.

---

## FR-004 Dataset Execution

Questions shall be retrieved from Dataset Manager.

Execution modes include

 Sequential
 Randomized
 Category Filtered
 Difficulty Filtered

Random execution shall use a reproducible random seed.

---

## FR-005 Provider Invocation

The Benchmark Engine shall invoke AI models through the Provider Manager.

The engine shall never communicate directly with external providers.

---

## FR-006 Response Collection

The engine shall store

 Raw Response
 Parsed Response
 Execution Time
 Token Usage
 Finish Reason
 Error Information

Responses are immutable.

---

## FR-007 Retry Policy

Retry behavior shall be configurable.

Possible retry conditions

 Timeout
 Temporary Provider Failure
 Rate Limit
 Network Error

Retries shall never overwrite previous logs.

---

## FR-008 Parallel Execution

The engine shall support

 Single Execution
 Sequential Batch
 Parallel Batch

Parallel execution should be configurable.

---

## FR-009 Benchmark Reproducibility

Every benchmark execution shall record

 Provider Version
 Model Version
 Dataset Version
 Prompt Version
 Benchmark Version
 Configuration

This information is required for reproducibility.

---

# Non-Functional Requirements

## Performance

The engine shall support long-running benchmark jobs.

Background execution is recommended.

---

## Scalability

Multiple benchmark jobs should execute concurrently.

---

## Reliability

Partial failures shall not invalidate completed benchmark runs.

---

## Extensibility

The execution pipeline shall support future integration of

 RAG
 Persona
 Prompt Optimization
 Reflection Memory
 Tool Calling

without modifying the execution workflow.

---

# Architecture

```text
               Benchmark Engine

                     │

      ┌──────────────┼──────────────┐
      ▼              ▼              ▼

Dataset Manager  Model Manager  Prompt Generator

      │              │              │
      └──────────────┼──────────────┘
                     ▼

             Provider Manager

                     ▼

              External AI Model

                     ▼

               Response Collector

                     ▼

              Result Repository
```

The Benchmark Engine orchestrates execution but delegates specialized tasks to other components.

---

# Internal Components

## Benchmark Scheduler

Schedules benchmark execution.

Supports

 Immediate Execution
 Batch Execution
 Future Scheduled Execution

---

## Prompt Generator

Generates benchmark prompts.

Inputs

 Prompt Template
 Question
 Configuration

Output

 Final Prompt

---

## Execution Coordinator

Coordinates benchmark execution.

Responsible for

 Dataset Loading
 Model Selection
 Provider Invocation
 Response Collection

---

## Response Collector

Collects responses from AI providers.

Stores

 Raw Output
 Parsed Output
 Metadata

---

## Retry Manager

Handles retry logic.

Supports configurable retry policies.

---

## Execution Logger

Records execution events.

Events include

 Start
 Finish
 Failure
 Retry
 Cancellation

---

# Execution Flow

```text
User

↓

Select Benchmark

↓

Select Models

↓

Load Dataset

↓

Generate Prompt

↓

Provider Manager

↓

AI Model

↓

Collect Response

↓

Store Benchmark Run

↓

Scoring Engine
```

---

# Benchmark Pipeline

```text
Dataset

↓

Question

↓

Prompt Generation

↓

Provider Execution

↓

Response Collection

↓

Execution Log

↓

Scoring Engine
```

The Benchmark Engine completes its responsibility once responses have been collected and stored.

---

# Execution Configuration

Benchmark execution shall support configurable parameters.

Examples

 Temperature
 Max Tokens
 Top-P
 Timeout
 Retry Count
 Parallel Workers
 Random Seed

Configuration shall be stored with every Benchmark Run.

---

# Error Handling

Possible execution errors include

 Provider Unavailable
 Authentication Failure
 Timeout
 Rate Limit
 Invalid Prompt
 Invalid Dataset
 Execution Cancelled

Errors shall be logged without terminating unrelated benchmark runs.

---

# Logging

The Benchmark Engine shall log

 Benchmark Start
 Benchmark Finish
 Model
 Dataset
 Prompt Version
 Execution Time
 Token Usage
 Retry Count
 Error Information

Logs shall be immutable.

---

# Versioning

Each Benchmark Run shall record

 Benchmark Version
 Dataset Version
 Prompt Version
 Provider Version
 Model Version
 Execution Configuration

This information guarantees reproducibility.

---

# Future Extension

Future versions may support

 RAG Pipeline Integration
 Persona Engine
 Memory Engine
 Reflection Injection
 Tool Calling
 Multi-Agent Benchmark
 Human-in-the-Loop Evaluation
 Streaming Evaluation
 Automatic Regression Benchmark
 Continuous Benchmark Execution

These extensions shall integrate without changing the Benchmark Engine's core responsibilities.

---

# Dependencies

Depends on

 Provider Manager
 Model Manager
 Dataset Manager

Provides data to

 Scoring Engine
 Result Engine
 Experiment Engine

---

# Summary

The Benchmark Engine is the execution core of Psychology AI Lab.

It ensures that every AI model is evaluated under identical, reproducible conditions by coordinating dataset loading, prompt generation, provider communication, and response collection. By separating execution from evaluation, the Benchmark Engine enables fair comparison between models and provides a stable foundation for future extensions such as RAG, Persona evaluation, and advanced counseling benchmarks.
