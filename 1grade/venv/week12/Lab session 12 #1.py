import time
import random


class Vehicle(object):
    count = 1

    def __init__(self, number):
        self.mNumber = number
        self.mMax_speed = 0
        self.mPosition = 0
        self.mSpeed = 0
        self.mStartEngine = 0
        self.mPrize = 0
        self.mTime = 0
        pass

    def accelerate(self, acceleration):
        if self.mStartEngine:
            if (self.mSpeed + acceleration < self.mMax_speed) and (self.mSpeed + acceleration > 0):
                self.mSpeed += acceleration
            elif self.mSpeed + acceleration >= self.mMax_speed:
                self.mSpeed = self.mMax_speed
            elif self.mSpeed + acceleration <= 0:
                self.mSpeed = 0
            self.mPosition += self.mSpeed

    def get_position(self):
        return self.mPosition

    def get_number(self):
        return self.mNumber

    def start_engine(self):
        self.mStartEngine = 1

    def stop_engine(self):
        self.mStartEngine = 0

    def set_time(self, seconds):
        self.mTime = seconds

    def get_time(self):
        return self.mTime


class Mclaren(Vehicle):
    def __init__(self, number):
        Vehicle.__init__(self, number)
        self.mMax_speed = 200


class Porsche(Vehicle):
    def __init__(self, number):
        Vehicle.__init__(self, number)
        self.mMax_speed = 190


class Ferrari(Vehicle):
    def __init__(self, number):
        Vehicle.__init__(self, number)
        self.mMax_speed = 180


car1 = Mclaren(1)
car2 = Porsche(2)
car3 = Ferrari(3)
car4 = Mclaren(4)
car5 = Porsche(5)
car6 = Ferrari(6)

car_list = [car1, car2, car3, car4, car5, car6]
prize_list = []
sec = 0
prize = 0

for car in car_list:
    car.start_engine()

print("{}: ".format(sec), end="")
sec += 1
for car in car_list:
    print("{}".format(car.get_position()), end=" ")

print()
print("race Start")
print("---------------------------")

while True:
    if len(prize_list) < len(car_list):
        print("{}: ".format(sec), end="")
        for car in car_list:
            car.accelerate(random.randint(-10, 50))
            print("{}".format(car.get_position()), end=" ")
            if car.get_position() >= 1000:
                car.stop_engine()
                if car not in prize_list:
                    prize_list.append(car)
                    car.set_time(sec)
        print()
        time.sleep(1)
        sec += 1
    else:
        break


print("---------------------------")
print("Result")
print("---------------------------")

last_sec = 0
result = []

for i in range(len(prize_list)):
    if last_sec != prize_list[i].get_time():
        prize = i + 1
    result.append((prize, prize_list[i]))
    last_sec = prize_list[i].get_time()

for prize, car in result:
    print("{} Prize is car{}".format(prize, car.get_number()))
