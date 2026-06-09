import streamlit as st
import pandas as pd

from database.data_operations import save_dataframe
from utils.ui_styles import page_header
from utils.ui_components import show_data_summary, init_session_state
from utils.charts import product_sales_chart, region_sales_chart

page_header(
    "📤 Data Upload",
    "Upload sales data and persist it across all pages"
)

init_session_state()

col1, col2 = st.columns([1, 2])

with col1:

    file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    use_sample = st.button(
        "Load Sample Dataset",
        use_container_width=True
    )

with col2:

    if use_sample:

        df = pd.read_csv("dataset/sample_sales_data.csv")
        st.session_state.sales_df = df
        st.success("Sample dataset loaded into session!")

    elif file:

        df = pd.read_csv(file)
        st.session_state.sales_df = df

    if st.session_state.sales_df is not None:

        df = st.session_state.sales_df

        show_data_summary(df)

        st.dataframe(
            df.head(10),
            use_container_width=True,
            hide_index=True
        )

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

        if st.button(
            "💾 Save to Database",
            type="primary",
            use_container_width=True
        ):

            save_dataframe(df)

            st.success("Data saved successfully to SQLite database!")

    else:

        st.info(
            "Upload a CSV or click **Load Sample Dataset** to begin."
        )
