import streamlit as st

from utils.charts import (
    region_sales_chart,
    region_product_heatmap,
    category_sales_chart
)


def region_analysis(df):

    st.subheader("Regional & Category Insights")

    c1, c2 = st.columns(2)

    with c1:
        st.plotly_chart(
            region_sales_chart(df),
            use_container_width=True
        )

    with c2:
        st.plotly_chart(
            category_sales_chart(df),
            use_container_width=True
        )

    st.plotly_chart(
        region_product_heatmap(df),
        use_container_width=True
    )
