employee_happiness = list(map(int, input().split(" ")))
factor = int(input())

multiplied_happiness = list(map(lambda x: x * factor, employee_happiness))

average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_employees = list(filter(lambda x: x >= average_happiness, multiplied_happiness))

if len(happy_employees) >= len(employee_happiness):
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}.", end= " ")
    print("Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness)}. ", end= " ")
    print("Employees are not happy!")
