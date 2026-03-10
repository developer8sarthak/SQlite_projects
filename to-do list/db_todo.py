import sqlite3

connection = sqlite3.connect("todo.db")

c = connection.cursor()

def add_task(task):
    c.execute("INSERT INTO tasks(task) VALUES(?)" , (task,))
    connection.commit()
def remove_task(task_id):
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
def view_task():
    c.execute("SELECT * FROM tasks")
    for row in c.fetchall():
        print(row[0] , row[1])
print("Welcome to the TO-DO list application")
print("You can select weather what you wanna do ")
print("1. ADD task")
print("2. remove task")
print("3. view task")

exits  = "y"
while exits != 'e':
    choice = input("enter your choice :")
    if choice == "1":
        task = input("enter the task you want to add:")
        add_task(task)
        print("task added")
        exits  = input("e/y   : ")
    elif choice == "2":
        num = int(input("enter the id of the task you wanna remove"))
        remove_task(num)
        exits  = input("e/y   :")
    elif choice == "3": 
        view_task()

    else :
        print("You enterd  the wrong option")
        exits  = input("e/y  :")
        



