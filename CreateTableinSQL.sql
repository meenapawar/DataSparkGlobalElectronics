CREATE TABLE Project.data_spark (
    Order_Number INT,
	Line_Item INT,
	Order_Date DATE,
	CustomerKey INT,
	StoreKey INT,
	ProductKey INT,
	Quantity INT,
	Currency_Code TEXT,
	Gender TEXT,
	Name TEXT,
	Cus_City TEXT,
	Cus_State TEXT,
	Cus_Country TEXT,
	Birthday DATETIME,
	Age INT,
    Store_Country TEXT,
	Store_State TEXT,
	Square_Meters FLOAT,
	Open_Date DATE,
	Product_Name TEXT,
	Brand TEXT,
	Color TEXT,
	Unit_Cost_USD TEXT,
	Unit_price_USD TEXT,
	SubcategoryKey INT,
	Subcategory TEXT,
	CategoryKey INT,
	Category TEXT,
	Exchange FLOAT
);


UPDATE project.data_spark
SET Unit_price_USD = CAST(REPLACE(REPLACE(TRIM(Unit_price_USD), '$', ''), ',', '') AS DECIMAL(10, 2));

UPDATE project.data_spark
SET Unit_Cost_USD = CAST(REPLACE(REPLACE(TRIM(Unit_Cost_USD), '$', ''), ',', '') AS DECIMAL(10, 2));

#delete from project.data_spark;

#SET SQL_SAFE_UPDATES = 1;


