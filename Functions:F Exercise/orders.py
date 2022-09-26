def calculate(item, quantity):
    if item == "coffee":
        price = quantity * 1.50
        print(f"{float(price):.2f}")
    elif item == "water":
        return float(quantity)
    elif item == "coke":
        price = quantity * 1.40
        return float(price)
    elif item == "snacks":
        price = quantity * 2.00

product = input()
quantity = int(input())

calculate(product, quantity)