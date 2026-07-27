import streamlit as st
import os
import time  # Fixed: Added the missing native tracking package!
import pandas as pd
import matplotlib.pyplot as plt
from agent import analyze_data
from crew_agent import run_team_analysis
from sql_agent import convert_csv_to_sqlite, analyze_sql_database
from style import apply_glossy_ui 

# Initialize page settings
st.set_page_config(page_title="AI Data Analyst", layout="wide")

# Apply the premium frosted glass UI theme style
apply_glossy_ui()

st.title("🤖 Your Automated AI Data Analyst")

# File Upload Section
uploaded_file = st.file_uploader("Upload your data (CSV format)", type=["csv"])

if uploaded_file is not None:
    with open("temp_data.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("Data uploaded successfully!")
    
    # Setup our local background SQL database automatically
    db_filename = "local_company.db"
    convert_csv_to_sqlite("temp_data.csv", db_filename)
    
    # Operational multi-tabs setup with correct single variable index handling
    tab1, tab2, tab3, tab4 = st.tabs([
        "💬 Chat with Data", 
        "📊 Automated Profile Report", 
        "👥 Executive Multi-Agent Crew",
        "🗄️ SQL Database Engine"
    ])
    
    with tab1:
        user_query = st.text_input("Ask a question or request a chart:", key="tab1_q")
        if st.button("Analyze", key="btn_single"):
            if user_query:
                plt.clf()
                plt.close('all')
                with st.spinner("Analyzing data..."):
                    # Benchmark execution run time
                    start_time = time.time()
                    result = analyze_data("temp_data.csv", user_query)
                    end_time = time.time()
                    
                    st.write("### 📊 Analysis Result:")
                    st.write(result)
                    st.caption(f"⚡ Analysis processed in {end_time - start_time:.2f} seconds.")
                    
                    # Safely render charts if any were generated in memory
                    fig = plt.gcf()
                    if fig and fig.axes:
                        st.write("### 📈 Generated Visualization:")
                        st.pyplot(fig)
            else:
                st.warning("Please enter a question first.")
                
    with tab2:
        st.write("### 📑 Full Automated Dataset Insights")
        df = pd.read_csv("temp_data.csv")
        
        # Fixed: Explicitly parsing tuple values to protect from streamlit value crashes
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records (Rows)", df.shape[0])
        col2.metric("Total Attributes (Columns)", df.shape[1])
        col3.metric("Missing Values Found", int(df.isna().sum().sum()))
        
        st.write("#### 🔍 Data Schema Overview")
        schema_df = pd.DataFrame({
            "Data Type": df.dtypes.astype(str),
            "Non-Null Count": df.notna().sum(),
            "Unique Values": df.nunique()
        })
        st.dataframe(schema_df, use_container_width=True)
        
        st.write("#### 📋 First 5 Rows Preview")
        st.dataframe(df.head(), use_container_width=True)
        
    with tab3:
        st.write("### 👥 Strategic Multi-Agent Execution Pipeline")
        crew_query = st.text_input("What high-level business question should the expert team analyze?", key="crew_input")
        if st.button("Activate Team Breakdown", key="btn_crew"):
            if crew_query:
                with st.spinner("Processing framework pipeline..."):
                    crew_report = run_team_analysis("temp_data.csv", crew_query)
                    st.session_state['final_report'] = crew_report
            else:
                st.warning("Please enter a question for the team.")
        
        if 'final_report' in st.session_state:
            st.write("### 📜 Final Executive Report Summary:")
            st.write(st.session_state['final_report'])
            st.download_button(
                label="📥 Download Executive Report (.txt)",
                data=st.session_state['final_report'],
                file_name="AI_Executive_Analysis_Report.txt",
                mime="text/plain"
            )

    with tab4:
        st.write("### 🗄️ Real-Time SQL Query Automation Engine")
        st.info("The application has converted your file into a relational SQLite database table named: `customer_data`")
        
        sql_query = st.text_input(
            "Ask a structured question (The AI will write SQL syntax, query the database, and display it):", 
            key="sql_input"
        )
        
        if st.button("Run SQL Generation Pipeline", key="btn_sql"):
            if sql_query:
                with st.spinner("AI writing SQL query, executing schema scan, and fetching records..."):
                    generated_sql, sql_result = analyze_sql_database(db_filename, sql_query)
                    
                    st.write(f"**Generated SQL Query:** `{generated_sql}`")
                    st.write("### 🛢️ Live SQL Query Pipeline Result:")
                    
                    if isinstance(sql_result, pd.DataFrame):
                        st.dataframe(sql_result, use_container_width=True)
                    else:
                        st.error(f"Execution Error: {sql_result}")
            else:
                st.warning("Please enter an operational data question.")
