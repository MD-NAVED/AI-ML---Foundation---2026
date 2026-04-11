# Selecting & Filtering
# You often need to separate your features (X) from your target variable (y), or remove irrelevant columns.
# *   **`df.drop()`**: Removes specified rows or columns. Often used to drop the target column from the feature set: `X = df.drop('target', axis=1)`.
# *   **`df.loc[]`**: Label-based indexing to select rows and columns.
# *   **`df.iloc[]`**: Integer/position-based indexing. Useful for splitting sequences or traditional array indexing.
# *   **Boolean Indexing**: Filtering rows based on conditions, e.g., `df[df['Age'] > 18]`.

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

df = pd.DataFrame(
    [[1, 2], [4, 5], [7, 8]],
    index=["cobra", "viper", "sidewinder"],
    columns=["max_speed", "shield"],
)
# print(df)
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




