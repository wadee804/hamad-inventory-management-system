import streamlit as st
import pandas as pd

# --- ENTERPRISE CONFIGURATION ---
st.set_page_config(
    page_title="Inventory Management System | Hamad Yasin",
    page_icon="💼",
    layout="wide"
)

# --- CLEAN BUSINESS UI STYLING ---
st.markdown("""
    <style>
    /* Global Reset */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Professional Header */
    .header-section {
        background-color: #161b22;
        padding: 40px 20px;
        border-radius: 12px;
        border-bottom: 3px solid #30363d;
        margin-bottom: 30px;
        text-align: center;
    }
    .header-title {
        color: #f0f6fc;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .header-subtitle {
        color: #8b949e;
        font-size: 30px;
        margin-top: 8px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #010409 !important;
        border-right: 1px solid #30363d;
    }

    /* Metric Cards - Minimalist */
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
    }

    /* Professional Search Input */
    .stTextInput>div>div>input {
        background-color: #0d1117 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        border-radius: 8px;
        padding: 12px;
    }
    .stTextInput>div>div>input:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 8px rgba(88, 166, 255, 0.2);
    }

    /* Corporate Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #161b22;
        color: #8b949e;
        text-align: center;
        padding: 12px 0;
        font-size: 0.85rem;
        border-top: 1px solid #30363d;
        z-index: 999;
    }
    .footer b {
        color: #58a6ff;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Clean Table View */
    .stDataFrame {
        border: 1px solid #30363d;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: SYSTEM CONTROLS ---
with st.sidebar:
    st.markdown("<h3 style='color: white;'>Control Panel</h3>", unsafe_allow_html=True)
    st.markdown("---")
    uploaded_file = st.file_uploader("Upload Inventory File (Excel/CSV)", type=["xlsx", "csv"])
    
    st.markdown("<br><br>" * 6, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<p style='text-align:center; font-size:12px; color:#484f58;'>Enterprise Edition v3.0</p>", unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
st.markdown("""
    <div class="header-section">
        <h1 class="header-title">Product Inventory System</h1>
        <p class="header-subtitle">Centralized Asset Management & Real-time Stock Tracking</p>
    </div>
""", unsafe_allow_html=True)

if uploaded_file is not None:
    try:
        # Load Data
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Executive Metrics Grid
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Total Articles", len(df))
        with m2:
            st.metric("System Health", "Good")
        with m3:
            st.metric("Last Updated", pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"))
        st.markdown("<br>", unsafe_allow_html=True)

        # Search Interface
        st.markdown("#### Search Inventory")
        search_query = st.text_input("", placeholder="Enter SKU, Color, or Product Name to filter database...")

        if search_query:
            # Original search logic from your code
            filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
            
            if not filtered_df.empty:
                st.markdown(f"**Found {len(filtered_df)} items matching your request.**")
                st.dataframe(filtered_df, use_container_width=True)
                
                # Report Download
                csv = filtered_df.to_csv(index=False).encode('utf-8')
                st.download_button("Download Search Results", data=csv, file_name=f"Inventory_Report_{search_query}.csv", mime='text/csv')
            else:
                st.warning("No records found for the given search criteria.")
        else:
            st.markdown("#### Master Database Feed")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
else:
    # Clean Initial State
    st.markdown("""
        <div style='text-align: center; padding: 100px; border: 1px dashed #30363d; border-radius: 12px; background: #161b22; margin-top: 20px;'>
            <h3 style='color: #8b949e;'>System Offline</h3>
            <p style='color: #484f58;'>Please upload an inventory spreadsheet from the sidebar to activate the dashboard.</p>
        </div>
    """, unsafe_allow_html=True)

# --- PROFESSIONAL FOOTER ---
st.markdown("""
    <div class="footer">
        DESIGNED & DEVELOPED BY <b>HAMAD YASIN</b> | &copy; 2026 PRIVATE ENTERPRISE LICENSE
    </div>
    """, unsafe_allow_html=True)
