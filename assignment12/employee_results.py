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
        sql_statement = """
        SELECT last_name, SUM(price * quantity) AS revenue
        FROM employees e
        JOIN orders o ON e.employee_id = o.employee_id
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p ON l.product_id = p.product_id
        GROUP BY e.employee_id;
        """

        df = pd.read_sql_query(sql_statement, conn)
        df.sort_values(by='revenue', ascending=False, inplace=True)

        df.plot(
            x='last_name',
            y='revenue',
            kind='bar',
            color='violet',
            title='Revenue by Employee Last Name'
        )

        plt.xlabel('Employee Last Name')
        plt.ylabel('Revenue ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

except sqlite3.Error as e:
    print(f"SQL Error: {e}")