def read_data():
    inputPath = "score.txt"
    inputTextFile = open(inputPath, "r")
    inputText = inputTextFile.read()
    outputData = []
    text_split = inputText.split()
    for i in range(len(text_split)):
        text_split[i] = text_split[i].strip(",")

    for i in range(len(text_split) // 3):
        if outputData: #배열 속 데이터가 있다면
            cnt = 0
            for j in range(len(outputData)):
                if text_split[3 * i] == outputData[j][0]:
                    outputData[j].append([text_split[3 * i + 1], text_split[3 * i + 2]])
                    cnt = 1
                    break
            if cnt == 0:
                outputData.append([text_split[3 * i], [text_split[3 * i + 1], text_split[3 * i + 2]]])

        else:
            outputData.append([text_split[3 * i], [text_split[3 * i + 1], text_split[3 * i + 2]]])

    inputTextFile.close()
    return outputData

def id_print(dataList):
    StudentID = input("Input your Student ID: ")
    for i in dataList:
        if i[0] == StudentID:
            sum = 0
            max = 0
            min = 100
            for j in range(len(i) - 1):
                print(i[j+1][0], ":", i[j+1][1])
                if max < int(i[j+1][1]):
                    max = int(i[j+1][1])
                if min > int(i[j+1][1]):
                    min = int(i[j+1][1])
                sum += int(i[j+1][1])
            print("Average :", sum / len(i) - 1 ,"Max :" , max,"min :",min )
            break

def sub_print(dataList):
    subject = input("Input the subject :")
    minScore = int(input("Min score :"))
    text1 = ""
    print("Sudent ID who gets over",minScore,"in math :", end=" ")
    for i in dataList:
        for j in range(len(i) - 1):
            if i[j + 1][0] == subject:
                if int(i[j + 1][1]) > minScore:
                    text1 += i[0]+", "
    text1 = text1.strip(", ")
    print(text1)


def histogram(dataList):
    subject = input("Input the subject :")
    highScoreCnt = 0
    midScoreCnt = 0
    lowScoreCnt = 0
    for i in dataList:
        for j in range(len(i) - 1):
            if i[j + 1][0] == subject:
                if int(i[j + 1][1]) > 90:
                    highScoreCnt += 1

                elif int(i[j + 1][1]) > 80:
                    midScoreCnt += 1

                elif int(i[j + 1][1]) > 70:
                    lowScoreCnt += 1

    max = highScoreCnt
    if max < midScoreCnt:
        max = midScoreCnt
    if max < lowScoreCnt:
        max = lowScoreCnt

    print("histogram for", subject,"\n")
    his_list = [[' ' for j in range(3)] for i in range(max)]

    for i in range(highScoreCnt):
        his_list[max - i - 1][0] = "*"

    for i in range(midScoreCnt):
        his_list[max - i - 1][1] = "*"

    for i in range(lowScoreCnt):
        his_list[max - i - 1][2] = "*"

    for i in range(max):
        print("\t",his_list[i][0],"\t\t",his_list[i][1] ,"\t\t ",his_list[i][2])

    print("-----" * 7)

    print(" 90-100\t  80-89 \t 70-79")
    # print(his_list)
    # print(highScoreCnt, midScoreCnt, lowScoreCnt)

dataList = read_data()

id_print(dataList)
print("")
sub_print(dataList)
print("")
histogram(dataList)