import pandas as pd
from sqlalchemy import create_engine

# Update your URL
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/olist_database"
engine = create_engine(DATABASE_URL)

df_customers = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\customers.csv")

# Preview
print(df_customers.head())

# Insert into DB
df_customers.to_sql("customers", engine, if_exists="append", index=False)

print(" Customers table inserted!")
print("Loading orders")

df_orders = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\orders.csv")
df_orders.columns = df_orders.columns.str.replace('"', '').str.strip()
print("Orders columns after cleaning:", df_orders.columns.tolist())

# Convert date columns
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    if col in df_orders.columns:
        df_orders[col] = pd.to_datetime(df_orders[col], errors='coerce')
    else:
        print(f" Missing column: {col}")

df_orders.to_sql("orders", engine, if_exists="append", index=False)




print("Orders table inserted!")

print("Loading products.")

df_products = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\products.csv")

df_products = df_products[[
    "product_id",
    "product_category_name",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]]


numeric_cols = [
    "product_weight_g", "product_length_cm", 
    "product_height_cm", "product_width_cm"
]

for col in numeric_cols:
    df_products[col] = pd.to_numeric(df_products[col], errors='coerce')

df_products.to_sql("products", engine, if_exists="append", index=False)

print(" Products table inserted!")

print("Loading sellers")
df_sellers = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\sellers.csv")
df_sellers.to_sql("sellers", engine, if_exists="append", index=False)
print(" Sellers table inserted!")

print("Loading order_items")

df_items = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\order_items.csv")

df_items = df_items[[
    "order_id",
    "order_item_id",
    "product_id",
    "seller_id",
    "price",
    "freight_value"
]]
df_items["price"] = pd.to_numeric(df_items["price"], errors="coerce")
df_items["freight_value"] = pd.to_numeric(df_items["freight_value"], errors="coerce")

df_items.to_sql("order_items", engine, if_exists="append", index=False)

print("Order Items inserted")

print("Loading payments")

df_pay = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\payments.csv")

df_pay["payment_value"] = pd.to_numeric(df_pay["payment_value"], errors="coerce")

df_pay.to_sql("payments", engine, if_exists="append", index=False)

print(" Payments inserted")

print("Loading reviews")

df_reviews = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\reviews.csv")


df_reviews = df_reviews[[
    "review_id",
    "order_id",
    "review_score",
    "review_comment_title",
    "review_comment_message"
]]
df=df_reviews
# Drop duplicates by review_id 
df = df.drop_duplicates(subset=["review_id"])

# Insert
df.to_sql("reviews", engine, if_exists="append", index=False)

print(" Reviews inserted successfully")



