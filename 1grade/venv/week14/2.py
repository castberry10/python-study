data = [1, 10, 9, 23, 17, 24, 7, 12, 30]
val1 = []
def func(x):
    if x % 2 == 0:
        return x + 1
    else:
        return 0

for i in data:
    res = func(i)
    if res != 0:
        val1.append(res)


val2 = [i + 1 for i in list(filter(lambda x: x % 2 == 0, data))]

print(val1)
print(val2)