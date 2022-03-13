def myAdd(a, b):
    return a+b
def mySubtract(a, b):
    return a-b
def myMutiply(a, b):
    return a*b
def myDivide(a, b):
    return a/b

def myCalculate(func, i, j):
    return func(i,j)

print(myCalculate(myAdd, 1, 2))
print(myCalculate(mySubtract, 1, 2))
print(myCalculate(myMutiply, 1, 2))
print(myCalculate(myDivide, 1, 2))