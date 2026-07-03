# 23_BACKEND.md

# Backend Architecture

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the backend architecture of Psychology AI Lab.

The backend is the core of the research platform. It orchestrates benchmark execution, AI provider integration, experiment management, scoring, RAG evaluation, package generation, and persistent storage.

Its design emphasizes reproducibility, modularity, and scientific evaluation rather than high-throughput production serving.

---

# Design Principles

The backend shall follow these principles

 Modular Architecture
 Clean Architecture
 Domain-Driven Design (DDD)
 Provider Independent
 Event-Oriented
 Version Controlled
 Reproducible
 Extensible

Every module shall have a single responsibility.

---

# Technology Stack

Recommended implementation

Framework

 FastAPI

Language

 Python 3.12+

ORM

 SQLAlchemy 2.x

Migration

 Alembic

Validation

 Pydantic v2

HTTP Client

 httpx

Authentication

 JWT

Background Jobs

 Celery (Future)
 Redis Queue (Future)

Database

 PostgreSQL

Development Database

 SQLite

Vector Database

 Qdrant

---

# High-Level Architecture

```text
                 Frontend (Flutter Web)
                         │
                    REST API
                         │
                  FastAPI Backend
                         │
 ┌───────────────┬───────────────┬───────────────┐
 ▼               ▼               ▼
Application   Domain        Infrastructure
     │             │               │
     └─────────────┼───────────────┘
                   ▼
               PostgreSQL
                   │
             Qdrant (RAG)
                   │
             External AI APIs
```

The backend isolates business logic from infrastructure.

---

# Layered Architecture

## Presentation Layer

Responsibilities

 REST API
 Authentication
 Request Validation
 Response Serialization

Components

 Controllers
 Routers
 Middleware

---

## Application Layer

Coordinates business workflows.

Responsibilities

 Benchmark Execution
 Experiment Workflow
 Package Generation
 RAG Workflow

Contains use cases only.

---

## Domain Layer

Core business logic.

Contains

 Entities
 Value Objects
 Domain Services
 Repository Interfaces

The Domain Layer has no dependency on frameworks.

---

## Infrastructure Layer

Implements external services.

Responsibilities

 Database
 AI Providers
 Vector Database
 File Storage
 Logging

---

# Directory Structure

```text
backend

├── app
│   ├── api
│   ├── core
│   ├── domain
│   ├── application
│   ├── infrastructure
│   ├── repositories
│   ├── services
│   ├── models
│   ├── schemas
│   ├── workers
│   └── main.py
│
├── migrations
├── tests
├── scripts
└── requirements.txt
```

---

# Core Modules

Version 1 consists of

 Provider Manager
 Model Manager
 Dataset Manager
 Benchmark Engine
 Scoring Engine
 Result Engine
 Experiment Engine
 RAG Engine
 Package Builder

Each module is independently testable.

---

# API Layer

Responsibilities

 REST Endpoints
 Authentication
 Validation
 Error Handling

The API Layer never contains business logic.

---

# Service Layer

Coordinates workflows.

Examples

 BenchmarkService
 ExperimentService
 PackageService
 DatasetService
 RAGService

Services call Domain objects.

---

# Repository Layer

Repositories abstract persistence.

Examples

 ProviderRepository
 ModelRepository
 DatasetRepository
 BenchmarkRepository
 ResultRepository
 ExperimentRepository

Repository implementations are infrastructure concerns.

---

# AI Provider Adapters

Each provider implements a common interface.

Examples

```text
ProviderAdapter

├── OpenAIAdapter
├── GeminiAdapter
├── ClaudeAdapter
├── OpenRouterAdapter
└── OllamaAdapter (Future)
```

The Benchmark Engine communicates only with the common interface.

---

# Background Processing

Long-running tasks execute asynchronously.

Examples

 Benchmark Execution
 Experiment Execution
 Package Build
 Dataset Import
 RAG Indexing

Future versions may use Celery or Redis Queue.

---

# Database Access

SQLAlchemy manages relational data.

Responsibilities

 Transactions
 ORM Mapping
 Query Optimization
 Version Management

All schema changes use Alembic migrations.

---

# RAG Infrastructure

The backend supports

Knowledge Repository

↓

Embedding Engine

↓

Qdrant

↓

Retriever

↓

Prompt Augmentation

↓

Benchmark Engine

The RAG pipeline remains modular.

---

# Logging

Centralized structured logging.

Logs include

 API Requests
 Benchmark Runs
 Provider Calls
 Experiment Status
 Package Builds
 Errors

Sensitive information shall never be logged.

---

# Error Handling

Global exception handling shall normalize errors.

Examples

 Validation Error
 Authentication Error
 Provider Error
 Benchmark Error
 Database Error

Responses follow a consistent API format.

---

# Security

Version 1 supports

 JWT Authentication
 HTTPS
 Input Validation
 SQL Injection Protection
 Rate Limiting (Future)

API keys shall never be exposed to clients.

---

# Configuration

Configuration is environment-based.

Examples

 Database URL
 API Keys
 Qdrant URL
 Logging Level

Secrets are stored outside source code.

---

# Testing Strategy

Testing includes

Unit Tests

 Domain Logic

Integration Tests

 API
 Database
 AI Providers

Benchmark Tests

 End-to-End Evaluation

Regression Tests

 Benchmark Stability

---

# Deployment

Development

 Docker Compose

Production

 Docker
 Nginx
 PostgreSQL
 Qdrant

Future versions may support Kubernetes.

---

# Monitoring

Recommended tools

 Prometheus
 Grafana
 OpenTelemetry

Metrics include

 API Latency
 Benchmark Duration
 Provider Response Time
 Error Rate

---

# Scalability

The backend shall support horizontal scaling.

Stateless API servers enable load balancing.

Persistent state remains in PostgreSQL and Qdrant.

---

# Future Extension

Future versions may support

 gRPC
 GraphQL
 WebSocket
 Distributed Workers
 Multi-Tenant Architecture
 Human Evaluation Workflow
 AI Agent Framework
 Continuous Benchmark Runner
 Automatic Regression Detection

---

# Relationship with AIMindary

Psychology AI Lab backend is responsible for

 Research
 Benchmarking
 Validation
 Package Generation

AIMindary backend is responsible for

 Counseling Sessions
 User Memory
 Long-term Support
 Production Inference

The two systems remain loosely coupled through validated packages produced by the Package Builder.

---

# Summary

The Psychology AI Lab backend is a modular, domain-driven research platform built around reproducible AI evaluation.

Using FastAPI, SQLAlchemy, PostgreSQL, and Qdrant, it separates business logic from infrastructure while providing a scalable foundation for benchmarking, experimentation, RAG evaluation, and package generation. This architecture ensures that improvements to AI counseling systems are scientifically validated before deployment into production environments such as AIMindary.
