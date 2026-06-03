# AI-Powered Investor Intelligence Platform

> End-to-end Financial Document Intelligence Platform using Azure OpenAI, Azure AI Search, Azure SQL, FastAPI, React and AKS.

---

## Project Goal

Build an enterprise-grade application capable of:

* Processing financial reports
* Extracting key financial insights
* Generating analytics dashboards
* Supporting RAG-based financial research
* Deploying to Azure Kubernetes Service (AKS)

---

## Phase 1: Project Planning

Status: Completed

Activities:

* Selected Financial Statement Analysis as the use case.
* Chose annual reports as the primary data source.
* Selected Tesla, Apple and Microsoft annual reports.
* Defined RAG + Dashboard architecture approach.
* Decided to build an Investor Intelligence Platform instead of a chatbot.

---

## Phase 2: Dataset Preparation

Status: Completed

Activities:

* Downloaded annual reports.
* Stored PDF files under:

```text
data/raw_pdfs/
```

* Selected publicly available investor reports.

---

## Phase 3: PDF to Markdown Conversion

Status: Completed

Module:

```text
ingestion/pdf_to_markdown.py
```

Objective:

Convert annual report PDFs into markdown format suitable for downstream LLM processing.

Library:

```text
PyMuPDF4LLM
```

Output:

```text
data/markdown/
```

---

## Phase 4: Semantic Chunking

Status: In Progress

Module:

```text
chunking/semantic_chunker.py
```

Objective:

Generate semantically meaningful chunks from markdown documents.

Library:

```text
LangChain SemanticChunker
```

Embedding Model:

```text
Azure OpenAI Embeddings
```

Output:

```text
Document Chunks
```

---

## Phase 5: Azure OpenAI Integration

Status: Pending

Module:

```text
llm/azure_openai.py
```

Objective:

Centralize Azure OpenAI configuration and model initialization.

Deliverables:

* Embedding Model Configuration
* GPT Model Configuration
* Azure OpenAI Client

---

## Phase 6: Azure AI Search Integration

Status: Pending

Module:

```text
vectorstore/azure_ai_search.py
```

Objective:

Store document chunks and embeddings for retrieval.

Deliverables:

* Create Index
* Upload Chunks
* Vector Search
* Metadata Filtering

---

## Phase 7: KPI Extraction

Status: Pending

Module:

```text
extraction/kpi_extractor.py
```

Objective:

Extract financial KPIs using Retrieval-Augmented Generation (RAG).

KPIs:

* Revenue
* Net Income
* Cash Flow
* Debt
* Operating Margin

Output:

```text
Structured Financial Metrics
```

---

## Phase 8: Azure SQL Integration

Status: Pending

Module:

```text
database/azure_sql.py
```

Objective:

Store extracted KPI data for dashboard consumption.

Output:

```text
Financial Metrics Database
```

---

## Phase 9: FastAPI Backend

Status: Pending

Objective:

Expose APIs for application functionality.

Endpoints:

* Upload Documents
* Dashboard Data
* Company Comparison
* AI Research

---

## Phase 10: React Frontend

Status: Pending

Pages:

### Dashboard

Display:

* Revenue
* Net Income
* Cash Flow
* Debt
* Documents Processed

### Company Comparison

Display:

* Company-to-Company Financial Comparisons
* Revenue Trends
* Profit Trends

### AI Research

Support financial report research through RAG.

Example Questions:

* Why did revenue increase?
* What are the major risks?
* What acquisitions were discussed?
* Compare AI investments across companies.

---

## Phase 11: RAG Research Pipeline

Status: Pending

Module:

```text
rag/rag_pipeline.py
```

Objective:

Retrieve relevant chunks and generate grounded financial insights.

Components:

* Retriever
* Prompt Builder
* GPT Response Generator

---

## Phase 12: Containerization

Status: Pending

Deliverables:

* Backend Docker Image
* Frontend Docker Image
* Docker Compose Configuration

---

## Phase 13: AKS Deployment

Status: Pending

Deliverables:

* Kubernetes Deployment
* Services
* Ingress
* Production Validation

---

## Final Deliverable

AI-Powered Investor Intelligence Platform

Capabilities:

* Financial Report Processing
* Semantic Search
* KPI Extraction
* Dashboard Analytics
* Company Comparison
* RAG-Based Financial Research
* Cloud-Native Deployment
