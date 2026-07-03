# 33_TEST_RULE.md

# Test Rules

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the testing standards and quality assurance rules for Psychology AI Lab.

The objective is to ensure that every component of the platform is reliable, reproducible, and scientifically valid. Because Psychology AI Lab is a research platform, testing must verify not only software correctness but also the integrity and reproducibility of benchmark results.

---

# Testing Principles

Testing shall follow these principles

 Automated
 Reproducible
 Deterministic
 Independent
 Provider Independent
 Version Controlled
 Evidence Based

Every feature shall be testable in isolation.

---

# Testing Objectives

The testing strategy verifies

 Software correctness
 API behavior
 Benchmark reproducibility
 Scoring consistency
 RAG correctness
 Package integrity
 Performance
 Regression prevention

---

# Test Pyramid

The recommended testing hierarchy is

```text id=mk7eas
                Manual Review
                      ▲
               End-to-End Tests
                      ▲
            Integration Tests
                      ▲
                Unit Tests
```

Most tests should be Unit Tests.

---

# Test Categories

Version 1 includes

 Unit Tests
 Integration Tests
 API Tests
 Benchmark Tests
 Regression Tests
 Package Tests

Future versions may include

 Human Evaluation Tests
 UI Automation Tests
 Load Tests
 Security Tests

---

# Unit Tests

Unit Tests verify isolated business logic.

Targets include

 Domain Models
 Scoring Engine
 Benchmark Engine
 Prompt Processing
 Dataset Validation
 Package Builder

Unit Tests shall not depend on external AI providers.

---

# Integration Tests

Integration Tests verify interactions between components.

Examples

 Backend ↔ Database
 Backend ↔ Qdrant
 Backend ↔ Provider Manager
 Package Builder ↔ Repository

Mock providers should be used whenever possible.

---

# API Tests

REST APIs shall be tested for

 Success Responses
 Error Responses
 Validation
 Authentication
 Authorization
 Pagination
 Filtering

All public endpoints shall have automated API tests.

---

# Benchmark Tests

Benchmark Tests verify that benchmark execution behaves correctly.

Tests include

 Dataset Loading
 Prompt Generation
 Provider Invocation
 Result Storage
 Scoring
 Statistics

Benchmark definitions shall remain version-controlled.

---

# Scoring Tests

The Scoring Engine shall verify

 Category Scores
 Overall Score
 Weighting
 Missing Data Handling
 Boundary Conditions

Known benchmark examples shall produce consistent scores.

---

# RAG Tests

RAG functionality shall be tested for

 Embedding Generation
 Vector Search
 Retrieval Quality
 Prompt Augmentation
 Citation Integrity

Future versions may evaluate retrieval precision and recall.

---

# Package Tests

Package Builder shall verify

 Manifest Generation
 Dependency Resolution
 Archive Creation
 Version Metadata
 Integrity Validation

Generated packages shall be reproducible.

---

# Regression Tests

Regression Tests ensure that new changes do not alter previously validated behavior.

Regression targets include

 Benchmark Scores
 Prompt Processing
 API Responses
 Package Structure
 RAG Pipeline

Unexpected score changes shall trigger investigation.

---

# Deterministic Testing

Where possible

 Fixed datasets
 Fixed prompts
 Fixed scoring rules
 Fixed configuration

Randomness shall be minimized or explicitly controlled.

---

# Mocking Strategy

External services should be mocked for automated testing.

Examples

 AI Providers
 Authentication Services
 External APIs

This improves repeatability and reduces cost.

---

# Test Data

Test datasets shall be

 Version Controlled
 Immutable
 Small
 Representative

Synthetic data is preferred for automated tests.

---

# Continuous Integration

Every commit shall execute

 Unit Tests
 Integration Tests
 API Tests

Pull requests shall not be merged unless all required tests pass.

---

# Code Coverage

Recommended minimum coverage

 Domain Layer 90%
 Application Layer 80%
 API Layer 80%
 Infrastructure Layer 70%

Coverage is a quality indicator, not a substitute for meaningful tests.

---

# Performance Testing

Performance metrics include

 API Response Time
 Benchmark Duration
 Database Query Time
 Package Build Time

Performance benchmarks shall be recorded over time.

---

# Security Testing

Security tests should verify

 Authentication
 Authorization
 Input Validation
 SQL Injection Protection
 API Key Protection

Future versions may include automated vulnerability scanning.

---

# Error Handling Tests

The platform shall correctly handle

 Invalid Requests
 Provider Failures
 Database Failures
 Timeouts
 Network Errors
 Invalid Datasets

Errors shall return standardized responses.

---

# Acceptance Criteria

A feature is considered complete when

 All required tests pass
 Code review is completed
 Documentation is updated
 Regression tests succeed
 Benchmark reproducibility is maintained

---

# Test Reporting

Each test execution should record

 Test Name
 Result
 Duration
 Environment
 Version
 Timestamp

Historical test reports shall be retained.

---

# Future Extension

Future versions may include

 Human Reviewer Validation
 AI Judge Comparison
 Multi-Provider Regression Tests
 Continuous Benchmark Monitoring
 UI Automation
 Distributed Test Execution
 Automatic Benchmark Certification

---

# Relationship with AIMindary

Psychology AI Lab performs validation before deployment.

Only components that satisfy testing requirements and benchmark validation should be exported to AIMindary through the Package Builder.

This testing process ensures that production counseling benefits from scientifically verified improvements rather than unvalidated experimental changes.

---

# Summary

The Test Rules establish a comprehensive quality assurance framework for Psychology AI Lab.

By combining automated software testing with benchmark validation, reproducibility checks, regression testing, and package verification, the platform ensures that both the software and the underlying AI research remain reliable, repeatable, and evidence-based. These rules provide the foundation for confidently transferring validated counseling technologies into AIMindary.
