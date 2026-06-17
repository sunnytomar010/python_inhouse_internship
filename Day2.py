# marks=[78, 85, 92, 88, 76,45]
# # avg=sum(marks)/len(marks)
# # above_avg=(filter(lambda x: x>avg, marks))

# # print( above_avg)
# #new list=[operation for item in iterable... if condition]
# # squares=[m**2 for m in marks if m>80]
# # print(squares)
# names=["Alice", "Bob", "Charlie", "David", "Eve"]
# new_names=[name.upper() for name in names ]
# print(new_names)

student = [
    {'name': 'Sunny',
     'age': 20 ,
     'rollno': 240,
     'mark': 85
     }
]

def addstud():
    newdict = {}
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    rollno = int(input("Enter roll no: "))

    newdict['name'] = name
    newdict['age'] = age
    newdict['rollno'] = rollno

    student.append(newdict)
    print("Student added successfully!\n")


def display():
    if not student:
        print("No students found.")
        return

    for s in student:
        print("\nName:", s['name'])
        print("Age:", s['age'])
        print("Roll No:", s['rollno'])

def grade():
    for s in student:
        mark = s.get('mark', None)
        if mark is None:
            print(f"{s['name']} does not have a mark assigned.")
            continue
        if mark >= 90:
            g='A'
        elif mark >= 80:
            g='B'
        elif mark >= 70:
            g='C'
        elif mark >= 60:
            g='D'
        else:
            g='E'
        print(f"{s['name']} has grade: {g}")


while True:
    choice = int(input(
        "\nSelect operation:\n"
        "1. Add student\n"
        "2. Show students\n"
        "3. Assign grade\n"
        "0. Exit\n"
        "Enter choice: "
    ))

    if choice == 1:
        addstud()
    elif choice == 2:
        display()
    elif choice == 3:
        grade()
    elif choice == 0:
        print("Exiting program.")
        break
    else:
        print("Wrong input!")