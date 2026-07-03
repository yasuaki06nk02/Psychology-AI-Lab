# 41_VERSION2.md

# Version 2 Roadmap — RAG Evaluation Platform

Project Psychology AI Lab

Version 2.0.0

Status Design

---

# Purpose

Version 2 expands the MVP by introducing a complete RAG (Retrieval-Augmented Generation) Evaluation Platform.

The objective is no longer simply to compare AI models, but to scientifically measure how much performance improves when external psychological knowledge is supplied.

Version 2 answers the following research question

 How much does RAG improve AI counseling performance, and which RAG configuration provides the greatest measurable benefit

---

# Primary Goals

Version 2 shall enable researchers to

 Compare Standard AI vs RAG AI
 Compare multiple Knowledge Packages
 Compare Embedding Models
 Compare Retrieval Strategies
 Compare Chunking Strategies
 Compare Prompt Injection Methods
 Measure improvement quantitatively

Every experiment shall be reproducible.

---

# Scope

Included

 Knowledge Package Management
 Vector Database Integration
 Embedding Management
 Retrieval Configuration
 RAG Benchmark Execution
 RAG Comparison Dashboard
 RAG Experiment Tracking

Excluded

 Persona Optimization
 Memory Engine
 Production Deployment
 Continuous Learning

---

# Architecture

```text id=v7rm9q
Dataset

↓

Benchmark Engine

↓

RAG Engine

↓

Embedding Model

↓

Vector Database

↓

Knowledge Retrieval

↓

Prompt Builder

↓

AI Provider

↓

Scoring Engine

↓

Result Engine
```

The RAG Engine becomes a core component of the benchmark pipeline.

---

# New Modules

Version 2 introduces

```text id=m6s0xh
Knowledge Manager

Embedding Manager

Retrieval Manager

Chunk Manager

Vector Database Manager

RAG Engine

RAG Evaluator

RAG Dashboard
```

---

# Knowledge Packages

Knowledge shall be organized into versioned packages.

Examples

 CBT Package
 Schema Therapy Package
 ACT Package
 Psychoeducation Package
 DSM Package
 ICD Package
 Research Paper Package

Packages shall remain immutable after publication.

---

# Embedding Evaluation

Supported embedding providers may include

 OpenAI Embeddings
 Gemini Embeddings
 Voyage AI
 Cohere
 BAAI BGE
 Nomic
 Local Embeddings

Researchers shall compare embedding quality using identical datasets.

---

# Chunking Evaluation

Version 2 shall compare chunking strategies.

Examples

 Fixed Length
 Recursive
 Semantic
 Paragraph-Based
 Sliding Window

Chunk metadata shall be recorded for every experiment.

---

# Retrieval Strategies

Supported retrieval methods

 Top-K Similarity
 Hybrid Search
 MMR (Maximal Marginal Relevance)
 Metadata Filtering

Future versions may include graph-based retrieval.

---

# Prompt Augmentation

Retrieved knowledge shall be inserted using configurable templates.

Examples

```text id=k9s9qk
Developer Prompt

↓

Retrieved Knowledge

↓

User Prompt
```

Different injection templates may be benchmarked independently.

---

# Benchmark Workflow

```text id=3z9c1w
Select Dataset

↓

Select Knowledge Package

↓

Select Embedding Model

↓

Select Retrieval Strategy

↓

Run Benchmark

↓

Score Results

↓

Compare with Baseline
```

Baseline results from Version 1 shall always remain available for comparison.

---

# Evaluation Metrics

Version 2 extends scoring with

 Knowledge Accuracy
 Citation Quality
 Retrieval Precision
 Retrieval Recall (optional)
 Hallucination Reduction
 Context Utilization

Overall counseling scores remain unchanged.

---

# Dashboard Enhancements

New dashboard features include

 Knowledge Package Comparison
 Embedding Comparison
 Retrieval Strategy Comparison
 RAG Performance Gain
 Citation Statistics
 Knowledge Coverage

Visualizations should clearly distinguish baseline and RAG-enhanced results.

---

# Database Additions

New entities include

 Knowledge Packages
 Embedding Models
 Retrieval Configurations
 Chunk Configurations
 Vector Collections
 RAG Benchmark Results

All entities shall be version-controlled.

---

# API Additions

New endpoints

 ragpackages
 ragembeddings
 ragretrieval
 ragchunks
 ragrun
 ragresults
 ragcompare

These APIs extend, rather than replace, the Version 1 API.

---

# Success Criteria

Version 2 is complete when it can

✓ Import knowledge packages

✓ Generate embeddings

✓ Build vector indexes

✓ Execute RAG benchmarks

✓ Compare RAG against baseline

✓ Rank RAG configurations

✓ Export reproducible experiment reports

---

# Deliverables

Version 2 produces

 Knowledge Packages
 Vector Indexes
 RAG Benchmark Reports
 Embedding Comparisons
 Retrieval Comparisons
 Performance Gain Reports

These artifacts provide the evidence needed before introducing RAG into production.

---

# Out of Scope

The following remain outside Version 2

 Persona Optimization
 Therapist Style Evaluation
 Memory Engine
 Long-term Learning
 AI Self-Reflection
 Production Package Deployment

These are addressed in later versions.

---

# Roadmap Position

## Version 1

Baseline AI Benchmark

↓

## Version 2

RAG Evaluation

↓

## Version 3

Persona Evaluation

↓

## Version 4

Package Generation

↓

## AIMindary Production

Validated counseling components are deployed only after successful evaluation.

---

# Relationship with AIMindary

Version 2 evaluates whether external psychological knowledge meaningfully improves counseling performance.

Only RAG configurations that demonstrate measurable improvements through controlled benchmarking should be exported as Knowledge Packages for use in AIMindary.

This preserves the evidence-based philosophy of the project by ensuring that production knowledge is scientifically validated before deployment.

---

# Summary

Version 2 transforms Psychology AI Lab from a baseline benchmarking platform into a comprehensive RAG evaluation environment.

By systematically comparing knowledge packages, embedding models, retrieval strategies, and prompt augmentation techniques against Version 1 baselines, the platform quantifies the real contribution of external knowledge to AI counseling quality. These validated findings form the basis for future production-ready knowledge packages used by AIMindary.
