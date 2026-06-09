def remove_outliers(df):

    q1 = df["total_sales"].quantile(0.25)

    q3 = df["total_sales"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr

    upper = q3 + 1.5 * iqr

    df = df[
        (df["total_sales"] >= lower)
        &
        (df["total_sales"] <= upper)
    ]

    return df