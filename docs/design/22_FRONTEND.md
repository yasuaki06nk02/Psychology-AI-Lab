# 22_FRONTEND.md

# Frontend Architecture

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the frontend architecture for Psychology AI Lab.

The frontend is designed as a research and evaluation platform for AI counseling systems. Its primary objective is to provide researchers with an intuitive interface for benchmarking AI models, comparing results, evaluating RAG configurations, and publishing validated packages for production systems such as AIMindary.

The frontend is optimized for research workflows rather than end-user counseling.

---

# Design Principles

The frontend shall follow these principles

 Research-first
 Data-driven
 Responsive
 Component-based
 Provider-independent
 Extensible
 Accessible

The interface shall emphasize clarity and reproducibility over visual complexity.

---

# Technology Stack

Recommended technologies

Frontend Framework

 Flutter Web

State Management

 Riverpod

Routing

 GoRouter

Networking

 Dio

Charts

 fl_chart

Data Table

 PlutoGrid

JSON Serialization

 json_serializable

Theme

 Material 3

Future versions may support desktop and mobile applications using the same Flutter codebase.

---

# Application Architecture

```text id=8kgxgf
Presentation Layer

↓

State Management

↓

Service Layer

↓

REST API

↓

Psychology AI Lab Backend
```

The frontend communicates exclusively through the REST API.

---

# Screen Structure

Version 1 consists of the following modules.

```text id=r4tx5f
Dashboard

Providers

Models

Datasets

Benchmarks

Experiments

Results

RAG

Packages

Settings
```

---

# Navigation

```text id=k1rjya
Dashboard

├── Providers
├── Models
├── Datasets
├── Benchmarks
├── Experiments
├── Results
├── RAG
├── Packages
└── Settings
```

Navigation shall remain consistent across all pages.

---

# Dashboard

Purpose

Provide a research overview.

Displays

 Registered Providers
 Available Models
 Dataset Count
 Benchmark Count
 Experiment Count
 Recent Benchmark Results
 Leaderboard
 System Status

Widgets shall update automatically.

---

# Provider Management

Functions

 List Providers
 Register Provider
 Edit Provider
 Health Check
 Connection Status

Displays

 Provider Name
 Status
 Models
 API Status

---

# Model Management

Functions

 List Models
 Filter Models
 View Capabilities
 Enable  Disable Models

Displays

 Model Name
 Provider
 Version
 Context Window
 Supported Features

---

# Dataset Management

Functions

 Browse Datasets
 Import Dataset
 Export Dataset
 Publish Dataset
 View Questions

Displays

 Dataset Metadata
 Version
 Question Count
 Categories

---

# Benchmark Screen

Functions

 Select Benchmark
 Select Dataset
 Select Models
 Configure Parameters
 Execute Benchmark

Configuration includes

 Temperature
 Max Tokens
 Prompt Template
 Retry Policy

Progress shall update in real time.

---

# Experiment Screen

Functions

 Create Experiment
 Configure Variables
 Define Hypothesis
 Execute Experiment
 Compare Results

Displays

 Experiment Status
 Benchmark Runs
 Statistics
 Improvement Metrics

---

# Result Screen

Functions

 Browse Results
 Compare Results
 Search History
 Export Results

Displays

 Overall Score
 Category Scores
 Response Time
 Token Usage
 Metadata

Supports side-by-side comparison.

---

# RAG Screen

Functions

 Select Knowledge Package
 Select Embedding Model
 Select Vector Database
 Select Retrieval Strategy
 Compare RAG Configurations

Displays

 Retrieved Documents
 Similarity Scores
 Benchmark Improvements

Future versions may visualize retrieval quality.

---

# Package Builder Screen

Functions

 Build Package
 Validate Package
 Publish Package
 Download Package

Displays

 Package Metadata
 Version
 Dependencies
 Validation Status

---

# Settings

Functions

 Theme
 API Configuration
 Database Connection
 Logging
 System Information

Future versions may support user management.

---

# State Management

Riverpod shall manage application state.

Major providers include

 Provider State
 Model State
 Dataset State
 Benchmark State
 Experiment State
 Result State
 RAG State
 Package State

Each feature shall manage its own state independently.

---

# Service Layer

Every screen communicates through service classes.

Examples

```text id=c2r2l9
ProviderService

ModelService

DatasetService

BenchmarkService

ExperimentService

ResultService

RAGService

PackageService
```

Services communicate with the REST API only.

---

# Component Library

Reusable UI components include

 Navigation Drawer
 Data Table
 Score Card
 Benchmark Progress
 Comparison Table
 Status Badge
 Search Panel
 Filter Panel
 Loading Indicator
 Error Dialog

Reusable components improve maintainability.

---

# Charts

Version 1 includes

 Score Distribution
 Benchmark History
 Model Comparison
 Category Breakdown
 Leaderboard
 RAG Comparison

Future versions may include interactive dashboards.

---

# Error Handling

Frontend shall display user-friendly messages.

Examples

 Provider Offline
 Authentication Failed
 Benchmark Running
 Dataset Missing
 Network Error

Technical details shall be logged separately.

---

# Loading States

Long-running operations shall display progress indicators.

Examples

 Benchmark Execution
 Experiment Execution
 Package Build
 Dataset Import
 RAG Evaluation

Users shall be able to monitor progress without refreshing the page.

---

# Notifications

The frontend shall support

 Success Notifications
 Warning Notifications
 Error Notifications
 Background Task Completion

Future versions may support desktop notifications.

---

# Security

The frontend shall

 Never store API keys in plain text
 Use HTTPS
 Validate API responses
 Protect authentication tokens

Sensitive configuration shall remain on the backend whenever possible.

---

# Accessibility

The interface should support

 Keyboard Navigation
 Screen Readers
 Responsive Layout
 High Contrast Themes

Accessibility improvements shall be incremental.

---

# Future Extension

Future versions may include

 Dark Mode
 Multi-language UI
 Plugin System
 Real-time Collaboration
 Human Evaluation Workspace
 Annotation Tools
 Experiment Templates
 AI-generated Reports
 AIMindary Integration Dashboard

---

# Relationship with AIMindary

Psychology AI Lab is a research application.

AIMindary is a production counseling application.

The frontend focuses on

 Research
 Benchmarking
 Validation
 Analysis
 Package Publication

Production counseling remains outside the scope of this application.

---

# Summary

The frontend of Psychology AI Lab provides a modular, research-oriented interface for evaluating AI counseling systems.

Built with Flutter Web, it enables researchers to manage providers, models, datasets, benchmarks, experiments, RAG configurations, and deployment packages through a unified, component-based architecture. By separating research workflows from production counseling, the frontend supports continuous, evidence-based improvement of AI systems while maintaining usability, reproducibility, and extensibility.
