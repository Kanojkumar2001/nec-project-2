import streamlit as st
import pandas as pd
import plotly.express as px

from preprocessing.preprocessing_pipeline import run_pipeline
from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_data_summary,
    show_no_data_message,
    init_session_state
)

init_session_state()

page_header(
    "🧹 Data Preprocessing",
    "Clean data, engineer features, and export processed dataset"
)

df = data_loader_sidebar(key_prefix="preprocess")

if df is not None:

    show_data_summary(df)

    with st.expander("View Raw Data", expanded=False):
        st.dataframe(df, use_container_width=True, hide_index=True)

    if st.button("Run Preprocessing Pipeline", type="primary"):

        with st.spinner("Cleaning data and creating features..."):

            processed_df = run_pipeline(df)
            st.session_state.processed_df = processed_df

        st.success("Preprocessing completed!")

    if st.session_state.get("processed_df") is not None:

        processed_df = st.session_state.processed_df

        st.subheader("Processed Data Preview")

        st.dataframe(
            processed_df.head(15),
            use_container_width=True,
            hide_index=True
        )

        c1, c2 = st.columns(2)

        with c1:

            feature_cols = ["year", "month", "day", "quantity", "total_sales"]

            fig = px.scatter(
                processed_df,
                x="quantity",
                y="total_sales",
                color="region",
                size="unit_price",
                hover_name="product_name",
                title="Engineered Features: Quantity vs Revenue"
            )

            st.plotly_chart(fig, use_container_width=True)

        with c2:

            month_df = (
                processed_df.groupby("month")["total_sales"]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                month_df,
                x="month",
                y="total_sales",
                title="Monthly Revenue (Processed)",
                color="total_sales",
                color_continuous_scale="Viridis"
            )

            st.plotly_chart(fig, use_container_width=True)

        st.markdown("##### New Features Added")
        st.markdown(
            "- `year`, `month`, `day` — extracted from order date  \n"
            "- `total_sales` — recalculated as quantity × unit price  \n"
            "- Duplicates removed, missing values handled, outliers filtered"
        )

        output_path = "dataset/processed_sales_data.csv"

        processed_df.to_csv(output_path, index=False)

        st.download_button(
            label="⬇️ Download Processed CSV",
            data=processed_df.to_csv(index=False),
            file_name="processed_sales_data.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.info(f"Saved locally to `{output_path}`")

else:

    show_no_data_message()
