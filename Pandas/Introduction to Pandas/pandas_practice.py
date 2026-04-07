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
import matplotlib.pyplot as plt 





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


# air_quality = pd.read_csv("data/air_quality_no2.csv",index_col=0,parse_dates=True) # .index_col() method:- is used to set the index of the dataframe
# # print(air_quality.head())


# print(air_quality.plot()) # .plot() method:- is used to display the plot of the dataframe
# plt.show()


# print(air_quality["station_paris"].plot()) # .plot() method:- is used to display the plot of the dataframe
# plt.show()


# print(air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)) # .plot.scatter() method:- is used to display the scatter plot of the dataframe
# plt.show()


# print([ 
#     method_name
#     for method_name in dir(air_quality.plot)
#     if not method_name.startswith("_")
# ])# list comprehension:- is used to display the list of the dataframe


# print(air_quality.plot.box())
# plt.show()


# axs = air_quality.plot.area(figsize=(12,4), subplots=True)#
# print(axs)
# plt.show()

# fig, axs = plt.subplots(figsize=(12, 4)) # subplots() method:- is used to display the subplots of the dataframe

# air_quality.plot.area(ax=axs) # .plot.area() method:- is used to display the area plot of the dataframe

# axs.set_ylabel("NO$_2$ concentration") # set_ylabel() method:- is used to set the y-axis label of the dataframe

# fig.savefig("no2_concentrations.png") # savefig() method:- is used to save the dataframe to an image file

# plt.show() # show() method:- is used to display the plot of the dataframe



# air_quality["london_mg_per_cubic"] = air_quality["station_london"] *1.8
# print(air_quality.head())


# air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
# print(air_quality.head())


# air_quality_renamed = air_quality.rename(
#     columns= {
#          "station_antwerp": "BETR801",
#         "station_paris": "FR04014",
#         "station_london": "London Westminster",
#     }
# )
# print(air_quality_renamed.head())

# air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
# print(air_quality_renamed.head()) # .rename() method:- is used to rename the columns of the dataframe 





# gamer_data = pd.read_csv("data/Video+Game+Sales/VDS.csv")
# print(gamer_data[["title","total_sales"]].head(50))

# print(titanic["Age"].mean()) # .mean() method:- is used to display the mean of the dataframe

# print(titanic[["Age","Fare"]].median()) # .median() method:- is used to display the median of the dataframe

# print(titanic[["Age","Fare"]].describe()) # .describe() method:- is used to display the description of the dataframe

# print(titanic[["Age","Sex"]].groupby("Sex").max()) # .max() method:- is used to display the maximum of the dataframe

# print(titanic.groupby("Sex")["Age"].mean()) # .groupby() method:- is used to group the dataframe by the specified column    

# print(titanic["Pclass"].value_counts()) # .value_counts() method:- is used to display the value counts of the dataframe
# print(titanic.groupby("Pclass")["Pclass"].value_counts())

# print(titanic.sort_values(by ="Age").head()) # .sort_values() method:- is used to sort the dataframe by the specified column

# print(titanic.sort_values(["Age","Pclass"],ascending=False).head()) # .sort_values() method:- is used to sort the dataframe by the specified column


air_quality = pd.read_csv("data/air_quality_pm25_long.csv")
# print(air_quality.head()) 

# Filter no2 parameters (actually the 'air_quality_pm25_long.csv' contains 'no2' data)
no2 = air_quality[air_quality["parameter"] == "no2"]


no2_subset = no2.sort_index().groupby(["location"]).head(2)



# print(air_quality.pivot_table(
#     values="value",
#     index="location",
#     columns="parameter",
#     aggfunc="mean"
# ))

# no2_pivot = no2.pivot_table(
#     values="value",
#     index="location",
#     columns="parameter",
#     aggfunc="mean"
# )
# print(no2_pivot)


air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv",parse_dates=True)


air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]

 




# air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",parse_dates=True)

# air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]



# air_quality = pd.concat([air_quality_no2, air_quality_pm25],axis=0)
# # .concat() method:- is used to concatenate the dataframes



# print('shape of the air_quality_no2',air_quality_no2.shape) # .shape method:- is used to display the shape of the dataframe
# print('shape of the air_quality_pm25',air_quality_pm25.shape) # .shape method:- is used to display the shape of the dataframe

