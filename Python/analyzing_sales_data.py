# Import data
import pandas as pd
df = pd.read_csv("sample-store.csv")


# Change column names(lowercase, remove any special character, clean redundant words in the name)
df.columns = df.columns.str.lower()\
    .str.replace(" ","_")\
    .str.replace("-","_")\
    .str.replace("/region","")


# Convert str to date
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['order_date'])

df[['order_date','ship_date']]


# Count missing value
df.isna().sum()


# Filter data row contain missing values
df = df.dropna()
df = df.reset_index()


# Count no. of columns and rows
print(f"Columns: {len(df.columns)}")
print(f"Columns: {len(df['row_id'])}")


# Export data of California into csv file
sample_store_california = df.query("state == 'California'")

sample_store_california.to_csv('sample_store_california.csv')


# Export data of California and Texas in 2017 into csv file
store_california_texas_2017 = df[df['order_date'].dt.year == 2017]\
    .query("state == 'California' | state == 'Texas'")

store_california_texas_2017.to_csv('store_california_texas_2017.csv')


# Show total sales, average sales and its std in 2017
df[df['order_date'].dt.year == 2017]['sales'].agg(['sum', 'mean', 'std']).round(2)


# Show bottom 5 states in sales betwenn 15 Apr 2017 to 31 Dec 2019
df[(df['order_date'] >= '2017-04-15') & (df['order_date'] <= '2019-12-31')]\
    .groupby('state')[['state', 'sales']]\
    .sum().sort_values('sales').head(5)


# Find proportion of total sales of West + Central Region in 2017
df_2017 = df[df['order_date'].dt.year == 2019]

(df_2017.query("region == 'West' | region == 'Central'")['sales'].sum() / df_2017['sales'].sum()).round(4)


# Top 10 products with highest no. of quantity sold
df_2019_2020 = df[(df['order_date'].dt.year >= 2019) & (df['order_date'].dt.year <= 2020)]

df_2019_2020[['sub_category', 'quantity', 'sales']]\
    .groupby('sub_category').sum()\
    .sort_values('quantity', ascending=False).head(10)


# Top 10 products with highest total sales
df_2019_2020 = df[(df['order_date'].dt.year >= 2019) & (df['order_date'].dt.year <= 2020)]

df_2019_2020[['sub_category', 'quantity', 'sales']]\
    .groupby('sub_category').sum()\
    .sort_values('sales', ascending=False).head(10)


# Create a bar graph
df[['category', 'sub_category', 'sales']]\
    .groupby('category').sum()\
    .sort_values('sales', ascending=False)\
    .plot(kind='bar')


# Find sub-category with lowest profit
df[['sub_category', 'sales', 'profit']].groupby('sub_category').sum().round(2).sort_values('profit')
