import streamlit as st

from utils.charts import (
    sales_trend_chart,
    monthly_sales_chart,
    product_sales_chart
)


def sales_analysis(df):

    st.subheader("Sales Performance")

    tab1, tab2, tab3 = st.tabs([
        "Daily Trend",
        "Monthly Revenue",
        "Top Products"
    ])

    with tab1:
        st.plotly_chart(
            sales_trend_chart(df),
            use_container_width=True
        )

    with tab2:
        st.plotly_chart(
            monthly_sales_chart(df),
            use_container_width=True
        )

    with tab3:
        st.plotly_chart(
            product_sales_chart(df),
            use_container_width=True
        )
