import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


db_path = os.environ.get(
    'LESSON_DB_PATH',
    os.path.join(os.path.dirname(__file__), '..', 'python_homework', 'db', 'lesson.db')
)

db_path = os.path.abspath(db_path)


try:
    with sqlite3.connect(db_path) as conn:
        sql = """
        SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p ON l.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id
        """
        df = pd.read_sql_query(sql, conn)

    df['cumulative'] = df['total_price'].cumsum()

    df.plot(x='order_id', y='cumulative', kind='line', marker='o', color='teal', title='Cumulative Revenue by Order')
    plt.xlabel('Order ID')
    plt.ylabel('Cumulative Revenue ($)')
    plt.grid(True)
    plt.tight_layout()

    plt.show()

except sqlite3.Error as e:
    print(f"SQL Error: {e}")