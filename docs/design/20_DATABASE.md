# 20_DATABASE.md

# Database Design

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the logical database architecture of Psychology AI Lab.

The database is designed to support reproducible AI benchmarking, experiment management, RAG evaluation, and package generation while maintaining complete traceability between research artifacts and benchmark results.

Every entity within the database shall be version-controlled where applicable.

---

# Design Principles

The database design follows these principles

 Normalized data model
 Immutable benchmark records
 Version-controlled entities
 Reproducible experiments
 Provider-independent structure
 Auditability
 Extensibility

Historical benchmark data shall never be overwritten.

---

# Database Architecture

Version 1 supports

 SQLite (Development)
 PostgreSQL (Production)

Future versions may support

 MySQL
 SQL Server
 Cloud SQL

Vector search is intentionally separated from the relational database.

---

# High-Level Entity Relationship

```text
Provider
    │
    └────── Model
               │
               ▼
         Benchmark Run
               │
      ┌────────┴────────┐
      ▼                 ▼
 Dataset            Prompt Template
      │
      ▼
 Questions
      │
      ▼
 Responses
      │
      ▼
 Scores
      │
      ▼
 Benchmark Result
      │
      ▼
 Experiment
      │
      ▼
 Package
```

---

# Core Tables

## providers

Stores AI providers.

Fields

 id
 name
 display_name
 api_base_url
 status
 created_at
 updated_at

---

## models

Stores benchmarkable AI models.

Fields

 id
 provider_id
 model_name
 display_name
 version
 context_window
 max_output_tokens
 capabilities (JSON)
 status
 created_at

Relationship

```
Provider

1

↓

N

Model
```

---

## datasets

Stores benchmark datasets.

Fields

 id
 dataset_name
 version
 description
 category
 language
 question_count
 created_at

---

## questions

Stores benchmark questions.

Fields

 id
 dataset_id
 category
 difficulty
 question_type
 prompt
 expected_answer
 explanation
 tags (JSON)

Relationship

```
Dataset

1

↓

N

Question
```

---

## prompt_templates

Stores prompt templates.

Fields

 id
 name
 version
 system_prompt
 developer_prompt
 user_template
 variables (JSON)

---

## benchmarks

Stores benchmark definitions.

Fields

 id
 name
 dataset_id
 prompt_template_id
 benchmark_version
 scoring_version

---

## benchmark_runs

Stores every benchmark execution.

Fields

 id
 benchmark_id
 model_id
 experiment_id
 configuration (JSON)
 status
 started_at
 completed_at

---

## responses

Stores raw AI responses.

Fields

 id
 benchmark_run_id
 raw_response
 parsed_response
 execution_time_ms
 input_tokens
 output_tokens
 finish_reason

Responses are immutable.

---

## scores

Stores evaluation results.

Fields

 id
 benchmark_run_id
 overall_score
 category_scores (JSON)
 evaluation_method
 scoring_version

Future

 ACS score
 Human evaluation

---

## experiments

Stores research experiments.

Fields

 id
 experiment_name
 objective
 hypothesis
 status
 researcher
 created_at

---

## experiment_runs

Associates Benchmark Runs with Experiments.

Fields

 id
 experiment_id
 benchmark_run_id

Supports many Benchmark Runs per Experiment.

---

## knowledge_packages

Stores validated knowledge packages.

Fields

 id
 package_name
 version
 description
 source_experiment
 checksum

---

## persona_packages

Stores validated persona definitions.

Fields

 id
 package_name
 version
 therapeutic_alliance_strategy
 communication_style

---

## prompt_packages

Stores reusable prompt packages.

Fields

 id
 package_name
 version
 prompt_template_id

---

## counseling_packages

Stores production deployment packages.

Fields

 id
 package_name
 version
 knowledge_package_id
 persona_package_id
 prompt_package_id

---

# Future RAG Tables

## embedding_models

Stores embedding model information.

Fields

 id
 name
 version
 provider

---

## vector_databases

Stores vector database configurations.

Fields

 id
 database_type
 version
 configuration

---

## retrieval_strategies

Stores retrieval algorithms.

Fields

 id
 strategy_name
 version
 parameters

---

## rag_configurations

Stores complete RAG configurations.

Fields

 id
 embedding_model_id
 vector_database_id
 retrieval_strategy_id
 top_k
 chunk_size
 chunk_overlap

---

## rag_runs

Stores RAG benchmark metadata.

Fields

 id
 benchmark_run_id
 rag_configuration_id
 retrieved_documents
 similarity_scores

---

# Versioning Strategy

The following entities require explicit versioning

 Provider
 Model
 Dataset
 Prompt Template
 Benchmark
 Scoring Rule
 Knowledge Package
 Persona Package
 Prompt Package
 Counseling Package
 RAG Configuration

Historical versions shall never be modified.

---

# Audit Requirements

Every record shall maintain

 created_at
 updated_at
 created_by (Future)
 version

Critical entities shall additionally record

 source_experiment
 benchmark_version
 package_version

---

# Indexing Strategy

Recommended indexes

Providers

 name

Models

 provider_id
 model_name

Datasets

 version
 category

Questions

 dataset_id
 category

Benchmark Runs

 benchmark_id
 model_id
 experiment_id

Scores

 benchmark_run_id
 overall_score

Experiments

 status
 created_at

Packages

 version
 package_name

---

# Database Constraints

The database shall enforce

 Foreign key integrity
 Unique version identifiers
 Immutable benchmark records
 Immutable package versions
 Required metadata
 Referential consistency

---

# Backup Strategy

Recommended

Development

 SQLite file backup

Production

 Daily PostgreSQL backup
 Point-in-time recovery
 Automated snapshot retention

---

# Migration Strategy

Schema changes shall use migration tools.

Recommended

 Alembic (FastAPI)
 SQLAlchemy ORM

All schema changes shall be version-controlled.

---

# Future Extension

Future versions may introduce

 Human Reviewer tables
 Expert Evaluation
 Annotation System
 Session Memory Evaluation
 Reflection Memory Evaluation
 Longitudinal Counseling Evaluation
 Multi-Agent Benchmark Results
 User Simulation Results
 Benchmark Leaderboards

---

# Summary

The Psychology AI Lab database is designed as a normalized, version-controlled, and research-oriented data model.

Its structure supports reproducible benchmarking, experiment management, RAG evaluation, and package deployment while preserving complete traceability between AI models, benchmark executions, evaluation results, and production-ready counseling packages. The database serves as the long-term foundation for evidence-based AI counseling research and continuous model improvement.
