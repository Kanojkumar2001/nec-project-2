import streamlit as st


def inject_custom_css():

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main-header {
            background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 50%, #0ea5e9 100%);
            padding: 2rem 2.5rem;
            border-radius: 16px;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.25);
        }

        .main-header h1 {
            color: white !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
            margin-bottom: 0.4rem !important;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .main-header .header-icon {
            height: 2.4rem;
            width: auto;
            border-radius: 0.6rem;
            object-fit: contain;
        }

        .main-header p {
            color: rgba(255, 255, 255, 0.9) !important;
            font-size: 1.05rem !important;
            margin: 0 !important;
        }

        .feature-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.25rem;
            height: 100%;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.1);
        }

        .feature-card h3 {
            color: #1e293b;
            font-size: 1.05rem;
            margin-bottom: 0.5rem;
        }

        .feature-card p {
            color: #64748b;
            font-size: 0.9rem;
            margin: 0;
        }

        .info-box {
            background: #f0f9ff;
            border-left: 4px solid #2563eb;
            padding: 1rem 1.25rem;
            border-radius: 0 8px 8px 0;
            margin: 1rem 0;
        }

        .status-safe {
            color: #059669;
            font-weight: 600;
        }

        .status-alert {
            color: #dc2626;
            font-weight: 600;
        }

        div[data-testid="stMetric"] {
            background: linear-gradient(145deg, #f8fafc, #ffffff);
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
        }

        div[data-testid="stMetric"] label {
            color: #64748b !important;
        }

        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #1e293b !important;
            font-weight: 700 !important;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            padding: 10px 20px;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
        }

        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] a {
            color: #1e293b !important;
        }

        .block-container {
            padding-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def page_header(title, subtitle=""):

    inject_custom_css()

    st.markdown(
        f"""
        <div class="main-header">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
