import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def read_csv(file_path):
    """Read the Superstore CSV file into a DataFrame."""
    print("\n📂 Loading CSV data...")
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None

def connect_to_database():
    """Establish MySQL database connection."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        print("✅ Database connection established.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Connection failed: {err}")
        return None

def create_table(cursor):
    """Create table if it doesn't exist."""
    query = """
    CREATE TABLE IF NOT EXISTS superstore (
        Row_ID INT PRIMARY KEY,
        Order_ID VARCHAR(255),
        Order_Date DATE,
        Ship_Date DATE,
        Ship_Mode VARCHAR(255),
        Customer_ID VARCHAR(255),
        Customer_Name VARCHAR(255),
        Segment VARCHAR(255),
        Country VARCHAR(255),
        City VARCHAR(255),
        State VARCHAR(255),
        Postal_Code INT,
        Region VARCHAR(255),
        Product_ID VARCHAR(255),
        Category VARCHAR(255),
        Sub_Category VARCHAR(255),
        Product_Name VARCHAR(255),
        Sales FLOAT,
        Quantity INT,
        Discount FLOAT,
        Profit FLOAT
    )
    """
    cursor.execute(query)
    print("🛠️  Table checked/created successfully.")

def insert_data(df, cursor, conn):
    """Insert data from CSV to MySQL."""
    print("📥 Inserting data into database...")
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT IGNORE INTO superstore VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    print(f"✅ {len(df)} rows inserted successfully.")

def main():
    df = read_csv("superstore.csv")
    if df is None:
        return
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        create_table(cursor)
        insert_data(df, cursor, conn)
        conn.close()
        print("🔚 Process completed. Connection closed.")

if __name__ == "__main__":
    main()

