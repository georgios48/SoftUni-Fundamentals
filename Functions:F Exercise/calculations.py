def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b

def action(act, a, b):
    if act == "multiply":
        return multiply(a, b)
    elif act == "divide":
        return divide(a, b)
    elif act == "add":
        return add(a, b)
    elif act == "subtract":
        return subtract(a, b)

act = input()
a = int(input())
b = int(input())
print(action(act, a, b))