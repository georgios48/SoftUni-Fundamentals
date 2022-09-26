words = list(input().split(" "))
words = [word for word in words if len(word) % 2 == 0]
final_list = " ".join(word for word in words)

for word in words:
    print(word)