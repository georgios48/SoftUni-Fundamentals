def between(symbol1, symbol2):
    collected_char = []
    for char in range(ord(symbol1) + 1, ord(symbol2)):
        collected_char.append(chr(char))
    return collected_char


first_char = input()
second_char = input()

print(between(first_char, second_char))
