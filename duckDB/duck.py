from duckdb import query
import duckdb 
import pandas as pd
import  os

# data = {
#     'Name': ['Amit', 'Rahul', 'Neha', 'Pooja', 'Rohan'],
#     'Age': [25, 30, 28, 22, 35],
#     'Salary': [50000, 60000, 55000, 45000, 70000],
#     'Department': ['IT', 'HR', 'IT', 'Finance', 'HR']
# }

# df = pd.DataFrame(data)

# query = """
# SELECT Name ,Salary
# FROM df
# """

# query2 = """
# SELECT * 
# FROM df
# WHERE Age > 25
# """

# query3 = """
# SELECT Name ,Salary
# FROM df
# WHERE Department = 'IT'
# ORDER BY Salary DESC
# """


# query = """
#     SELECT 
#         Department, 
#         MAX(Age) as Sabse_Bada_Employee_Age, 
#         SUM(Salary) as Total_Department_Karcha
#     FROM df
#     GROUP BY Department
# """

# result_df = duckdb.query(query).df()
# print(result_df)


file_path = "C:/Users/andyk/Desktop/AI-ML Foundation/data/vds.csv"


# d_path = r"C:\Users\andyk\Desktop\AI-ML Foundation\data"
# print(os.listdir(d_path))




query = f"""
SELECT *
FROM '{file_path}'
"""


query = f"""
    SELECT 
        Publisher,
        SUM(total_sales) as Total_Sales
    FROM read_csv_auto('{file_path}')
    GROUP BY Publisher
    ORDER BY Total_Sales DESC
    LIMIT 5
"""


# query = f"""
#     SELECT
#         genre,
#         COUNT(*) as Total_Action_Games
#         FROM '{file_path}'
#         WHERE genre = 'Action'
#         GROUP BY genre
#         ORDER BY Total_Action_Games DESC
#         LIMIT 5
#         """


query = f"""
    SELECT 
        title,
        total_sales
    FROM read_csv_auto('{file_path}')
    WHERE YEAR(release_date) = 2010
    ORDER BY total_sales DESC
    LIMIT 5
    
"""
result_df = duckdb.query(query).df()
print(result_df)    