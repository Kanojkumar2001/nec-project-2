import streamlit as st

from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_data_summary,
    show_no_data_message
)
from utils.charts import (
    sales_trend_chart,
    product_sales_chart,
    region_sales_chart,
    category_sales_chart,
    monthly_sales_chart,
    quantity_distribution_chart,
    price_quantity_scatter,
    region_product_heatmap
)

page_header(
    "📊 Exploratory Data Analysis",
    "Deep-dive into sales patterns, products, and regional performance"
)

df = data_loader_sidebar(key_prefix="eda")

if df is not None:

    show_data_summary(df)

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Trends",
        "🏷️ Products",
        "🌍 Regions",
        "🔍 Advanced"
    ])

    with tab1:

        c1, c2 = st.columns(2)

        with c1:
            st.plotly_chart(
                sales_trend_chart(df),
                use_container_width=True
            )

        with c2:
            st.plotly_chart(
                monthly_sales_chart(df),
                use_container_width=True
            )

    with tab2:

        c1, c2 = st.columns(2)

        with c1:
            st.plotly_chart(
                product_sales_chart(df),
                use_container_width=True
            )

        with c2:
            st.plotly_chart(
                quantity_distribution_chart(df),
                use_container_width=True
            )

    with tab3:

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

    with tab4:

        c1, c2 = st.columns(2)

        with c1:
            st.plotly_chart(
                price_quantity_scatter(df),
                use_container_width=True
            )

        with c2:
            st.plotly_chart(
                region_product_heatmap(df),
                use_container_width=True
            )

        with st.expander("Full Dataset"):

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

else:

    show_no_data_message()
