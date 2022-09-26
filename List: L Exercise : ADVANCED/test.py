text = input()

vowels = ['a', 'u', 'o', 'e', 'i']

result = [ch for ch in text if ch.lower() not in vowels]

print("".join(result))