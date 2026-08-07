# Retail Sales Analyzer

A small Python class for loading, cleaning, analysing, and visualising retail sales data from a CSV file.

## Files

- `retail_sales_analyzer.py` — the `RetailSalesAnalyzer` class
- `retail_sales_demo_values.csv` — sample data (used as the default input)

## Requirements

- `pandas`
- `matplotlib`

```bash
pip install pandas matplotlib
```

## Expected CSV Format

| Column   | Description                  |
|----------|-------------------------------|
| Date     | Sale date                     |
| Product  | Product name                  |
| Quantity | Units sold                    |
| Sales    | Price per unit                |

## Usage

```python
from retail_sales_analyzer import RetailSalesAnalyzer

# Uses retail_sales_demo_values.csv by default
analyzer = RetailSalesAnalyzer()

# Or point it at your own file
# analyzer = RetailSalesAnalyzer('my_sales_data.csv')

analyzer.load_data()
analyzer.clean_data()

# Statistics
print(analyzer.best_seller())
print(analyzer.average_daily_sales())
print(analyzer.total_sales_per_product())

# Or get everything at once
stats = analyzer.summary()

# Visualisations
analyzer.plot_sales_per_product()
analyzer.plot_sales_trend()
```

## Methods

| Method                          | Description                                      |
|----------------------------------|---------------------------------------------------|
| `load_data()`                   | Reads the CSV into a DataFrame                     |
| `clean_data()`                  | Drops missing rows, adds `Total_Sales` column      |
| `total_sales_per_product()`     | Total sales (Quantity × Sales) grouped by product  |
| `best_seller(n=1)`               | Top-n best-selling product(s)                      |
| `average_daily_sales()`         | Average sale value grouped by date                 |
| `summary()`                     | Returns all stats above as a dict                  |
| `plot_sales_per_product()`      | Bar chart of total sales per product               |
| `plot_sales_trend()`            | Line chart of sales over time                      |

## Notes

- Data cleaning and stat/plot methods will automatically call `load_data()` / `clean_data()` if they haven't been run yet, so you don't need to call every method in order.