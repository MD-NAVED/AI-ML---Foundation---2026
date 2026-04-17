# Important Pandas Methods for Machine Learning

When preparing data for Machine Learning, Pandas is your primary tool for data manipulation, cleaning, and feature engineering. Here is a categorized cheat sheet of the most critical Pandas methods you'll use in ML workflows.

<!-- ## 1. Data Input & Output
Before you can train a model, you need to load your data (and potentially save cleaned data later).
*   **`pd.read_csv()`**: Loads data from a CSV file into a DataFrame. (See also: `read_excel()`, `read_sql()`)
*   **`df.to_csv()`**: Saves a DataFrame to a CSV file (often used with `index=False` so you don't save the row numbers). -->

<!-- ## 3. Data Cleaning
Machine learning models cannot handle missing values or incorrect data types well.
*   **`df.isnull()` / `df.isna()`**: Returns a Boolean mask indicating missing values. Often chained with `.sum()` (e.g., `df.isnull().sum()`) to count missing values per column.
*   **`df.dropna()`**: Drops rows or columns containing missing values.
*   **`df.fillna(value)`**: Replaces missing values with a specified value (like the mean, median, or a constant like 0).
*   **`df.drop_duplicates()`**: Removes duplicate rows from the dataset.
*   **`df.replace()`**: Replaces specific values with other values (e.g., replacing '?' with `np.nan`). -->

<!-- ## 4. Selecting & Filtering
You often need to separate your features (X) from your target variable (y), or remove irrelevant columns.
*   **`df.drop()`**: Removes specified rows or columns. Often used to drop the target column from the feature set: `X = df.drop('target', axis=1)`.
*   **`df.loc[]`**: Label-based indexing to select rows and columns.
*   **`df.iloc[]`**: Integer/position-based indexing. Useful for splitting sequences or traditional array indexing.
*   **Boolean Indexing**: Filtering rows based on conditions, e.g., `df[df['Age'] > 18]`. -->

<!-- ## 5. Feature Engineering
Transforming raw data into meaningful features that the model can understand.
*   **`pd.get_dummies()`**: Performs One-Hot Encoding on categorical variables. ML models usually require numerical input, so converting text categories into binary columns is essential.
*   **`df['col'].apply(func)`**: Applies a custom Python function along an axis of the DataFrame. Great for complex feature transformations.
*   **`df['col'].map(dict_or_func)`**: Maps values of a Series using a given dictionary or function. Good for label encoding (e.g., mapping 'Yes' -> 1, 'No' -> 0).
*   **`pd.to_numeric()`**: Converts arguments to numeric types. Useful when numbers are accidentally loaded as strings.
*   **`pd.to_datetime()`**: Converts strings to datetime objects, allowing you to extract sub-features like year, month, or day of the week via the `.dt` accessor.
*   **`pd.cut()` / `pd.qcut()`**: Bins continuous values into discrete intervals (e.g., converting continuous ages into discrete bins like 'Child', 'Adult', 'Senior'). -->

<!-- ## 6. Aggregation & Grouping
Sometimes you need to aggregate data to create new features (e.g., calculating average spending per customer).
*   **`df.groupby('col')`**: Groups the DataFrame by a specific column, usually followed by an aggregation function like `.mean()`, `.sum()`, or `.agg()`.
*   **`df.pivot_table()`**: Creates a spreadsheet-style pivot table. -->

<!-- ## 7. Combining Datasets
If your features are spread across multiple tables, you need to bring them together.
*   **`pd.concat()`**: Concatenates DataFrames along a particular axis (stacking them vertically or horizontally).
*   **`pd.merge()`**: Joins DataFrames based on a common key column (similar to SQL joins). -->
