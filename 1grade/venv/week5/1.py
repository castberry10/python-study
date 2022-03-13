import string

inputData = input("your string: ")
nowData = ""
for i in range(len(inputData)):
    if(inputData[i] in string.digits or inputData[i] in string.punctuation):
        nowData += inputData[i]

print(nowData)
