from sqlalchemy import create_engine

# Change password if needed
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/olist_database"

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("✅ Connection successful!")
    connection.close()

except Exception as e:
    print("❌ Connection failed!")
    print(e)
