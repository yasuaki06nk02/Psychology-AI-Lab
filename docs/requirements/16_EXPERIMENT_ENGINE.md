# 16_EXPERIMENT_ENGINE.md

# Experiment Engine

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

The Experiment Engine is responsible for planning, organizing, executing, and analyzing benchmark experiments within Psychology AI Lab.

Unlike the Benchmark Engine, which executes a single benchmark run, the Experiment Engine manages an entire research experiment consisting of multiple benchmark runs under controlled conditions.

Its purpose is to ensure that AI model evaluation follows a scientific, reproducible, and evidence-based methodology.

---

# Responsibilities

The Experiment Engine is responsible for

 Creating experiments
 Managing experiment configurations
 Defining research objectives
 Managing benchmark runs
 Comparing experimental conditions
 Tracking experiment history
 Recording hypotheses
 Managing variables
 Supporting statistical comparison
 Producing experiment summaries

The Experiment Engine is not responsible for

 Benchmark execution
 AI communication
 Score calculation
 Dataset authoring
 Result storage

---

# Functional Requirements

## FR-001 Experiment Creation

The system shall allow users to create an experiment.

Each experiment shall contain

 Experiment Name
 Description
 Objective
 Research Question
 Benchmark Definition
 Dataset Version
 Experiment Configuration

Every experiment receives a unique identifier.

---

## FR-002 Hypothesis Management

An experiment may define one or more research hypotheses.

Examples

 GPT-5 performs better than Gemini on CBT datasets.
 RAG improves Treatment Planning scores.
 Persona A increases Therapeutic Alliance.
 Prompt Version 2 improves Reflection quality.

Hypotheses remain associated with the experiment.

---

## FR-003 Variable Management

The Experiment Engine shall support controlled experimentation.

Independent Variables may include

 AI Model
 Prompt Template
 Persona
 Knowledge Package
 RAG Configuration
 Temperature
 Context Window

Dependent Variables include

 Overall Score
 Category Scores
 ACS
 Response Time
 Token Usage

Controlled Variables remain fixed throughout the experiment.

---

## FR-004 Benchmark Run Management

An experiment may contain one or more Benchmark Runs.

Examples

```text
Experiment

├── Benchmark Run 001
├── Benchmark Run 002
├── Benchmark Run 003
└── Benchmark Run 004
```

Each Benchmark Run shall preserve complete execution metadata.

---

## FR-005 Baseline Comparison

Experiments shall support baseline comparisons.

Examples

 Baseline Model vs Candidate Model
 Prompt A vs Prompt B
 Without RAG vs With RAG
 Before Fine-tuning vs After Fine-tuning

Baseline comparisons are first-class objects within the experiment.

---

## FR-006 Statistical Summary

The Experiment Engine shall calculate experiment-level summaries.

Examples

 Mean Score
 Median Score
 Standard Deviation
 Minimum
 Maximum
 Improvement Rate

Future versions may include statistical significance testing.

---

## FR-007 Experiment Notes

Researchers may attach notes to experiments.

Examples

 Observations
 Unexpected Behavior
 Limitations
 Future Improvements

Notes become part of the permanent experiment record.

---

## FR-008 Experiment Status

Experiments shall support lifecycle management.

States include

 Draft
 Scheduled
 Running
 Completed
 Failed
 Archived

---

# Non-Functional Requirements

## Reproducibility

Every experiment shall be reproducible using recorded metadata.

---

## Traceability

Every Benchmark Run shall be traceable back to its parent experiment.

---

## Extensibility

Future research methodologies shall integrate without redesigning the Experiment Engine.

---

## Reliability

Failed Benchmark Runs shall not invalidate the entire experiment unless explicitly configured.

---

# Architecture

```text
                 Experiment Engine

                        │

        ┌───────────────┼────────────────┐
        ▼               ▼                ▼

Hypothesis       Variables        Benchmark Runs

        │               │                │
        └───────────────┼────────────────┘
                        ▼

               Experiment Summary

                        ▼

                 Result Engine
```

The Experiment Engine orchestrates scientific evaluation while delegating execution and scoring to specialized components.

---

# Internal Components

## Experiment Manager

Responsible for

 Experiment Creation
 Configuration
 Lifecycle Management

---

## Hypothesis Manager

Stores research hypotheses.

Supports multiple hypotheses per experiment.

---

## Variable Manager

Manages

 Independent Variables
 Dependent Variables
 Controlled Variables

Ensures reproducible experimental conditions.

---

## Benchmark Coordinator

Schedules and monitors Benchmark Runs associated with an experiment.

---

## Comparison Engine

Generates comparisons between Benchmark Runs.

Supports

 Baseline Comparison
 Multi-model Comparison
 Historical Comparison

---

## Statistics Engine

Calculates experiment-level metrics.

Version 1 includes

 Average
 Median
 Standard Deviation
 Improvement Percentage

Future versions may support

 t-test
 ANOVA
 Confidence Intervals
 Effect Size

---

## Experiment Logger

Records

 Experiment Creation
 Configuration Changes
 Benchmark Progress
 Completion Status

Experiment logs are immutable after completion.

---

# Data Flow

```text
Research Question

↓

Experiment

↓

Hypothesis

↓

Variables

↓

Benchmark Runs

↓

Scoring Engine

↓

Result Engine

↓

Experiment Analysis
```

---

# Experiment Lifecycle

```text
Draft

↓

Configured

↓

Running

↓

Completed

↓

Reviewed

↓

Archived
```

Only completed experiments may be used for official benchmark comparison.

---

# Experiment Metadata

Each experiment shall record

 Experiment ID
 Research Objective
 Research Question
 Hypothesis
 Dataset Version
 Prompt Version
 Provider
 AI Model
 Benchmark Version
 Scoring Version
 Configuration
 Researcher
 Timestamp

---

# Comparison Workflow

```text
Baseline

       │

Candidate

       │

Benchmark Runs

       ▼

Statistics

       ▼

Improvement Report
```

The comparison workflow enables objective measurement of changes introduced by new models, prompts, personas, or RAG configurations.

---

# Error Handling

Possible experiment errors include

 Invalid Configuration
 Missing Benchmark
 Missing Dataset
 Benchmark Failure
 Interrupted Experiment
 Duplicate Experiment

Errors shall be recorded without deleting completed Benchmark Runs.

---

# Logging

The Experiment Engine shall log

 Experiment Creation
 Status Changes
 Configuration
 Benchmark Assignments
 Completion
 Errors
 Research Notes

Logs shall be immutable after experiment completion.

---

# Versioning

Every experiment shall record

 Experiment Version
 Benchmark Version
 Dataset Version
 Prompt Version
 Provider Version
 Model Version
 Scoring Version

This information ensures complete reproducibility.

---

# Future Extension

Future versions may support

 Human Expert Evaluation
 Blind Evaluation
 Multi-center Research
 Peer Review Workflow
 Automatic Regression Detection
 Continuous Benchmarking
 Research Collaboration
 Publication Export
 AI-generated Experiment Recommendations
 Automatic Hypothesis Generation

---

# Dependencies

Depends on

 Benchmark Engine
 Scoring Engine
 Result Engine
 Dataset Manager
 Model Manager

Provides data to

 Dashboard
 Analytics
 Package Builder
 Research Reports

---

# Summary

The Experiment Engine is the scientific research management layer of Psychology AI Lab.

It transforms individual benchmark executions into structured, reproducible research experiments by managing hypotheses, experimental variables, benchmark runs, statistical summaries, and research metadata. By separating experimentation from execution, the platform enables evidence-based evaluation of AI counseling systems and provides a rigorous foundation for comparing models, prompts, RAG configurations, personas, and future counseling strategies.
