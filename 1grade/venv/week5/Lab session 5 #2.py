import string
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digit = string.digits
punc = string.punctuation


def func(str):
    check = 0
    lower = 0
    upper = 0
    digits = 0
    puncs = 0
    if len(str) < 8:
        print("Password should be at least 8")
        check += 1
    for i in str:
        if i in lowerCase:
            lower += 1
        if i in upperCase:
            upper += 1
        if i in digit:
            digits += 1
        if i in punc:
            puncs += 1
    if lower == 0:
        print("Password should include LowerCase")
        check += 1
    if upper == 0:
        print("Password should include UpperCase")
        check += 1
    if digits == 0:
        print("Password should include digit")
        check += 1
    if puncs == 0:
        print("Password should include special character")
        check += 1
    return check


while True:
    str = input("Enter your Password: ")
    if func(str) == 0:
        print("Nice Password!")
        break
