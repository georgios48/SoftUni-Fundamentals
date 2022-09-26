number_wagons = int(input())
wagons = [0] * number_wagons

while True:
    command = input()
    if command == "End":
        break

    data = command.split(" ")

    current_command = data[0]

    if current_command == "add":
        wagons[-1] += int(data[1])

    elif current_command == "insert":
        index = int(data[1])
        people_number = int(data[2])
        wagons[index] += people_number
    elif current_command == "leave":
        index = int(data[1])
        people_number = int(data[2])
        wagons[index] -= people_number

print(wagons)