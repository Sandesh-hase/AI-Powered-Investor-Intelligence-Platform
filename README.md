# AI-Powered Investor Intelligence Platform

<img width="1906" height="945" alt="RAGproject" src="https://github.com/user-attachments/assets/5024af81-e07e-47ed-a4ab-a40c439522f2" />

This repository contains the Python backend for an AI-powered Investor Intelligence Platform, including document ingestion, semantic search, KPI extraction, Azure AI Search integration, Azure OpenAI integration, and PostgreSQL-based KPI storage.

## Prerequisites

* Python 3.12+
* UV Package Manager

## Setup

### 1. Install UV

#### Windows

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### macOS/Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

---

### 2. Create Virtual Environment

```bash
uv venv
```

---

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file and configure all required environment variables before running the application.

---

### 6. Run the Application

```bash
python app.py
```

---

## Project Features

* Annual Report Upload & Processing
* KPI Extraction using Azure OpenAI
* Azure AI Search Integration
* Semantic Search & Retrieval
* RAG-based Chatbot
* PostgreSQL KPI Storage
* Investor Insights Dashboard
* Production-Grade Modular Architecture

---

## Technology Stack

### Backend

* FastAPI
* Python 3.12

### AI Services

* Azure OpenAI
* Azure AI Search

### Database

* Azure PostgreSQL

### Deployment

* Docker
* Azure Container Registry (ACR)
* Azure Kubernetes Service (AKS)

### Package Management

* UV

---

## Notes

* Ensure all Azure resources are configured before running the application.
* Verify that PostgreSQL firewall rules allow access from the application.
* Store secrets in environment variables and never commit `.env` files to source control.
* For production deployments, use Azure Key Vault or Kubernetes Secrets for secret management.
