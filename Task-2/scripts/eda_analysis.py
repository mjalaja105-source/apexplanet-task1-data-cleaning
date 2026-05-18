# ==========================================
# TASK 2 - EDA & BUSINESS INTELLIGENCE
# ==========================================

# IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import os

# ==========================================
# CREATE FOLDERS
# ==========================================

os.makedirs("../visualizations", exist_ok=True)
os.makedirs("../reports", exist_ok=True)
os.makedirs("../dashboard_mockup", exist_ok=True)

# ==========================================
# LOAD DATASET
# ==========================================

print("\nLoading Dataset...\n")

df = pd.read_csv("../dataset/cleaned_superstore.csv")

print("Dataset Loaded Successfully!")

# ==========================================
# BASIC DATA INFO
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

# ==========================================
# DESCRIPTIVE STATISTICS
# ==========================================

stats = df.describe(include='all')

stats.to_csv("../reports/descriptive_statistics.csv")

print("\nDescriptive Statistics Saved!")

# ==========================================
# KPI SUMMARY
# ==========================================

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_discount = df['Discount'].mean()

kpi_summary = f"""
=========================
KPI SUMMARY
=========================

Total Sales      : {total_sales:.2f}
Total Profit     : {total_profit:.2f}
Total Orders     : {total_orders}
Average Discount : {avg_discount:.2f}
"""

with open("../reports/kpi_summary.txt", "w", encoding="utf-8") as file:
    file.write(kpi_summary)

print("KPI Summary Saved!")

# ==========================================
# SALES DISTRIBUTION
# ==========================================

plt.figure(figsize=(10,5))

sns.histplot(df['Sales'], bins=30, kde=True)

plt.title("Sales Distribution")

plt.savefig("../visualizations/sales_distribution.png")

plt.close()

# ==========================================
# PROFIT DISTRIBUTION
# ==========================================

plt.figure(figsize=(10,5))

sns.histplot(df['Profit'], bins=30, kde=True)

plt.title("Profit Distribution")

plt.savefig("../visualizations/profit_distribution.png")

plt.close()

# ==========================================
# ORDERS BY REGION
# ==========================================

plt.figure(figsize=(8,5))

df['Region'].value_counts().plot(kind='bar')

plt.title("Orders By Region")

plt.xlabel("Region")
plt.ylabel("Orders")

plt.savefig("../visualizations/orders_by_region.png")

plt.close()

# ==========================================
# SALES BY CATEGORY
# ==========================================

plt.figure(figsize=(8,5))

df.groupby('Category')['Sales'].sum().plot(kind='bar')

plt.title("Sales By Category")

plt.ylabel("Sales")

plt.savefig("../visualizations/sales_by_category.png")

plt.close()

# ==========================================
# SALES VS PROFIT
# ==========================================

plt.figure(figsize=(8,5))

sns.scatterplot(x='Sales', y='Profit', data=df)

plt.title("Sales vs Profit")

plt.savefig("../visualizations/sales_vs_profit.png")

plt.close()

# ==========================================
# DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(8,5))

sns.scatterplot(x='Discount', y='Profit', data=df)

plt.title("Discount vs Profit")

plt.savefig("../visualizations/discount_vs_profit.png")

plt.close()

# ==========================================
# CORRELATION HEATMAP
# ==========================================

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.savefig("../visualizations/correlation_heatmap.png")

plt.close()

# ==========================================
# PAIRPLOT
# ==========================================

pairplot = sns.pairplot(
    numeric_df[['Sales', 'Profit', 'Discount']]
)

pairplot.savefig("../visualizations/pairplot.png")

plt.close()

# ==========================================
# CREATE SQLITE DATABASE
# ==========================================

connection = sqlite3.connect("../reports/superstore.db")

df.to_sql(
    "superstore",
    connection,
    if_exists="replace",
    index=False
)

print("SQLite Database Created!")

# ==========================================
# SQL QUERIES
# ==========================================

queries = {

    "Top 5 Sales":

    """
    SELECT Category, SUM(Sales) as Total_Sales
    FROM superstore
    GROUP BY Category
    ORDER BY Total_Sales DESC
    LIMIT 5;
    """,

    "Profit By Region":

    """
    SELECT Region, SUM(Profit) as Total_Profit
    FROM superstore
    GROUP BY Region;
    """,

    "Average Discount":

    """
    SELECT AVG(Discount) as Avg_Discount
    FROM superstore;
    """,

    "Top Customers":

    """
    SELECT "Customer Name", SUM(Sales) as Total_Sales
    FROM superstore
    GROUP BY "Customer Name"
    ORDER BY Total_Sales DESC
    LIMIT 10;
    """
}

results = ""

for title, query in queries.items():

    result = pd.read_sql_query(query, connection)

    results += f"\n\n====================\n{title}\n====================\n"

    results += result.to_string(index=False)

with open(
    "../reports/sql_query_results.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(results)

print("SQL Query Results Saved!")

# ==========================================
# CREATE SQL FILE
# ==========================================

sql_script = ""

for title, query in queries.items():

    sql_script += f"\n-- {title}\n{query}\n"

with open(
    "sql_queries.sql",
    "w",
    encoding="utf-8"
) as file:

    file.write(sql_script)

print("SQL File Created!")

# ==========================================
# EDA REPORT
# ==========================================

eda_report = f"""
=================================
EDA REPORT
=================================

1. Dataset contains sales transactions.

2. Highest sales observed in certain categories.

3. Correlation analysis performed on:
   - Sales
   - Profit
   - Discount

4. Multiple visualizations generated.

5. SQL business questions answered.

6. KPI summary created successfully.

Task 2 completed successfully.
"""

with open(
    "../reports/eda_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(eda_report)

print("EDA Report Saved!")

# ==========================================
# DASHBOARD MOCKUP
# ==========================================

plt.figure(figsize=(12,6))

plt.text(
    0.3,
    0.8,
    "BUSINESS DASHBOARD MOCKUP",
    fontsize=20
)

plt.text(0.1,0.6,f"Total Sales : {total_sales:.2f}")
plt.text(0.1,0.5,f"Total Profit : {total_profit:.2f}")
plt.text(0.1,0.4,f"Total Orders : {total_orders}")

plt.axis('off')

plt.savefig("../dashboard_mockup/dashboard_mockup.png")

plt.close()

print("Dashboard Mockup Saved!")

# ==========================================
# CLOSE DATABASE
# ==========================================

connection.close()

print("\nTASK 2 COMPLETED SUCCESSFULLY!")