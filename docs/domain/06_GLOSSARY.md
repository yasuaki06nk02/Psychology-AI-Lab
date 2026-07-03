# 06_GLOSSARY.md

# Glossary

Project: Psychology AI Lab

Version: 0.1.0

Status: Draft

---

# Purpose

This glossary defines the official terminology used throughout Psychology AI Lab.

All specifications, APIs, database schemas, source code, documentation, and benchmark reports must use these definitions consistently.

A single concept should have a single official name.

---

# Core Terms

## Provider

An external AI service that hosts one or more language models.

Examples:

* OpenAI
* Google Gemini
* Anthropic
* OpenRouter

---

## AI Model

A specific Large Language Model (LLM) that generates responses.

Examples:

* GPT-5
* Gemini 2.5 Pro
* Claude Sonnet

---

## Dataset

A version-controlled collection of benchmark questions.

A dataset is immutable once released.

---

## Question

A single evaluation item contained within a dataset.

Question types include:

* Multiple Choice
* Short Answer
* Essay
* Clinical Case
* Dialogue

---

## Prompt Template

A reusable template used to construct prompts for AI models.

Contains:

* System Prompt
* Developer Prompt
* User Prompt
* Variables

---

## Benchmark

A standardized evaluation definition consisting of:

* Dataset
* Prompt Template
* Evaluation Rules
* Scoring Method

---

## Benchmark Run

One execution of a Benchmark against one AI Model.

Every run is recorded.

---

## Response

The raw output returned by an AI model.

Responses are immutable.

---

## Score

A numerical evaluation derived from a Response.

Examples include:

* Accuracy
* Empathy
* Safety
* Reflection
* Overall Score

---

## Benchmark Result

The complete output of a Benchmark Run.

Includes:

* Metadata
* Scores
* Logs
* Configuration

---

## Experiment

A collection of Benchmark Runs performed for comparison.

Examples:

* Compare multiple models
* Compare prompts
* Compare datasets
* Compare RAG configurations

---

# Future Terms

## Knowledge Package

A reusable collection of psychological knowledge used for RAG.

---

## Persona Package

A reusable definition of counselor personality and behavior.

---

## Prompt Package

A reusable collection of prompt templates.

---

## Counseling Package

A deployable package combining:

* Knowledge
* Persona
* Prompt
* Configuration

Designed for applications such as AIMindary.

---

## RAG

Retrieval-Augmented Generation.

An architecture that augments AI responses using external knowledge retrieval.

---

## Embedding

A numerical vector representation of text used for semantic search.

---

## Retriever

A component that selects relevant knowledge from a vector database.

---

## Vector Database

A database optimized for similarity search using embeddings.

Examples:

* Qdrant
* Chroma
* Milvus

---

## Therapeutic Alliance

The quality of the collaborative relationship established between the AI counselor and the user.

This is a major evaluation target in future benchmark versions.

---

## Reflection

The AI's ability to summarize, organize, and clarify the user's thoughts and emotions.

---

## Insight

A meaningful observation generated from dialogue that helps deepen the user's understanding.

---

## Treatment Planning

The AI's ability to propose appropriate next steps while respecting the limits of AI counseling.

---

## ACS (AIMindary Counseling Score)

The comprehensive evaluation score used to assess counseling quality.

Future ACS dimensions include:

* Knowledge
* Empathy
* Therapeutic Alliance
* Case Formulation
* Intervention
* Reflection
* Treatment Planning
* Safety
* Long-term Consistency

---

# Naming Rules

The following names are official.

| Official Term    | Avoid        |
| ---------------- | ------------ |
| Provider         | Service      |
| AI Model         | LLM Instance |
| Dataset          | Question Set |
| Benchmark        | Test         |
| Benchmark Run    | Trial        |
| Experiment       | Session      |
| Benchmark Result | Output       |
| Prompt Template  | Prompt       |
| Score            | Rating       |

---

# Summary

This glossary establishes the common language of Psychology AI Lab.

All future specifications and implementations must follow these definitions to ensure consistency, reproducibility, and compatibility across documentation, source code, and AI-assisted development.
