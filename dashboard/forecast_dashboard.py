import streamlit as st

from utils.charts import (
    quantity_distribution_chart,
    price_quantity_scatter
)


def forecast_dashboard(df):

    st.subheader("Product & Pricing Analysis")

    c1, c2 = st.columns(2)

    with c1:
        st.plotly_chart(
            quantity_distribution_chart(df),
            use_container_width=True
        )

    with c2:
        st.plotly_chart(
            price_quantity_scatter(df),
            use_container_width=True
        )
