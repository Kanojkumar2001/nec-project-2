import streamlit as st

from inventory.inventory_optimizer import optimize_inventory
from inventory.stock_alerts import generate_stock_alert
from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_no_data_message
)
from utils.charts import inventory_gauge_chart
from dashboard.inventory_dashboard import inventory_dashboard

page_header(
    "📦 Inventory Optimization",
    "Calculate reorder points, safety stock, and stock alerts"
)

df = data_loader_sidebar(key_prefix="inventory")

tab1, tab2 = st.tabs([
    "⚙️ Manual Calculator",
    "📊 Data-Driven Insights"
])

with tab1:

    st.subheader("Inventory Parameters")

    c1, c2, c3 = st.columns(3)

    current_stock = c1.number_input(
        "Current Stock",
        min_value=0,
        value=100
    )

    average_sales = c2.number_input(
        "Average Daily Sales",
        min_value=1.0,
        value=20.0
    )

    lead_time = c3.number_input(
        "Lead Time (Days)",
        min_value=1,
        value=5
    )

    if st.button("Optimize Inventory", type="primary"):

        result = optimize_inventory(
            current_stock,
            average_sales,
            lead_time
        )

        alert = generate_stock_alert(
            current_stock,
            result["reorder_point"]
        )

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Reorder Point", f"{result['reorder_point']:.0f}")
        m2.metric("Safety Stock", f"{result['safety_stock']:.0f}")
        m3.metric("Recommended Stock", f"{result['recommended_stock']:.0f}")
        m4.metric("Status", result["status"])

        st.plotly_chart(
            inventory_gauge_chart(
                current_stock,
                result["reorder_point"],
                result["recommended_stock"]
            ),
            use_container_width=True
        )

        if "Low Stock" in alert:
            st.error(alert)
        else:
            st.success(alert)

with tab2:

    if df is not None:
        inventory_dashboard(df)
    else:
        show_no_data_message()
