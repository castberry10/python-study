def myPrint():
    print("Intput Your Information \n----------------------")

def myInput():
    stuNo = input("학번 : ")
    stuName = input("이름 : ")
    stuTy = input("학과 : ")
    return stuNo, stuName, stuTy

def myResult(stuID, name, major):
    print("----------------------")
    print(stuID, name, major)

def myProg():
    myPrint()
    stuID, name, major = myInput()
    myResult(stuID, name, major)

myProg()