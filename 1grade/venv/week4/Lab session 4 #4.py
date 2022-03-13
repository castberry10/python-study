import random

x = random.randint(1, 9)
y = random.randint(1, 9)
z = random.randint(1, 9)
while x == y:
    y = random.randint(1, 9)
while x == z or y == z:
    z = random.randint(1, 9)


def baseball(a, b, c):

    strike = 0
    ball = 0

    if a == x:
        strike += 1
    if b == y:
        strike += 1
    if c == z:
        strike += 1
    if a == y:
        ball += 1
    if a == z:
        ball += 1
    if b == x:
        ball += 1
    if b == z:
        ball += 1
    if c == x:
        ball += 1
    if c == y:
        ball += 1

    return strike, ball


print("Start Baseball Game!!")

while True:
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))

    strike, ball = baseball(a, b, c)

    print("Strike : {} Ball : {}".format(strike, ball))

    if strike == 3:
        print("Victory")
        break
