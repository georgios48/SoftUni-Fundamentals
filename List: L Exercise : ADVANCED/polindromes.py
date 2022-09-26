words = input().split(" ")
searching_word = input()

def palidnrome_filter(word):
    if word == word[::-1]:
        return word

palindrome_words = [word for word in words if palidnrome_filter(word)]

print(palindrome_words)
print(palindrome_words.count(searching_word))