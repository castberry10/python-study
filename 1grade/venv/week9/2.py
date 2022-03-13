def make_ma(size):
    ma = [[0 for j in range(size)] for i in range(size)]
    lastNum = size * size

    x = 0 # x가 높을수록 아래
    y = 0 # y가 높을수옥 오른쪽

    inputNum = 1
    MAX_INDEX = size - 1 # 마지막 줄의 인덱스
    ma[MAX_INDEX][MAX_INDEX//2] = inputNum #맨 아래쪽 가운데
    x,y = MAX_INDEX, MAX_INDEX//2
    inputNum += 1
    while True:
        if inputNum > lastNum: #End?
            return ma

        if x + 1 > MAX_INDEX and y + 1 > MAX_INDEX: # 맨오른쪽 밑에서 오른쪽아래로 내려간 경우
            ma[x - 1][y] = inputNum
            x, y = x - 1, y
            inputNum += 1
        elif x + 1 > MAX_INDEX or y + 1 > MAX_INDEX: # 범위를 넘는가?
            if x + 1 > MAX_INDEX: #x가 넘는가?
                cnt = 0
                for i in range(size):
                    if ma[i][y+1] == 0:
                        ma[i][y+1] = inputNum
                        inputNum += 1
                        x,y = i, y+1
                        cnt = 1
                        break
                if cnt == 0:#이동해도 칸이 없다면
                    ma[x-1][y] = inputNum
                    x, y = x - 1, y
                    inputNum += 1

                cnt = 3
            elif y + 1 > MAX_INDEX:#y가 넘는가?
                for i in range(size):
                    if ma[x+1][i] == 0:
                        ma[x+1][i] = inputNum
                        inputNum += 1
                        x , y = x + 1, i
                        cnt = 1
                        break
                if cnt == 3: #이동해도 칸이 없다면
                    ma[x-1][y] = inputNum
                    x , y = x -1 , y
                    inputNum += 1
        else:
            if ma[x+1][y+1] == 0: #오른쪽 아래칸이 비어있다면
                ma[x + 1][y + 1] = inputNum
                x, y = x + 1, y + 1
                inputNum += 1
            else:
                ma[x - 1][y] = inputNum
                x, y = x - 1,y
                inputNum += 1

def print_ma(ma, size):
    for i in range(size):
        for j in range(size):
            print("\t", ma[i][j],sep="", end="")
        print()

def test_ma(ma, size):
    test_list = []
    sum = 0
    for i in range(size):
        sum = 0
        for j in range(size):
            sum += ma[i][j]
        test_list.append(sum)

    for i in range(size):
        sum = 0
        for j in range(size):
            sum += ma[j][i]
        test_list.append(sum)

    sum = 0
    for i in range(size):
        sum += ma[i][i]
    test_list.append(sum)

    sum = 0
    for i in range(size):
        sum += ma[i][size - 1 -i]

    test_list.append(sum)
    print(test_list)

while True:
    size = int(input("Input Odd Number : "))
    if size % 2 == 0:
        print("홀수를 입력하시오")
    if size % 2 == 1:
        break

ma = make_ma(size)
print_ma(ma, size)
test_ma(ma,size)