chack = int(input("1. encrypt 2. decrypt: "))
inputPath = input("input FileName: ")
outputPath = input("output FileName: ")
key = int(input("key: "))

inputTextFile = open(inputPath,"r")
inputText = inputTextFile.read()

if(chack == 1):
    outputText = ""
    for i in inputText:
        outputText += chr(ord(i) + key)
    outputTextFile = open(outputPath, "w")
    outputTextFile.write(outputText)

elif(chack == 2):
    outputText = ""
    for i in inputText:
        outputText += chr(ord(i) - key)
    outputTextFile = open(outputPath, "w")
    outputTextFile.write(outputText)

print(inputPath, "-->", outputPath, "Success")
outputTextFile.close()
inputTextFile.close()