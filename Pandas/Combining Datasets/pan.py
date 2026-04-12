# Combining Datasets

# If your features are spread across multiple tables, you need to bring them together.

# *   **`pd.concat()`**: Concatenates DataFrames along a particular axis (stacking them vertically or horizontally).

# *   **`pd.merge()`**: Joins DataFrames based on a common key column (similar to SQL joins).


import pandas as pd


#concat() :-

# df1 = pd.DataFrame({
#     "Name" : ['Anmit','Bhavna'],
#     "Score":['85',92]
# })

# df2 = pd.DataFrame({
#     'Name': ['Chetan', 'Diya'],
#     'Score': [78, 88]
# })

# # print(df1)
# # print(df2)

# combine_df = pd.concat([df1, df2],ignore_index=True)
# combine_df = pd.concat([df1, df2],ignore_index=True,axis=1)
# # print(combine_df)


# # mearge() :-

# df_students = pd.DataFrame({
#     'Roll_No': [1, 2, 3],
#     'Name': ['Amit', 'Bhavna', 'Chetan']
# })


# df_marks = pd.DataFrame({
#     'Roll_No': [2, 1, 4],
#     'Subject_Marks': [95, 88, 70]
# })

# final_result = pd.merge(df_students,df_marks,on='Roll_No',how='outer') # inner, left, right, outer
# print(final_result)


