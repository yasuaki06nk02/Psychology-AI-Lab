# README.md

# Psychology AI Lab

A scientific research platform for evaluating, benchmarking, and improving AI-based psychological counseling systems.

---

# Overview

Psychology AI Lab is a research-first evaluation environment designed to systematically measure the performance of AI models in psychological counseling tasks.

It is not a production chatbot system.

Instead, it is a controlled experimental lab where AI systems are tested, compared, and validated before any deployment into production systems such as AIMindary.

---

# Core Philosophy

The project is built on one principle

 No improvement is accepted unless it is measurable.

Every change to prompts, models, retrieval systems, or architectures must demonstrate

 Improved counseling quality
 Reproducible results
 Controlled experimental conditions

---

# Key Objectives

Psychology AI Lab is designed to

 Benchmark AI models on psychological counseling tasks
 Evaluate empathy, reflection, and CBT adherence
 Compare AI providers (OpenAI, Gemini, Claude, etc.)
 Measure the impact of RAG systems
 Evaluate counseling personas
 Produce validated AI counseling components
 Export safe and tested packages to AIMindary

---

# System Architecture

```text id=a1x9qk
Frontend (Flutter Web)
        │
        ▼
Backend (FastAPI)
        │
        ▼
Benchmark Engine
        │
        ├───────────────┐
        ▼               ▼
Provider Manager     RAG Engine (v2+)
        │               │
        ▼               ▼
AI Providers       Vector Database
        │               │
        └──────┬────────┘
               ▼
        Scoring Engine
               ▼
        Result Engine
               ▼
         PostgreSQL
```

---

# Project Versions

## Version 1 — MVP (Baseline Benchmark)

 AI model comparison
 Dataset-based evaluation
 Scoring system
 Provider integration
 No RAG, no memory

## Version 2 — RAG Evaluation

 Knowledge integration
 Embedding systems
 Retrieval benchmarking
 RAG performance comparison

## Version 3 — Persona Evaluation

 Therapist style modeling
 Persona benchmarking
 Communication strategy evaluation

## Version 4 — Package Builder

 Export validated AI components
 Safe deployment to AIMindary

## Future Versions

 Memory systems
 Multi-agent therapy systems
 Continuous learning platform

---

# Key Features

## Benchmark Engine

Runs structured psychological evaluation tasks across multiple AI models.

## Scoring Engine

Evaluates responses using

 Empathy
 CBT adherence
 Reflection quality
 Safety
 Completeness

## Provider Manager

Unified interface for multiple AI providers

 OpenAI
 Gemini
 Claude
 OpenRouter

## RAG Engine (v2+)

Retrieves psychological knowledge from vector databases to improve responses.

## Experiment Engine

Enables controlled comparison of

 Models
 Prompts
 Personas
 RAG configurations

---

# Project Structure

```text id=p7qk2m
psychology-ai-lab
│
├── 00_PROJECT.md
├── 01_PRODUCT_VISION.md
├── ...
├── 91_DEVELOPMENT_ORDER.md
├── 99_AI_AGENT.md
│
├── backend
├── frontend
├── infrastructure
└── docs
```

---

# Getting Started

## 1. Clone Repository

```bash
git clone repository-url
cd psychology-ai-lab
```

---

## 2. Setup Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn mainapp --reload
```

---

## 3. Setup Frontend

```bash
cd frontend
flutter pub get
flutter run -d chrome
```

---

## 4. Run Database

```bash
docker-compose up -d postgres qdrant
```

---

# Development Principles

 Follow `91_DEVELOPMENT_ORDER.md`
 Follow `99_AI_AGENT.md` for AI-assisted coding
 Keep benchmark data immutable
 Never mix research and production systems
 Always write tests for new features
 Maintain reproducibility at all times

---

# AI Agent Usage

This project is optimized for AI coding agents.

Recommended agents

 Claude Code
 OpenAI Codex
 Gemini CLI

Agents should

 Follow dependency order strictly
 Implement smallest possible feature units
 Write tests alongside implementation
 Avoid architectural changes without justification

---

# Relationship with AIMindary

Psychology AI Lab is a research system only.

AIMindary is a production counseling system.

Only validated outputs from this lab are transferred to AIMindary

 Prompt Packages
 Knowledge Packages
 Persona Packages
 Evaluation Packages

No direct runtime coupling exists.

---

# Roadmap Summary

```text id=r4m8zq
MVP (v1)
  ↓
RAG Evaluation (v2)
  ↓
Persona Evaluation (v3)
  ↓
Package Builder (v4)
  ↓
Memory & Multi-Agent Systems (v5+)
```

---

# Success Criteria

The project is successful if it can

 Reproducibly benchmark AI counseling models
 Quantify improvements from RAG and personas
 Compare AI providers objectively
 Generate validated AI counseling packages
 Support research-grade experimentation

---

# Guiding Principles

 Scientific rigor
 Reproducibility
 Transparency
 Modularity
 Separation of research and production
 Evidence-based improvement

---

# Final Note

Psychology AI Lab is not just a software project.

It is a scientific infrastructure for understanding and improving AI-based psychological counseling systems.

Every component exists to support one goal

 Build AI counseling systems that can be trusted through evidence, not intuition.
