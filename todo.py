import time

# Open the file with read/write modes
filename_path = 'C:/Users/Magdy/Desktop/TODo List.txt'

with open(filename_path, 'r+') as file:
    menu = 0
    while menu != 7:
        print("Choose what do you want: ")
        print("1 for Adding new tasks, ")
        print("2 to View completed tasks, ")
        print("3 to View not completed tasks, ")
        print("4 to Delete completed tasks, ")
        print("5 to View all tasks, ")
        print("6 to Mark a task a completed. ")
        print("7 to Exit the program. ")
        menu = int(input())

        if menu == 1:
            with open(filename_path, 'a') as file:
                userChoose = 'Y'
                # Get the current number of lines to continue numbering
                with open(filename_path, 'r') as read_file:
                    lines = read_file.readlines()
                    line_number = len(lines) + 1  # Start numbering from the next line
                    
                while userChoose.capitalize() != 'N':  # This loop adds the tasks to the file
                    task = input("Add your task: ")
                    
                    op = input("Is it done yet? \nY for yes, N for No ")
                    if op.capitalize() == 'Y':
                        status = '1'
                    else:
                        status = '0'

                    # Write the task with line number
                    file.write(f'{line_number} {task} {status}\n')
                    line_number += 1

                    print("Task added! ")
                    time.sleep(2)
                    userChoose = input("Do you want to add another task? \nY for yes, N for No ")

        elif menu == 2:
            with open(filename_path, 'r') as file:
                for line in file:
                    if line.rstrip().endswith('1'):
                        print(line, end='')
            time.sleep(2)

        elif menu == 3:
            with open(filename_path, 'r') as file:
                for line in file:
                    if line.rstrip().endswith('0'):
                        print(line, end='')
            time.sleep(2)

        elif menu == 4:
            with open(filename_path, 'r') as file:
                lines = file.readlines()

            with open(filename_path, 'w') as file:
                for line in lines:
                    if not line.rstrip().endswith('1'):
                        file.write(line)

            print("Completed tasks have been deleted.")
            time.sleep(2)

        elif menu == 5:
            with open(filename_path, 'r') as file:
                lines = file.readlines()
            for line in lines:
                print(line, end='')
            time.sleep(2)

        elif menu == 6:
            with open(filename_path, 'r+') as file:
                lines = file.readlines()
                num = int(input("Enter the number of the task: "))

            found = False  # Flag to check if the task number exists

            with open(filename_path, 'w') as file:
                for line in lines:
                    # Split the line to separate the task number from the rest of the line
                    task_number, task_details = int(line.split()[0]), " ".join(line.split()[1:])
                    
                    if task_number == num:

                        found = True
                        if task_details.rstrip().endswith('1'):
                            print("Task is already completed!")
                            time.sleep(2)

                        elif task_details.rstrip().endswith('0'):
                            task_details = task_details.rstrip()[:-1] + '1'
                            print("Task has been marked as completed!")
                            time.sleep(2)
                        
                    # Write the line back to the file, with the updated status if applicable
                    file.write(f'{task_number} {task_details}\n')

            if not found:
                print("Task number not found!")

