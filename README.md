# Superstore Sales Analysis

## ✨ Project Overview

Analyze and visualize sales data from a fictional retail superstore using **Python**, **Pandas**, **Seaborn**, **Matplotlib**, and **MySQL**. This project is ideal for data science learners and professionals looking to practice real-world data workflows.

---

## 📊 Features

- Load and clean sales data from a CSV file
- Detect and remove missing or duplicate values
- Visualize sales performance by region and product category
- Identify top-selling products
- Load cleaned data into a MySQL database using environment variables
- Organized and modular script structure

---

## 📁 Project Structure

```
📁 Superstore Sales Analysis
├── superstore_analysis.py      # Load, clean, explore, and visualize
├── analyze_sales.py           # Visualize category sales and top products
├── insert_to_mysql.py         # Insert cleaned data into MySQL
├── superstore.sql             # SQL schema for MySQL table
├── superstore.csv             # Dataset (not uploaded to GitHub)
├── .gitignore                 # Git ignored files (includes .env)
├── requirements.txt           # List of required Python packages
└── README.md                  # This file
```

---

## ⚙️ Getting Started

### ✔️ 1. Clone the Repository
```bash
git clone https://github.com/manasisuyal13/superstore-sales-analysis.git
cd superstore-sales-analysis
```

### ✔️ 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### ✔️ 3. Set Up Environment Variables
Create a `.env` file in your project root:
```
MYSQL_HOST=localhost
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=SuperstoreDB
```

---

## 🚀 Usage

### 📊 Run the Main Analysis
```bash
python superstore_analysis.py
```
- Cleans the data
- Shows basic info and missing values
- Plots sales by region and category

### 💼 Load Data into MySQL
```bash
python insert_to_mysql.py
```
- Connects to MySQL
- Creates `superstore` table
- Loads data from CSV

### 🔍 Visualize Top Products and Category Sales
```bash
python analyze_sales.py
```
- Horizontal bar plot of category-wise sales
- Printout of top 5 best-selling products

---

## 📈 SQL Schema (`superstore.sql`)
```sql
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
);
```

---

## 📄 Requirements
```txt
pandas
matplotlib
seaborn
mysql-connector-python
python-dotenv
```

---

## 👤 Author
**Manasi Suyal**

---

## 🔒 License
MIT License — Free to use and modify.

---

> ✨ Feel free to star this repo, fork it, or suggest improvements!

