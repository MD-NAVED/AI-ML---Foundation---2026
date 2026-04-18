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






# query = f"""
# SELECT *
# FROM '{file_path}'
# """


# query = f"""
#     SELECT 
#         Publisher,
#         SUM(total_sales) as Total_Sales
#     FROM read_csv_auto('{file_path}')
#     GROUP BY Publisher
#     ORDER BY Total_Sales DESC
#     LIMIT 5
# """


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


# query = f"""
#     SELECT 
#         title,
#         total_sales
#     FROM read_csv_auto('{file_path}')
#     WHERE YEAR(release_date) = 2010
#     ORDER BY total_sales DESC
#     LIMIT 5
    
# """


# query = f"""
    
#     SELECT 
#         console,
#         SUM(total_sales) as Duniya_Bhar_Ki_Income
#     FROM read_csv_auto('{file_path}')
#     GROUP BY console
#     ORDER BY Duniya_Bhar_Ki_Income DESC
#     LIMIT 5


# """

# ==========================================
# 💼 TASK 3: Double Filter ka Jadoo (AND)
# ==========================================
# Manager ki demand: "Naved, 'Action' games toh bohot saare publishers banate hain, par mujhe un
# Action games ki list chahiye jo EXCLUSIVELY 'Nintendo' company ne banaye hon. Mujhe 
# un Games ka Title aur unki Total Sales chahiye."
# 
# Aapke liye Hints:
# 1. Dikhana kya kya hai: SELECT title, total_sales
# 2. Dataset lana hai: FROM read_csv_auto('{file_path}')
# 3. Yahan 'Double Filter' lagega: jahan genre 'Action' ho AUR publisher 'Nintendo' ho.
#    (Aise Likhna Hai -> WHERE genre = 'Action' AND publisher = 'Nintendo')
# 4. Group (SUM/COUNT) karne ki koi zaroorat nahi hai.
# 5. Rank wise highest pehle: ORDER BY total_sales DESC
# 6. Sirf Top 5 Theek rahenge: LIMIT 5
# ==========================================

query = f"""
     
      SELECT 
        title,
        total_sales
    FROM read_csv_auto('{file_path}')
    WHERE genre = 'Action' AND publisher = 'Nintendo'
    ORDER BY total_sales DESC
    LIMIT 5


"""


# result_df = duckdb.query(query).df()
# print("\n--- TOP 5 SELLING PLATFORMS 🎮 ---")
# print(result_df)




result_df = duckdb.query(query).df()
print("\n--- TOP 5 SELLING GAMES OF Nintendo 🎮 ---")
print(result_df)




