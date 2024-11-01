#1.Query for fetching Count of customers based on age:
SELECT 
    Gender, Age, COUNT(*) AS Customer_Count
FROM
    project.data_spark
GROUP BY Gender , Age
ORDER BY Customer_Count desc;


#2.Query for fetching average age of customer:
SELECT 
    AVG(Age) AS Average_Age
FROM 
    project.data_spark;  


#3.Query for Purchase frequency of a product
SELECT 
    COUNT(Order_Number) AS Purchase_Frequency,
    Product_Name
FROM 
    project.data_spark
GROUP BY 
    Product_Name
    order by count(Order_Number) desc;
    
    
 #4.Query for Count the number of customers in each age group for each country.   
    SELECT 
    Age_Group,
    Cus_Country,
    COUNT(CustomerKey) AS Segment_Size
FROM 
    (
        SELECT 
            CustomerKey,
            CASE 
                WHEN Age BETWEEN 18 AND 25 THEN '18-25'
                WHEN Age BETWEEN 26 AND 35 THEN '26-35'
                WHEN Age BETWEEN 36 AND 45 THEN '36-45'
                WHEN Age BETWEEN 46 AND 60 THEN '46-60'
                ELSE '60+' 
            END AS Age_Group,
            Cus_Country
        FROM 
            project.data_spark
    ) AS Segments
GROUP BY 
    Age_Group, Cus_Country
ORDER BY 
    Segment_Size DESC;


#5.Query for Yearly Sales Totals
SELECT 
    DATE_FORMAT(Order_Date, '%Y') AS Sales_Year,
    SUM(Quantity) AS Total_Sales
FROM
    project.data_spark
GROUP BY Sales_Year
ORDER BY Sales_Year;
    
    
#6.Query for Top Products by Quantity Sold
    SELECT 
    ProductKey,
    Product_Name,
    SUM(Quantity) AS Total_Quantity_Sold
FROM 
    project.data_spark
GROUP BY 
    ProductKey, Product_Name
ORDER BY 
    Total_Quantity_Sold DESC
LIMIT 10;


#7.Query for Most Popular Products by Revenue
SELECT 
    ProductKey,
    Product_Name,
    SUM(Quantity),
    Sum(Unit_price_USD),
    SUM(Quantity * Unit_price_USD) AS Total_Revenue
FROM 
    project.data_spark
GROUP BY 
    ProductKey, Product_Name
ORDER BY 
    Total_Revenue DESC
LIMIT 10;


#8.Query for Calculating profit margin by comparing unit cost and unit price.
SELECT 
    ProductKey,
    Product_Name,
    Unit_price_USD,
    Unit_Cost_USD,
    ((Unit_price_USD - Unit_Cost_USD) / Unit_price_USD) * 100 AS Profit_Margin
FROM 
    project.data_spark;
    
    
#9.Query for sales performance across different product categories and subcategories    
    SELECT 
    Category,
    Subcategory,
    SUM(Unit_price_USD) AS Total_Revenue,
    SUM(Quantity) AS Total_Quantity_Sold,
    AVG(Unit_price_USD) AS Average_Sales_Per_Order
FROM 
    project.data_spark
GROUP BY 
    Category, 
    Subcategory
ORDER BY 
    Total_Revenue DESC;
    
    
#10.Query for store performance based on sales, size (square meters), and operational data (open date).
SELECT 
    Store_Country,
    SUM(Unit_Price_USD) AS Total_Sales,
    COUNT(DISTINCT StoreKey) AS Total_Stores,
    SUM(Square_Meters) AS Total_Square_Meters,
    DATEDIFF(CURDATE(), MIN(Open_Date)) AS Operational_Age,
    SUM(Unit_Price_USD) / COUNT(DISTINCT StoreKey) AS Average_Sales_Per_Store,
    SUM(Unit_Price_USD) / SUM(Square_Meters) AS Sales_Per_Square_Meter,
    SUM(Unit_Price_USD) / DATEDIFF(CURDATE(), MIN(Open_Date)) AS Sales_Per_Day
FROM
    project.data_spark
GROUP BY Store_Country
ORDER BY Total_Sales DESC;
 
 
#11.Query For maximum sale by Year
   SELECT 
    DATE_FORMAT(Order_Date, '%Y') AS Sales_Year, 
    SUM(Unit_Price_USD) AS Total_Sales
FROM 
    project.data_spark
GROUP BY 
    Sales_Year
ORDER BY 
    Total_Sales DESC Limit 1;
    
    
#12.Query For minimum sale by Year
SELECT 
    DATE_FORMAT(Order_Date, '%Y') AS Sales_Year, 
    SUM(Unit_Price_USD) AS Total_Sales
FROM 
    project.data_spark
GROUP BY 
    Sales_Year
ORDER BY 
    Total_Sales ASC Limit 1;
    

#13.Query for Top Brands by Revenue
    SELECT 
    Brand, SUM(Unit_price_USD) AS Total_Revenue
FROM
    project.data_spark
GROUP BY Brand
ORDER BY Total_Revenue DESC
LIMIT 10;


#14.Query to dispaly the impact of sales figures, by considering exchange rates.
SELECT 
    Currency_Code,
    SUM(Unit_price_USD) / MAX(Exchange) AS Total_Sales_USD,
    SUM(Unit_Cost_USD) / MAX(Exchange) AS Total_Cost_USD,
    (SUM(Unit_price_USD) / MAX(Exchange)) - 
     (SUM(Unit_Cost_USD) / MAX(Exchange)) AS Total_Profit_USD
FROM 
    project.data_spark
GROUP BY 
    Currency_Code
HAVING 
    MAX(Exchange) > 0  -- Ensure exchange rate is valid
ORDER BY 
    Total_Sales_USD DESC;