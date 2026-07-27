import os
import pandas as pd
import matplotlib.pyplot as plt
from langchain_community.llms import Ollama

# Hardware-optimized model call
llm = Ollama(model="qwen2.5-coder:1.5b", temperature=0)

def analyze_data(file_path, user_query):
    """Executes pre-formatted python data analytics pipelines instantly."""
    df = pd.read_csv(file_path)
    columns_info = list(df.columns)
    
    # Highly constrained prompt that forces immediate termination after the script
    prompt = f"""You are a strict Python compiler. Convert the user request into raw Python pandas code.
DataFrame Name: `df`
Available Columns: {columns_info}

CRITICAL RULES:
1. Output ONLY the raw executable Python lines. No markdown blocks, no text explanations.
2. Do NOT use any introductory or concluding text. Stop generating immediately when the script ends.

EXAMPLE PATTERN:
Request: "How many records are there?"
Code: print(len(df))

User Request: "{user_query}"
Code:"""
    
    # Run the high-speed single pass call
    generated_code = llm.invoke(prompt).strip()
    
    # Clean any accidental markdown artifacts safely
    if "```" in generated_code:
        generated_code = generated_code.replace("```python", "").replace("```", "").strip()
        
    # Redirect standard output stream to capture print statements
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        # Execute the python script in a protected local namespace
        local_vars = {"df": df, "plt": plt, "pd": pd}
        exec(generated_code, globals(), local_vars)
        
        sys.stdout = old_stdout
        output_text = redirected_output.getvalue().strip()
        
        if not output_text:
            output_text = "Analysis completed. (Visualization generated if requested)."
            
        return output_text
    except Exception as e:
        sys.stdout = old_stdout
        return f"Execution Error: {str(e)}\n\nGenerated Code:\n`{generated_code}`"
