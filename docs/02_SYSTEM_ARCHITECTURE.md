# 02_SYSTEM_ARCHITECTURE.md

# System Architecture

Project: Psychology AI Lab

Version: 0.1.0

Status: Draft

---

# Purpose

This document defines the overall architecture of Psychology AI Lab.

The architecture is designed around a modular, AI-native research platform that enables objective evaluation, comparison, and continuous improvement of AI counseling systems.

Each component has a single responsibility and communicates through well-defined interfaces.

The system must be extensible, reproducible, and suitable for AI-assisted software development.

---

# Design Goals

The architecture is designed to satisfy the following goals.

* Modular
* Extensible
* Reproducible
* Provider Independent
* AI Native
* Testable
* Observable
* Version Controlled

Every component should be independently replaceable without affecting unrelated modules.

---

# High-Level Architecture

```text
                           Psychology AI Lab

 ┌──────────────────────────────────────────────────────────────┐
 │                        Frontend (Next.js)                    │
 │                                                              │
 │ Dashboard │ Models │ Datasets │ Benchmarks │ Results │ Lab   │
 └──────────────────────────────────────────────────────────────┘
                              │
                              ▼
 ┌──────────────────────────────────────────────────────────────┐
 │                    Backend API (FastAPI)                     │
 └──────────────────────────────────────────────────────────────┘
                              │
     ┌──────────────┬──────────┼──────────┬──────────────┐
     ▼              ▼          ▼          ▼              ▼
Provider      Dataset      Benchmark   Scoring     Experiment
Manager       Manager       Engine      Engine        Engine
     │              │          │          │              │
     └──────────────┴──────────┴──────────┴──────────────┘
                              │
                              ▼
                     Result Repository
                              │
                              ▼
                       SQLite / PostgreSQL

Future Extensions

RAG Engine
Embedding Engine
Vector Database
Package Builder
Persona Studio
Prompt Studio
Knowledge Manager
```

---

# Layer Architecture

The platform is organized into five logical layers.

```text
Presentation Layer

↓

Application Layer

↓

Domain Layer

↓

Infrastructure Layer

↓

External Services
```

---

## Presentation Layer

Responsible for user interaction.

Components include:

* Dashboard
* Model Management
* Dataset Management
* Benchmark Execution
* Result Viewer
* Experiment Viewer

Technology:

* Next.js
* React
* TypeScript
* Material UI

---

## Application Layer

Coordinates business workflows.

Examples:

* Execute Benchmark
* Calculate Score
* Compare Models
* Store Results
* Generate Reports

The application layer contains orchestration logic only.

Business rules belong to the domain layer.

---

## Domain Layer

Contains the core business logic.

Primary domain objects include:

* AI Model
* Provider
* Dataset
* Benchmark
* Benchmark Run
* Result
* Experiment
* Score

Future domain objects:

* Knowledge Package
* Persona Package
* Prompt Package
* Counseling Package

The domain layer should remain independent of frameworks.

---

## Infrastructure Layer

Responsible for external technologies.

Examples:

* Database
* AI Providers
* File Storage
* Logging
* Configuration
* Authentication
* Docker
* Background Tasks

Infrastructure components should never contain business rules.

---

## External Services

The system communicates with external AI providers.

Supported providers include:

* OpenAI
* Google Gemini
* Anthropic
* OpenRouter

Future providers may be added without modifying benchmark logic.

---

# Core Components

Version 1 includes the following components.

## Provider Manager

Responsible for:

* AI provider configuration
* API credentials
* Model discovery
* Model metadata

---

## Model Manager

Responsible for:

* Registered models
* Model capabilities
* Provider association
* Model version tracking

---

## Dataset Manager

Responsible for:

* Benchmark datasets
* Dataset versioning
* Question management
* Metadata

---

## Benchmark Engine

Responsible for:

* Prompt generation
* Model execution
* Answer collection
* Retry handling

The Benchmark Engine does not calculate scores.

---

## Scoring Engine

Responsible for:

* Answer evaluation
* Score calculation
* Category scoring
* Overall benchmark score

Future versions will introduce ACS (AIMindary Counseling Score).

---

## Result Engine

Responsible for:

* Persisting benchmark results
* Version history
* Report generation
* Export

---

## Experiment Engine

Responsible for:

* Running benchmark sessions
* Managing experiment configurations
* Recording execution metadata
* Comparing benchmark runs

---

# Data Flow

The benchmark execution flow is defined below.

```text
User

↓

Select AI Model

↓

Select Benchmark Dataset

↓

Create Experiment

↓

Benchmark Engine

↓

Provider Manager

↓

AI Model

↓

Response

↓

Scoring Engine

↓

Result Engine

↓

Database

↓

Dashboard
```

---

# Future Architecture

Version 2 introduces the RAG layer.

```text
Knowledge Manager

↓

Embedding Engine

↓

Vector Database

↓

Retriever

↓

Benchmark Engine

↓

Scoring Engine
```

The Benchmark Engine should not require modification when RAG is introduced.

Only the input generation pipeline should change.

---

# Package Architecture

Future versions generate reusable packages.

Examples include:

* Knowledge Package
* Persona Package
* Prompt Package
* Counseling Package

Packages should be version-controlled and independently deployable.

AIMindary consumes these packages but does not generate them.

---

# Architectural Principles

The architecture follows the following principles.

## Single Responsibility

Each component performs one clearly defined role.

---

## Loose Coupling

Modules communicate through interfaces.

Internal implementations should remain isolated.

---

## High Cohesion

Related functionality should remain within the same component.

Responsibilities should not overlap.

---

## Provider Independence

Business logic should never depend directly on a specific AI provider.

Adding a new provider should require only a new provider adapter.

---

## Versioning

Every benchmark result should record:

* Model Version
* Provider Version
* Dataset Version
* Prompt Version
* Benchmark Version
* Experiment Version

Every result must be reproducible.

---

## Testability

Every component should support:

* Unit Testing
* Integration Testing
* Regression Testing

External providers should be mockable.

---

## Future Compatibility

The architecture must support future expansion without major redesign.

Planned extensions include:

* RAG Evaluation
* Persona Evaluation
* Prompt Evaluation
* Embedding Comparison
* Vector Database Comparison
* Human Expert Review
* Continuous Benchmarking
* AIMindary Package Builder

---

# Architecture Summary

Psychology AI Lab adopts a modular architecture that separates evaluation, experimentation, scoring, and infrastructure into independent components.

This separation enables objective benchmarking, reproducible experiments, and continuous improvement of AI counseling systems while remaining provider-independent and extensible.

The architecture forms the technical foundation upon which all future capabilities—including RAG evaluation, counseling optimization, and package generation—will be built.
