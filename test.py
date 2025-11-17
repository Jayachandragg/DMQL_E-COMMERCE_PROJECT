import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# 1. PostgreSQL connection string
# -------------------------------
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/olist_database"
engine = create_engine(DATABASE_URL)

# -------------------------------
# 2. Path to your reviews.csv file
# -------------------------------
reviews_path = r"D:\UB\2nd semester\DMQL\project\data\reviews.csv"

print("📥 Loading reviews CSV...")
print("Loading reviews...")

df_reviews = pd.read_csv(r"D:\UB\2nd semester\DMQL\project\data\reviews.csv")


df_reviews = df_reviews[[
    "review_id",
    "order_id",
    "review_score",
    "review_comment_title",
    "review_comment_message"
]]
df=df_reviews
# Drop duplicates by review_id (just in case)
df = df.drop_duplicates(subset=["review_id"])

# Insert
df.to_sql("reviews", engine, if_exists="append", index=False)

print("✅ Reviews inserted successfully!")

# Convert timestamps
