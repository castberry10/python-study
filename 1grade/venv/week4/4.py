import random

print("Start Baseball Game!")
firL = random.randint(1, 9)

while True:
    secL = random.randint(1, 9)
    if (firL != secL):
        break

while True:
    thiL = random.randint(1, 9)
    if (thiL != secL and thiL != firL):
        break


# 숫자 배정 끝

while True:
    ball = 0
    strike = 0

    firD = int(input("a: "))
    secD = int(input("b: "))
    thiD = int(input("c: "))

    if(firD == firL and secD == secL and thiD == thiL):
        print("Victory")
        break

    if(firD == firL):
        strike += 1
    elif(firD == secL or firD == thiL):
        ball += 1

    if (secD == secL):
        strike += 1
    elif (secD == firL or secD == thiL):
        ball += 1

    if (thiD == thiL):
        strike += 1
    elif (thiD == secL or thiD == firL):
        ball += 1

    print("Strike : " + str(strike) + " Ball : " + str(ball))