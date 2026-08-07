import pandas as pd

## READ DATA
df = pd.read_csv('retail_sales_demo_values.csv')

## DATA CLEANING
# Remove rows with missing values in any column
new_df = df.dropna()

## DATA MANIPULATION AND ANALYSIS
# Calculating Total Sales per Product
new_df['Total_Sales'] = new_df['Quantity'] * new_df['Sales']
product_sales = new_df.groupby('Product')['Total_Sales'].sum()

# Identify the best-selling product
best_seller = product_sales.nlargest(1)

# Compute average daily sales
average_daily_sales = new_df.groupby('Date')['Sales'].mean()

## VISUALISATION
# Plot sales trends over time


# Display sales per product in a bar chart

