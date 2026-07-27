# 🤖 Local Glassmorphism AI Data Analyst Platform

A premium, production-ready, multi-agent AI Data Analyst platform built to automate data processing pipelines securely, locally, and completely for free. 

The application features a modern **Glassmorphic / Frosted-Glass UI theme** that automatically adapts dynamically between Light and Dark mode options.

---

## 🚀 Visual Core Architectures

### 1. 💬 Chat with Data Agent
- **Engine**: LangChain + Local `llama3.2:1b` model.
- **Capability**: Safely writes native Python `pandas` manipulation queries in a localized memory sandbox to answer structural queries and build visualizations.

### 2. 📊 Automated Dataset Profiling
- **Engine**: Native Pandas Profiler.
- **Capability**: Instantly parses massive uploaded CSV records upon landing to map out shape variables, missing elements, data schemas, and primary row previews.

### 3. 👥 Strategic Multi-Agent Pipeline
- **Engine**: Custom Python Sequential Multi-Agent orchestration.
- **Role A (Senior Data Scientist)**: Handles mathematical validation and statistical summaries.
- **Role B (BI Manager)**: Translates raw technical findings into beautiful executive summaries with bulleted text reports.

### 4. 🗄️ Real-Time SQL Query Automation Engine
- **Engine**: Python Native SQLite3 Relational Database Engine.
- **Capability**: Converts incoming files into relational database schemas instantly. Includes a **Few-Shot Prompting framework** for rapid text-to-SQL compile routines without hallucination lags.

---

## 🛠️ High-Performance Tech Stack

- **UI Interface**: Streamlit Platform (HTML5/Custom CSS Injection).
- **Orchestration Framework**: LangChain Community Ecosystem.
- **Local LLM Engine**: Ollama Backend Framework (`llama3.2:1b`).
- **Data Engineering Foundations**: Pandas DataFrames, SQLite3 Relational Architecture.

---

## 💻 Step-by-Step Local Deployment Guide

### 1. Initialize Local Model Engines
Ensure Ollama is running actively on your machine, then open terminal/PowerShell and download the lightweight 1B model:
```bash
ollama run llama3.2:1b
```

### 2. Install Project Dependencies
Run the installation setup pipeline inside your active Python virtual environment terminal:
```bash
pip install streamlit pandas matplotlib langchain-community langchain-experimental
```

### 3. Launch the Application Platform
Execute the command pipeline to fire up your local browser portal dashboard link:
```bash
streamlit run app.py
```
