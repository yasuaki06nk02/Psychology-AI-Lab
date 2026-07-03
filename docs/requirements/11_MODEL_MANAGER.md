# 11_MODEL_MANAGER.md

# Model Manager

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

The Model Manager is responsible for managing all AI models available within Psychology AI Lab.

It provides a centralized registry of benchmarkable models while maintaining model metadata, capabilities, configuration, version history, and benchmark compatibility.

The Model Manager abstracts model-specific information from the Benchmark Engine, enabling consistent evaluation across multiple providers.

---

# Responsibilities

The Model Manager is responsible for

 Registering AI models
 Managing model metadata
 Associating models with providers
 Managing model versions
 Managing benchmark configuration
 Managing default execution parameters
 Tracking model availability
 Providing model information to other components

The Model Manager is not responsible for

 API communication
 Benchmark execution
 Prompt generation
 Score calculation
 Dataset management
 Result storage

---

# Functional Requirements

## FR-001 Model Registration

The system shall support registering one or more AI models.

Examples include

 GPT-5
 GPT-5 Mini
 Gemini 2.5 Pro
 Gemini 2.5 Flash
 Claude Sonnet
 Claude Opus
 DeepSeek
 Qwen
 Llama

Every model belongs to exactly one Provider.

---

## FR-002 Model Metadata

Each model shall maintain metadata including

 Model ID
 Display Name
 Provider
 Version
 Release Date
 Context Window
 Maximum Output Tokens
 Supported Languages
 Status

---

## FR-003 Model Capabilities

Each model shall expose its supported capabilities.

Examples

 Chat
 JSON Output
 Function Calling
 Streaming
 Vision
 Image Generation
 Tool Calling
 Thinking Mode
 Embeddings (Future)

Capabilities are read-only metadata.

---

## FR-004 Default Parameters

Each model shall maintain default execution parameters.

Examples

 Temperature
 Top-P
 Max Tokens
 Frequency Penalty
 Presence Penalty

These values may be overridden by Benchmark configurations.

---

## FR-005 Model Availability

The system shall track whether a model is

 Available
 Deprecated
 Experimental
 Disabled

Unavailable models shall not be selectable for new benchmark runs.

---

## FR-006 Version Management

Every benchmark execution shall record the exact model version used.

If a provider updates a model, benchmark history must remain reproducible.

---

## FR-007 Benchmark Compatibility

The Model Manager shall expose compatibility information.

Examples

 Supports Multiple Choice
 Supports Long Context
 Supports Multi-turn Dialogue
 Supports JSON Output
 Supports Structured Evaluation

---

# Non-Functional Requirements

## Performance

Model metadata shall be cached to reduce unnecessary provider requests.

---

## Reliability

Model information shall remain available even if the provider is temporarily offline.

---

## Security

The Model Manager shall not store API credentials.

Authentication is managed exclusively by the Provider Manager.

---

## Extensibility

New models shall be registered without requiring changes to Benchmark Engine logic.

---

# Architecture

```text
Provider Manager
        │
        ▼
   Model Manager
        │
 ┌──────┼───────────────┐
 ▼      ▼               ▼
 GPT-5  Gemini 2.5 Pro  Claude Sonnet
```

The Model Manager acts as the authoritative registry of AI models.

---

# Components

## Model Registry

Stores all registered models.

Responsibilities

 Registration
 Lookup
 Version Management
 Availability

---

## Metadata Manager

Maintains model metadata.

Responsibilities

 Context Window
 Supported Features
 Provider Association
 Release Information

---

## Capability Manager

Stores supported model capabilities.

Capability data is used during benchmark planning.

---

## Configuration Manager

Maintains default execution parameters.

Allows benchmark-specific overrides.

---

## Version Manager

Tracks historical versions of every model.

Ensures benchmark reproducibility.

---

# Data Flow

```text
Benchmark Engine

↓

Model Manager

↓

Provider Manager

↓

AI Provider

↓

AI Model

↓

Response
```

The Benchmark Engine requests a model from the Model Manager.

The Model Manager resolves the appropriate Provider before execution.

---

# Model Configuration

Each model shall define

 Provider
 Model Identifier
 Display Name
 Default Parameters
 Supported Capabilities
 Benchmark Compatibility
 Status
 Version

---

# Model Selection

Users shall be able to

 Select one model
 Select multiple models
 Select all supported models

Multiple selected models may participate in the same Experiment.

---

# Model Categories

Models may be categorized for reporting purposes.

Examples

Commercial Models

 GPT
 Gemini
 Claude

Open Models

 Llama
 Qwen
 DeepSeek

Local Models (Future)

 Ollama
 LM Studio

---

# Benchmark Constraints

Some benchmarks may require specific capabilities.

Examples

Vision Benchmark

Requires

 Image Input

Long Conversation Benchmark

Requires

 Large Context Window

JSON Evaluation

Requires

 Structured Output

The Model Manager shall expose these compatibility flags.

---

# Error Handling

Possible model-related errors include

 Model Not Found
 Unsupported Capability
 Deprecated Model
 Disabled Model
 Provider Unavailable
 Invalid Configuration

Errors shall be standardized before reaching Benchmark Engine.

---

# Logging

The Model Manager shall log

 Model Name
 Provider
 Version
 Configuration
 Selection Timestamp
 Availability Changes

Sensitive information shall never be logged.

---

# Versioning

Every benchmark result shall record

 Provider
 Model
 Model Version
 Configuration
 Benchmark Version
 Timestamp

Version history shall never be overwritten.

---

# Future Extension

Future versions may support

 Automatic Model Discovery
 Cost Estimation
 Token Usage Prediction
 Performance Profiles
 Recommended Benchmark Selection
 Fine-Tuned Models
 Custom Models
 Local Models
 Ensemble Models

---

# Dependencies

Depends on

 Provider Manager

Used by

 Benchmark Engine
 Experiment Engine
 Result Engine

---

# Summary

The Model Manager provides a centralized and provider-independent registry of all AI models available within Psychology AI Lab.

It maintains model metadata, capabilities, versions, and benchmark compatibility while ensuring that benchmark execution remains reproducible, extensible, and independent of provider-specific implementations.
