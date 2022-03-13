import random

ans = random.randint(1, 20)
count = 0

while True:
    n = int(input("input : "))
    count += 1
    if n == ans:
        print("정답입니다. 시도횟수 : {}".format(count))
        break
    elif n > ans:
        print("정답은 {}보다 작습니다.".format(n))
    elif n < ans:
        print("정답은 {}보다 큽니다.".format(n))
