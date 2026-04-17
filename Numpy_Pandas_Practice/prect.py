import numpy as np
import pandas as pd

# data_array = np.array([
#     [25, 50000, 85],
#     [30, 60000, np.nan],
#     [np.nan, 75000, 92],
#     [22, np.nan, 78],
#     [28, 55000, np.nan]
# ])

# data_array = pd.DataFrame(data_array, columns=["Age", "Salary", "Score"])

# print(data_array)
# print(data_array.isna().sum())
# data_array = data_array.fillna(data_array.mean())
# # print(data_array)

# filtered_age = data_array[data_array["Age"] > 25]

# filtered_age = filtered_age.sort_values(by="Salary", ascending=False)
# print("--- Task 2 Output ---")
# print(filtered_age)



# data_array["Age_Group"] = pd.cut(data_array["Age"], bins=[0, 24, 30, 100], labels=["<25", "25-30", ">30"])


# summary = data_array.groupby("Age_Group", observed=False).agg({'Salary': 'mean', 'Score': 'sum'})


# print(summary)


incomes_array = np.random.randint(10000, 100000, size=10)
# print(incomes_array)
incomes_array = pd.DataFrame({"income":incomes_array})
# print(incomes_array)
incomes_array["log_income"] = np.log(incomes_array["income"])
incomes_array["Square_income"] = np.sqrt(incomes_array["income"])
print(incomes_array)


