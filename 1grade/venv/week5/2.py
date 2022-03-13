import string


while True:
    inputData = input("your string: ")

    checkDig = 1
    checkU = 1
    checkL = 1
    checkPun = 1

    for i in range(len(inputData)):
        if inputData[i] in string.ascii_lowercase:
            checkL = 0

        if inputData[i] in string.ascii_uppercase:
            checkU = 0

        if inputData[i] in string.punctuation:
            checkPun = 0

        if inputData[i] in string.digits:
            checkDig = 0

    if checkL == 1:
        print("Password should include Lowercase")

    if checkU == 1:
        print("Password should include Uppercase")

    if checkDig == 1:
        print("Password should include digit")

    if checkPun == 1:
        print("Password should include special character")

    if len(inputData) < 8:
        print("Password should be at least 8")

    if (checkL + checkU + checkDig + checkPun) == 0 and len(inputData) >= 8:
        print("Nice Password!")
        break


