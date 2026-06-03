# AI-Powered Investor Intelligence Platform

This repository contains a frontend React application and a Python backend for ingestion, vector search, KPI extraction, RAG, and Azure OpenAI integration.

## Project Structure

- `frontend/` - React application
- `backend/` - Python API and processing pipelines
- `data/` - raw PDFs and converted Markdown documents
- `config/` - shared configuration files
- `docker/` - Dockerfiles and Docker Compose setup

## Getting Started

1. Configure settings in `config/settings.yaml`.
2. Install frontend dependencies with `npm install` in `frontend/`.
3. Install backend dependencies and run `uvicorn backend.main:app --reload`.
4. Start Docker compose with `docker-compose -f docker/docker-compose.yml up --build`.
