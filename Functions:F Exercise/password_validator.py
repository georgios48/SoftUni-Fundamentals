def valid(pw):
    validated = True
    digit_counter = 0

    if 6 > len(pw) and len(pw) < 10:
        print("Password must be between 6 and 10 characters")
        validated = False
    if not pw.isalnum():
        print("Password must consist only of letters and digits")
        validated = False
    for element in pw:
        if element.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        validated = False

    if validated == True:
        print("Password is valid")


password = input()

valid(password)