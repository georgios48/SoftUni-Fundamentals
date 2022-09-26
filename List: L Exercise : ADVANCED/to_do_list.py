tasks = []

while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    priority_number = int(command[0])
    duty = command[1]

    tasks.append((priority_number, duty))

final_list = [task_data[1] for task_data in sorted(tasks)]
print(final_list)

