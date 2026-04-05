"""
Pandas Practice Script

This script provides a collection of essential Pandas operations and methods, 
serving as a quick reference guide for data manipulation and analysis.

Key concepts covered:
- Creating DataFrames and Series.
- Reading and saving data (CSV, Excel).
- Data inspection (.head(), .tail(), .info(), .describe(), .dtypes, .shape).
- Data selection and filtering (conditional filtering, .isin(), .notna()).
- Indexing and slicing with .loc[] and .iloc[].
"""

import pandas as pd





# df = pd.DataFrame({
#     "Name" : ["Andy", "Bob", "Charlie", "David"],
#     "Age" : [25, 30, 35, 40],
#     "City" : ["New York", "Los Angeles", "Chicago", "Houston"]

# })   

# print(df["Age"]) 

# print(df["Name"])

# print(df["City"])

# ages = pd.Series([22,35,58],name ="Age")


# print(ages.max())

# print(ages.describe())

# print(df["Age"].max())

# print(df["Age"].describe()) 


titanic = pd.read_csv("data/titanic.csv") # .reads_ mathod:- is used to read the csv/excel/json/html/sql/txt file

# print(titanic)  

# print(titanic.head(10)) # .head() method:- is used to display the first 10 rows of the csv file


# print(titanic.tail(10)) # .tail() method:- is used to display the last 10 rows of the csv file      

# print(titanic.dtypes) # .dtypes method:- is used to display the data types of the csv file


# titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False) # .to_excel() method:- is used to save the dataframe to an excel file 


# titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")  # .read_excel() method:- is used to read the excel file


# titanic.info() # .info() method:- is used to display the information of the dataframe

# age = titanic["Age"]
# print(age.head())

# print(type(titanic["Age"])) # .shape method:- is used to display the shape of the dataframe

# print(titanic["Age"].shape) # .shape method:- is used to display the shape of the dataframe


# age_sex = titanic[["Age", "Sex","Name"]] # .[] method:- is used to display the columns of the dataframe
# print(age_sex.head())   
# print( type(titanic[["Age", "Sex"]]))
# print(titanic[["Age","Sex","Name"]].shape)



# print(titanic[titanic["Age"] > 35].shape) 


# class_23 = titanic[titanic["Pclass"].isin([2,3])] # .isin() method:- is used to display the rows of the dataframe that satisfy the condition
# print(class_23.head())  



# class_23 = titanic[titanic["Pclass"] == 2 | titanic["Pclass"] == 3] 
# print(class_23.head())



# age_not_na = titanic[titanic["Age"].notna()] # .notna() method:- is used to display the rows of the dataframe that satisfy the condition
# print(age_not_na.head())

# print(age_not_na.shape)

# adult_names = titanic.loc[titanic["Age"] >= 35,"Name"] # .loc[] method:- is used to display the rows and columns of the dataframe that satisfy the condition
# print(adult_names.head())


# print(titanic.iloc[9:25, 2:5]) # .iloc[] method:- is used to display the rows and columns of the dataframe that satisfy the condition

