def func(Str, n):
    list = []
    for i in range(0, len(Str), n):
        list.append(Str[i:i+n])

    list.reverse()
    str2 = ""
    for i in list:
        str2 += i

    return str2


def func2(Str, n):

    list = []
    list.append(Str[:len(Str) % n])
    for i in range(len(Str) % n, len(Str), n):
        list.append(Str[i:i+n])

    list.reverse()
    str2 = ""
    for i in list:
        str2 += i

    return str2



secuYN = int(input("1. encrypt 2. decrypt: "))
inFname = input("input FileName: ")
outFname = input("output FileName: ")
key = int(input("Key: "))

inFp = open(inFname, "r", encoding="utf-8")
outFp = open(outFname, "w", encoding="utf-8")


inStr = inFp.read()

if secuYN == 1:
    outStr = func(inStr, key)
else:
    outStr = func2(inStr, key)

outFp.write(outStr)


outFp.close()
inFp.close()
print("%s --> %s Success" % (inFname, outFname))
