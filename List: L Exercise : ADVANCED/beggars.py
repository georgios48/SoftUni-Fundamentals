list = input().split(", ")
list_int = [int(i) for i in list]
total_beggars = int(input())
current_sum = 0

final_sum = []
beggar_counter = 0

while beggar_counter < total_beggars:
    for current_index in range(beggar_counter, len(list_int), total_beggars):
        current_sum += list_int[current_index]

    final_sum.append(current_sum)
    current_sum = 0
    beggar_counter += 1

print(final_sum)