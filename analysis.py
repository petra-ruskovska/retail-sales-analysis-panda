import pandas as pd
import matplotlib.pyplot as plt


class RetailSalesAnalyzer:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = None          # raw data
        self.clean_df = None    # cleaned data with Total_Sales column

    # ------------------------------------------------------------------
    # DATA LOADING
    # ------------------------------------------------------------------
    def load_data(self) -> pd.DataFrame:
        """Read the CSV file into a DataFrame."""
        self.df = pd.read_csv(self.filepath)
        return self.df

    def clean_data(self) -> pd.DataFrame:
        """Drop rows with missing values and compute Total_Sales per row."""
        if self.df is None:
            self.load_data()

        self.clean_df = self.df.dropna().copy()
        self.clean_df['Total_Sales'] = (
            self.clean_df['Quantity'] * self.clean_df['Sales']
        )
        return self.clean_df

    # ------------------------------------------------------------------
    # DATA ANALYSING
    # ------------------------------------------------------------------
    def total_sales_per_product(self) -> pd.Series:
        """Total sales (Quantity * Sales) grouped by Product."""
        if self.clean_df is None:
            self.clean_data()
        return self.clean_df.groupby('Product')['Total_Sales'].sum()

    def best_seller(self, n: int = 1) -> pd.Series:
        """Return the top-n best-selling product(s) by total sales."""
        return self.total_sales_per_product().nlargest(n)

    def average_daily_sales(self) -> pd.Series:
        """Average Sales value grouped by Date."""
        if self.clean_df is None:
            self.clean_data()
        return self.clean_df.groupby('Date')['Sales'].mean()

    def summary(self) -> dict:
        """Convenience method returning all key stats in one dict."""
        return {
            'total_sales_per_product': self.total_sales_per_product(),
            'best_seller': self.best_seller(),
            'average_daily_sales': self.average_daily_sales(),
        }

    # ------------------------------------------------------------------
    # DATA VISUALISATION
    # ------------------------------------------------------------------
    def plot_sales_trend(self, figsize=(10, 5)):
        """Line plot of Sales over time (uses row order / Date if sorted)."""
        if self.clean_df is None:
            self.clean_data()

        self.clean_df.sort_values('Date')['Sales'].plot(
            figsize=figsize,
            title='Sales Trend Over Time',
            xlabel='Index / Date',
            ylabel='Sales',
        )
        plt.tight_layout()
        plt.show()

    def plot_sales_per_product(self, figsize=(10, 5), color='skyblue'):
        """Bar chart of total sales per product."""
        totals = self.total_sales_per_product()

        totals.plot.bar(
            title='Sales per Product',
            ylabel='Total Sales',
            xlabel='Product',
            figsize=figsize,
            color=color,
        )
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    analyzer = RetailSalesAnalyzer('retail_sales_demo_values.csv')
    analyzer.load_data()
    analyzer.clean_data()

    print("Total Sales per Product:\n", analyzer.total_sales_per_product())
    print("\nBest seller:\n", analyzer.best_seller())
    print("\nAverage daily sales:\n", analyzer.average_daily_sales())

    analyzer.plot_sales_per_product()
    # analyzer.plot_sales_trend()