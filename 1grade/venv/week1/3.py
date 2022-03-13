import math

a = int(input("a의 값을 입력하세요: "))
b = int(input("b의 값을 입력하세요: "))
c = int(input("c의 값을 입력하세요: "))

x1 = ( (-b + (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)
x2 = ( (-b - (math.sqrt(math.pow(b,2) - 4 * a * c)))/2 * a)

print("x1 = " , x1)
print("x2 = " , x2)
