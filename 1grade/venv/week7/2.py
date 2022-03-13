chack = int(input("1. encrypt 2. decrypt: "))
inputPath = input("input FileName: ")
outputPath = input("output FileName: ")
key = int(input("key: "))

inputTextFile = open(inputPath, "r")
inputText = inputTextFile.read()
textCnt = len(inputText)

if textCnt % key == 0:
    repeatNum = textCnt // key
    remainderNum = 0
elif textCnt % key != 0:
    repeatNum = textCnt // key + 1
    remainderNum = textCnt % key

#print(repeatNum, remainderNum)

outputList = []
outputText = ""
tempText = ""

if chack == 1:
    index = 0
    for i in range(repeatNum): # 나눈 수 만큼 반복
        for j in range(key):
            tempText += inputText[index]
            index += 1
            if index == textCnt - 1:
                break
        outputList.append(tempText)
        tempText = ""


    if remainderNum != 0:
        for j in range(remainderNum):
            tempText += inputText[index]
            index += 1
        outputList.append(tempText)
        tempText = ""

    outputList.reverse()


    for i in range(len(outputList)): #문제 없음
       outputText += outputList[i]

    outputTextFile = open(outputPath, "w")
    outputTextFile.write(outputText)

elif chack == 2:
    index = 0
    if remainderNum != 0:
        for j in range(remainderNum):
            tempText += inputText[index]
            index += 1
        outputList.append(tempText)
        tempText = ""

    for i in range(repeatNum):
        for j in range(key):
            tempText += inputText[index]
            index += 1
        outputList.append(tempText)
        tempText = ""

    outputList.reverse()

    for i in range(len(outputList)):
        outputText += outputList[i]
    outputTextFile = open(outputPath, "w")
    outputTextFile.write(outputText)

print(inputPath, "-->", outputPath, "Success")

outputTextFile.close()
inputTextFile.close()
