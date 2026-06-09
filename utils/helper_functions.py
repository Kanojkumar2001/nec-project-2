import pandas as pd


def load_csv(file):

    df = pd.read_csv(file)

    return df


def calculate_total_sales(df):

    df["total_sales"] = df["quantity"] * df["unit_price"]

    return df


def get_data_summary(df):

    return {
        "total_records": len(df),
        "unique_products": df["product_name"].nunique(),
        "unique_regions": df["region"].nunique(),
        "unique_categories": df["category"].nunique(),
        "total_revenue": df["total_sales"].sum(),
        "avg_order_value": df["total_sales"].mean(),
        "total_quantity": df["quantity"].sum(),
        "top_product": (
            df.groupby("product_name")["total_sales"]
            .sum()
            .idxmax()
        ),
        "top_region": (
            df.groupby("region")["total_sales"]
            .sum()
            .idxmax()
        ),
    }


def prepare_chart_data(df):

    chart_df = df.copy()

    chart_df["order_date"] = pd.to_datetime(
        chart_df["order_date"],
        errors="coerce"
    )

    return chart_df