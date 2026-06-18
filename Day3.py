#import modules
# import math
# print(math.sqrt(16))
# print(math.pi)

# import numpy as np
# import pandas as pd

# from math import sqrt, pi
# print(sqrt(25))
# print(pi)
# import math
# import random
# # print(math.sqrt(25))
# # print(math.floor(3.7))
# # print(math.ceil(3.2))
# # print(random.randint(1, 10))
# x=math.ceil(4.2)
# y=math.floor(4.8)
# z=random.randint(1, 1)
# print(x+y)
# print(x==y)
# print(z)

#------------------------------------------------------

#Exception handling
# try:
#     num=int(input("Enter a number: "))
#     result=10/num
#     print("Result:",result)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter a valid number.")
# finally:
#     print("Program finished - this always runs.")


#------------------------------------------------------

# def calculator():
#         num1=input("Enter 1st number: ")
#         num2=input("Enter 2nd number: ")
#         try:
#             num1=float(num1)
#             num2=float(num2)
        

#             operation=input("Enter operation (+, -, *, /): ")

#             if operation == '+':
#                print(num1+num2)
#             elif operation == '-':
#                print(num1-num2)
#             elif operation == '*':
#                 print(num1*num2)
#             elif operation == '/':
#                 print(num1/num2)
#             else: 
#              print("Enter a Valid operation")
            
#         except ZeroDivisionError:
#             print("Cannot divide by zero.")
#         except ValueError:
#             print("Please enter a valid number.")
#         finally:    
#              print("Program finished - this always runs.")

# calculator()

#------------------------------------------------------
# "r" - read only not create new file if not exist
# "w" - write-overwrites cretes new file if not exist
# "a" - append-add to end crete new file if not exist


#read-------------------
# with open("student.txt", "r") as file:
#     # content = file.read()
#     # print(content)

#     # for line in file:
#     #     print(line.strip())

#     lines = file.readlines()
#     print(lines[1])
#     print(lines)
#     print(len(lines))


#write-------------------
# with open("student.txt", "w") as file:
#     file.write("College of Engineering\n")
#     file.write("Department of Computer Science\n")
# #print("File written successfully.")

# #append-------------------
# with open("student.txt", "a") as file:
#     file.write("This is an appended line.\n")
#     file.write("Urraayy Bhaiya chutti hogyi...chutti hogyi")
#  #After both:student.txt has 4 lines
# #print("File appended successfully.") 
# with open("student.txt", "r") as file:
#     content = file.read()
#     print(content) 
# with open("example.txt", "w") as file:
#     file.write("College of Engineering\n")
#     file.write("Department of Computer Science\n") 

#json-------------------
#json.dump() - python dictionary to json file
#json.load() - json file to python dictionary
# import json
# student_dict = {'name': 'sunny', 'score':85,'enrolled':True}
# json_string = json.dumps(student_dict, indent=4)
# print(json_string)
# print(type(json_string))

# api_response = '{"name": "sunny", "score": 85, "enrolled": true}'
# python_dict = json.loads(api_response)
# print(python_dict['name'])

# import json
# student=[
#     {"name": "sunny", "score": 85, "enrolled": True},
#     {"name": "Tarang", "score": 92, "enrolled": True}
# ]
# json_file = json.dumps(student, indent=4)
# print(json_file)

# back_to_dict=json.loads(json_file)
# print(back_to_dict)

#oops------------------------------------------------------
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade='A' if score >=85 else 'B'

s1=Student("sunny", 85)
s2=Student("tarang", 98)
print(s1.name, s1.score, s1.grade)
print(s2.name, s2.score, s2.grade)

