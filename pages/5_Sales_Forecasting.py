import os

import pandas as pd
import streamlit as st
import plotly.express as px

from models.predict import predict_sales
from preprocessing.preprocessing_pipeline import run_pipeline
from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_no_data_message
)
from utils.charts import forecast_timeline_chart

page_header(
    "📈 Sales Forecasting",
    "Predict revenue using the trained ML model"
)

model_exists = os.path.exists("models/sales_forecast_model.pkl")

if not model_exists:

    st.warning(
        "No trained model found. Go to **Model Training** page first."
    )

df = data_loader_sidebar(key_prefix="forecast")

tab1, tab2 = st.tabs([
    "🔮 Single Prediction",
    "📅 Batch Forecast"
])

with tab1:

    st.subheader("Predict Sales for a Single Order")

    c1, c2, c3, c4 = st.columns(4)

    year = c1.number_input("Year", 2025, 2035, 2026)
    month = c2.number_input("Month", 1, 12, 6)
    day = c3.number_input("Day", 1, 31, 15)
    quantity = c4.number_input("Quantity", 1, 10000, 100)

    if st.button("Predict Sales", type="primary", disabled=not model_exists):

        data = pd.DataFrame({
            "year": [year],
            "month": [month],
            "day": [day],
            "quantity": [quantity]
        })

        prediction = predict_sales(data)

        st.success(f"**Predicted Revenue: ₹ {prediction[0]:,.2f}**")

        st.metric(
            "Estimated per-unit revenue",
            f"₹ {prediction[0] / quantity:,.2f}"
        )

with tab2:

    st.subheader("30-Day Sales Forecast")

    if df is None:

        show_no_data_message()

    elif not model_exists:

        st.warning("Train a model first to generate forecasts.")

    else:

        forecast_days = st.slider(
            "Forecast horizon (days)",
            min_value=7,
            max_value=60,
            value=30
        )

        avg_quantity = int(df["quantity"].mean())

        if st.button("Generate Forecast", type="primary"):

            chart_df = run_pipeline(df) if "year" not in df.columns else df.copy()

            last_date = pd.to_datetime(chart_df["order_date"]).max()

            forecast_rows = []

            for i in range(1, forecast_days + 1):

                future_date = last_date + pd.Timedelta(days=i)

                input_data = pd.DataFrame({
                    "year": [future_date.year],
                    "month": [future_date.month],
                    "day": [future_date.day],
                    "quantity": [avg_quantity]
                })

                predicted = predict_sales(input_data)[0]

                forecast_rows.append({
                    "forecast_date": future_date,
                    "predicted_sales": predicted,
                    "quantity": avg_quantity
                })

            forecast_df = pd.DataFrame(forecast_rows)

            total_forecast = forecast_df["predicted_sales"].sum()
            avg_forecast = forecast_df["predicted_sales"].mean()

            m1, m2, m3 = st.columns(3)

            m1.metric(
                f"Total ({forecast_days} days)",
                f"₹ {total_forecast:,.0f}"
            )
            m2.metric("Daily Average", f"₹ {avg_forecast:,.0f}")
            m3.metric("Avg Quantity Used", avg_quantity)

            st.plotly_chart(
                forecast_timeline_chart(chart_df, forecast_df),
                use_container_width=True
            )

            fig = px.bar(
                forecast_df,
                x="forecast_date",
                y="predicted_sales",
                title="Daily Forecast Breakdown",
                labels={
                    "forecast_date": "Date",
                    "predicted_sales": "Predicted Revenue (₹)"
                },
                color="predicted_sales",
                color_continuous_scale="Greens"
            )

            fig.update_layout(showlegend=False)

            st.plotly_chart(fig, use_container_width=True)

            st.download_button(
                label="⬇️ Download Forecast CSV",
                data=forecast_df.to_csv(index=False),
                file_name="sales_forecast.csv",
                mime="text/csv"
            )
