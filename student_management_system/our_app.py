import sqlite3

connection = sqlite3.connect('students.db')
# add studnent , show all students , store them by , roll no, name , age , class
c = connection.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY,
        name TEXT ,
        age INTEGER,
        class TEXT
    )
""")
def add_student():
    exit = 'y'
    while exit != 'n':
        roll_no = int(input("Enter roll number :"))
        name = input("Enter name:")
        age = int(input("Enter age : "))
        class_name = input("Enter class : ")

        c.execute(" INSERT INTO students VALUES  (?, ?, ?, ?)", (roll_no , name , age, class_name))
        exit = input("Do you want to add more students ? (y/n) : ")
        connection.commit()

def show_students():
    c.execute("SELECT * from students")
    students = c.fetchall()

    for student in students:
        print(f"Roll no : {student[0]} , Name : {student[1]} , Age : {student[2]} , class : {student[3]}")

print("Welcome to student management system")
return_choice = 'y'
while return_choice != 'n':
    print("1. Add student")
    print("2. Show students")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add_student()
    elif choice == 2:
        show_students()
    else:
        print("Invalid choice")
    return_choice = input("Do you want to continue ? (y/n) : ")




