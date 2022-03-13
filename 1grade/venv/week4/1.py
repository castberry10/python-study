data1 = int(input("Input a: "))
data2 = int(input("Input b: "))
data3 = int(input("Input c: "))
data4 = int(input("Input d: "))
data5 = int(input("Input e: "))

if(data1>data2):
    maxData1 = data1
else:
    maxData1 = data2

if(data3>data4):
    maxData2 = data3
else:
    maxData2 = data4

if(maxData1 > maxData2):
    maxData3 = maxData1
else:
    maxData3 = maxData2

if(maxData3 > data5):
    printData = maxData3
else:
    printData = data5

print(printData)