#  Data Cleaning
# Machine learning models cannot handle missing values or incorrect data types well.
# *   **`df.isnull()` / `df.isna()`**: Returns a Boolean mask indicating missing values. Often chained with `.sum()` (e.g., `df.isnull().sum()`) to count missing values per column.
# *   **`df.dropna()`**: Drops rows or columns containing missing values.
# *   **`df.fillna(value)`**: Replaces missing values with a specified value (like the mean, median, or a constant like 0).
# *   **`df.drop_duplicates()`**: Removes duplicate rows from the dataset.
# *   **`df.replace()`**: Replaces specific values with other values (e.g., replacing '?' with `np.nan`).


from pandas.core import series
import pandas as pd
import numpy as np





# df = pd.DataFrame(dict(
#      age=[5, 6, np.nan],
#         born=[
#             pd.NaT,
#             pd.Timestamp("1939-05-27"),
#             pd.Timestamp("1940-04-25"),
#         ],
#         name=["Alfred", "Batman", ""],
#         toy=[None, "Batmobile", "Joker"],
# ))


# print(df) # this is printing df normally! just as i expected it to be! 
# print(df.isna()) # isna() - is used to check for missing values in the dataframe. It returns a boolean mask(true/false) indicating missing values. True means missing value and False means not a missing value. 
# print(df.isna().sum()) # sum() - is used to count the number of missing values in the dataframe. 
# print(df.isnull()) # isnull() - is used to check for missing values in the dataframe. It returns a boolean mask(true/false) indicating missing values. True means missing value and False means not a missing value. Same as isna()!

# print(df["age"].isna()) #you can also use on series.df



# print(df.notna()) # notna() - is used to check for non-missing values in the dataframe. It returns a boolean mask(true/false) indicating non-missing values. True means not a missing value and False means missing value. Same as isnull()!
# print(df[["toy", "age"]].notna()) # you can also use on series.df


# # print(df["age"].dropna()) # dropna() - is used to drop missing values from the dataframe. It returns a new dataframe with missing values dropped. 

# df = pd.DataFrame(
#     {
#         "name": ["Alfred", "Batman", "Catwoman"],
#         "toy": [np.nan, "Batmobile", "Bullwhip"],
#         "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
#     }
# )
# print(df)

# print(df.dropna()) # dropna() - is used to drop missing values from the dataframe. It returns a new dataframe with missing values dropped. 
# print(df.dropna(axis="columns")) # axis="columns" - is used to drop columns containing missing values. 
# print(df.dropna(how="all")) # how="all" - is used to drop rows or columns containing all missing values. 

# print(df.fillna(value=0)) # fillna() - is used to fill missing values in the dataframe. It returns a new dataframe with missing values filled. 
# print(df["born"].fillna(value=0)) # it is also works on serie


df = pd.DataFrame({
    "brand": ["YAMAHA", "HONDA", "YAMAHA", "BMW", "HONDA", "BMW"],
    "price": [215000, 150000, 215000, 1500000, 150000, 1500000],
    "color": ["red", "blue", "red", "black", "blue", "black"]
})

# print(df.duplicated()) # duplicates() - is used to check for duplicate values in the dataframe. It returns a boolean mask(true/false) indicating duplicate values. True means duplicate value and False means not a duplicate value. 
# print(df.drop_duplicates()) # drop_duplicates() - is used to drop duplicate values from the dataframe. It returns a new dataframe with duplicate values dropped. 
# print(df["brand"].drop_duplicates())


# replace mathod:-


# series replacement

# s = pd.Series([1,2,3,4,5])
# print(s.replace(4, 0)) # replace() - is used to replace values in the dataframe. It returns a new dataframe with values replaced. 


# dataframe replacement
# df = pd.DataFrame({
#     "A": [1,2,3,4,5],
#     "B": [6,7,8,9,10],
#     "C": ["a","b","c","d","e"]
# })
# # print(df)
# print(df.replace(4, 0)) # replace() - is used to replace values in the dataframe. It returns a new dataframe with values replaced. 


# list like replacment
# print(df.replace([1,2,3,4,5], 0))

# dictionary like replacment
# print(df.replace({1: 0, 2: 1, 3: 2, 4: 3, 5: 4}))
# print(df.replace({"A": {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}}))
# print(df.replace({2 : 10 , 4:100})) 
# print(df.replace({"A":{1:100 , 4:400}}))

# to_replace:-  

# s = pd.Series([10, "a","a","c","a"])
# print(s.replace(to_replace = "a", value=np.nan)) # to_replace() - is used to replace values in the dataframe. It returns a new dataframe with values replaced. 





df = pd.DataFrame(
   {
       "A": [0, 1, 2, 3, 4],
       "B": ["a", "b", "c", "d", "e"],
       "C": ["f", "g", "h", "i", "j"],
   }
)

# print(df.replace(to_replace = "[a-g]",  value="e", regex=True)) # regex=True - is used to replace values in the dataframe. It returns a new dataframe with values replaced.

# print(df.replace(to_replace={"B": "[a-b]" ,"C":"[h-j]"}, value="e" , regex=True))

