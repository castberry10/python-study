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

    max2 = a
    if (b > max2) and (b < max):
        max2 = b
    if (c > max2) and (c < max):
        max2 = c
    if (d > max2) and (d < max):
        max2 = d
    if (e > max2) and (e < max):
        max2 = e

    return max2


a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))
e = int(input("Input e: "))

print(func(a, b, c, d, e))
