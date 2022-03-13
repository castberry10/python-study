import random

print("start Up&Down Game")
landom = random.randint(1,20)
cnt = 0
while True:
    inputData = int(input("User Input: "))
    cnt += 1
    if(inputData < landom):
        print("Up")
    elif (inputData > landom):
        print("Down")
    elif (inputData == landom):
        print("Victory! You had "+ str(cnt) + " tries")
        break