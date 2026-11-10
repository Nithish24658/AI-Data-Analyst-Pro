
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from style import apply_glossy_ui
from data_engine import profile_dataset


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="wide"
)

apply_glossy_ui()

st.title("🤖 Your Automated AI Data Analyst")

st.caption(
    "An offline-first data analytics and business intelligence platform."
)


# --------------------------------------------------
# 2. DATA UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your business dataset",
    type=["csv"],
    help="Upload a CSV file to explore its data and generate insights."
)


if uploaded_file is not None:

    try:
        # Read uploaded dataset
        df = pd.read_csv(uploaded_file)

        if df.empty:
            st.error("The uploaded dataset is empty.")
            st.stop()

        # Preserve uploaded data for existing modules
        df.to_csv("temp_data.csv", index=False)

        st.success("Dataset uploaded successfully!")

        # Dataset information
        st.caption(
            f"File: {uploaded_file.name} | "
            f"Size: {uploaded_file.size / 1024:.2f} KB"
        )

        # --------------------------------------------------
        # 3. GENERATE VERIFIED DATA PROFILE
        # --------------------------------------------------

        profile = profile_dataset(df)

        overview = profile["dataset_overview"]

        # --------------------------------------------------
        # 4. APPLICATION TABS
        # --------------------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs([
            "💬 Chat with Data",
            "📊 Automated Profile Report",
            "👥 Executive Multi-Agent Crew",
            "🗄️ SQL Database Engine"
        ])


        # --------------------------------------------------
        # TAB 1: CHAT WITH DATA
        # --------------------------------------------------

        with tab1:

            st.subheader("💬 Chat with Your Dataset")

            st.info(
                "Natural-language analytics is temporarily "
                "under development. We are replacing unrestricted "
                "AI-generated Python execution with a validated "
                "analytics engine."
            )

            st.text_input(
                "Ask a question about your dataset:",
                placeholder="Example: What is the average purchase amount?",
                disabled=True,
                key="chat_question"
            )

            st.button(
                "Analyze",
                disabled=True,
                key="chat_analyze"
            )


        # --------------------------------------------------
        # TAB 2: AUTOMATED PROFILE REPORT
        # --------------------------------------------------

        with tab2:

            st.subheader("📑 Full Automated Dataset Insights")

            # Dataset overview
            st.write("### 📌 Dataset Overview")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Records",
                overview["total_rows"]
            )

            col2.metric(
                "Total Columns",
                overview["total_columns"]
            )

            col3.metric(
                "Missing Values",
                overview["total_missing_values"]
            )

            col4.metric(
                "Duplicate Rows",
                overview["duplicate_rows"]
            )


            # --------------------------------------------------
            # DATA SCHEMA AND QUALITY
            # --------------------------------------------------

            st.divider()

            st.write("### 🔍 Data Schema & Quality Overview")

            schema_df = pd.DataFrame(
                profile["column_details"]
            )

            st.dataframe(
                schema_df,
                use_container_width=True,
                hide_index=True
            )


            # --------------------------------------------------
            # NUMERICAL ANALYSIS
            # --------------------------------------------------

            st.divider()

            st.write("### 📊 Numerical Analysis")

            numeric_summary = profile["numeric_summary"]

            if numeric_summary:

                numeric_df = pd.DataFrame.from_dict(
                    numeric_summary,
                    orient="index"
                )

                numeric_df.index.name = "Column"

                st.dataframe(
                    numeric_df,
                    use_container_width=True
                )

            else:

                st.info(
                    "No numerical columns were found "
                    "in this dataset."
                )


            # --------------------------------------------------
            # CATEGORICAL ANALYSIS
            # --------------------------------------------------

            st.divider()

            st.write("### 📌 Categorical Analysis")

            categorical_summary = profile[
                "categorical_summary"
            ]

            if categorical_summary:

                for column, distribution in (
                    categorical_summary.items()
                ):

                    st.write(f"**{column}**")

                    category_df = pd.DataFrame(
                        list(distribution.items()),
                        columns=["Category", "Count"]
                    )

                    st.dataframe(
                        category_df,
                        use_container_width=True,
                        hide_index=True
                    )

            else:

                st.info(
                    "No categorical columns were found."
                )


            # --------------------------------------------------
            # DATA QUALITY FINDINGS
            # --------------------------------------------------

            st.divider()

            st.write("### ⚠️ Data Quality Findings")

            # Missing values
            missing_columns = [
                item
                for item in profile["column_details"]
                if item["missing_count"] > 0
            ]

            if missing_columns:

                st.warning("Missing values detected:")

                missing_df = pd.DataFrame(
                    missing_columns
                )

                st.dataframe(
                    missing_df[
                        [
                            "column_name",
                            "missing_count",
                            "missing_percentage"
                        ]
                    ],
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.success("No missing values found.")


            # Duplicate records
            if overview["duplicate_rows"] > 0:

                st.warning(
                    f"Found {overview['duplicate_rows']} "
                    "duplicate records."
                )

            else:

                st.success("No duplicate records found.")


            # Duplicate column names
            if profile["duplicate_columns"]:

                st.warning(
                    "Duplicate column names detected: "
                    + ", ".join(
                        profile["duplicate_columns"]
                    )
                )

            else:

                st.success("No duplicate column names found.")


            # Constant columns
            if profile["constant_columns"]:

                st.warning(
                    "Constant columns detected: "
                    + ", ".join(
                        profile["constant_columns"]
                    )
                )

            else:

                st.success("No constant columns found.")


            # --------------------------------------------------
            # DATASET PREVIEW
            # --------------------------------------------------

            st.divider()

            st.write("### 📋 First 5 Rows Preview")

            st.dataframe(
                df.head(),
                use_container_width=True
            )

            # Full dataset download
            st.download_button(
                label="📥 Download Dataset",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="processed_dataset.csv",
                mime="text/csv"
            )


        # --------------------------------------------------
        # TAB 3: EXECUTIVE MULTI-AGENT CREW
        # --------------------------------------------------

        with tab3:

            st.subheader(
                "👥 Strategic Multi-Agent Analysis"
            )

            st.info(
                "The multi-agent analysis module is temporarily "
                "under development. It will be re-enabled after "
                "we connect it to verified statistical results."
            )

            st.text_input(
                "Enter a business question:",
                placeholder="Example: What are the main customer trends?",
                disabled=True,
                key="crew_question"
            )

            st.button(
                "Activate Team Breakdown",
                disabled=True,
                key="crew_button"
            )


        # --------------------------------------------------
        # TAB 4: SQL DATABASE ENGINE
        # --------------------------------------------------

        with tab4:

            st.subheader(
                "🗄️ Natural Language to SQL Analytics"
            )

            st.info(
                "The SQL module is temporarily under development. "
                "We will implement read-only SQL validation, "
                "query restrictions and execution safeguards "
                "before enabling it."
            )

            st.text_input(
                "Ask a database question:",
                placeholder="Example: Show the top 5 customers",
                disabled=True,
                key="sql_question"
            )

            st.button(
                "Run SQL Analysis",
                disabled=True,
                key="sql_button"
            )


    except pd.errors.EmptyDataError:

        st.error(
            "The uploaded CSV file does not contain any data."
        )

    except pd.errors.ParserError:

        st.error(
            "Unable to read this CSV file. "
            "Please check its formatting."
        )

    except Exception as error:

        st.error(
            f"An error occurred while processing the dataset: {error}"
        )


else:

    st.info(
        "Please upload a CSV dataset to start your analysis."
    )

    st.markdown(
        """
        ### Available capabilities

        - Automated dataset profiling
        - Missing-value detection
        - Duplicate-record identification
        - Numerical statistical analysis
        - Categorical distribution analysis
        - Data-quality reporting
        """
    )
