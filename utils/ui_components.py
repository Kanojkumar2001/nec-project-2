import os
import pandas as pd
import streamlit as st
from utils.helper_functions import get_data_summary

def init_session_state():
    """Initializes standard session state variables for the application."""
    if "sales_df" not in st.session_state:
        st.session_state.sales_df = None
    if "processed_df" not in st.session_state:
        st.session_state.processed_df = None

def data_loader_sidebar(show_processed=False, key_prefix=""):
    """
    Renders sidebar controls to select the data source.
    Returns the selected pandas DataFrame, or None if no data is available.
    """
    st.sidebar.markdown("### 💾 Data Options")
    
    options = ["Sample Dataset"]
    
    # Check if user has uploaded a custom dataset or if database/sales_data files exist
    default_dataset_exists = os.path.exists("dataset/sales_data.csv")
    processed_dataset_exists = os.path.exists("dataset/processed_sales_data.csv")
    
    if default_dataset_exists:
        options.append("Default Dataset")
    if st.session_state.get("sales_df") is not None:
        options.append("Uploaded Dataset")
    if processed_dataset_exists:
        options.append("Processed Dataset")
    elif st.session_state.get("processed_df") is not None:
        options.append("Processed Dataset")
        
    # Decide default selection index
    default_idx = 0
    if show_processed and "Processed Dataset" in options:
        default_idx = options.index("Processed Dataset")
    elif not show_processed and "Default Dataset" in options:
        default_idx = options.index("Default Dataset")
        
    source = st.sidebar.selectbox(
        "Select Active Dataset",
        options,
        index=default_idx,
        key=f"{key_prefix}_data_source_select"
    )
    
    df = None
    if source == "Sample Dataset":
        sample_path = "dataset/sample_sales_data.csv"
        if os.path.exists(sample_path):
            df = pd.read_csv(sample_path)
        else:
            st.sidebar.error("Sample dataset file not found!")
    elif source == "Default Dataset":
        df = pd.read_csv("dataset/sales_data.csv")
    elif source == "Uploaded Dataset":
        df = st.session_state.sales_df
    elif source == "Processed Dataset":
        if os.path.exists("dataset/processed_sales_data.csv"):
            df = pd.read_csv("dataset/processed_sales_data.csv")
        else:
            df = st.session_state.processed_df
            
    # Quick data integrity check / processing
    if df is not None:
        # Calculate total_sales if missing but columns exist
        if "total_sales" not in df.columns and "quantity" in df.columns and "unit_price" in df.columns:
            df["total_sales"] = df["quantity"] * df["unit_price"]
            
    return df

def show_data_summary(df):
    """Displays key statistics of the dataset in a nice visual layout."""
    if df is None or len(df) == 0:
        st.warning("Cannot show summary for empty dataset.")
        return
        
    # Make sure total_sales is calculated
    if "total_sales" not in df.columns and "quantity" in df.columns and "unit_price" in df.columns:
        df["total_sales"] = df["quantity"] * df["unit_price"]
        
    try:
        summary = get_data_summary(df)
        
        st.markdown("### 📊 Dataset Quick Stats")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Records", f"{summary['total_records']:,}")
        c2.metric("Products", f"{summary['unique_products']:,}")
        c3.metric("Regions", f"{summary['unique_regions']:,}")
        c4.metric("Revenue", f"₹ {summary['total_revenue']:,.2f}")
    except Exception as e:
        # Fallback if dataframe is missing expected column names
        st.warning(f"Unable to compute full stats: {e}")
        st.write(df.head(2))

def show_no_data_message():
    """Renders a standard warning when no data is loaded/configured."""
    st.info("💡 Please load or upload a dataset using the **Data Upload** page or select one in the sidebar.")
