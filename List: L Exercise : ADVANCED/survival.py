list = input().split()
n = int(input())
last_element = 0
list = [int (i) for i in list]
cntr = 0

while cntr < n:
    list.remove(min(list))
    cntr += 1
temp = str(list)[1:-1]
print(temp)