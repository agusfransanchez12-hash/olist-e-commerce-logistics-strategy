import pandas as pd
import sqlite3
# Load the main datasets
orders = pd.read_csv("olist_orders_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")

# -------------------------------------------------------------
# 1. Check for nulls and duplicates in EACH of the tables.
# -------------------------------------------------------------

print("=== 1. PEDIDOS (orders) ===")
print("Nulos:\n", orders.isnull().sum())
print("Duplicados:", orders.duplicated().sum())

print("\n=== 2. ÍTEMS DE PEDIDOS (items) ===")
print("Nulos:\n", items.isnull().sum())
print("Duplicados:", items.duplicated().sum())

print("\n=== 3. PAGOS (payments) ===")
print("Nulos:\n", payments.isnull().sum())
print("Duplicados:", payments.duplicated().sum())

print("\n=== 4. RESEÑAS (reviews) ===")
print("Nulos:\n", reviews.isnull().sum())
print("Duplicados:", reviews.duplicated().sum())

print("\n=== 5. PRODUCTOS (products) ===")
print("Nulos:\n", products.isnull().sum())
print("Duplicados:", products.duplicated().sum())

print("\n=== 6. CLIENTES (customers) ===")
print("Nulos:\n", customers.isnull().sum())
print("Duplicados:", customers.duplicated().sum())

print("\n=== 7. VENDEDORES (sellers) ===")
print("Nulos:\n", sellers.isnull().sum())
print("Duplicados:", sellers.duplicated().sum())
# ============================================================
# 2. Manual cleaning and conversion, column by column
# ============================================================

# We manually convert each date column to the standard text format (ISO) recognized by SQL.
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at']).dt.strftime('%Y-%m-%d %H:%M:%S')
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date']).dt.strftime('%Y-%m-%d %H:%M:%S')
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date']).dt.strftime('%Y-%m-%d %H:%M:%S')
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date']).dt.strftime('%Y-%m-%d %H:%M:%S')

# We fill in the categorical null values ​​manually.
products['product_category_name'] = products['product_category_name'].fillna('sin_categoria')


# ============================================================
# 3. EXPORT TO SQLITE (7 INDIVIDUAL TABLES)
# ============================================================
conn = sqlite3.connect('olist_db.db')

orders.to_sql('orders', conn, if_exists='replace', index=False)
customers.to_sql('customers', conn, if_exists='replace', index=False)
items.to_sql('order_items', conn, if_exists='replace', index=False)
payments.to_sql('payments', conn, if_exists='replace', index=False)
reviews.to_sql('reviews', conn, if_exists='replace', index=False)
products.to_sql('products', conn, if_exists='replace', index=False)
sellers.to_sql('sellers', conn, if_exists='replace', index=False)

conn.close()
