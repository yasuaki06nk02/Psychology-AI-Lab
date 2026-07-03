# 17_RAG_ENGINE.md

# RAG Engine

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

The RAG (Retrieval-Augmented Generation) Engine is responsible for evaluating how external knowledge influences the performance of AI counseling models.

Unlike conventional RAG systems that focus on improving production responses, the RAG Engine in Psychology AI Lab exists to measure, compare, optimize, and validate RAG configurations under controlled experimental conditions.

Its primary objective is to quantify the impact of knowledge retrieval on counseling quality using reproducible benchmarks.

---

# Responsibilities

The RAG Engine is responsible for

 Managing knowledge retrieval
 Managing embedding models
 Managing vector databases
 Retrieving contextual knowledge
 Constructing augmented prompts
 Comparing RAG configurations
 Recording retrieval metadata
 Supporting RAG benchmarking
 Measuring RAG effectiveness

The RAG Engine is not responsible for

 Benchmark execution
 Score calculation
 Dataset management
 AI provider management
 Report generation

---

# Functional Requirements

## FR-001 Knowledge Package Management

The engine shall support multiple Knowledge Packages.

Examples

 CBT Knowledge
 Schema Therapy
 ACT
 DSM-5
 ICD-11
 Public Psychologist Examination
 Clinical Interview Manual

Each package shall be independently versioned.

---

## FR-002 Embedding Model Management

The system shall support multiple embedding models.

Examples

 OpenAI Embeddings
 Gemini Embeddings
 BGE
 E5
 Jina Embeddings
 Nomic Embeddings

Embedding model versions shall be recorded.

---

## FR-003 Vector Database Management

The engine shall support multiple vector databases.

Examples

 Qdrant
 Chroma
 Milvus
 Pinecone
 Weaviate
 PostgreSQL + pgvector

Vector database implementations shall be interchangeable.

---

## FR-004 Retrieval Strategies

The engine shall support multiple retrieval strategies.

Examples

 Top-K Retrieval
 Similarity Search
 Hybrid Search
 MMR (Maximum Marginal Relevance)
 Metadata Filtering
 Multi-stage Retrieval

Retrieval strategy shall be configurable.

---

## FR-005 Prompt Augmentation

Retrieved knowledge shall be incorporated into prompts.

The augmented prompt shall preserve

 Original Question
 Retrieved Context
 Prompt Template
 Version Information

Every generated prompt shall be reproducible.

---

## FR-006 Retrieval Metadata

Each benchmark shall record

 Knowledge Package
 Embedding Model
 Vector Database
 Retrieval Strategy
 Top-K
 Retrieved Documents
 Similarity Scores

Metadata is required for reproducibility.

---

## FR-007 RAG Benchmarking

The system shall support direct comparison between

 No RAG
 Single Knowledge Package
 Multiple Knowledge Packages
 Different Embedding Models
 Different Retrieval Strategies

The Benchmark Engine shall remain unchanged.

---

## FR-008 Knowledge Evaluation

The engine shall support evaluating

 Retrieval Accuracy
 Context Relevance
 Knowledge Coverage
 Hallucination Reduction
 Counseling Quality Improvement

These metrics are used by the Scoring Engine.

---

# Non-Functional Requirements

## Reproducibility

Identical retrieval configurations shall produce identical benchmark inputs whenever possible.

---

## Modularity

Embedding models, vector databases, and retrieval strategies shall be replaceable independently.

---

## Scalability

The engine shall support large knowledge bases containing millions of documents.

---

## Extensibility

Future retrieval algorithms shall integrate without modifying the Benchmark Engine.

---

# Architecture

```text
                  Benchmark Engine
                         │
                         ▼
                    RAG Engine
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
Knowledge Manager  Embedding Engine  Retriever
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                 Vector Database
                         │
                         ▼
               Retrieved Knowledge
                         │
                         ▼
               Prompt Augmentation
                         │
                         ▼
                   AI Provider
```

The RAG Engine augments benchmark prompts while remaining independent of benchmark execution.

---

# Internal Components

## Knowledge Manager

Responsible for

 Knowledge Packages
 Version Management
 Metadata
 Import  Export

---

## Embedding Manager

Responsible for

 Embedding Generation
 Embedding Model Selection
 Embedding Version Management

---

## Vector Database Adapter

Provides a common interface to supported vector databases.

---

## Retriever

Responsible for

 Similarity Search
 Ranking
 Filtering
 Top-K Selection

---

## Prompt Augmentor

Combines

 Original Prompt
 Retrieved Context
 Prompt Template

Produces the final augmented prompt.

---

## Retrieval Logger

Records

 Retrieved Documents
 Similarity Scores
 Retrieval Time
 Knowledge Versions

Logs are immutable.

---

# Retrieval Pipeline

```text
User Question

↓

Embedding

↓

Vector Search

↓

Relevant Documents

↓

Prompt Augmentation

↓

Benchmark Engine

↓

AI Model

↓

Response
```

---

# Knowledge Package Structure

A Knowledge Package shall contain

 Package ID
 Name
 Description
 Version
 Source Documents
 Metadata
 Tags
 License

Knowledge Packages are immutable once published.

---

# Benchmark Variables

Typical independent variables include

 Knowledge Package
 Embedding Model
 Vector Database
 Retrieval Strategy
 Top-K
 Chunk Size
 Chunk Overlap

Dependent variables include

 Benchmark Score
 ACS
 Hallucination Rate
 Response Quality
 Retrieval Accuracy

---

# Error Handling

Possible RAG errors include

 Missing Knowledge Package
 Embedding Failure
 Vector Database Unavailable
 Retrieval Failure
 Empty Retrieval Result
 Invalid Prompt Augmentation

Errors shall be logged without affecting benchmark history.

---

# Logging

The RAG Engine shall log

 Knowledge Package
 Embedding Model
 Vector Database
 Retrieval Strategy
 Retrieved Documents
 Similarity Scores
 Retrieval Time

Sensitive knowledge sources shall be protected.

---

# Versioning

Every benchmark using RAG shall record

 Knowledge Package Version
 Embedding Model Version
 Vector Database Version
 Retrieval Strategy Version
 Prompt Version
 Benchmark Version

Complete metadata is required for reproducibility.

---

# Future Extension

Future versions may support

 Graph RAG
 Agentic RAG
 Multi-Hop Retrieval
 Knowledge Fusion
 Dynamic Knowledge Selection
 Automatic Knowledge Evaluation
 Knowledge Conflict Detection
 Personalized Knowledge Packages
 Memory-Augmented RAG
 Continuous Knowledge Learning

---

# Dependencies

Depends on

 Dataset Manager
 Benchmark Engine
 Model Manager
 Provider Manager

Provides data to

 Scoring Engine
 Result Engine
 Experiment Engine
 Package Builder

---

# Relationship with Psychology AI Lab

The RAG Engine is not intended to maximize response quality alone.

Its primary purpose is to scientifically evaluate how different knowledge sources, embedding models, vector databases, and retrieval strategies influence AI counseling performance.

Every RAG configuration is treated as an experimental variable that can be objectively measured and compared.

---

# Summary

The RAG Engine provides a modular and reproducible framework for evaluating Retrieval-Augmented Generation within Psychology AI Lab.

By separating knowledge management, embedding, retrieval, and prompt augmentation into independent components, the platform enables systematic comparison of RAG strategies and quantifies their contribution to AI counseling quality. This evidence-based approach allows validated Knowledge Packages to be deployed confidently into applications such as AIMindary.
