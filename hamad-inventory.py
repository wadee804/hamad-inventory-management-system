import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Inventory Management | Hamad Yasin",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM PROFESSIONAL CSS ---
st.markdown("""
    <style>
    /* Main Background and Text */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header Styling */
    .main-header {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #1E3A8A;
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid #1E3A8A;
        margin-bottom: 30px;
    }

    /* Professional Sidebar */
    .css-1d391kg {
        background-color: #1E3A8A !important;
    }
    
    /* Blinking Footer with Ownership */
    @keyframes blinker {
        50% { opacity: 0; }
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #ffffff;
        color: #1E3A8A;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        border-top: 1px solid #e5e7eb;
        z-index: 100;
    }
    .blinking {
        animation: blinker 1.5s linear infinite;
        color: #ef4444;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR / OWNERSHIP ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/inventory-flow.png", width=80)
    st.title("Admin Panel")
    st.markdown("---")
    st.header("🔗 Data Connection")
    uploaded_file = st.file_uploader("Upload Inventory (Excel/CSV)", type=["xlsx", "csv"])
    st.markdown("---")
    st.info("💡 **Ownership:** This system is privately owned and maintained by Hamad Yasin.")

# --- MAIN INTERFACE ---
st.markdown("<h1 class='main-header'>📦 Product Inventory Analytics Dashboard</h1>", unsafe_allow_html=True)

if uploaded_file is not None:
    try:
        # Load Data
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Dashboard Metrics (Summary Cards)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Articles", len(df))
        with col2:
            # Check if 'Total Stock' column exists for analytics
            total_stock_val = df['Total Stock'].sum() if 'Total Stock' in df.columns else "N/A"
            st.metric("Total Inventory Stock", total_stock_val)
        with col3:
             st.metric("Status", "Active", delta="Synced")

        st.markdown("### 🔍 Search Engine")
        search_query = st.text_input("", placeholder="Enter Article Code (SKU), Color, or Category...")

        # Processing Search Logic
        if search_query:
            filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
            
            st.subheader(f"📊 Results for: '{search_query}'")
            if not filtered_df.empty:
                st.dataframe(filtered_df, use_container_width=True)
                
                # Export functionality for the filtered list
                csv = filtered_df.to_csv(index=False).encode('utf-8')
                st.download_button("📩 Download Search Result (CSV)", data=csv, file_name=f"Search_{search_query}.csv", mime='text/csv')
            else:
                st.warning("⚠️ No records found matching your query.")
        else:
            st.subheader("📋 Complete Inventory Overview")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    # Professional Welcome Screen
    st.markdown("""
        <div style='text-align: center; padding: 50px; border: 2px dashed #cbd5e1; border-radius: 15px; background: white;'>
            <h2 style='color: #64748b;'>Welcome to the Inventory Portal</h2>
            <p style='color: #94a3b8;'>Please upload your product database from the sidebar to begin searching.</p>
        </div>
    """, unsafe_allow_html=True)

# --- BLINKING FOOTER ---
st.markdown(f"""
    <div class='footer'>
        Developed with ❤️ By <span class='blinking'>Hamad Yasin</span> | © 2026 All Rights Reserved
    </div>
    """, unsafe_allow_html=True)