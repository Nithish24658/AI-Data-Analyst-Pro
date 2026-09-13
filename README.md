# 🤖 AI Data Analyst Pro

> A local, privacy-first AI analytics workspace for exploring datasets, generating insights, automating SQL, and producing executive-ready analysis.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/) [![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C)](https://www.langchain.com/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Why this project?

AI Data Analyst Pro demonstrates how modern analytics workflows can be combined into one local application. A user can upload a CSV, profile its structure, ask natural-language questions, generate visualizations, run SQL-style analysis, and request a higher-level business interpretation.

The project is intentionally designed around a **local-first workflow**, using Ollama for the language model so that uploaded analytical data does not need to be sent to a hosted LLM service by default.

## ✨ Core capabilities

| Capability | What it demonstrates |
|---|---|
| 💬 Chat with Data | Natural-language questions translated into pandas-based analysis |
| 📊 Dataset Profiling | Schema, row/column counts, missing values, unique values, and previews |
| 👥 Multi-Agent Analysis | Technical/statistical analysis followed by business-oriented interpretation |
| 🗄️ Text-to-SQL | CSV → SQLite conversion and natural-language SQL analysis |
| 🎙️ Voice Queries | Optional speech-to-text input for SQL questions |
| 📈 Visualization | Python/Matplotlib charts generated from analytical requests |
| 🔒 Local LLM | Ollama-powered inference for a privacy-conscious workflow |

## 🧠 Architecture

```text
                         ┌──────────────────────┐
                         │     Streamlit UI     │
                         └──────────┬───────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
       ┌─────────────┐       ┌──────────────┐      ┌──────────────┐
       │ Chat Agent │       │ Data Profiler│      │ SQL Engine   │
       └──────┬──────┘       └──────────────┘      └──────┬───────┘
              │                                            │
              ▼                                            ▼
       ┌─────────────┐                              ┌──────────────┐
       │ Ollama LLM  │                              │   SQLite     │
       └──────┬──────┘                              └──────────────┘
              │
              ▼
       ┌─────────────┐
       │ Multi-Agent │
       │  Business   │
       │ Interpretation│
       └─────────────┘
```

## 🛠️ Tech stack

- **Python** — application and analytics logic
- **Streamlit** — interactive web interface
- **Pandas** — data manipulation and profiling
- **Matplotlib** — analytical visualization
- **SQLite3** — relational analytics layer
- **LangChain Community** — LLM integration/orchestration
- **Ollama** — local LLM runtime
- **Optional:** `streamlit-mic-recorder` for voice input

## 📁 Project structure

```text
AI-Data-Analyst-Pro/
├── app.py                 # Streamlit application entry point
├── agent.py               # Chat-with-data analysis agent
├── crew_agent.py          # Multi-agent business analysis pipeline
├── sql_agent.py           # CSV → SQLite and text-to-SQL workflow
├── style.py               # Custom application styling
├── requirements.txt       # Python dependencies
├── .gitignore             # Local/runtime files excluded from Git
└── README.md              # Project documentation
```

## 🚀 Run locally

### 1. Clone

```bash
git clone https://github.com/Nithish24658/AI-Data-Analyst-Pro.git
cd AI-Data-Analyst-Pro
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama and pull the local model

```bash
ollama run llama3.2:1b
```

### 5. Launch the app

```bash
streamlit run app.py
```

## 🔐 Data & security notes

- Uploaded CSVs are processed locally by the application.
- Runtime database files and temporary datasets are excluded through `.gitignore`.
- Do **not** commit credentials, API keys, private datasets, or `.streamlit/secrets.toml`.
- This project is a portfolio/academic application; production deployments should add authentication, stronger sandboxing, input validation, logging, and resource limits.

## 📌 Portfolio value

This project showcases practical skills across **Data Analytics, Python, SQL, Business Intelligence, LLM applications, data profiling, visualization, and analytics automation** rather than demonstrating a single isolated model.

## 👤 Author

**Nithishsaran KM** — M.Sc. Data Science | Data Analytics | Python | SQL | Power BI | Machine Learning

GitHub: [@Nithish24658](https://github.com/Nithish24658)

---

⭐ If this project helps you, consider starring the repository.