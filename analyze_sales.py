import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    """Load CSV data."""
    try:
        df = pd.read_csv(path)
        print("✅ CSV data loaded.")
        return df
    except FileNotFoundError:
        print("❌ File not found!")
        return None

def sales_by_category(df):
    """Bar chart of sales by category."""
    print("📊 Plotting sales by category...")
    category_sales = df.groupby("Category")["Sales"].sum().sort_values()
    plt.figure(figsize=(8, 5))
    category_sales.plot(kind='barh', color='skyblue')
    plt.title("Total Sales by Category")
    plt.xlabel("Sales")
    plt.ylabel("Category")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def top_products(df, n=5):
    """Top N selling products."""
    top = df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False).head(n)
    print(f"🏆 Top {n} Products:")
    print(top)

def main():
    df = load_data("superstore.csv")
    if df is not None:
        sales_by_category(df)
        top_products(df)

if __name__ == "__main__":
    main()
