from database.db_connection import get_connection
from database.create_tables import create_sales_table
import pandas as pd


def save_dataframe(df):

    create_sales_table()

    conn = get_connection()

    df.to_sql(
        "sales_data",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()


def load_sales_data():

    conn = get_connection()

    query = """
    SELECT * FROM sales_data
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df