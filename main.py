def listOptions():

    print("Press 1 to add a task ")
    print("Press 2 to remove a task ")
    print("Press 3 to add a task to completed list ")
    print("Press 0 to delete the list and start again ")



listOptions()

def main():

    toDoList = []
    completedList = []

    print(f"Currently your to-do-list is: {toDoList} ")
    number = int(input("Please enter a number: "))

    while len(toDoList)<3:
        if number == 1:
            task = input("Please enter a task: ")
            toDoList.append(task)
            print(toDoList)
        

        if number == 2:
            task = input("Please remove a task: ")
            toDoList.remove(task)



        if number == 3:
            task = input("Great, You did it! ")
            completedList.append(task)





main()
