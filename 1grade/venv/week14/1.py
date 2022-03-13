def myPrint(*args, sep=" ", end="\n"):
    string = ""

    for i in args:
        string += str(i)
        if i == args[len(args) - 1]:
            break
        string += sep

    string += end
    print(string, end="")

myPrint("Hello", "World")
myPrint("Hello", "World", sep="/")
myPrint("Hello", "World", end="~\n")
myPrint("Hello", "World", sep="/", end="~\n")
myPrint("1 + 2 =", 1 + 2)
print("-----------------------")
print("Hello", "World")
print("Hello", "World", sep="/")
print("Hello", "World", end="~\n")
print("Hello", "World", sep="/", end="~\n")
print("1 + 2 =", 1 + 2)