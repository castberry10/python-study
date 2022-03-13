for_n = int(input("input n: "))

listN = []
for i in range(for_n):
    a = int(input("list["+str(i)+"] : "))
    listN.append(a)

for i in range(len(listN) - 1):
    if listN[i] > listN[i + 1]:
        listN[i], listN[i + 1] = listN[i + 1], listN[i]


for i in range(len(listN) - 2):
    if listN[i] > listN[i + 1]:
        listN[i], listN[i + 1] = listN[i + 1], listN[i]

print(listN[len(listN) - 1])
print(listN[len(listN) - 2])
