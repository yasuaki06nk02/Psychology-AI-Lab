# 12_DATASET_MANAGER.md

# Dataset Manager

Project: Psychology AI Lab

Version: 0.1.0

Status: Draft

---

# Purpose

The Dataset Manager is responsible for managing all benchmark datasets used within Psychology AI Lab.

A dataset represents a version-controlled collection of evaluation items used to assess AI counseling capabilities. The Dataset Manager ensures that datasets are reproducible, traceable, extensible, and independent of AI providers.

Every benchmark executed within Psychology AI Lab must reference a specific dataset version.

---

# Responsibilities

The Dataset Manager is responsible for:

* Managing benchmark datasets
* Managing dataset versions
* Managing benchmark questions
* Managing dataset metadata
* Importing and exporting datasets
* Validating dataset integrity
* Categorizing datasets
* Providing datasets to the Benchmark Engine

The Dataset Manager is **not responsible** for:

* Benchmark execution
* AI communication
* Score calculation
* Result generation
* Experiment management

---

# Functional Requirements

## FR-001 Dataset Registration

The system shall support registering benchmark datasets.

Examples include:

* Certified Public Psychologist Examination
* Clinical Psychology Examination
* CBT Knowledge Benchmark
* Schema Therapy Benchmark
* ACT Benchmark
* Depression Case Benchmark
* Anxiety Case Benchmark
* Sleep Counseling Benchmark
* Relationship Counseling Benchmark
* Workplace Mental Health Benchmark

Each dataset shall have a unique identifier.

---

## FR-002 Dataset Versioning

Every dataset shall be version controlled.

A new version shall be created whenever:

* Questions are added
* Questions are modified
* Evaluation criteria change
* Metadata changes

Published dataset versions shall remain immutable.

---

## FR-003 Question Management

Each dataset contains one or more benchmark questions.

Supported question types include:

* Multiple Choice
* Short Answer
* Essay
* Clinical Case
* Conversation Analysis
* Role Play
* Multi-turn Dialogue

Future versions may support multimedia questions.

---

## FR-004 Metadata Management

Each dataset shall maintain metadata including:

* Dataset ID
* Dataset Name
* Description
* Category
* Author
* Version
* Language
* License
* Number of Questions
* Creation Date
* Last Updated

---

## FR-005 Category Management

Datasets shall be grouped by category.

Examples:

Knowledge

* Public Psychologist Examination
* CBT
* ACT
* Schema Therapy

Clinical

* Depression
* Anxiety
* PTSD
* ADHD

Counseling

* Reflection
* Therapeutic Alliance
* Empathy
* Treatment Planning

Research

* Experimental Dataset
* Human Evaluation Dataset

---

## FR-006 Import and Export

Datasets shall support import and export.

Supported formats include:

* JSON
* YAML
* Markdown (Future)

Exported datasets shall preserve version information.

---

## FR-007 Validation

The Dataset Manager shall validate datasets before publication.

Validation includes:

* Required fields
* Duplicate question detection
* Missing answers
* Invalid categories
* Version consistency

Invalid datasets shall not be published.

---

# Non-Functional Requirements

## Performance

Datasets shall load efficiently even when containing thousands of questions.

Lazy loading may be used for large datasets.

---

## Reliability

Published datasets shall never change.

Historical benchmark results must remain reproducible.

---

## Extensibility

New question types shall be added without modifying existing dataset structures.

---

## Portability

Datasets shall remain independent of:

* AI Provider
* AI Model
* Benchmark Engine

Datasets should be reusable across projects.

---

# Architecture

```text
Dataset Manager
        │
        ▼
 Dataset Repository
        │
 ┌──────┼──────────────┐
 ▼      ▼              ▼
Metadata Questions Versions
        │
        ▼
 Benchmark Engine
```

The Dataset Manager acts as the authoritative source of benchmark data.

---

# Components

## Dataset Repository

Stores all datasets.

Responsibilities:

* Registration
* Lookup
* Version Management

---

## Question Manager

Maintains benchmark questions.

Responsibilities:

* CRUD Operations
* Validation
* Categorization

---

## Version Manager

Tracks dataset versions.

Historical versions shall remain immutable.

---

## Metadata Manager

Maintains descriptive information.

Examples:

* Description
* Author
* License
* Language

---

## Validation Engine

Validates datasets before publication.

Checks include:

* Required Fields
* Question Integrity
* Answer Integrity
* Duplicate Detection

---

# Dataset Structure

A dataset consists of:

* Metadata
* Categories
* Questions
* Evaluation Rules
* Version Information

Datasets shall not contain benchmark results.

---

# Question Structure

Every question shall include:

* Question ID
* Category
* Difficulty
* Question Type
* Prompt
* Expected Answer
* Explanation
* Tags

Optional fields include:

* Reference
* Source
* Notes

---

# Data Flow

```text
Dataset Manager

↓

Dataset Repository

↓

Benchmark Engine

↓

Question Selection

↓

Prompt Generation
```

The Benchmark Engine retrieves questions from the Dataset Manager during execution.

---

# Dataset Lifecycle

```text
Draft

↓

Validation

↓

Published

↓

Benchmark Usage

↓

Archived
```

Published datasets are immutable.

---

# Error Handling

Possible dataset errors include:

* Dataset Not Found
* Invalid Dataset
* Duplicate Dataset
* Missing Metadata
* Invalid Version
* Invalid Question
* Corrupted Dataset

Errors shall be standardized before reaching the Benchmark Engine.

---

# Logging

The Dataset Manager shall log:

* Dataset Creation
* Dataset Update
* Version Publication
* Import
* Export
* Validation Results

Benchmark execution shall not modify dataset logs.

---

# Versioning

Every benchmark result shall record:

* Dataset ID
* Dataset Version
* Question Set Version
* Benchmark Version

Version history shall never be overwritten.

---

# Future Extension

Future versions may support:

* Community Dataset Repository
* Peer Review Workflow
* Human Expert Annotation
* Clinical Validation
* Multi-language Datasets
* Image-based Questions
* Audio-based Questions
* Video-based Counseling Scenarios
* Automatic Dataset Generation
* Dataset Quality Metrics

---

# Dependencies

Depends on:

* Domain Model

Used by:

* Benchmark Engine
* Scoring Engine
* Experiment Engine

---

# Summary

The Dataset Manager provides a centralized, version-controlled repository for all benchmark datasets used within Psychology AI Lab.

It guarantees reproducibility, consistency, and long-term maintainability by separating benchmark data from benchmark execution. Every experiment performed within the platform depends on immutable, validated datasets, making reliable comparison between AI models possible.

