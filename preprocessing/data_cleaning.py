import pandas as pd


def clean_data(df):

    df = df.copy()

    df.drop_duplicates(inplace=True)

    critical_columns = [
        "order_date",
        "product_name",
        "category",
        "region",
        "quantity",
        "unit_price"
    ]

    existing_columns = [
        column for column in critical_columns
        if column in df.columns
    ]

    df.dropna(
        subset=existing_columns,
        inplace=True
    )

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    df[numeric_columns] = df[numeric_columns].fillna(0)

    return df