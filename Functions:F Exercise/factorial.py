def factorial(num, num2):
    fact_num = 1
    fact_num2 = 1
    for element in range(1, num + 1):
        fact_num *= element
    for element in range(1, num2 + 1):
        fact_num2 *= element

    return float(fact_num / fact_num2)


num = int(input())
num2 = int(input())

print(factorial(num,num2))