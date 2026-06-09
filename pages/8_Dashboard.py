import streamlit as st

from dashboard.kpi_dashboard import show_kpis
from dashboard.sales_analysis import sales_analysis
from dashboard.region_analysis import region_analysis
from dashboard.forecast_dashboard import forecast_dashboard
from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_no_data_message
)

page_header(
    "📊 Executive Dashboard",
    "Real-time KPIs and interactive sales analytics"
)

df = data_loader_sidebar(key_prefix="dashboard")

if df is not None:

    show_kpis(df)

    st.markdown("---")

    sales_analysis(df)

    st.markdown("---")

    region_analysis(df)

    st.markdown("---")

    forecast_dashboard(df)

else:

    show_no_data_message()
