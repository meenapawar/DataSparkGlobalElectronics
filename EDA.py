# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv(r"C:\Users\ramya\PycharmProjects\pythonProject1\DataSpark\Merged_sales_Data.csv")  # Replace with your dataset's file path

#Data columns histogram
data_hist = data.hist(figsize=(15,15))

# Gender & Age Distribution
plt.figure(figsize=(10, 5))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.show()

# Geographic Distribution
plt.figure(figsize=(12, 6))
data['Cus_Country'].value_counts().plot(kind='bar')
plt.title("Customer Country Distribution")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# Quantity Analysis
plt.figure(figsize=(20, 10))
sns.histplot(data['Brand'], bins=20, kde=True)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.show()

# Currency Code Distribution
sns.countplot(y='Currency_Code', data=data, order=data['Currency_Code'].value_counts().index)
plt.title("Currency Code Distribution")
plt.show()

# Popular Products
top_products = data['Product_Name'].value_counts().head(10)
plt.figure(figsize=(20, 10))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Most Popular Products")
plt.xlabel("Number of Orders")
plt.show()

# Sales by Category
category_sales = data.groupby('Category')['Quantity'].sum().sort_values()
plt.figure(figsize=(10, 6))
category_sales.plot(kind='barh')
plt.title("Total Sales by Category")
plt.xlabel("Total Quantity Sold")
plt.show()

# Subcategory Analysis
subcategory_sales = data.groupby('Subcategory')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(y=subcategory_sales.index, x=subcategory_sales.values)
plt.title("Top 10 Subcategories by Quantity Sold")
plt.xlabel("Total Quantity")
plt.show()
