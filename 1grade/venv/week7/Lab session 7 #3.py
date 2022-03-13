import random

def CreateList():
    a_list = []
    while True:
        if (len(a_list) == 10):
            break

        a = random.randint(0, 10)

        if not a in a_list:
            a_list.append(a)

    return a_list


def BubbleSort(list):
    print(list)
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
        print(list)

    return list


list1 = CreateList()
print("---------------BubbleSort------------------")
print(BubbleSort(list1))
print("---------------InsertionSort---------------")



def InsertionSort(list):
    print(list)
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
            else:
                break
        print(list)

    return list


list2 = CreateList()
print(InsertionSort(list2))
