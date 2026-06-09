def generate_summary(df):

    total_sales = df["total_sales"].sum()

    total_orders = len(df)

    avg_sales = df["total_sales"].mean()

    summary = f"""

    Total Sales : {total_sales}

    Total Orders : {total_orders}

    Average Sales : {avg_sales}

    """

    return summary