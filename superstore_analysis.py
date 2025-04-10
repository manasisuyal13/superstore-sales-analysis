# Import Libraries → Pandas (for data handling), Matplotlib & Seaborn (for visualization).
# Load Dataset → Read the CSV file.
# Explore Data → Show basic info, missing values, and dataset preview.
# Clean Data → Remove duplicates and missing values.
# Visualize Data → Create bar plots for sales by region & category.
# Run the Script → Execute everything when the file runs.


# superstore_analysis.py

# 📦 Import required libraries
import pandas as pd                    # For handling dataframes and CSV files
import matplotlib.pyplot as plt        # For visualizing data using basic plots
import seaborn as sns                  # For prettier and informative plots
# (Optional) For connecting to MySQL if needed later
import mysql.connector

# 🧮 Step 1: Load the dataset from a CSV file
def load_data(file_path):
    try:
        # Load the CSV into a pandas DataFrame
        data = pd.read_csv(file_path, encoding='ISO-8859-1')  # ✅ Added correct encoding
        print("✅ Dataset loaded successfully!")
        return data
    except Exception as e:
        # Handle file-not-found or read errors
        print(f"❌ Error loading dataset: {e}")
        return None

# 🔍 Step 2: Explore the dataset (structure, missing values, preview)
def explore_data(data):
    print("\n🔍 Dataset Info:")
    # Data types and column summary
    print(data.info())

    print("\n🧾 First 5 Rows:")
    print(data.head())                                # Preview top 5 rows

    print("\n🧼 Missing Values:")
    # Count missing values in each column
    print(data.isnull().sum())

# 🧹 Step 3: Clean the data
def clean_data(data):
    data.drop_duplicates(inplace=True)                # Remove duplicate rows
    # Remove rows with missing values
    data.dropna(inplace=True)
    print("\n🧹 Data cleaned (duplicates + missing removed)")
    return data

# 📊 Step 4: Visualize the data using bar plots
def visualize_data(data):
    # 🔷 Sales by Region
    plt.figure(figsize=(8, 5))
    sns.barplot(data=data, x='Region', y='Sales', estimator=sum, ci=None)
    plt.title("📍 Total Sales by Region")
    plt.ylabel("Sales (₹)")
    plt.tight_layout()
    plt.show()

    # 🔶 Sales by Category
    plt.figure(figsize=(8, 5))
    sns.barplot(data=data, x='Category', y='Sales',
                estimator=sum, ci=None, palette="Set2")
    plt.title("🛍️ Total Sales by Category")
    plt.ylabel("Sales (₹)")
    plt.tight_layout()
    plt.show()

# 🚀 Main execution function
def main():
    file_path = "superstore.csv"             # 📁 Path to your CSV file
    df = load_data(file_path)                         # Load dataset

    if df is not None:
        explore_data(df)                              # Explore dataset
        df = clean_data(df)                           # Clean dataset
        visualize_data(df)                            # Generate visualizations

# 🔄 Run main() when this script is executed
if __name__ == "__main__":
    main()
