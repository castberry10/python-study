import random

global count
count = 0
def func():
    global count
    count += 1

rand = random.randint(1,100)

for i in range(rand):
    func()

print("rand =", rand)
print("count =", count)