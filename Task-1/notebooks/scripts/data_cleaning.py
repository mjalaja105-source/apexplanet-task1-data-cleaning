# =========================
# APEX INTERNSHIP - TASK 1
# DATA IMMERSION & WRANGLING
# =========================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# CREATE OUTPUT FOLDERS
# =========================

os.makedirs("../data/cleaned", exist_ok=True)
os.makedirs("../visuals", exist_ok=True)
os.makedirs("../reports", exist_ok=True)

# =========================
# LOAD DATASET
# =========================

print("\nLoading Dataset...\n")

df = pd.read_csv(
    "../data/raw/Sample - Superstore.csv",
    encoding='latin1'
)

print("Dataset Loaded Successfully!\n")

# =========================
# BASIC DATA EXPLORATION
# =========================

print("========== FIRST 5 ROWS ==========\n")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns)

print("\n========== DATASET INFO ==========\n")
print(df.info())

print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())

# =========================
# CHECK MISSING VALUES
# =========================

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# Fill missing values
df.ffill(inplace=True)

print("\nMissing Values Handled Successfully!")

# =========================
# CHECK DUPLICATES
# =========================

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows Found: {duplicates}")

df.drop_duplicates(inplace=True)

print("Duplicates Removed Successfully!")

# =========================
# DATE FORMAT CONVERSION
# =========================

if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])

if 'Ship Date' in df.columns:
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print("\nDate Formatting Completed!")

# =========================
# STANDARDIZE TEXT COLUMNS
# =========================

text_columns = df.select_dtypes(include='object').columns

for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.title()

print("\nText Standardization Completed!")

# =========================
# FEATURE ENGINEERING
# =========================

if 'Order Date' in df.columns:

    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month
    df['Order Day'] = df['Order Date'].dt.day

print("\nFeature Engineering Completed!")

# =========================
# OUTLIER VISUALIZATION
# =========================

if 'Sales' in df.columns:

    plt.figure(figsize=(10, 5))

    sns.boxplot(x=df['Sales'])

    plt.title("Sales Outlier Detection")

    plt.savefig("../visuals/sales_outliers.png")

    plt.close()

print("\nOutlier Visualization Saved!")

# =========================
# SALES DISTRIBUTION
# =========================

if 'Sales' in df.columns:

    plt.figure(figsize=(10, 5))

    sns.histplot(df['Sales'], bins=30, kde=True)

    plt.title("Sales Distribution")

    plt.xlabel("Sales")
    plt.ylabel("Frequency")

    plt.savefig("../visuals/sales_distribution.png")

    plt.close()

print("Sales Distribution Chart Saved!")

# =========================
# CATEGORY COUNT VISUALIZATION
# =========================

if 'Category' in df.columns:

    plt.figure(figsize=(8, 5))

    df['Category'].value_counts().plot(kind='bar')

    plt.title("Category Count")

    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.savefig("../visuals/category_count.png")

    plt.close()

print("Category Count Chart Saved!")

# =========================
# SAVE CLEANED DATASET
# =========================

cleaned_file = "../data/cleaned/cleaned_superstore.csv"

df.to_csv(cleaned_file, index=False)

print(f"\nCleaned Dataset Saved Successfully!")
print(f"Location: {cleaned_file}")

# =========================
# CREATE DATA DICTIONARY
# =========================

data_dictionary = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Description": ["Add Description Here"] * len(df.columns)
})

data_dictionary.to_excel(
    "../reports/data_dictionary.xlsx",
    index=False
)

print("\nData Dictionary Created Successfully!")

# =========================
# PROJECT SUMMARY
# =========================

summary = f"""
===================================
FINAL PROJECT SUMMARY
===================================

Rows After Cleaning : {df.shape[0]}
Columns             : {df.shape[1]}

Tasks Completed:
[Done] Missing Value Handling
[Done] Duplicate Removal
[Done] Date Formatting
[Done] Text Standardization
[Done] Feature Engineering
[Done] Outlier Visualization
[Done] Data Visualization
[Done] Clean Dataset Export
[Done] Data Dictionary Creation

Project Completed Successfully!
"""

print(summary)

# =========================
# SAVE SUMMARY REPORT
# =========================

with open(
    "../reports/project_summary.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(summary)

print("Project Summary Saved Successfully!")

# =========================
# FINAL MESSAGE
# =========================

print("\nTASK 1 COMPLETED SUCCESSFULLY!")

# =========================
# CREATE README.md
# =========================

readme_content = """
# Apex Internship - Task 1
## Data Immersion & Wrangling

### Objective
The objective of this project is to clean and prepare raw business data for analysis using Python and data analytics techniques.

---

## Tools & Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code
- GitHub

---

## Dataset Used
Superstore Sales Dataset

---

## Tasks Performed
- Data loading and profiling
- Missing value handling
- Duplicate removal
- Date formatting
- Text standardization
- Feature engineering
- Outlier detection
- Data visualization
- Clean dataset generation

---

## Output Files

### Cleaned Dataset
- cleaned_superstore.csv

### Reports
- data_dictionary.xlsx
- project_summary.txt

### Visualizations
- sales_distribution.png
- sales_outliers.png
- category_count.png

---

## Project Outcome
Successfully transformed raw dataset into an analysis-ready dataset for future business intelligence and analytics tasks.

---

## Internship
ApexPlanet Software Pvt. Ltd.
Data Analytics Internship
"""

with open("../README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("README.md Created Successfully!")

# =========================
# CREATE .gitignore
# =========================

gitignore_content = """
.venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
"""

with open("../.gitignore", "w", encoding="utf-8") as file:
    file.write(gitignore_content)

print(".gitignore Created Successfully!")