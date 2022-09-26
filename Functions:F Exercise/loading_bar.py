def loading(num):
    if num == 100:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f"{num}% [{'%' * (num // 10)}\
{'.' * (10 - (num // 10))}]\nStill loading...")

number = int(input())
loading(number)