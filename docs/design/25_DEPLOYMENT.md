# 25_DEPLOYMENT.md

# Deployment Architecture

Project Psychology AI Lab

Version 0.1.0

Status Draft

---

# Purpose

This document defines the deployment architecture of Psychology AI Lab.

The deployment architecture is designed to support both local research environments and production-grade evaluation infrastructure while maintaining reproducibility, scalability, and operational simplicity.

The system is intended to run as a self-hosted research platform and can later be deployed to cloud infrastructure.

---

# Deployment Principles

The deployment architecture follows these principles

 Modular Services
 Containerized Deployment
 Environment Independence
 Horizontal Scalability
 Secure Configuration
 Reproducible Infrastructure
 Cloud Ready

All components should be deployable independently.

---

# Deployment Targets

Version 1 supports

Development

 Windows
 macOS
 Linux

Production

 Ubuntu Server
 Docker
 Docker Compose

Future versions may support

 Kubernetes
 AWS
 Azure
 Google Cloud
 DigitalOcean

---

# High-Level Deployment

```text id=a8t4rf
                Browser
                   │
             Flutter Web
                   │
              HTTPS  REST
                   │
             Nginx Reverse Proxy
                   │
          -------------------------
          │                       │
          ▼                       ▼
     FastAPI Backend         Static Frontend
          │
     -----------------------------
     │            │             │
     ▼            ▼             ▼
 PostgreSQL    Qdrant      Redis (Future)
     │
     ▼
 Backup Storage
```

---

# Container Architecture

Recommended Docker containers

```text id=vjlwmc
frontend

backend

postgres

qdrant

nginx

redis (Future)

worker (Future)
```

Each service runs independently.

---

# Frontend Deployment

Technology

 Flutter Web

Deployment

 Static Files
 Nginx

Responsibilities

 UI
 Dashboard
 Visualization

No business logic resides in the frontend.

---

# Backend Deployment

Technology

 FastAPI
 Uvicorn

Responsibilities

 REST API
 Benchmark Engine
 Experiment Engine
 RAG Engine
 Package Builder

Backend remains stateless.

---

# Database Deployment

Primary database

PostgreSQL

Stores

 Experiments
 Results
 Datasets
 Metadata
 Packages

The database should reside on persistent storage.

---

# Vector Database

Technology

Qdrant

Stores

 Embeddings
 Vector Indexes
 Retrieval Metadata

Qdrant is deployed independently from PostgreSQL.

---

# Reverse Proxy

Technology

Nginx

Responsibilities

 HTTPS
 Static Hosting
 API Routing
 Compression
 Security Headers

Future

 Load Balancing

---

# Background Workers

Future architecture

```text id=j2vxtu
Backend

      │

      ▼

Redis Queue

      │

      ▼

Worker

      │

      ▼

Benchmark Jobs
```

Used for

 Benchmark Execution
 Experiment Execution
 Package Generation
 Dataset Import

---

# Storage

Persistent storage includes

 PostgreSQL Data
 Qdrant Data
 Uploaded Datasets
 Generated Packages
 Logs
 Backups

Recommended directory structure

```text id=fr2bwf
data

postgres

qdrant

packages

uploads

logs

backups
```

---

# Environment Variables

Typical configuration

```text id=jlwmhv
DATABASE_URL

QDRANT_URL

JWT_SECRET

OPENAI_API_KEY

GOOGLE_API_KEY

ANTHROPIC_API_KEY

OPENROUTER_API_KEY

LOG_LEVEL
```

Secrets shall never be committed to source control.

---

# HTTPS

Production deployments shall support

 HTTPS
 TLS 1.3
 Automatic Certificate Renewal

Recommended

 Let's Encrypt
 Certbot

---

# Scaling Strategy

Version 1

Single Server

```text id=qjyyrh
Browser

↓

Nginx

↓

Backend

↓

PostgreSQL

↓

Qdrant
```

Future

Multiple Backend Instances

```text id=pp2adk
Load Balancer

      │

 ┌────┴────┐

 ▼         ▼

Backend Backend

      │

 PostgreSQL

      │

 Qdrant
```

Backend instances remain stateless.

---

# Monitoring

Recommended stack

 Prometheus
 Grafana

Metrics

 CPU
 Memory
 Disk
 API Latency
 Benchmark Duration
 Provider Response Time
 Error Rate

---

# Logging

Centralized logging.

Sources

 Backend
 Frontend
 Database
 Workers
 Nginx

Future

 Loki
 ELK Stack

---

# Backup Strategy

Database

 Daily Backup

Packages

 Versioned Archive

Datasets

 Immutable Backup

Configuration

 Version Controlled

Backups should be tested regularly.

---

# Disaster Recovery

Recovery procedures include

 Database Restore
 Package Restore
 Dataset Restore
 Configuration Restore

Recovery objectives

 Minimal Data Loss
 Rapid System Recovery

---

# Security

Recommended

 HTTPS
 JWT Authentication
 Firewall
 API Rate Limiting
 Secure Secrets Management
 Database Authentication

Production systems should disable debug mode.

---

# CICD

Recommended workflow

```text id=pz3jxu
GitHub

      │

      ▼

GitHub Actions

      │

      ▼

Testing

      │

      ▼

Docker Build

      │

      ▼

Deployment
```

Deployment should occur only after successful automated tests.

---

# Development Environment

Recommended local setup

```text id=xhzm5r
Flutter Web

↓

FastAPI

↓

SQLite

↓

Qdrant

↓

Docker Compose
```

Local development should require minimal configuration.

---

# Production Environment

Recommended production stack

```text id=5w5mjp
Flutter Web

↓

Nginx

↓

FastAPI

↓

PostgreSQL

↓

Qdrant

↓

Backup Server
```

Production should prioritize stability and reproducibility.

---

# Relationship with AIMindary

Psychology AI Lab and AIMindary are deployed independently.

```text id=lrm2el
Psychology AI Lab

      │

Validated Packages

      │

      ▼

AIMindary
```

The systems communicate through versioned packages rather than direct database access.

This separation ensures that research activities cannot affect production counseling services.

---

# Future Extension

Future versions may support

 Kubernetes
 Multi-region Deployment
 Auto Scaling
 Distributed Workers
 GPU Inference Nodes
 Cloud Object Storage
 Package Registry Service
 Multi-Tenant Deployment
 AI Evaluation Cluster

---

# Summary

The deployment architecture of Psychology AI Lab is designed to provide a reliable and reproducible research environment while remaining flexible enough to scale into a production-grade evaluation platform.

By combining Flutter Web, FastAPI, PostgreSQL, Qdrant, Docker, and Nginx, the system separates presentation, application logic, relational storage, and vector search into independent services. This modular deployment model supports continuous AI research, rigorous benchmarking, and the controlled delivery of validated counseling packages into AIMindary.
