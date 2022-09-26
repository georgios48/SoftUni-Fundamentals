list = input().split("|")
budget = float(input())
profit = 0
spent = 0
profit_price = 0

for current_item in list:
    item = current_item.split("->")
    item_price = item.pop()
    item_price = float(item_price)

    if "Clothes" in item:
        if item_price > 50.00 or item_price > budget:
            continue
        else:
            spent += item_price
            profit_price = item_price + (item_price * 0.40)
            profit += profit_price
            budget -= item_price
    elif "Shoes" in item:
        if item_price > 35.00 or item_price > budget:
            continue
        else:
            spent += item_price
            profit_price = item_price + (item_price * 0.40)
            profit += profit_price
            budget -= item_price
    elif "Accessories" in item:
        if item_price > 20.50 or item_price > budget:
            continue
        else:
            spent += item_price
            profit_price = item_price + (item_price * 0.40)
            profit += profit_price
            budget -= item_price
    print(f"{profit_price:.2f}", end = " ")

budget += profit
print(f"\nProfit: {(profit - spent):.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
