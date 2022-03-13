import string

chack = int(input("Choice your Function(1, 2, 3): "))
inputPath = "input.txt"
inputTextFile = open(inputPath,"r")
inputText = inputTextFile.read()

if chack == 1:
    maxWord = ""
    for i in inputText.split():
        i = i.strip(",.")
        if len(maxWord) < len(i):
            maxWord = i
    print(maxWord, len(maxWord))

elif chack == 2:
    findWord = input("enter your addional input: ") #문자열 입력받기
    saveWord = ""  #출력할 데이터
    for i in inputText.split():#파일 속 단어 개수만큼 반복(i 변수에 단어 계속 대입)
        i = i.strip(",.")#단어의 . , 등 특수 문자 지우기
        if findWord in i : #만약 입력받은 문자열이 포함 된 단어를 찾으면
            if saveWord == "": #만약 출력할 단어가 비어있으면(최초로 데이터를 넣는 경우)
                saveWord = i + "\n" # 출력할 단어에 찾은 단어를 넣기
            cnt = 0 #cnt가 하는일: 중복된 단어가 있는지 알기 위해
            for j in saveWord.split(): #출력할 데이터에 있는 단어 만큼 반복(중복된 단어가 있는지 알아보기 위해
                jU = j.upper() #대문자로 다 바꾸기
                iU = i.upper() #대문자로 다 바꾸기
                if jU == iU:  # 중복된 단어가 있다면
                    cnt = 1 #중복한 단어가 있다는 것을 알기 위해 1로 바꾸기 -
                            #만약 cnt가 0이라면 중복되는 단어가 없다는 것 -> 출력할 문자열에 찾은 단어를 넣기
                            #만약 cnt가 0이라면 중복되는 단어가 있다는 것 -> 이번 반복문은 그냥 아무것도 안하기
                else:  # 28줄에서 두 단어를 비교했는데 단어가 중복되지 않았다면
                    pass #cnt를 그냥 냅두기
            if cnt == 0: #cnt는 출력할 문자열에 겹치는 단어가 있는지
                saveWord += i + "\n"#cnt가 0-> 중복된 단어가 없다 -> 찾은 단어를 집어 넣기
    print(saveWord) # 출력할 문자열을 출력한다 ?

elif chack == 3:
    saveWord = ""
    for i in inputText.split():
        i = i.strip(",.")
        iL = i.lower()
        if i != iL:
            if saveWord == "":
                saveWord = i + " \n"
            cnt = 0
            for j in saveWord.split():
                jU = j.upper()
                iU = i.upper()
                if jU == iU:  # 중복된 단어라면
                    cnt+= 1
                else:  # 중복된 단어가 아니라면
                    pass
            if cnt == 0:
                saveWord += i + "\n"

    print(saveWord)

inputTextFile.close()
