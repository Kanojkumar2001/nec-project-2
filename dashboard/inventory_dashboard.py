import streamlit as st
import pandas as pd

from inventory.inventory_optimizer import optimize_inventory
from utils.charts import inventory_gauge_chart


def inventory_dashboard(df):

    st.subheader("Inventory Insights from Sales Data")

    product_stats = (
        df.groupby("product_name")
        .agg(
            avg_daily_sales=("quantity", "mean"),
            total_quantity=("quantity", "sum"),
            avg_revenue=("total_sales", "mean")
        )
        .reset_index()
        .sort_values("total_quantity", ascending=False)
    )

    st.dataframe(
        product_stats,
        use_container_width=True,
        hide_index=True
    )

    product = st.selectbox(
        "Select product for stock analysis",
        product_stats["product_name"].tolist()
    )

    selected = product_stats[
        product_stats["product_name"] == product
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    current_stock = col1.number_input(
        "Current Stock",
        min_value=0,
        value=int(selected["total_quantity"] * 0.3),
        key="inv_current"
    )

    avg_sales = col2.number_input(
        "Avg Daily Sales",
        min_value=1.0,
        value=float(max(selected["avg_daily_sales"], 1)),
        key="inv_avg"
    )

    lead_time = col3.number_input(
        "Lead Time (days)",
        min_value=1,
        value=5,
        key="inv_lead"
    )

    result = optimize_inventory(
        current_stock,
        avg_sales,
        lead_time
    )

    m1, m2, m3 = st.columns(3)

    m1.metric("Reorder Point", f"{result['reorder_point']:.0f} units")
    m2.metric("Safety Stock", f"{result['safety_stock']:.0f} units")
    m3.metric("Recommended Stock", f"{result['recommended_stock']:.0f} units")

    st.plotly_chart(
        inventory_gauge_chart(
            current_stock,
            result["reorder_point"],
            result["recommended_stock"]
        ),
        use_container_width=True
    )

    if result["status"] == "Reorder Required":
        st.error("⚠️ Reorder Required — stock is below the reorder point.")
    else:
        st.success("✅ Stock level is healthy.")
