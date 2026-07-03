# 30_PROMPT_STYLE.md

# Prompt Style Guide

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the prompt engineering standards used throughout Psychology AI Lab.

Its purpose is to ensure that all benchmark prompts are consistent, reproducible, provider-independent, and scientifically comparable.

A standardized prompt style minimizes experimental bias and enables fair comparison across AI models, prompt versions, RAG configurations, and counseling personas.

---

# Design Principles

All prompts shall follow these principles

 Clear
 Explicit
 Reproducible
 Modular
 Provider Independent
 Version Controlled
 Benchmark Friendly

Prompts should evaluate AI capability rather than exploit provider-specific optimizations.

---

# Prompt Architecture

Every benchmark prompt consists of four logical layers.

```text id=z4m8pe
System Prompt

↓

Developer Prompt

↓

Context (Optional)

↓

User Prompt
```

Each layer has a distinct responsibility.

---

# Layer 1 — System Prompt

The System Prompt defines the fundamental role and constraints of the AI.

Responsibilities

 Identity
 Behavioral Rules
 Ethical Constraints
 Global Instructions

Example

```text
You are a professional psychological counselor.

Always prioritize empathy, evidence-based reasoning,
and client safety.

Avoid unsupported medical advice.
```

System prompts should remain stable across benchmark versions.

---

# Layer 2 — Developer Prompt

The Developer Prompt defines benchmark-specific behavior.

Examples

 Follow CBT principles.
 Evaluate cognitive distortions.
 Produce structured responses.
 Do not invent information.
 Explain reasoning when appropriate.

Developer prompts should contain implementation-neutral instructions.

---

# Layer 3 — Context

Context is optional.

Possible sources

 Counseling history
 Memory Engine
 Retrieved RAG knowledge
 Persona configuration
 Session metadata

Example

```text
Previous Session

The client reported difficulty sleeping and excessive self-criticism.

Today's objective

Identify automatic thoughts.
```

Benchmark datasets shall specify whether context is enabled.

---

# Layer 4 — User Prompt

The User Prompt contains the benchmark question.

Example

```text
I keep thinking that everyone dislikes me because I made one mistake at work.

How should I think about this
```

The user prompt must remain unchanged across model comparisons.

---

# Prompt Template

Standard structure

```text
System Prompt

↓

Developer Prompt

↓

Context (Optional)

↓

User Prompt
```

This structure shall be used by all benchmark executions.

---

# Prompt Variables

Template variables may include

 {{persona}}
 {{context}}
 {{history}}
 {{knowledge}}
 {{question}}
 {{language}}

Variables shall be resolved before benchmark execution.

---

# Persona Injection

Personas are injected separately from benchmark prompts.

Example

```text
Persona

Warm
Reflective
Collaborative
Evidence-Based
```

Persona definitions shall be version-controlled.

---

# RAG Injection

Retrieved knowledge shall appear after the Developer Prompt and before the User Prompt.

Structure

```text
Developer Prompt

↓

Retrieved Knowledge

↓

User Prompt
```

Knowledge sources shall be recorded in benchmark metadata.

---

# Prompt Versioning

Every prompt shall include

 Prompt ID
 Version
 Author
 Description
 Creation Date

Published prompt versions are immutable.

---

# Prompt Categories

Examples

Counseling

 CBT
 Schema Therapy
 ACT
 Motivational Interviewing

Evaluation

 Reflection
 Cognitive Distortion
 Treatment Planning
 Risk Assessment

Knowledge

 DSM
 ICD
 Psychological Education

Research

 Benchmark
 Human Evaluation
 RAG Comparison

---

# Prompt Length

Prompts should remain concise while preserving reproducibility.

Recommended

System Prompt

 Stable
 Minimal

Developer Prompt

 Explicit
 Structured

Context

 Relevant Only

User Prompt

 Natural Language

---

# Benchmark Consistency

To ensure fair comparison

The following shall remain fixed

 User Prompt
 Dataset
 Benchmark Rules
 Scoring Rules

The following may vary

 AI Model
 Prompt Version
 Persona
 RAG Configuration
 Temperature

---

# Prompt Evaluation

Prompt quality may be evaluated using

 Response Quality
 Consistency
 Hallucination Rate
 Counseling Quality
 ACS
 Human Evaluation

Prompt evaluation is independent of model evaluation.

---

# Prompt Metadata

Every prompt shall include

 Prompt ID
 Name
 Version
 Category
 Language
 Description
 Author
 Dependencies

---

# Error Prevention

Prompt templates should avoid

 Ambiguous wording
 Contradictory instructions
 Provider-specific syntax
 Hidden assumptions
 Dynamic randomness

Prompt behavior should remain deterministic whenever possible.

---

# Example Benchmark Prompt

```text
System Prompt

You are a licensed psychological counselor.

--------------------------------

Developer Prompt

Use CBT principles.

Identify cognitive distortions.

Provide reflective listening.

Do not fabricate information.

--------------------------------

Context

Previous Session
The client experiences anxiety before work presentations.

--------------------------------

User Prompt

I made one mistake during my presentation today.

Now I feel like everyone thinks I'm incompetent.
```

---

# Future Extension

Future versions may support

 Multi-Agent Prompting
 Dynamic Prompt Composition
 Automatic Prompt Optimization
 Prompt Benchmark Leaderboards
 Prompt Regression Testing
 Prompt Explainability
 Prompt AB Testing
 Personalized Prompt Packages
 Memory-aware Prompt Templates

---

# Relationship with AIMindary

Psychology AI Lab evaluates prompts scientifically.

Validated prompt versions are exported through the Package Builder and deployed into AIMindary as Prompt Packages.

This ensures that only experimentally verified prompting strategies are used in production counseling.

---

# Summary

The Prompt Style Guide establishes a standardized framework for constructing benchmark prompts within Psychology AI Lab.

By separating System Prompts, Developer Prompts, Context, and User Prompts into clearly defined layers, the platform enables reproducible and provider-independent evaluation of AI counseling systems. Standardized prompt design supports fair benchmarking, controlled experimentation, and the reliable transfer of validated prompt strategies into AIMindary.
