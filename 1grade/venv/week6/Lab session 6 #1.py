secuYN = input("1. encrypt 2. decrypt: ")
inFname = input("input FileName: ")
outFname = input("output FileName: ")
key = int(input("Key: "))

if secuYN == "1":
    secu = key
elif secuYN == "2":
    secu = -key

inFp = open(inFname, "r", encoding="utf-8")
outFp = open(outFname, "w", encoding="utf-8")

inStr = inFp.read()

outStr = ""
'''
for i in range(len(inStr)):
    ch = inStr[i]
    chNum = ord(ch)
    chNum = chNum + secu
    ch2 = chr(chNum)
    outStr += ch2
'''
for i in inStr:
    outStr += chr(ord(i) + secu)

outFp.write(outStr)

outFp.close()
inFp.close()
print("%s --> %s Success" % (inFname, outFname))
