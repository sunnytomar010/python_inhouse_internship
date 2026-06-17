#Flatten a nested list
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flattened_list = [x for sublist in nested_list for x in sublist]
# print(flattened_list)

#Word frequency counter
# words = ["this", "is", "a", "test", "this", "is", "simple"]
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# print(freq)

#calculator
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def show_menu():
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")
#     print("5. Exit")

# while True:
#     show_menu()
#     choice = input("Enter your choice (1-5): ")
#     if(choice != "5"):
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))

#     if choice == "1":
#         print("Result:",add(a, b))
#     elif choice == "2":
#         print("Result:",subtract(a, b))
#     elif choice == "3":
#         print("Result:",multiply(a, b))
#     elif choice == "4":
#         print("Result:",divide(a, b))
#     elif choice == "5":
#         print("Exiting Operations")
#         break
#     else:
#         print("Invalid choice. Please select 1-5.")
