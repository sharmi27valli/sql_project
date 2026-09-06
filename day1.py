import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce"
)

print("connection estlished successfully!")

cursor=con.cursor()

query="select * from products"

query = """
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;
"""

df = pd.read_sql(query,con)

plt.bar(df["category"], df["product_count"])
plt.xlabel("Category")
plt.ylabel("Product Count")
plt.title("Products by Category")
plt.xticks(rotation=45)
plt.show()

query = """
SELECT category, AVG(price) AS average_price
FROM products
GROUP BY category;
"""

df = pd.read_sql(query, con)

plt.bar(df["category"], df["average_price"])
plt.xlabel("Category")
plt.ylabel("Average Price")
plt.title("Average Price by Category")
plt.xticks(rotation=45)
plt.show()

query = """
SELECT status, COUNT(*) AS order_count
FROM orders
GROUP BY status;
"""

query = """
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;
"""

df = pd.read_sql(query, con)

plt.pie(
    df["product_count"],
    labels=df["category"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Product Distribution by Category")
plt.show()


