number_list = list(map(int, input().split(".")))


number_list[-1] += 1

if number_list[-1] >= 10:
    number_list [-2] += 1
    number_list[-1] = 0

    if number_list[-2] >= 10:
        number_list[0] += 1
        number_list[-2] = 0


number_list = list(map(str, number_list))
print(".".join(number for number in number_list))

