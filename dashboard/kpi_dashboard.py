import streamlit as st

from utils.helper_functions import get_data_summary


def show_kpis(df):

    summary = get_data_summary(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Revenue",
        f"₹ {summary['total_revenue']:,.0f}"
    )

    c2.metric(
        "Total Orders",
        f"{summary['total_records']:,}"
    )

    c3.metric(
        "Avg Order Value",
        f"₹ {summary['avg_order_value']:,.0f}"
    )

    c4.metric(
        "Units Sold",
        f"{summary['total_quantity']:,}"
    )

    c5, c6, c7, c8 = st.columns(4)

    c5.metric("Products", summary["unique_products"])
    c6.metric("Regions", summary["unique_regions"])
    c7.metric("Top Product", summary["top_product"])
    c8.metric("Top Region", summary["top_region"])
