import streamlit as st
import pandas as pd
import plotly.express as px

from preprocessing.preprocessing_pipeline import run_pipeline
from models.train_model import train_model
from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_no_data_message
)
from utils.charts import forecast_comparison_chart

page_header(
    "🤖 Model Training",
    "Train a Random Forest regressor for sales forecasting"
)

df = data_loader_sidebar(
    show_processed=True,
    key_prefix="train"
)

if df is not None:

    st.info(
        f"Dataset ready with **{len(df)}** records. "
        "Features used: `year`, `month`, `day`, `quantity` → target: `total_sales`"
    )

    needs_pipeline = not all(
        col in df.columns
        for col in ["year", "month", "day"]
    )

    if needs_pipeline:
        df = run_pipeline(df)

    if st.button("🚀 Train Model", type="primary"):

        with st.spinner("Training Random Forest model..."):

            result = train_model(df)

        st.success("Model trained and saved successfully!")

        m1, m2, m3 = st.columns(3)

        m1.metric("R² Score", f"{result['r2']:.4f}")
        m2.metric("MAE", f"₹ {result['mae']:,.2f}")
        m3.metric("MSE", f"{result['mse']:,.2f}")

        c1, c2 = st.columns(2)

        with c1:

            st.plotly_chart(
                forecast_comparison_chart(
                    result["actual"],
                    result["predictions"]
                ),
                use_container_width=True
            )

        with c2:

            importance_df = pd.DataFrame({
                "feature": list(result["feature_importance"].keys()),
                "importance": list(result["feature_importance"].values())
            })

            fig = px.bar(
                importance_df,
                x="importance",
                y="feature",
                orientation="h",
                title="Feature Importance",
                color="importance",
                color_continuous_scale="Blues"
            )

            fig.update_layout(showlegend=False)

            st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            "Model saved to `models/sales_forecast_model.pkl` — "
            "use the **Sales Forecasting** page to predict."
        )

else:

    show_no_data_message()
