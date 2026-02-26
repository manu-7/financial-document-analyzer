# Financial Document Analyzer

## Project Overview

This project is an AI-powered financial document analysis system built using FastAPI and CrewAI. It processes uploaded financial PDFs and generates structured financial analysis using multi-agent orchestration.

---

## Bugs Identified and Fixed

During debugging, the following issues were identified and resolved:

### 1. Module Name Collision
- `agents.py` conflicted with an installed `agents` package.
- Renamed to `finance_agents.py`.

### 2. Undefined PDF Loader
- `Pdf` class was used but never imported.
- Replaced with `PyPDFLoader` from `langchain_community`.

### 3. Async Tool Misuse
- Tools were defined as `async` but not awaited.
- Converted to synchronous functions.

### 4. Missing LLM Configuration
- Agents were initialized without attaching an LLM.
- Integrated Groq LLM via CrewAI.

### 5. Model Deprecation
- Original Groq model was decommissioned.
- Updated to `llama-3.1-8b-instant`.

### 6. Token Limit Error
- Entire PDF exceeded Groq free-tier token limits.
- Implemented safe truncation to avoid overflow.

---

## Architecture

- FastAPI REST API
- CrewAI multi-agent orchestration
- Groq LLM integration
- PDF parsing via LangChain

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-link>
cd financial-document-analyzer