# Selecting & Filtering
# You often need to separate your features (X) from your target variable (y), or remove irrelevant columns.
# *   **`df.drop()`**: Removes specified rows or columns. Often used to drop the target column from the feature set: `X = df.drop('target', axis=1)`.
# *   **`df.loc[]`**: Label-based indexing to select rows and columns.
# *   **`df.iloc[]`**: Integer/position-based indexing. Useful for splitting sequences or traditional array indexing.
# *   **Boolean Indexing**: Filtering rows based on conditions, e.g., `df[df['Age'] > 18]`.

from matplotlib.cbook import print_cycles
import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [6, 7, 8, 9, 10],
#     'C': [11, 12, 13, 14, 15]
# })


#  # axis=0 is used to drop rows, axis=1 is used to drop columns.
# print(df.drop(4, axis=0))
# print(df.drop('A', axis=1))
# print(df.drop(0 ,axis=0),df.drop("A",axis=1))

# loc is used to select rows and columns by label
# print(df.loc[0:2,["A","B"]])
# print(df.loc[2:4, ["B","C"]])  

# df = pd.DataFrame(
#     [[1, 2], [4, 5], [7, 8]],
#     index=["cobra", "viper", "sidewinder"],
#     columns=["max_speed", "shield"],
# )
# # print(df)
# # print(df.loc[["viper", "cobra"], ["max_speed", "shield"]])
# # print(df.loc[["cobra", "viper"]])   
# print(df.loc["cobra" : "sidewinder", "max_speed"])


# Alignable boolean Series
# print(df.loc[
#     pd.Series([False, True,False],index=["cobra", "viper", "sidewinder"])
# ])  


#Index (same behavior as df.reindex)
# print(df.loc[pd.Index(["cobra","viper"], name="python")])
# # print(df.loc[pd.Index(["cobra", "viper"], name="foo")])


mydict = [
    {"a": 1,    "b" : 2,   "c": 3,   "d": 4},
    {"a": 100,  "b": 200,  "c": 300, "d": 400},
    {"a": 1000, "b": 2000, "c": 3000,"d": 4000},
] 
df   = pd.DataFrame(mydict)


# print(type(df.iloc[0,1,2])) # pands series
# print(df.ilocloc[[0]]) # pandas dataframe
# print(type(df.iloc[[0]])) # pandas dataframe

# print(df.iloc[[1,2]])

# print(df.iloc[: 3]) # slicing

# print(df.iloc[1:3]) # slicing

# print(df.iloc[:, 1:3]) # columns slicing

# print(df.iloc[1:3, 1:3]) # rows and columns slicing

# print(df.iloc[[True,False,True]]) # boolean indexing means (True=1, False=0)

# print(df.iloc[lambda x: x.index % 2 == 0]) # lambda function is used to select rows and columns by label

# print(df.iloc[0 ,1])

# print(df.iloc[[0,2],[1,3]]) # rows and columns slicing list of integers

# print(df.iloc[1:3,0:3]) # by object slicing

# print(df.iloc[:,lambda df:[0,1,2]]) #df is the dataframe and [0,1,2] is the list of columns to be selected
