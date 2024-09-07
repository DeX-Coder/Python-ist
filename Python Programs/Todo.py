import os
import pickle
import time
mainBanner = " ToDo "
print(mainBanner.center(80, "="))
mainTaskList = []
print("1. Add a Task\n2. Delete a Task\n3. Change/Edit a Task\n4. View Task List\n5. Exit\n0. re-Display Menu")

try:
    with open(".fsd8sbadba5adfva5dadf5bazvf65ad1bd1ba5db62dfa2.obb", "rb") as file:
        main = pickle.load(file)
        mainTaskList.extend(main)
except FileNotFoundError:
    pass

def loader(mainText="Please Wait"):
    
    for i in range(4):
        print(f'\r{mainText}...', end = "")
        time.sleep(0.1)
        print(f'\r{mainText}.. ', end = "")
        time.sleep(0.1)
        print(f'\r{mainText}.  ', end = "")
        time.sleep(0.1)
        print(f'\r{mainText}   ', end = "")
        time.sleep(0.1)
        print(f'\r{mainText}.  ', end = "")
        time.sleep(0.1)
        print(f'\r{mainText}.. ', end = "")
        time.sleep(0.1)
        print(f'\r{mainText}...', end = "")
        time.sleep(0.1)
        if i == 2:
            mainText = "Almost Done"
    print("\tDone!\n")


while True:
    try:
        userInput = int(input("Enter your choice: "))
        if userInput == 1:
            taskInput = input("Enter task to be added: ")
            mainTaskList.append(taskInput)
            print(f"Added Task: {taskInput}")

        if userInput == 2:
            count = 0
            loader("Loading")
            for items in mainTaskList:
                count += 1
                print(count, items)
            
            taskDeleteInput = int(input("Enter task number to be deleted: "))
            if taskDeleteInput != 0:
                store = mainTaskList.pop(taskDeleteInput-1)
                print(f"Deleted Task: {store}")

        if userInput == 3:
            count = 0
            loader("Loading")
            for items in mainTaskList:
                count += 1
                print(count, items)
            taskEditInput = int(input("Enter task number to be changed: "))
            if taskEditInput != 0:
                modifiedInput = input("Enter text to be replaced with: ")
                print(f"Modified {mainTaskList[taskEditInput-1]} --> {modifiedInput}")
                mainTaskList[taskEditInput-1] = modifiedInput

        if userInput == 4:
            count = 0
            print("Viewing Task List")
            loader()
            for items in mainTaskList:
                count += 1
                print(count, items)

        if userInput == 5:
            with open(".fsd8sbadba5adfva5dadf5bazvf65ad1bd1ba5db62dfa2.obb", "wb") as file:
                pickle.dump(mainTaskList, file)
            
            print("Bye!")
            exit()
        if userInput == 0:
            print(mainBanner.center(80, "="))
            print("1. Add a Task\n2. Delete a Task\n3. Change/Edit a Task\n4. View Task List\n5. Exit\n0. re-Display Menu")
        
        if userInput > 5:
            print("Enter from the correct options given above and try again!")
            continue
    except ValueError:
        print("Please enter a valid input!")
        continue