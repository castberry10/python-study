import random

list1 = [] # 버블 정렬
list2 = [] # 선택 정렬
cnt = 0
while True:
    num = random.randint(0, 10)
    if cnt == 10:
        break
    if num not in list1:
        list1.append(num)
        cnt += 1

cnt = 0
while True:
    num = random.randint(0, 10)
    if cnt == 10:
        break
    if num not in list2:
        list2.append(num)
        cnt += 1

print("---------------Bubble Sort------------------")
print(list1)
for j in range(len(list1) - 1):
    for i in range(len(list1) - j - 1 ):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
    print(list1)

print("---------------Insertion Sort---------------")
for i in range(len(list2)):
    for j in range(i, 0, -1):
        if list2[j - 1] > list2[j]:
            list2[j], list2[j - 1] = list2[j - 1], list2[j]
        else:
            break
    print(list2)