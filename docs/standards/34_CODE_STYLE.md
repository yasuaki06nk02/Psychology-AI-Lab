# 34_CODE_STYLE.md

# Code Style Guide

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the coding standards for Psychology AI Lab.

The objective is to ensure that the codebase remains consistent, readable, maintainable, and extensible throughout the lifetime of the project.

These rules apply to all source code, regardless of programming language or contributor.

---

# Design Principles

The codebase shall follow these principles

 Readability First
 Simplicity
 Maintainability
 Testability
 Modularity
 Consistency
 Explicitness

Code should be written for humans first and computers second.

---

# General Rules

Developers shall

 Prefer clear code over clever code.
 Write self-documenting code.
 Avoid unnecessary abstractions.
 Keep functions small.
 Keep classes focused.
 Eliminate duplicated logic.
 Favor composition over inheritance.

---

# Naming Conventions

## Variables

Use descriptive names.

Good

```text id=n0x5rf
benchmarkResult
providerManager
overallScore
```

Avoid

```text id=pwm2ra
a
temp
obj
x
```

---

## Functions

Functions should describe actions.

Examples

```text id=mwgddj
runBenchmark()

calculateScore()

buildPackage()

loadDataset()

validatePrompt()
```

Use verbs.

---

## Classes

Classes represent nouns.

Examples

```text id=umgo8u
BenchmarkEngine

ProviderManager

Experiment

ScoreCalculator

PackageBuilder
```

---

## Constants

Use uppercase snake case.

Examples

```text id=ehb1tk
MAX_RETRY_COUNT

DEFAULT_TIMEOUT

DEFAULT_TEMPERATURE
```

---

# File Naming

Use snake_case.

Examples

```text id=gw5s4r
benchmark_engine.py

provider_manager.py

score_calculator.py
```

Flutter files shall also use snake_case.

---

# Directory Naming

Directories use snake_case.

Example

```text id=clop4b
application

domain

infrastructure

repositories

services
```

---

# Function Design

Functions should

 Perform one responsibility.
 Be short.
 Return predictable results.
 Avoid hidden side effects.

Recommended length

20–40 lines

Very long functions should be refactored.

---

# Class Design

Each class shall have a single responsibility.

Avoid

 God Objects
 Utility Classes with unrelated methods
 Excessive inheritance

Prefer dependency injection.

---

# Layer Responsibilities

Presentation Layer

 UI
 API

Application Layer

 Use Cases
 Workflow

Domain Layer

 Business Rules

Infrastructure Layer

 Database
 External APIs
 File System

Business logic shall never exist in the Presentation Layer.

---

# Comments

Code should be understandable without excessive comments.

Comments should explain

 Why
 Business reasoning
 Non-obvious decisions

Avoid comments that simply restate the code.

Example

Poor

```text id=oh8tjt
 Increment i
i++;
```

Better

```text id=a2jszu
 Retry after provider rate limiting.
```

---

# Error Handling

Errors shall

 Be explicit
 Be typed
 Include meaningful messages

Avoid

```text id=n8e7lm
catch(Exception)
```

Prefer specific exception types.

---

# Logging

Log

 Benchmark execution
 Experiment execution
 Package publication
 Errors
 External API calls

Do not log

 API keys
 Secrets
 Personal data

---

# Dependency Management

Dependencies should be

 Minimal
 Well maintained
 Open Source when possible
 Version pinned

Unused dependencies shall be removed.

---

# Formatting

Recommended

Indentation

 4 spaces (Python)
 2 spaces (Dart formatting handled by formatter)

Maximum line length

 Approximately 100–120 characters

Use automatic formatters.

---

# Python Style

Follow

 PEP 8

Use

 Black
 Ruff
 isort

Type hints are required.

Example

```python
def calculate_score(result BenchmarkResult) - float
    ...
```

---

# Dart Style

Follow

 Effective Dart

Use

 dart format
 flutter analyze

Prefer immutable data models.

---

# API Code

REST endpoints should

 Validate input
 Return typed responses
 Avoid business logic

Controllers should remain thin.

---

# Database Code

Database access shall

 Use repositories
 Use transactions
 Avoid raw SQL when unnecessary

Schema changes require migrations.

---

# Testing Requirements

New code should include

 Unit Tests
 Integration Tests where applicable

Bug fixes should include regression tests whenever practical.

---

# Documentation

Public classes and interfaces should include documentation.

Documentation should explain

 Purpose
 Parameters
 Return values
 Exceptions

Complex algorithms should include implementation notes.

---

# Git Rules

Commits should be

 Small
 Atomic
 Descriptive

Examples

```text id=0a4t5g
Add benchmark comparison API

Fix score normalization bug

Implement package builder
```

Avoid generic commit messages.

---

# Code Review Checklist

Reviewers should verify

 Readability
 Naming
 Layer separation
 Tests
 Documentation
 Error handling
 Security
 Performance

---

# Refactoring

Refactoring is encouraged when it

 Simplifies code
 Improves readability
 Removes duplication
 Increases maintainability

Behavior shall not change unless explicitly intended.

---

# Future Extension

Future versions may include

 Static Analysis Rules
 Architecture Validation
 Dependency Graph Inspection
 Automatic Style Enforcement
 AI-assisted Code Review
 Complexity Analysis

---

# Relationship with AIMindary

Psychology AI Lab and AIMindary should follow the same coding standards whenever possible.

Sharing a consistent style guide makes it easier to transfer components such as the Provider Manager, Benchmark Engine, Package Builder, and RAG modules between the research platform and the production counseling system.

---

# Summary

The Code Style Guide establishes a consistent set of coding standards for Psychology AI Lab.

By emphasizing readability, modularity, clear architecture, strong typing, automated formatting, and comprehensive testing, these guidelines help ensure that the codebase remains maintainable, scalable, and suitable for long-term collaborative research and production integration with AIMindary.
