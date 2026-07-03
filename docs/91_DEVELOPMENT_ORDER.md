# 91_DEVELOPMENT_ORDER.md

# Development Order

Project Psychology AI Lab

Version 1.0

Status AI Agent Entry Point

---

# Purpose

This document defines the recommended implementation order for Psychology AI Lab.

It serves as the primary entry point for AI coding agents (e.g., Claude Code, Codex, Gemini CLI) and human developers by specifying which documents to read, the dependency order between modules, and the recommended implementation sequence.

The objective is to minimize implementation errors, avoid circular dependencies, and ensure a consistent development workflow.

---

# Development Principles

Implementation shall follow these principles

 Dependency First
 Bottom-Up Architecture
 Small Incremental Steps
 Test Before Expansion
 Documentation Driven
 Version Controlled

Do not implement higher-level modules before their dependencies are complete.

---

# Document Reading Order

Read the following documents in order before implementing any code.

## Phase 0 — Project Overview

1. 00_PROJECT.md
2. 01_PRODUCT_VISION.md
3. 02_SYSTEM_ARCHITECTURE.md
4. 05_DOMAIN_MODEL.md
5. 06_GLOSSARY.md

These documents define the overall architecture and terminology.

---

## Phase 1 — Core Requirements

Read

 10_MODEL_MANAGER.md
 11_PROVIDER_MANAGER.md
 12_DATASET_MANAGER.md
 13_BENCHMARK_ENGINE.md
 14_SCORING_ENGINE.md
 15_RESULT_ENGINE.md
 16_EXPERIMENT_ENGINE.md
 17_RAG_ENGINE.md
 18_PACKAGE_BUILDER.md

Do not begin implementation until these modules are understood.

---

## Phase 2 — Infrastructure

Read

 20_DATABASE.md
 21_API_SPEC.md
 22_FRONTEND.md
 23_BACKEND.md
 24_SEQUENCE_DIAGRAM.md
 25_DEPLOYMENT.md

These documents define how modules interact.

---

## Phase 3 — Development Rules

Read

 30_PROMPT_STYLE.md
 31_API_RULE.md
 32_DATABASE_RULE.md
 33_TEST_RULE.md
 34_CODE_STYLE.md

These documents define implementation standards.

---

## Phase 4 — Roadmap

Read

 40_MVP.md
 41_VERSION2.md
 42_FUTURE.md
 90_IMPLEMENTATION_ROADMAP.md

These documents define milestones and future direction.

---

# Implementation Order

The recommended implementation order is

```text
Project Setup
        │
        ▼
Backend Foundation
        │
        ▼
Database
        │
        ▼
Repository Layer
        │
        ▼
Provider Manager
        │
        ▼
Model Manager
        │
        ▼
Dataset Manager
        │
        ▼
Benchmark Engine
        │
        ▼
Scoring Engine
        │
        ▼
Result Engine
        │
        ▼
Experiment Engine
        │
        ▼
REST API
        │
        ▼
Frontend
        │
        ▼
Testing
        │
        ▼
MVP Complete
        │
        ▼
RAG Engine
        │
        ▼
Package Builder
        │
        ▼
Future Versions
```

Higher-level features shall not be implemented before lower-level dependencies are stable.

---

# Recommended Development Iteration

Each feature should follow the same development cycle.

```text
Read Specification

↓

Design

↓

Implement

↓

Unit Test

↓

Integration Test

↓

Documentation Update

↓

Commit

↓

Next Task
```

No feature is considered complete until tests pass and documentation is updated.

---

# Module Dependency Graph

```text
Provider Manager
        │
        ▼
Model Manager
        │
        ▼
Benchmark Engine
        │
        ▼
Scoring Engine
        │
        ▼
Result Engine
        │
        ▼
Experiment Engine
        │
        ▼
Package Builder
```

Supporting modules

```text
Database
        │
        ▼
Repositories
        │
        ▼
All Services
```

The Provider Manager is the primary gateway to external AI services.

---

# Testing Order

Testing should progress in the following sequence

1. Unit Tests
2. Integration Tests
3. API Tests
4. Benchmark Tests
5. Regression Tests

A module should not advance to the next stage until the current stage succeeds.

---

# Commit Strategy

Recommended commit order

1. Infrastructure
2. Domain Models
3. Services
4. API
5. Frontend
6. Tests
7. Documentation

Commit messages should describe a single logical change.

---

# AI Agent Workflow

For AI coding agents

1. Read only the documents required for the current task.
2. Avoid implementing unrelated features.
3. Respect layer boundaries.
4. Follow the architecture documents.
5. Write tests alongside implementation.
6. Update documentation if behavior changes.
7. Do not introduce provider-specific logic outside the Provider Manager.
8. Preserve reproducibility in all benchmark-related code.

This workflow minimizes context switching and improves implementation quality.

---

# Definition of Done

A task is complete only when all of the following are satisfied

 Feature implemented
 Unit tests pass
 Integration tests pass (where applicable)
 Documentation updated
 Code formatted
 Lint checks pass
 No known critical issues remain

---

# Version Progression

Development should follow this sequence

```text
Version 1
Baseline Benchmark
        │
        ▼
Version 2
RAG Evaluation
        │
        ▼
Version 3
Persona Evaluation
        │
        ▼
Version 4
Package Builder
        │
        ▼
Version 5+
Future Research Features
```

Do not begin implementation of a later version until the current version is stable.

---

# Relationship with AIMindary

Psychology AI Lab and AIMindary are separate projects.

Psychology AI Lab develops, benchmarks, and validates AI counseling components.

Only validated artifacts—such as Prompt Packages, Knowledge Packages, Persona Packages, and Evaluation Packages—should be transferred into AIMindary.

Implementation work for AIMindary should never compromise the independence or reproducibility of the research platform.

---

# Summary

This document serves as the implementation entry point for Psychology AI Lab.

By defining a clear document reading order, dependency-aware implementation sequence, testing workflow, and completion criteria, it enables both human developers and AI coding agents to build the platform systematically, consistently, and with minimal ambiguity. It should be the first document consulted before starting any development task.
