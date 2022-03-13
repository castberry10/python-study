def func1(list):
    max = 0
    for i in list:
        if max < i:
            max = i

    return max


def func2(list):
    max = 0
    for i in list:
        if max < i:
            max = i

    max2 = 0
    for i in list:
        if i < max and max2 < i:
            max2 = i

    return max2


n = int(input("Input n: "))
list = []
for i in range(n):
    list.append(int(input("list[{}] : ".format(i))))

print(func1(list))
print(func2(list))
