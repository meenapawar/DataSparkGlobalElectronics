# Global Electronics Data Analytics Project

## Project Overview
This project focuses on analyzing data for **Global Electronics**, a major consumer electronics retailer, to derive insights that can enhance customer satisfaction, optimize operations, and support business growth. Through **Exploratory Data Analysis (EDA)**, we aim to provide actionable recommendations based on data-driven insights. Our analysis includes **data cleaning and preprocessing**, **data exploration**, and **data visualization** using various tools, as well as database management with **SQL**.

## Problem Statement
Global Electronics, as a leading retailer, seeks to leverage data insights to:
- Improve customer satisfaction.
- Enhance operational efficiency.
- Drive sustainable business growth.

As part of the data analytics team, I am tasked with conducting EDA on datasets containing information on customers, products, sales, stores, and currency exchange rates. The goal is to identify key trends, correlations, and patterns that can guide business strategies.

## Project Workflow

### 1. Data Cleaning and Preprocessing
Data preprocessing ensures the datasets are clean, consistent, and ready for analysis. Key steps include:
- **Handling Missing Values:** Removing or imputing missing values based on their impact on data quality.
- **Data Standardization and Transformation:** Standardizing date formats, managing outliers, and ensuring accurate currency conversions.
- **Data Integration:** Merging datasets to provide a unified view of the data.

### 2. Exploratory Data Analysis (EDA)
EDA provides insights into data distribution, patterns, and outliers. Key steps include:
- **Statistical Analysis:** Summary statistics to understand central tendencies and variations.
- **Data Visualization:** Using histograms, box plots, scatter plots, and more to explore relationships and trends.
- **Correlation Analysis:** Identifying correlations between variables to uncover hidden patterns.

### 3. Data Management with SQL
After data cleaning, preprocessed datasets are imported into SQL tables, enabling efficient data retrieval and management. This step includes:
- **Loading Cleaned Data:** Importing cleaned datasets into SQL tables.
- **Query Development:** Developing SQL queries to extract insights, such as top-selling products, average customer age, and regional sales performance.
- **Data Retrieval for Analysis:** Using SQL to retrieve and aggregate data for EDA and visualization.

### 4. Visualization with Power BI/Tableau
Data visualization allows us to present insights interactively and accessibly. Key visualization steps include:
- **Developing Interactive Dashboards:** Creating dashboards with key metrics such as sales by region, product performance, and customer demographics.

## Technologies and Tools
- **Python:** Data cleaning, preprocessing, and EDA.
- **SQL (MySQL):** Data management and retrieval.
- **Power BI / Tableau:** Data visualization and dashboard development.

## SQL Queries
The following SQL queries have been developed for analysis:
1. Query to fetch the count of customers based on age.
2. Query for calculating the average age of customers.
3. Query to find the purchase frequency of a product.
4. Query for calculating the average customer age by region.
5. Query to count the number of customers in each age group for each country.
6. Query for yearly sales totals.
7. Query to find the top products by quantity sold.
8. Query to find the most popular products by revenue.
9. Query for calculating profit margin by comparing unit cost and unit price.
10. Query for analyzing sales performance across different product categories and subcategories.
11. Query for store performance based on sales, store size (square meters), and operational data (open date).
12. Query for maximum sales by year.
13. Query for minimum sales by year.
14. Query to identify the top brands by revenue.
15. Query to analyze the impact of sales figures, considering exchange rates.

## File Structure
- **SQLqueries.sql**: Contains all SQL queries for data retrieval and analysis.
- **MergeSalesData.py**: Python script for preprocessing data and merging sales data from various sources.
- **LoadInSqlTable.py**: Python script to load cleaned data into SQL tables.
- **DataSpark_PowerBI.pbix**: Power BI file with dashboards and visualizations.
- **DataSpark_PPT.pptx**: Presentation file summarizing the project's findings and recommendations.
- **CreateTableinSQL.sql**: SQL script for creating tables in MySQL database.

---

This README provides a comprehensive overview of the project, including the workflow, tools used, and SQL queries for analysis.
