# 31_API_RULE.md

# API Integration Rules

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the rules and standards for integrating external AI providers within Psychology AI Lab.

The objective is to ensure that every AI provider is accessed through a unified, reproducible, and provider-independent interface, allowing fair benchmarking across different models.

All provider-specific implementations shall remain isolated from the core benchmarking logic.

---

# Design Principles

API integration shall follow these principles

 Provider Independent
 Interface Driven
 Reproducible
 Version Controlled
 Secure
 Extensible
 Observable

The Benchmark Engine shall never communicate directly with provider-specific SDKs.

---

# Supported Providers

Version 1 supports

 OpenAI
 Google Gemini
 Anthropic Claude
 OpenRouter

Future versions may support

 Ollama
 Azure OpenAI
 AWS Bedrock
 NVIDIA NIM
 Groq
 Together AI
 Cohere
 Mistral AI
 DeepSeek
 Local LLM

---

# Provider Architecture

```text id=rfxm0n
Benchmark Engine

        │

        ▼

Provider Manager

        │

 ┌──────┼──────────────┐

 ▼      ▼              ▼

OpenAI Gemini Claude

        │

        ▼

HTTP API
```

The Provider Manager acts as the only gateway to external AI services.

---

# Provider Interface

Every provider implementation shall expose the same interface.

Required operations

 List Models
 Generate Response
 Health Check
 Get Provider Metadata

Optional operations

 Count Tokens
 Streaming
 Embeddings
 Vision
 Function Calling

---

# Standard Request Model

Every provider request shall contain

 Provider
 Model
 System Prompt
 Developer Prompt
 User Prompt
 Temperature
 Max Tokens
 Metadata

Additional provider-specific options shall be isolated within adapter implementations.

---

# Standard Response Model

Every provider response shall include

 Response Text
 Finish Reason
 Input Tokens
 Output Tokens
 Total Tokens
 Latency
 Provider Metadata

Responses shall be normalized before entering the Benchmark Engine.

---

# Provider Adapter Pattern

Each provider shall implement a common adapter.

Example

```text id=ksxkgv
AIProvider

│

├── OpenAIProvider

├── GeminiProvider

├── ClaudeProvider

└── OpenRouterProvider
```

The Benchmark Engine depends only on the `AIProvider` interface.

---

# Authentication

Authentication shall be provider-specific but abstracted from callers.

Supported methods

 API Key
 OAuth (Future)

API keys shall be loaded from environment variables or secure secret management systems.

---

# Rate Limiting

The Provider Manager shall detect and handle

 HTTP 429
 Provider quotas
 Retry delays

Retry strategies shall be configurable.

---

# Timeout Rules

Default request timeout

 120 seconds

Long-running requests shall be cancelled gracefully.

Timeout values shall be configurable per provider.

---

# Retry Policy

Recommended default

 Maximum retries 3
 Exponential backoff
 Retry only for transient failures

Requests that modify external state should not be retried automatically.

---

# Error Normalization

Provider-specific errors shall be converted into standardized error types.

Examples

 AUTHENTICATION_ERROR
 RATE_LIMIT
 TIMEOUT
 INVALID_MODEL
 NETWORK_ERROR
 SERVER_ERROR
 UNKNOWN_PROVIDER_ERROR

The Benchmark Engine shall never process raw provider errors directly.

---

# Token Accounting

Every provider response shall record

 Prompt Tokens
 Completion Tokens
 Total Tokens
 Estimated Cost (if available)

This information supports benchmarking and cost analysis.

---

# Logging

Every provider request shall log

 Provider
 Model
 Request Time
 Response Time
 Status
 Token Usage
 Error Code (if applicable)

Prompt contents should be masked or omitted when required for privacy.

---

# Security Rules

The integration layer shall

 Never expose API keys
 Validate provider responses
 Use HTTPS
 Sanitize request data
 Protect sensitive configuration

Secrets shall never be stored in source code.

---

# Provider Capability Detection

Each provider shall declare supported capabilities.

Examples

 Chat
 Streaming
 Vision
 Embeddings
 Tool Calling
 JSON Mode
 Function Calling

Capabilities shall be discoverable at runtime.

---

# Version Management

The following information shall be recorded for every benchmark

 Provider Name
 Provider Version
 Model Name
 Model Version
 API Version
 Prompt Version

This metadata supports reproducibility.

---

# Benchmark Fairness Rules

To ensure objective comparison

The following shall remain identical

 Dataset
 Prompt
 Temperature
 Max Tokens
 Scoring Rules

Only the selected provider or model should vary during provider comparison experiments.

---

# Streaming Support

Future versions may support

 Streaming Responses
 Partial Tokens
 Live Benchmark Display

Streaming shall not alter benchmark scoring.

---

# Provider Health Check

Each provider shall expose a health check.

Returned information

 Reachability
 Authentication Status
 Available Models
 Service Availability

Health checks shall be available from the dashboard.

---

# Future Extension

Future versions may include

 Automatic Provider Discovery
 Cost Optimization
 Smart Provider Routing
 Multi-Provider Ensemble
 Automatic Fallback
 Load Balancing
 Distributed Benchmark Execution
 Offline Model Support
 GPU Cluster Integration

---

# Relationship with AIMindary

Psychology AI Lab benchmarks AI providers through a unified abstraction layer.

AIMindary may reuse the same Provider Manager implementation, but production-specific behaviors—such as session memory, user personalization, and safety controls—remain independent from the research platform.

---

# Summary

The API Integration Rules define a standardized approach for connecting Psychology AI Lab to external AI providers.

By enforcing a provider-independent architecture, normalized request and response models, consistent error handling, and reproducible configuration management, the platform enables fair benchmarking across diverse AI models while remaining extensible to future providers and deployment environments.
