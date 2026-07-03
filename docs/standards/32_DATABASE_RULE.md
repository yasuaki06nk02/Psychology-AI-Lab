# 32_DATABASE_RULE.md

# Database Rules

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the database design rules and operational standards for Psychology AI Lab.

The goal is to ensure that all benchmark data, experiment records, RAG evaluations, and package information remain consistent, reproducible, traceable, and immutable throughout the lifecycle of the platform.

These rules apply to every database implementation used by Psychology AI Lab.

---

# Design Principles

The database shall follow these principles

 Normalized
 Immutable
 Version Controlled
 Provider Independent
 Reproducible
 Auditable
 Extensible

Database rules shall prioritize scientific reproducibility over storage optimization.

---

# Database Philosophy

Psychology AI Lab is a research platform.

Therefore, database records represent research evidence, not merely application state.

Benchmark results are experimental observations and must never be rewritten after publication.

---

# Primary Database

Version 1 uses

 PostgreSQL

Development environment

 SQLite

Vector search

 Qdrant

The relational database and vector database remain independent systems.

---

# Data Classification

The database stores the following categories

Research Data

 Benchmarks
 Experiments
 Results

Reference Data

 Providers
 Models
 Prompt Templates
 Datasets

Knowledge Data

 Knowledge Packages
 Persona Packages
 Prompt Packages

Operational Data

 Logs
 Jobs
 Configuration

---

# Versioning Rules

The following entities require explicit versioning

 Dataset
 Prompt
 Persona
 Knowledge Package
 Benchmark
 Experiment
 Scoring Rule
 RAG Configuration
 Package

Published versions are immutable.

---

# Immutability Rules

The following records shall never be modified

 Benchmark Results
 Experiment Results
 Published Datasets
 Published Packages
 Published Prompt Versions
 Published Persona Versions

Corrections require a new version rather than updating an existing record.

---

# Primary Key Rules

All entities shall use UUIDs as primary keys.

Example

```text id=p0d2zt
550e8400-e29b-41d4-a716-446655440000
```

UUIDs improve portability and simplify distributed deployments.

---

# Foreign Key Rules

Foreign keys shall enforce referential integrity.

Examples

 Model → Provider
 Question → Dataset
 Benchmark → Prompt Template
 Result → Benchmark Run
 Package → Experiment

Orphaned records shall not exist.

---

# Soft Delete Policy

Research data shall not be physically deleted.

Soft deletion shall be used where appropriate.

Fields

 deleted_at
 deleted_by (Future)

Critical benchmark records shall never be deleted.

---

# Audit Rules

Major entities shall record

 created_at
 updated_at
 version

Future versions may include

 created_by
 updated_by
 change_reason

Audit history shall remain permanent.

---

# Transaction Rules

The database shall use transactions for

 Benchmark Execution
 Experiment Creation
 Package Publication
 Dataset Import
 Version Publication

Transactions shall be atomic.

---

# Concurrency Rules

The database shall prevent

 Lost Updates
 Dirty Reads
 Partial Writes

Appropriate transaction isolation levels shall be used based on operation type.

---

# Naming Rules

Tables

 snake_case
 plural nouns

Examples

```text id=5vmqaj
providers

models

datasets

benchmark_runs

experiment_runs

knowledge_packages
```

Columns

 snake_case

Examples

```text id=9wxldg
created_at

updated_at

benchmark_version

overall_score
```

---

# Timestamp Rules

All timestamps shall use

 UTC

Displayed time zones shall be handled by the frontend.

---

# JSON Usage

JSON columns are permitted for

 Configuration
 Metadata
 Category Scores
 Provider Capabilities
 Tags

Core relational data shall not be stored as JSON.

---

# Index Rules

Indexes shall exist for

Primary Keys

Foreign Keys

Frequently Queried Fields

Examples

 model_id
 benchmark_id
 experiment_id
 dataset_version
 package_version

Indexes shall be reviewed regularly.

---

# Constraint Rules

The database shall enforce

 NOT NULL
 UNIQUE
 FOREIGN KEY
 CHECK Constraints

Application code shall not replace database integrity rules.

---

# Backup Rules

Minimum backup schedule

Development

 Manual

Production

 Daily Automatic Backup

Retention

 Configurable

Backup verification shall be performed periodically.

---

# Migration Rules

Schema changes require migration scripts.

Recommended tool

 Alembic

Schema history shall be version-controlled.

---

# Performance Rules

The database shall support

 Large Benchmark History
 Large Experiment History
 Efficient Search
 Efficient Aggregation

Performance optimization shall not compromise reproducibility.

---

# Security Rules

The database shall

 Require authentication
 Encrypt connections
 Restrict privileges
 Protect backups
 Prevent SQL Injection

Only the backend may access the database directly.

---

# Logging Rules

Database operations should log

 Benchmark Creation
 Package Publication
 Dataset Publication
 Experiment Execution
 Migration

Sensitive information shall not appear in logs.

---

# Data Retention

Research data shall be retained indefinitely unless explicitly archived.

Operational logs may have configurable retention periods.

---

# Relationship with Qdrant

PostgreSQL stores

 Metadata
 Results
 Configuration
 Versions

Qdrant stores

 Embeddings
 Vector Indexes
 Retrieval Structures

The two databases are synchronized through the RAG Engine rather than direct coupling.

---

# Future Extension

Future versions may support

 Database Partitioning
 Read Replicas
 Multi-Tenant Storage
 Data Warehouse
 Time-Series Database
 Graph Database
 Automatic Archiving
 Cloud Storage Integration

---

# Relationship with AIMindary

Psychology AI Lab maintains its own independent research database.

Only validated packages are transferred to AIMindary.

No direct database sharing shall occur between the two systems.

This separation protects production systems from experimental changes.

---

# Summary

The Database Rules establish the foundational standards for storing research data within Psychology AI Lab.

By enforcing immutability, version control, referential integrity, and comprehensive auditability, the database becomes a reliable scientific record of AI benchmarking and counseling research. These principles ensure that every experiment remains reproducible, every package traceable, and every deployment into AIMindary is supported by verifiable evidence.
