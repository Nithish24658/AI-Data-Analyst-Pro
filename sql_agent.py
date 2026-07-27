import os
import sqlite3
import pandas as pd
from langchain_community.llms import Ollama

# Connect to the local code specialist model
llm = Ollama(model="qwen2.5-coder:1.5b", temperature=0)

def convert_csv_to_sqlite(csv_path, db_path, table_name="customer_data"):
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(csv_path)
    df.columns = [c.replace(' ', '_').replace('.', '_') for c in df.columns]
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def analyze_sql_database(db_path, user_query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA table_info(customer_data);")
    columns_info = [row for row in cursor.fetchall()]
    
    # Rigid prompt featuring exact examples matching your column data types
    prompt = f"""You are a strict Text-to-SQL compiler for an SQLite database.
Table Name: customer_data
Available Columns: {columns_info}

Task: Convert the user's question into a single valid SQLite query string.

CRITICAL RULES:
1. Output ONLY the raw executable SQL query string. Do NOT include markdown code blocks (```), conversational commentary, or explanations.
2. If comparing two categories (e.g. "vs those without", "churned vs retained"), you MUST select the grouping column and use a GROUP BY clause. Do NOT filter down to one side using a WHERE clause.

GOLD STANDARD MATCHING EXAMPLES:
Question: "What is the average account length for churned customers vs those who stayed?"
SQL: SELECT Churn, AVG(Account_length) FROM customer_data GROUP BY Churn;

Question: "Show the average total day minutes for customers with a voice mail plan vs those without."
SQL: SELECT Voice_mail_plan, AVG(Total_day_minutes) FROM customer_data GROUP BY Voice_mail_plan;

User Question: "{user_query}"
SQL:"""
    
    generated_sql = llm.invoke(prompt).strip()
    
    # Strip stray markdown tags if they appear
    if "```" in generated_sql:
        generated_sql = generated_sql.replace("```sql", "").replace("```", "").strip()
        
    try:
        result_df = pd.read_sql_query(generated_sql, conn)
        conn.close()
        return generated_sql, result_df
    except Exception as e:
        conn.close()
        return generated_sql, f"SQL Execution Error: {str(e)}"
