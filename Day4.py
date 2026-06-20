#Numpy
#import numpy as np

# marks = np.array([20, 30, 40])
# marks = marks + 5
# print(marks)


#------------------------------------------------------------------
#  axis - a direction (rows vs column)
# shape - size in each axis eg(2,3)
# dtype - the single data type (int , float)
# ndim - a number of dimension

# print(np.linspace(0,1,5))



# marks = np.array([78,85,90,67,88])
# print(marks)

# ages= np.array([78,85,90,67,88])

# print(np.shape(marks))
# print(np.shape(ages))

# print(marks.dtype)
# print(ages.dtype)

# m=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(m[1,2]) #row,col
# print(m[0])     #whole 0th row
# print(m[:,1])   #whole 1st col
# print(m[0:2,1])

# a=np.arange(6)
# print(a.shape)

# print(a.reshape(2,3))
# print(a.flatten())

# data=np.arange(12)
# print(data.reshape(3,4))

# print(data.reshape(4,3))

# print(data.reshape(5,2))

# a=np.array([10,20,30])
# # b=np.array([3,4,5,5])

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)

# print(a+5)
# print(a*2)
# print(a/10)
# print(a**2)

#Aggregation-----------------------------------------------------------
# sum() sum of array
# mean() mean of array
# min() minimum of array
# max() maximum of array
# std() spread/ variation of arrays
# axis=direction axis=0 sum col wise axis=1 sum row wise

# import numpy as np
# m=np.array([[1,2,3,0],[4,5,6,66]])

# print(m.sum())
# print(m.sum(axis=0))
# print(m.sum(axis=1))

# marks=np.array([72,88,95,64,90,58])

# print(marks.mean())
# print(marks.max())
# print(marks.min())

# sumit=marks[marks>marks.mean()]

# print(sumit)

#bROADCASTING-------------------------------------------------------------
#Saves memory - the small array isnot really copied,
#  save scode - no loop to repeat values, 
# saves time- it runs in fast c;

#simple rules-------------------------------------------------------------

# 1.A sclaer work with any array
# 2.A row can add to every row of matriix 
# 3.Sizes must match OR one of them is 1


# #pandas------------------------------------------
# import pandas as pd
# df=pd.DataFrame({
#     'Name':['Rahul','Sneha'],
#     'Marks':[77,98]
# })
# print(type(df['Marks']))

# marks=pd.Series([78,76,78])
# print(marks)

# pd.read_csv("file.csv")---to read csv File
# pd.read_excel('file.xlxs') --- to read excel file



#-----------------------------------------------
#Data Frame
# keep only rows taht meet a condition
# put the full condiiton inside df[...]
# cobine conditons eith & (and)(or)
# wrap each condition in parantheses


#Sorting
# false===high to low
# default is ascending
# sort_values('col')
# df.sort_values('Salary',ascending=False)

import pandas as pd
# students={
#     'Name':['Rahul','Sneha','arjun','Divya','Karan'],
#     'Age':[21,22,23,21,22],
#     'Marks':[78,91,65,88,55],
#     'City':["Delhi",'Pune','Jaipur','Delhi','Pune']
# }
# df=pd.DataFrame(students)
# print(df)

# marks=pd.Series([78,67,87,98],name='Marks')
# print(marks)
# print(type(marks))

# Temp=pd.Series([78,67,87,98])
# print(Temp.mean())

students=pd.DataFrame({
     'Name':['Rahul','Sneha','arjun','Divya','Karan'],
     'Age':[25,22,23,21,22],
     'Marks':[78,91,'null',88,'null'],
     'City':["Delhi",'Pune','Jaipur','Delhi','Pune']
 })

students.to_csv('student2.csv',index=False)
stu=pd.read_csv('student2.csv')
# print(stu)

# print('Shape (rows,cols):',stu.shape)
# print('\nColumn nmaes:',list(stu.columns))
# print(stu.head(3))

# print(stu.info())

# print(stu.describe())

# print(stu.shape)
# print(stu.tail(2))

# it_staff=stu[stu['City']=='Pune']
# print(it_staff)

# rich_sales=stu[(stu['City']=='Pune')&(stu['Marks']>60)]
# print('\n MArks > 60')
# print(rich_sales)

# print(stu[stu['Age']>22])
# print(stu.sort_values('Age', ascending=True))

print(stu.isnull().sum())
print(stu.head())
print('\n')

i = stu['Marks'].mean()
stu['Marks'] = stu['Marks'].fillna(i)

print(stu.head())
