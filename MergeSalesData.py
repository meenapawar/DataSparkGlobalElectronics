#Load the data
import pandas as pd
from datetime import datetime

sales_data_raw = pd.read_csv(r'C:\Users\ramya\OneDrive\Documents\Python Scripts\DataSpark\Sales.csv')
customers_data_raw = pd.read_csv(r'C:\Users\ramya\OneDrive\Documents\Python Scripts\DataSpark\Customers.csv', encoding='Windows-1252')
products_data_raw = pd.read_csv(r'C:\Users\ramya\OneDrive\Documents\Python Scripts\DataSpark\Products.csv')
stores_data_raw = pd.read_csv(r'C:\Users\ramya\OneDrive\Documents\Python Scripts\DataSpark\Stores.csv')
Exchange_data_raw = pd.read_csv(r'C:\Users\ramya\OneDrive\Documents\Python Scripts\DataSpark\Exchange_Rates.csv')

#Print the info of all the table
print(sales_data_raw.info()) #Col rename, delivery date can be dropped, dates have object dtype, unique key [order number]
print(customers_data_raw.info())#Col rename, zip code can be dropped, birthday convert to date and calculate age,unique key [customerkey]
print(products_data_raw.info())#Col rename, unique key [product key]
print(stores_data_raw.info())#Col rename, null in squre meters, open date to date, unique key [store key]
print(Exchange_data_raw.info())#Col rename, Date to date, unique key[currency]

#sales_info cleaning
#rename column
sales_data_raw = sales_data_raw.rename(columns = {'Order Number':'Order_Number', 'Line Item':'Line_Item', 'Order Date':'Order_Date', 'Delivery Date':'Delivery_date', 'Currency Code':'Currency_Code'})

#check for the data type and convert if wrong
sales_data_raw['Order_Date'] = pd.to_datetime(sales_data_raw['Order_Date'])

#check for null value and handle
sales_data_raw = sales_data_raw.drop(['Delivery_date'], axis=1)

print("Sales datatype", sales_data_raw.dtypes)
print("Sales null", sales_data_raw.isnull().sum())
print("Sales Duplicate", sales_data_raw.duplicated().sum())
print(sales_data_raw.head())

sales_data_raw.to_csv('Clean_sales.csv', index=False)


#customer_info cleaning
#rename column
customers_data_raw = customers_data_raw.rename(columns={'City': 'Cus_City', 'State': 'Cus_State', 'Country': 'Cus_Country'})

#drop state and zip codes
customers_data_raw = customers_data_raw.drop(['Zip Code'], axis=1)
customers_data_raw = customers_data_raw.drop(['State Code'], axis=1)
customers_data_raw = customers_data_raw.drop(['Continent'], axis=1)

#check for the data type and convert if wrong
customers_data_raw['Birthday'] = pd.to_datetime(customers_data_raw['Birthday'])

# Define a function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Calculate the age for each customer
age = customers_data_raw['Birthday'].apply(calculate_age)

# Insert the 'Age' column right after 'Birthday'
birthday_index = customers_data_raw.columns.get_loc('Birthday')
customers_data_raw.insert(birthday_index + 1, 'Age', age)

print("Customer datatype", customers_data_raw.dtypes)
print("Customer null", customers_data_raw.isnull().sum())
print("Customer Duplicate", customers_data_raw.duplicated().sum())
print(customers_data_raw.head())

customers_data_raw.to_csv('Clean_customers.csv', index=False)

#Products_info cleaning
#rename column
products_data_raw = products_data_raw.rename(columns={'Product Name': 'Product_Name', 'Unit Cost USD': 'Unit_Cost_USD', 'Unit Price USD': 'Unit_price_USD'})

print("products datatype", sales_data_raw.dtypes)
print("products null", products_data_raw.isnull().sum())
print("products Duplicate", products_data_raw.duplicated().sum())
print(products_data_raw.head())

products_data_raw.to_csv('Clean_products.csv', index=False)


#Stores info Clean
#replace NA cell with 0
stores_data_raw.fillna(0, inplace=True)

#Rename the column
stores_data_raw = stores_data_raw.rename(columns={'Country': 'Store_Country', 'State': 'Store_State', 'Square Meters': 'Square_Meters', 'Open Date': 'Open_Date'})

#datatype conversion
stores_data_raw['Open_Date'] = pd.to_datetime(stores_data_raw['Open_Date'])

print("Stores datatype", stores_data_raw.dtypes)
print("Stores null", stores_data_raw.isnull().sum())
print("Stores Duplicate", stores_data_raw.duplicated().sum())
print(stores_data_raw.head())

stores_data_raw.to_csv('Clean_stores.csv', index=False)

#Stores info Clean
#datatype conversion
Exchange_data_raw['Date'] = pd.to_datetime(Exchange_data_raw['Date'])

print("rate datatype", Exchange_data_raw.dtypes)
print("rate null", Exchange_data_raw.isnull().sum())
print("rate Duplicate", Exchange_data_raw.duplicated().sum())
print(Exchange_data_raw.head())

Exchange_data_raw.to_csv('Clean_exchange_rate.csv', index=False)

#merge all the CSV file to a single file
df1 = pd.merge(sales_data_raw, customers_data_raw, how='inner', on='CustomerKey')
df2 = pd.merge(df1, stores_data_raw, how='inner',on='StoreKey')
df3 = pd.merge(df2, products_data_raw, how='inner',on='ProductKey')
Merged_sales_data = pd.merge(df3, Exchange_data_raw,how='inner' , left_on=['Order_Date', 'Currency_Code'], right_on=['Date', 'Currency'])
#order_date and date are similar and currency and currency_code are similar
Merged_sales_data = Merged_sales_data.drop(columns=['Date', 'Currency'])

print("merged datatype", Merged_sales_data.dtypes)
print("merged null", Merged_sales_data.isnull().sum())
print("merged Duplicate", Merged_sales_data.duplicated().sum())
print(Merged_sales_data.head())


Merged_sales_data.to_csv('Merged_sales_Data.csv', index=False)
