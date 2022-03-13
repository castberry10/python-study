def readData(s):
    data = []
    for i in s:
        flag = 0
        sp = i.split(', ')
        for j in range(len(data)):
            if sp[0] == data[j][0]:
                data[j].append([sp[1], int(sp[2])])
                flag = 1
                break
        if flag == 0:
            data.append([sp[0], [sp[1], int(sp[2])]])
            
    return data


def inputStudentId(data):
    sum = 0
    max = 0
    min = 999

    stuID = input("Input your Studend ID : ")

    for set in data:
        if stuID == set[0]:
            for subject in range(1, len(set)):
                print("{} : {}".format(set[subject][0], set[subject][1]))
                sum += set[subject][1]
                if max < set[subject][1]:
                    max = set[subject][1]
                if min > set[subject][1]:
                    min = set[subject][1]
            print("Average : {}, Max : {}, Min : {}".format(sum / 3, max, min))

    print()


def inputSubjectID(data):
    stuList = []
    Subject = input("Input the subject : ")
    MinScore = int(input("Min score : "))

    for set in data:
        for subject in range(1, len(set)):
            if Subject == set[subject][0]:
                if MinScore < set[subject][1]:
                    stuList.append(set[0])

    print("Student ID who gets over {} in {} : ".format(MinScore, Subject), end="")
    for i in range(len(stuList) - 1):
        print(stuList[i], end=", ")
    print(stuList[len(stuList) - 1])
    print()


def printHistogram(data):
    stuList1 = [" "] * len(data)
    stuList2 = [" "] * len(data)
    stuList3 = [" "] * len(data)
    index = [0, 0, 0]

    Subject = input("Input the subject : ")

    for set in data:
        for subject in range(1, len(set)):
            if Subject == set[subject][0]:
                if (set[subject][1] <= 100) and (set[subject][1] >= 90):
                    stuList1[index[0]] = "*"
                    index[0] += 1
                    break
                elif (set[subject][1] <= 89) and (set[subject][1] >= 80):
                    stuList2[index[1]] = "*"
                    index[1] += 1
                    break
                elif (set[subject][1] <= 79) and (set[subject][1] >= 70):
                    stuList3[index[2]] = "*"
                    index[2] += 1
                    break

    index.sort()

    print("Histogram for {}".format(Subject))

    for i in range(index[2], -1, -1):
        print("\t{}\t\t\t{}\t\t\t{}".format(stuList1[i], stuList2[i], stuList3[i]))

    print("-" * 35)
    print("90-100\t\t 80-89\t\t  70-79")


f = open('score.txt')
s = f.read().split('\n')
data = readData(s)
inputStudentId(data)
inputSubjectID(data)
printHistogram(data)