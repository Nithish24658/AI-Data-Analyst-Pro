import streamlit as st

def apply_glossy_ui():
    """Injects custom Glassmorphism CSS variables that adapt dynamically to Streamlit's menu choices."""
    st.markdown("""
        <style>
        /* 1. Use Streamlit's built-in global theme variables directly */
        .stApp {
            background: var(--background-color) !important;
            color: var(--text-color) !important;
            font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
        }

        /* 2. Force all standard labels, text blocks, and headers to match the adaptive text token */
        .stApp p, .stApp span, .stApp label, .stApp h1, .stApp h2, .stApp h3 {
            color: var(--text-color) !important;
        }

        /* 3. Adapting Input Form Fields Text Color dynamically */
        .stTextInput input {
            background: rgba(128, 128, 128, 0.08) !important;
            border: 1px solid rgba(128, 128, 128, 0.2) !important;
            color: var(--text-color) !important;
            border-radius: 12px !important;
            padding: 12px 16px !important;
        }
        .stTextInput input:focus {
            border-color: #06b6d4 !important;
            box-shadow: 0 0 12px rgba(6, 182, 212, 0.2) !important;
        }

        /* 4. Glassmorphism Navigation Tabs Line Layout Row */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background: rgba(128, 128, 128, 0.06) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(128, 128, 128, 0.15) !important;
            padding: 8px 16px !important;
            border-radius: 16px !important;
            margin-bottom: 24px;
        }

        /* 5. Inactive navigation text elements opacity balance */
        .stTabs [data-baseweb="tab"] {
            color: var(--text-color) !important;
            opacity: 0.6;
            border-radius: 10px !important;
            padding: 8px 16px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            font-weight: 600 !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            opacity: 1 !important;
            background: rgba(128, 128, 128, 0.1) !important;
        }

        /* 6. Active Focus Tab Highlighting Element */
        .stTabs [aria-selected="true"] {
            opacity: 1 !important;
            color: #06b6d4 !important; 
            background: rgba(6, 182, 212, 0.12) !important;
            border: 1px solid rgba(6, 182, 212, 0.4) !important;
            box-shadow: 0 0 16px rgba(6, 182, 212, 0.2) !important;
        }

        /* 7. Frosted Glass Status Notifications and Metric Cards */
        div[data-testid="stMetric"], div[data-testid="stNotification"], .stAlert {
            background: rgba(128, 128, 128, 0.04) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border: 1px solid rgba(128, 128, 128, 0.15) !important;
            border-radius: 20px !important;
            padding: 20px !important;
            box-shadow: 0 8px 24px 0 rgba(0, 0, 0, 0.05) !important;
        }

        /* 8. Glowing Call-To-Action Operations Buttons */
        .stButton > button {
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.2) 0%, rgba(59, 130, 246, 0.2) 100%) !important;
            color: var(--text-color) !important;
            border: 1px solid rgba(6, 182, 212, 0.5) !important;
            border-radius: 12px !important;
            padding: 10px 24px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
        }
        .stButton > button:hover {
            border-color: #06b6d4 !important;
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.3) !important;
        }
        </style>
    """, unsafe_allow_html=True)
