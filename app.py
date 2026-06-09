import os

import pandas as pd
import streamlit as st

from utils.file_manager import create_project_folders
from utils.ui_styles import inject_custom_css, page_header
from utils.charts import sales_trend_chart, region_sales_chart

create_project_folders()

st.set_page_config(
    page_title="Intelligent Sales Forecasting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()

page_header(
    "📈 Intelligent Sales Forecasting System",
    "AI-powered sales analytics, forecasting, and inventory optimization"
)

st.markdown("---")

col_left, col_right = st.columns([2, 1])

with col_left:

    st.markdown("### Welcome")

    st.markdown(
        """
        This platform helps you analyze sales data, train ML forecasting models,
        predict future revenue, optimize inventory, and generate business reports —
        all from a single interactive dashboard.
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📊 Analytics</h3>
                <p>Interactive charts for trends, regions, products, and categories.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🤖 Forecasting</h3>
                <p>Train Random Forest models and predict future sales revenue.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>📦 Inventory</h3>
                <p>Reorder points, safety stock, and low-stock alerts.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

with col_right:

    st.markdown("### Quick Start")

    st.markdown(
        """
        1. **Data Upload** — Load your sales CSV
        2. **Preprocessing** — Clean & engineer features
        3. **EDA / Dashboard** — Explore insights
        4. **Model Training** — Train forecast model
        5. **Forecasting** — Predict sales
        6. **Inventory** — Optimize stock levels
        """
    )

default_path = "dataset/sales_data.csv"

if os.path.exists(default_path):

    df = pd.read_csv(default_path)

    st.markdown("---")
    st.markdown("### 📌 Live Preview — Default Dataset")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Records", len(df))
    m2.metric("Products", df["product_name"].nunique())
    m3.metric("Regions", df["region"].nunique())
    m4.metric("Revenue", f"₹ {df['total_sales'].sum():,.0f}")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.plotly_chart(
            sales_trend_chart(df),
            use_container_width=True
        )

    with chart_col2:
        st.plotly_chart(
            region_sales_chart(df),
            use_container_width=True
        )

else:

    st.info(
        "Upload sales data from the sidebar pages to get started."
    )
