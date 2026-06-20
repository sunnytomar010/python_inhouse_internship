import numpy as np
# marks=np.array([67,88,98,65,45,90])
# norm=(marks-np.mean(marks))/np.std(marks)
# print(norm)
# #----------------------------------------------------------
# rows=np.arange(1,6).reshape(5,1)
# col=np.arange(1,6)


# table=rows * col
# print(table)
# #--------------------------------------------------------------------

# image=np.array([[1,2,3],[4,5,6]])
# print(image.flatten())

# #---------------------------
# m=[89,76,54,98,39,23,89]

# um=[0 if x<40 else x for x in m]
# print(um)

#--------------------------------------------------------------------------

import pandas as pd

employees = pd.DataFrame({
    "Name": ["Rahul", "Sneha", "Arjun", "Divya", "Karan","Priya", "Aman", "Neha", "Rohit", "Anjali"],
    "Age": [25, 28, 30, 24, 35, 29, 26, 31, 27, 33],
    "Salary": [50000, 65000, "None", 48000, 80000, 72000, "None", 60000, 55000, 90000],
    "Experience": [2, 5, "None", 1, 10, 6, 3, "None", 4, 8],
    "Department": ["IT", "HR", "Finance", "IT", "Sales","HR", "Marketing", "Finance", "IT", "Sales"]
})

employees.to_csv("employees.csv", index=False)
# emp=pd.read_csv('employees.csv')
# print(emp)

df = pd.read_csv("employees.csv")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(0)
# print(df)

df["Seniority"] = "Junior"
df.loc[df["Experience"] >= 5, "Seniority"] = "Senior"
# print(df)

print(df.groupby("Seniority", as_index=False)["Salary"].mean())