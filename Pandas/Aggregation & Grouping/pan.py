#  Aggregation & Grouping

# Sometimes you need to aggregate data to create new features (e.g., calculating average spending per customer).

# *   **`df.groupby('col')`**: Groups the DataFrame by a specific column, usually followed by an aggregation function like `.mean()`, `.sum()`, or `.agg()`

# *   **`df.pivot_table()`**: Creates a spreadsheet-style pivot table.

from matplotlib.pyplot import plot
from matplotlib.pyplot import fill
import pandas as pd




# Groupby() method is used to group the DataFrame by a specific column, usually followed by an aggregation function like .mean(), .sum(), or .agg()

df = pd.DataFrame({
    'Fruit': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple'],
    'Store': ['Store A', 'Store A', 'Store B', 'Store B', 'Store A'],
    'Sales_kg': [10, 15, 20, 5, 30]
})

# print(df)

total_sale_per_fruit = df.groupby('Fruit')['Sales_kg'].sum()

# print(total_sale_per_fruit)

total_avg_data = df.groupby('Store')['Sales_kg'].mean()

# print(total_avg_data)

pivot_result = df.pivot_table(
    values='Sales_kg',
    index='Fruit',
    columns='Store',
    aggfunc='sum',
    fill_value= 0
)
print("\n--- Pivot Table Ka Jawab ---")
print(pivot_result)
