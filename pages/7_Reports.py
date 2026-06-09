import streamlit as st
import pandas as pd

from reports.generate_excel_report import generate_excel_report
from reports.generate_pdf_report import generate_pdf_report
from reports.report_summary import generate_summary
from reports.report_templates import sales_report_template
from utils.ui_styles import page_header
from utils.ui_components import (
    data_loader_sidebar,
    show_data_summary,
    show_no_data_message
)
from utils.charts import product_sales_chart, region_sales_chart

page_header(
    "📄 Reports",
    "Generate Excel and PDF business reports from your sales data"
)

df = data_loader_sidebar(key_prefix="reports")

if df is not None:

    show_data_summary(df)

    st.markdown("---")

    summary = generate_summary(df)

    st.markdown("### Report Preview")
    st.markdown(summary)

    c1, c2 = st.columns(2)

    with c1:
        st.plotly_chart(
            product_sales_chart(df),
            use_container_width=True
        )

    with c2:
        st.plotly_chart(
            region_sales_chart(df),
            use_container_width=True
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📗 Generate Excel Report",
            type="primary",
            use_container_width=True
        ):

            path = "outputs/reports/sales_report.xlsx"

            generate_excel_report(df, path)
            st.session_state.excel_ready = True

        if st.session_state.get("excel_ready", False):

            path = "outputs/reports/sales_report.xlsx"

            with open(path, "rb") as report_file:
                st.download_button(
                    label="⬇️ Download Excel Report",
                    data=report_file.read(),
                    file_name="sales_report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

            st.success("Excel report generated successfully!")

    with col2:

        if st.button(
            "📕 Generate PDF Report",
            use_container_width=True
        ):

            content = sales_report_template()

            summary_text = generate_summary(df)

            path = "outputs/reports/sales_report.pdf"

            generate_pdf_report(
                path,
                content + summary_text
            )
            st.session_state.pdf_ready = True

        if st.session_state.get("pdf_ready", False):

            path = "outputs/reports/sales_report.pdf"

            with open(path, "rb") as report_file:
                st.download_button(
                    label="⬇️ Download PDF Report",
                    data=report_file.read(),
                    file_name="sales_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

            st.success("PDF report generated successfully!")

else:

    show_no_data_message()
