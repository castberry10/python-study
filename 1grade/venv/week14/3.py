def myFilter(f, data_list):
    list_ = []
    for i in data_list:
        if f(i):
            list_.append(i)
    return list_


def myMap(f, data_list):
    list_ = []

    for i in data_list:
        list_.append(f(i))

    return list_

data_list = [1, 10, 9, 23, 17, 24, 7, 12, 30]

val1 = myFilter(lambda x: x % 3 == 0, data_list)
print(val1)
val2 = myMap(lambda x: x * 2 + 10, data_list)
print(val2)