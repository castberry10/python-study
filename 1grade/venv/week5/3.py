import string

inputData = input("your string: ")
nowData = ""
maxLenString = ""
i = 1
nowData += inputData[0]
while True:
    if i == len(inputData):
        if len(maxLenString) < len(nowData):
            maxLenString = nowData
        print(maxLenString)
        break
    while True:
        if ord(inputData[i - 1]) < ord(inputData[i]):
            nowData += inputData[i]
            i += 1
            break
        else:
            if len(maxLenString) < len(nowData):
               maxLenString = nowData
            nowData = inputData[i]
            i += 1
            break
