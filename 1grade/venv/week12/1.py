import time as t
import random


class Car(object):
    def __init__(self, name, speed, location, engine, end_time, acceleration, end):
        self.mName = name
        self.mSpeed = speed
        self.mLocation = location
        self.mEngine = engine
        self.mEndTime = end_time
        self.mAcceleration = acceleration
        self.mEnd = end

    def set_engine_on(self):
        self.mEngine = True

    def set_engine_off(self):
        self.mEngine = False

    def set_acceleration(self):
        self.mAcceleration = random.randint(-20, 50)

    def set_end(self):
        self.mEnd = True

    def set_location(self):
        self.mLocation += self.mSpeed


class Mclaren(Car):

    def set_speed(self):
        maxSpeed = 200
        self.mSpeed += self.mAcceleration

        if self.mSpeed < 0:
            self.mSpeed = 0
        if self.mSpeed > maxSpeed:
            self.mSpeed = maxSpeed


class Ferrari(Car):

    def set_speed(self):
        maxSpeed = 190
        self.mSpeed += self.mAcceleration

        if self.mSpeed < 0:
            self.mSpeed = 0
        if self.mSpeed > maxSpeed:
            self.mSpeed = maxSpeed


class Porsche(Car):

    def set_speed(self):
        maxSpeed = 180
        self.mSpeed += self.mAcceleration

        if self.mSpeed < 0:
            self.mSpeed = 0
        if self.mSpeed > maxSpeed:
            self.mSpeed = maxSpeed


time = 0
car = [1,2,3,4,5,6]
car[0] = Mclaren("car1", 0, 0, False, 0, 0, False)
car[1] = Mclaren("car2", 0, 0, False, 0, 0, False)
car[2] = Ferrari("car3", 0, 0, False, 0, 0, False)
car[3] = Ferrari("car4", 0, 0, False, 0, 0, False)
car[4] = Porsche("car5", 0, 0, False, 0, 0, False)
car[5] = Porsche("car6", 0, 0, False, 0, 0, False)

print("%d: %d %d %d %d %d %d" % (time, car[0].mLocation,
                                 car[1].mLocation, car[2].mLocation, car[3].mLocation,
                                 car[4].mLocation, car[5].mLocation))

for i in range(6):
    car[i].set_engine_on()

print("race Start")
print("------" * 3)

time = 1
while True:

    for i in range(6):
        if car[i].mLocation >= 1000 and car[i].mEnd is False:
            car[i].set_end() # car.mEnd = True
            car[i].mEndTime = time
            car[i].set_engine_off()

    if car[1].mEnd == car[2].mEnd == car[3].mEnd == car[4].mEnd == car[5].mEnd == car[0].mEnd is True:
        print("------" * 3)
        print("Result")
        print("------" * 3)
        break

    for i in range(6):
        if car[i].mEnd is False:
            car[i].set_acceleration()
            car[i].set_speed()
            car[i].set_location()

    t.sleep(1)
    print("%d: %d %d %d %d %d %d" % (time, car[0].mLocation,
                                     car[1].mLocation, car[2].mLocation, car[3].mLocation,
                                     car[4].mLocation, car[5].mLocation))
    time += 1
temp = 0
winNum = 1
winD = 0
time = 0

while True:
    winD = 0
    if time >= 6:
        break

    for i in range(6):
        if car[i].mEndTime == temp:
            print(str(winNum) + " Prize is " + str(car[i].mName))
            winD += 1
            time += 1

    winNum += winD
    temp += 1
