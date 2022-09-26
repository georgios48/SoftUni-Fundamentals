energy = 100
coins = 100

rest_ctr = 0
order_ctr = 0
ingredient = 0

failed_bool = 0

events = input().split("|")

for event in events:
    current_event = event.split("-")

    if "rest" in current_event:
        value = current_event.pop(-1)
        energy += int(value)
        if energy >= 100:
            energy = 100
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
            rest_ctr = 1
        else:
            print(f"You gained {value} energy.")
            print(f"Current energy: {energy}.")
    elif "order" in current_event:
        value = current_event.pop(-1)
        if energy >= 30:
            coins += int(value)
            print(f"You earned {value} coins.")
            energy -= 30
            order_ctr = 1
        else:
            print("You had to rest!")
            energy += 50
            failed_bool = 1
            continue
    else:
        value = current_event.pop(-1)
        if coins >= int(value):
            temp = str(current_event)[2:-2]
            print(f"You bought {temp}.")
            coins -= int(value)
            ingredient = 1
        else:
            temp = str(current_event)[2:-2]
            print(f"Closed! Cannot afford {temp}.")
            failed_bool = 1
            break
if failed_bool == 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

