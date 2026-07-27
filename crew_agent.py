import pandas as pd
from langchain_community.llms import Ollama

# Initialize the lightweight code model
llm = Ollama(model="qwen2.5-coder:1.5b", temperature=0)

def run_team_analysis(file_path, user_question):
    df = pd.read_csv(file_path)
    columns_info = list(df.columns)
    
    # Pass a dense summary snapshot to ensure rapid processing speeds
    data_summary_profile = f"Rows: {df.shape[0]}, Cols: {df.shape[1]}. Columns: {columns_info}"
    
    scientist_prompt = f"""
    You are a Data Scientist. Dataset Context: {data_summary_profile}. 
    Answer this question using brief statistical facts: {user_question}
    """
    st_math_findings = llm.invoke(scientist_prompt)
    
    manager_prompt = f"""
    You are a BI Manager. Take these findings: {st_math_findings}
    Convert them into a short bulleted executive report for leadership.
    """
    final_executive_report = llm.invoke(manager_prompt)
    return final_executive_report
