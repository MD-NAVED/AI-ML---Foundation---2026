#  Feature Engineering

# 1 = Transforming raw data into meaningful features that the model can understand.

# 2 = **`pd.get_dummies()`**: Performs One-Hot Encoding on categorical variables. ML models usually require numerical input, so converting text categories into binary columns is essential.

# 3 = **`df['col'].apply(func)`**: Applies a custom Python function along an axis of the DataFrame. Great for complex feature transformations.

# 4 = **`df['col'].map(dict_or_func)`**: Maps values of a Series using a given dictionary or function. Good for label encoding (e.g., mapping 'Yes' -> 1, 'No' -> 0).

# 5 = **`pd.to_numeric()`**: Converts arguments to numeric types. Useful when numbers are accidentally loaded as strings.

# 6 = **`pd.to_datetime()`**: Converts strings to datetime objects, allowing you to extract sub-features like year, month, or day of the week via the `.dt` accessor.

# 7 = **`pd.cut()` / `pd.qcut()`**: Bins continuous values into discrete intervals (e.g., converting continuous ages into discrete bins like 'Child', 'Adult', 'Senior').


from numpy import dtype
from sys import prefix
import pandas as pd
import numpy as np
 
# print(pd.get_dummies(s)) # get_dummies is used to convert categorical variables into dummy/indicator variables.

# s1 = ["a","b",np.nan] # nan is a missing value
# # print(pd.get_dummies(s1))

# print(pd.get_dummies(s1,dummy_na=True)) # dummy_na=True is used to convert nan into a dummy variable.


# df = pd.DataFrame({  "A": ["a", "b", "a"],
#                      "B": ["b", "a", "c"], 
#                      "C": [1, 2, 3]})

# # print(pd.get_dummies(df))

# df = pd.get_dummies(df, prefix=["col1","col2"])

# # print(df) # prefix is used to give a prefix to the dummy variables.

# print(pd.get_dummies(pd.Series(list("abc")),drop_first=True)) # drop_first=True is used to drop the first dummy variable.

# print(pd.get_dummies(pd.Series(list("abc")),dtype=float)) # dtype is used to convert the dummy variables into float type.



# .apply() method is used to apply a function along an axis of the DataFrame.



# df = pd.DataFrame({
#     'Branch': ['East', 'East', 'West', 'West'],
#     'Sales': [100, 150, 200, 50],
#     'Returns': [5, 10, 20, 5]
# })

# # def profit_ratio(group):
#     return group['Sales'].sum() / group['Returns'].sum()

# print(df.groupby('Branch').apply(profit_ratio))


# def get_status(group):
#     return pd.Series({
#         'Max_Sales': group['Sales'].max(),
#         'Min_Sales': group['Sales'].min()
#     })

# status = df.groupby('Branch').apply(get_status)
# print(status)


# df = pd.DataFrame({
#     'Category': ['A', 'A', 'B', 'B'],
#     'Value': [10, 20, 30, 40],
#     'Weight': [1, 2, 1, 2]
# })

# print(df)
# weighted_avg = df.groupby('Category').apply(lambda  x: (x['Value']* x['Weight']).sum() / x['Weight'].sum()) 
# print(weighted_avg)


# .map() method is used to map values of a Series using a given dictionary or function.

cat  = pd.Categorical(['a','b','c'])

# print(cat.map(lambda x: x.upper())) # with function

# print(cat.map({'a':1,'b':2,'c':3})) # with dictionary

# print(cat.map({'a': 'first' , 'b': 'second' , 'c': 'third'})) # with index mapping  

# print(cat.map({"a": "first", "b": "second"}, na_action=None)) # with na_action=None

# cat = pd.Categorical(["a", "a", "b"]) 
# calls = []
# def f(x):
#     calls.append(x)
#     return x.upper()
# result = cat.map(f) 
 
# print(result)




# to_numeric method is used to convert arguments to numeric types. Useful when numbers are accidentally loaded as strings.


# s = pd.Series(['10','20.5','30'])
# print(s)

# numerical_s = pd.to_numeric(s)
# print(numerical_s)

s = pd.Series(['1','2','apple','4.5','-'])

# numerical_s = pd.to_numeric(s, errors='coerce')
# print(numerical_s) # errors='coerce' is used to convert non-numeric values to NaN.


# Note: In Pandas 3.0+, `errors='ignore'` has been REMOVED. 
# It will give a ValueError. You can only use 'raise' or 'coerce'.

# =====================================================================================
# pd.to_datetime()
# Used to convert strings/objects into actual datetime objects.
# Essential for Feature Engineering (extracting year, month, day, day of week).
# =====================================================================================

# date_series = pd.Series(['2023-10-01', '2023-10-05', 'Not-a-Date', '2023-10-15'])

# # Convert to datetime, bad data becomes NaT (Not a Time)
# datetime_series = pd.to_datetime(date_series, errors='coerce')
# # print("--- Converted Datetime Series ---")
# # print(datetime_series)

# # # =====================================================================================
# Extracting Features using .dt Accessor
# =====================================================================================
# print("\n--- Extracting Year, Month, Day ---")
# df_dates = pd.DataFrame({'Date': datetime_series})
# df_dates['Year'] = df_dates['Date'].dt.year
# df_dates['Month'] = df_dates['Date'].dt.month
# df_dates['Day_Name'] = df_dates['Date'].dt.day_name() # e.g. Monday, Tuesday

# print(df_dates)


# =====================================================================================
# pd.cut() / pd.qcut()
# Used to bin continuous values into discrete intervals.
# =====================================================================================

ages = pd.Series([10,20,35,37,41,52,57,63])

ages_categories = pd.cut(ages, 
bins =[0,18,60,100],
labels=['Child','Adult','Senior']
)

# print(ages_categories)



marks = ([10,20,30,40,50,60,70,80,90,100])

marks_quartiles = pd.qcut(marks,
q=4,
labels=['Poor','Fair','Good','Excellent']
)

print(marks_quartiles)