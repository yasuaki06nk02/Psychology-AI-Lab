# 21_API_SPEC.md

# API Specification

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the REST API specification for Psychology AI Lab.

The API provides a consistent interface for managing AI providers, models, datasets, benchmarks, experiments, RAG configurations, packages, and benchmark results.

All APIs shall be provider-independent and versioned to ensure backward compatibility.

---

# Design Principles

The API follows these principles

 RESTful
 Stateless
 Versioned
 Consistent JSON format
 OpenAPI compatible
 Provider independent
 Reproducible

Future versions may additionally expose GraphQL and gRPC interfaces.

---

# Base URL

```text id=m6z7u2
apiv1
```

Future versions

```text id=hbg0rq
apiv2
```

---

# Authentication

Version 1 supports

 API Key
 JWT Authentication

Future versions

 OAuth2
 OpenID Connect
 SSO

Every authenticated request shall include

```http
Authorization Bearer token
```

---

# Standard Response

Successful response

```json
{
  success true,
  data { },
  message null
}
```

Error response

```json
{
  success false,
  error {
    code MODEL_NOT_FOUND,
    message Requested model does not exist.
  }
}
```

---

# Provider APIs

## List Providers

```http
GET providers
```

Returns

 Provider ID
 Name
 Status
 Supported Models

---

## Get Provider

```http
GET providers{providerId}
```

---

## Register Provider

```http
POST providers
```

---

## Update Provider

```http
PUT providers{providerId}
```

---

## Delete Provider

```http
DELETE providers{providerId}
```

Deletion should normally be soft delete.

---

# Model APIs

## List Models

```http
GET models
```

Supports filters

 Provider
 Status
 Capability

---

## Get Model

```http
GET models{modelId}
```

---

## Register Model

```http
POST models
```

---

## Update Model

```http
PUT models{modelId}
```

---

## Disable Model

```http
PATCH models{modelId}disable
```

---

# Dataset APIs

## List Datasets

```http
GET datasets
```

---

## Get Dataset

```http
GET datasets{datasetId}
```

---

## Create Dataset

```http
POST datasets
```

---

## Publish Dataset

```http
POST datasets{datasetId}publish
```

Creates an immutable dataset version.

---

## Import Dataset

```http
POST datasetsimport
```

---

## Export Dataset

```http
GET datasets{datasetId}export
```

---

# Benchmark APIs

## List Benchmarks

```http
GET benchmarks
```

---

## Execute Benchmark

```http
POST benchmarksrun
```

Request

```json
{
  benchmarkId ...,
  modelId ...,
  datasetVersion ...,
  promptVersion ...
}
```

Returns

```json
{
  benchmarkRunId ...,
  status Running
}
```

---

## Benchmark Status

```http
GET benchmarksrun{runId}
```

---

## Cancel Benchmark

```http
POST benchmarksrun{runId}cancel
```

---

# Scoring APIs

## Score Benchmark

```http
POST scoresrun
```

---

## Get Score

```http
GET scores{benchmarkRunId}
```

---

## Recalculate Score

```http
POST scores{benchmarkRunId}recalculate
```

---

# Result APIs

## List Results

```http
GET results
```

Supports filters

 Model
 Benchmark
 Experiment
 Date

---

## Get Result

```http
GET results{resultId}
```

---

## Compare Results

```http
POST resultscompare
```

Example request

```json
{
  resultIds [
    A,
    B,
    C
  ]
}
```

---

## Export Results

```http
GET resultsexport
```

Supported formats

 JSON
 CSV

---

# Experiment APIs

## List Experiments

```http
GET experiments
```

---

## Create Experiment

```http
POST experiments
```

---

## Get Experiment

```http
GET experiments{experimentId}
```

---

## Execute Experiment

```http
POST experiments{experimentId}run
```

---

## Experiment Summary

```http
GET experiments{experimentId}summary
```

---

# RAG APIs

## List Knowledge Packages

```http
GET ragpackages
```

---

## Create Knowledge Package

```http
POST ragpackages
```

---

## List Embedding Models

```http
GET ragembeddings
```

---

## List Retrieval Strategies

```http
GET ragretrieval
```

---

## Execute RAG Benchmark

```http
POST ragrun
```

---

## RAG Comparison

```http
GET ragcomparison
```

---

# Package APIs

## List Packages

```http
GET packages
```

---

## Build Package

```http
POST packagesbuild
```

---

## Download Package

```http
GET packages{packageId}download
```

---

## Publish Package

```http
POST packages{packageId}publish
```

---

# Dashboard APIs

## Dashboard Summary

```http
GET dashboard
```

Returns

 Models
 Benchmarks
 Experiments
 Recent Results
 Top Scores

---

## Benchmark Statistics

```http
GET dashboardstatistics
```

---

## Leaderboard

```http
GET dashboardleaderboard
```

---

# Health APIs

## System Status

```http
GET health
```

---

## Provider Status

```http
GET healthproviders
```

---

## Database Status

```http
GET healthdatabase
```

---

# Pagination

List APIs support

```text
page=1

&pageSize=20
```

---

# Sorting

Example

```text
sort=createdAt

order=desc
```

---

# Filtering

Example

```text
provider=OpenAI

&model=GPT-5

&status=Completed
```

---

# HTTP Status Codes

 Code  Meaning               
 ----  --------------------- 
 200   OK                    
 201   Created               
 202   Accepted              
 204   No Content            
 400   Bad Request           
 401   Unauthorized          
 403   Forbidden             
 404   Not Found             
 409   Conflict              
 422   Validation Error      
 429   Too Many Requests     
 500   Internal Server Error 

---

# Error Codes

Examples

 PROVIDER_NOT_FOUND
 MODEL_NOT_FOUND
 DATASET_NOT_FOUND
 BENCHMARK_NOT_FOUND
 EXPERIMENT_NOT_FOUND
 PACKAGE_NOT_FOUND
 INVALID_CONFIGURATION
 VALIDATION_FAILED
 EXECUTION_TIMEOUT
 RATE_LIMIT

---

# Versioning Strategy

API versions shall remain backward compatible.

Example

```text
apiv1
apiv2
```

Deprecated endpoints shall remain available for at least one major version.

---

# Future Extension

Future versions may support

 GraphQL API
 gRPC
 WebSocket Streaming
 Server-Sent Events
 Batch APIs
 Async Job Queue
 AI Agent APIs
 Human Review APIs
 Plugin APIs
 Public Benchmark APIs

---

# Summary

The Psychology AI Lab API provides a unified, versioned, and provider-independent interface for managing every aspect of AI counseling research.

It enables external applications—including AIMindary—to execute benchmarks, retrieve evaluation results, compare experiments, manage RAG configurations, and deploy validated packages through a consistent REST architecture designed for long-term extensibility and reproducibility.
