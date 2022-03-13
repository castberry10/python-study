def func(a, b, c, d, e):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    if d > max:
        max = d
    if e > max:
        max = e

    return max


a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))
e = int(input("Input e: "))

print(func(a, b, c, d, e))
