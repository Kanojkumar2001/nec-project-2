import pandas as pd

from utils.helper_functions import calculate_total_sales


def create_features(df):

    df = df.copy()

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["day"] = df["order_date"].dt.day

    df = calculate_total_sales(df)

    return df
