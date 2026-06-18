#write a program using math and random to generate 10 random float scores (50-100) and find there mean;
# import math
# import random as r
# scores=[r.randint(50,100) for x in range(10)]
# mean=math.fsum(scores)/len(scores)
# print(mean)

#--------------------------------------------------------------------------------------------------------



#Create student.txt with 5 names and scores. read it ,claculate average and print the top scorer.
students = []
total = 0

with open("student.txt", "w") as f:
    f.write("Sunny 90\n")
    f.write("Ravi 80\n")
    f.write("Sumit 72\n")
    f.write("Tarang 96\n")
    f.write("Shashi 86\n")

with open("student.txt", "r") as file:
    for line in file:
        name, score = line.split()
        score = int(score)
        students.append((name, score))
        total += score

average = total / len(students)
top_student = max(students, key=lambda x: x[1])

print("Average Score:", average)
print("Top Scorer:", top_student[0])
print("Top Score:", top_student[1])


#------------------------------------------------------------------------------------------------------------------------



#Create a python dict for an ai model config. convert to json,save to confog.json,then load and print
# import json
# model_config = { "model_name": "GPT-4", "learning_rate": 0.001,"batch_size": 32}

# with open("config.json", "w") as file:
#     file1=json.dump(model_config, file, indent=4)


# with open("config.json", "r") as file:
#     data = json.load(file)

# print(data)


#-----------------------------------------------------------------------------------------------------------------------------



#Build a BankAcount class with deposit(),withdraw(),and get_balance() method.
# Include exception handling for overdraft

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self):
#         amount = input("Enter deposit amount: ")
#         try:
#             amount = float(amount)
#             self.balance += amount
#             print("Amount deposited:", amount)
#         except ValueError:
#             print("Please enter a valid amount.")
#         finally:
#             print("Transaction completed.")

#     def withdraw(self):
#         amount = input("Enter withdrawal amount: ")
#         try:
#             amount = float(amount)
#             if amount > self.balance:
#                 raise ValueError("Insufficient balance.")
#             self.balance -= amount
#             print("Amount withdrawn:", amount)

#         except ValueError:
#             print("INsufficient Ammount")

#         finally:
#             print("Transaction completed.")

#     def get_balance(self):
#         print("Current Balance:", self.balance)


# account = BankAccount(1000)
# account.deposit()
# account.withdraw()
# account.get_balance()


