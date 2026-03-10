print("hello welcome back to your TO-DO list application")

file_path  = "to_do.txt"
def add_task(task):
    with open(file_path,  "a") as file:
        file.write("\n" + task)
        print("added")
def delet(num):
    with open(file_path, "r") as f:
        lines = f.readlines()
            
        if num  < 0 or num  > len(lines):
            print("You enterd  a invalid choice")
        
        lines.pop(num)
        
        with open(file_path, "w") as f:
            f.write(lines)
print("put your choice in  for the TO-DO application")
print("1. add task")
print("2. remove task")
print("3. view all tasks")

exits  = "y"
while exits != 'e':
    choice = input("enter your choice :")
    if choice == "1":
        task = input("enter the task you want to add:")
        add_task(task)
        print("task added")
        exits  = input("e/y   : ")
    elif choice == "2":
        num = int(input("enter the number index of the task you are trying to remove"))
        delet(num)
        exits  = input("e/y   :")
    elif choice == "3": 
        with open(file_path , "r") as file:
            content = file.readlines()

            for con  in content:
                print(f"1.{con}")
           
            exits  = input("e/y   :")

    else :
        print("You enterd  the wrong option")
        exits  = input("e/y  :")
        

