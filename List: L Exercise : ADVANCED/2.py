factor = int(input())
count = int(input())

list = []

for element in range(1, count + 1):
    element *= factor
    list.append(element)

print(list)