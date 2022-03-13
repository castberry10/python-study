def func(str):
    result = ""
    candidate = str[0]
    index = 0

    for i in range(1, len(str)):
        if str[i] > str[index]:
            candidate += str[i]
            index += 1
            if len(result) < len(candidate):
                result = candidate
                index = i
        else:
            candidate = str[i]
            index = i
    return result

str = input("input string: ")
print(func(str))
