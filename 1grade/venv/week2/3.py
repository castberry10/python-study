year = int(input("연도룰 입력하세요 : "))

if(year % 4 == 0 and year % 100 != 0):
    print(True)
elif(year % 400 == 0):
    print(True)
else:
    print(False)

