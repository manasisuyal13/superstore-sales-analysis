🍋 Superstore Sales Analysis

This project analyzes and visualizes sales data from a fictional retail superstore using Python and MySQL. It is designed for data enthusiasts, students, and professionals looking to learn real-world data analysis techniques such as data cleaning, visualization, and SQL integration.

📊 Features

Load and clean sales data from a CSV file

Explore data structure and detect missing values

Visualize sales by region and category using Matplotlib & Seaborn

Identify top-selling products

Insert dataset into a MySQL database securely using environment variables

Modular scripts for analysis, visualization, and database loading

📁 Project Structure

📁 Superstore Sales Analysis
├── superstore_analysis.py # Main script: load, clean, explore, and visualize
├── analyze_sales.py # Extra visualizations (top products, sales by category)
├── insert_to_mysql.py # Load data into MySQL from CSV
├── superstore.sql # SQL script for table creation
├── superstore.csv # CSV dataset (not uploaded to GitHub)
├── .gitignore # Files and folders to ignore (includes .env)
├── requirements.txt # Required Python packages
└── README.md # Project documentation (you are here!)

🔧 Installation & Usage

1. Clone the Repository

git clone https://github.com/manasisuyal13/superstore-sales-analysis.git
cd superstore-sales-analysis

2. Install Dependencies

pip install -r requirements.txt

3. Set Up Environment Variables

Create a .env file in the root directory:

MYSQL_HOST=localhost
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=SuperstoreDB

4. Run Scripts

📊 Run Main Analysis

python superstore_analysis.py

💼 Insert Data into MySQL

python insert_to_mysql.py

📊 View Top Products and Category Sales

python analyze_sales.py

📈 SQL Table Structure (superstore.sql)

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

📊 requirements.txt

pandas
matplotlib
seaborn
mysql-connector-python
python-dotenv

👤 Author

Manasi Suyal

🔒 License

MIT License — Free to use and modify.

✨ Feel free to fork this project, suggest improvements, or star it to show support!
