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
        
        # 1. Import BOTH functions from the package
        try:
            from streamlit_mic_recorder import speech_to_text
        except Exception:
            speech_to_text = None
            st.warning("Optional dependency `streamlit_mic_recorder` not available — voice input disabled.")

        st.write("🎙️ **Option A: Speak your question**")

        # Initialize query tracking buckets in session state memory
        if 'sql_view_query' not in st.session_state:
            st.session_state['sql_view_query'] = ""
        if 'sql_view_data' not in st.session_state:
            st.session_state['sql_view_data'] = None

        # Use the correct speech_to_text function to convert voice to text instantly
        if speech_to_text:
            try:
                spoken_text = speech_to_text(
                    start_prompt="Click to start speaking ⏺️",
                    stop_prompt="Stop recording ⏹️",
                    language='en',
                    key="mic_stt"
                )
            except Exception:
                spoken_text = ""
                st.warning("Voice capture failed — please use the text input.")
        else:
            spoken_text = ""

        # If voice text is captured, immediately pass it to the SQL pipeline
        if spoken_text:
            st.success(f"Captured Audio: *\"{spoken_text}\"*")
            with st.spinner("AI writing SQL query from voice input..."):
                gen_sql, sql_res = analyze_sql_database(db_filename, spoken_text)
                st.session_state['sql_view_query'] = gen_sql
                st.session_state['sql_view_data'] = sql_res

        st.write("✍️ **Option B: Type your question**")

        # Pre-fill typing input if voice text was captured
        default_value = spoken_text if spoken_text else ""
        sql_query = st.text_input(
            "Ask a structured question:", 
            value=default_value,
            key="sql_input"
        )
        
        # Run manual button update
        if st.button("Run SQL Generation Pipeline", key="btn_sql"):
            if sql_query:
                with st.spinner("AI writing SQL query, executing schema scan, and fetching records..."):
                    gen_sql, sql_res = analyze_sql_database(db_filename, sql_query)
                    st.session_state['sql_view_query'] = gen_sql
                    st.session_state['sql_view_data'] = sql_res
            else:
                st.warning("Please enter or speak an operational data question.")
                
        # --- RENDERING ENGINE: Displays the output data grid ---
        if st.session_state['sql_view_query']:
            st.write(f"**Generated SQL Query:** `{st.session_state['sql_view_query']}`")
            st.write("### 🛢️ Live SQL Query Pipeline Result:")
            
            if isinstance(st.session_state['sql_view_data'], pd.DataFrame):
                st.dataframe(st.session_state['sql_view_data'], use_container_width=True)
            else:
                st.error(f"Execution Error: {st.session_state['sql_view_data']}")
