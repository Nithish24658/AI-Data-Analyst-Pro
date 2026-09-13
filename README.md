# 🤖 AI Data Analyst Pro

> A local, privacy-first AI analytics workspace for exploring datasets, generating insights, automating SQL, and producing executive-ready analysis.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/) [![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C)](https://www.langchain.com/)

## 🎯 Why this project?

AI Data Analyst Pro combines practical analytics workflows into one local application. Upload a CSV, inspect its structure, ask natural-language questions, generate visualizations, run SQL-style analysis, and request an executive interpretation.

The application uses **Ollama for local LLM inference**, keeping the core analysis workflow local by default.

## ✨ Core capabilities

| Capability | What it demonstrates |
|---|---|
| 💬 Chat with Data | Natural-language questions translated into pandas-based analysis |
| 📊 Dataset Profiling | Schema, row/column counts, missing values, unique values, and previews |
| 👥 Multi-Agent Analysis | Technical analysis followed by business-oriented interpretation |
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
       │ Business    │
       │ Interpretation│
       └─────────────┘
```

## 🛠️ Tech stack

**Python · Streamlit · Pandas · Matplotlib · SQLite3 · LangChain Community · Ollama**

Optional voice input: `streamlit-mic-recorder`.

## 📁 Project structure

```text
AI-Data-Analyst-Pro/
├── app.py                 # Streamlit application entry point
├── agent.py               # Chat-with-data analysis agent
├── crew_agent.py          # Multi-agent business analysis pipeline
├── sql_agent.py           # CSV → SQLite and text-to-SQL workflow
├── style.py               # Custom application styling
├── requirements.txt       # Python dependencies
├── .gitignore             # Runtime/local files excluded from Git
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

### 4. Start the local LLM

The current application code uses the `qwen2.5-coder:1.5b` Ollama model:

```bash
ollama run qwen2.5-coder:1.5b
```

### 5. Launch the application

```bash
streamlit run app.py
```

## 🔐 Data & security notes

- Uploaded CSVs are processed locally by the application.
- Runtime database files and temporary datasets are excluded through `.gitignore`.
- Never commit credentials, API keys, private datasets, or `.streamlit/secrets.toml`.
- Before production deployment, add authentication, stronger code-execution sandboxing, input validation, logging, and resource limits.

## 📌 Portfolio value

This project demonstrates practical skills across **Data Analytics, Python, SQL, LLM applications, data profiling, visualization, and analytics automation**.

## 👤 Author

**Nithishsaran KM** — M.Sc. Data Science | Data Analytics | Python | SQL | Power BI | Machine Learning

GitHub: [@Nithish24658](https://github.com/Nithish24658)

---

⭐ If this project helps you, consider starring the repository.