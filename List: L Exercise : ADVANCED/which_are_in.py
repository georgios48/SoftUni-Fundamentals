first_list = list(input().split(", "))
second_list = list(input().split(", "))
substrings = []

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word and first_word not in substrings:
            substrings.append(first_word)

print(substrings)