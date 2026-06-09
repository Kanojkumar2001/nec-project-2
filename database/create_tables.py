from database.db_connection import get_connection

def create_sales_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_date TEXT,
        product_name TEXT,
        category TEXT,
        region TEXT,
        quantity INTEGER,
        unit_price REAL,
        total_sales REAL
    )
    """)

    conn.commit()
    conn.close()

    print("sales_data table created successfully")

if __name__ == "__main__":
    create_sales_table()