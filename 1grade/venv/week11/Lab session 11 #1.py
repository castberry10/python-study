fobj = open("input.txt", "r")

dic = dict()

for line in fobj:
    s = line.split()
    id = int(s[1])
    if id in list(dic.keys()):
        dic[id] += 1
    else:
        dic[id] = 1


print(len(dic))
max1 = max(list(dic.values()))

list1 = sorted(dic.values(), reverse=True)

for key, value in dic.items():
    if value == list1[0]:
        print("most frequently called id is {}, {} TImes".format(key, value))
        break

for i in range(5):
    for key, value in dic.items():
        if value == list1[i]:
            print("{}: {}, {}Times".format(i + 1, key, value))