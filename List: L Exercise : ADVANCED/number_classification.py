numbers = list(map(int, input().split(", ")))

positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]
even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]

positive = list(map(str, positive))
negative = list(map(str, negative))
even = list(map(str, even))
odd = list(map(str, odd))

positive = ", ".join(element for element in positive)
negative = ", ".join(element for element in negative)
even = ", ".join(element for element in even)
odd = ", ".join(element for element in odd)

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")