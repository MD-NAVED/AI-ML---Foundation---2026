from duckdb import query
import duckdb 
import pandas as pd


data = {
    'Name': ['Amit', 'Rahul', 'Neha', 'Pooja', 'Rohan'],
    'Age': [25, 30, 28, 22, 35],
    'Salary': [50000, 60000, 55000, 45000, 70000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

query = """
SELECT Name ,Salary
FROM df
"""

query2 = """
SELECT * 
FROM df
WHERE Age > 25
"""

query3 = """
SELECT Name ,Salary
FROM df
WHERE Department = 'IT'
ORDER BY Salary DESC
"""




result_df = duckdb.query(query).df()
print(result_df)

