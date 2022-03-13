def magicSquare(n):
    x = n // 2
    y = n - 1
    count = 1

    arr = [[0] * n for i in range(n)]

    while count <= n * n:
        arr[y][x] = count
        count += 1

        x += 1
        y += 1

        if x == n:
            x = 0

        if y == n:
            y = 0

        if arr[y][x] != 0:
            x -= 1
            y -= 2
            if x == n:
                x = 0

            if y == n:
                y = 0

    return arr

def printSquare(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            print("%5d" % list[i][j], end=" ")
        print()


def checkSquare(list):
    sumList = []

    for i in range(len(list)):
        sum = 0
        for j in range(len(list[0])):
            sum += list[i][j]
        sumList.append(sum)

    for i in range(len(list)):
        sum = 0
        for j in range(len(list[0])):
            sum += list[j][i]
        sumList.append(sum)

    sum = 0
    for i in range(len(list)):
        sum += list[i][i]
    sumList.append(sum)

    sum = 0
    for i in range(len(list)):
        sum += list[i][n - 1 - i]
    sumList.append(sum)

    print(sumList)


while True:
    n = int(input("Input Odd Number : "))
    if n % 2 == 1:
        break

list = magicSquare(n)
print()
printSquare(list)
print()
checkSquare(list)