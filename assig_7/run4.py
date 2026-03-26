import random

class Car:

    def __init__(self, reg, max_speed):
        self.registration_number = reg
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed = self.current_speed + change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours


# tạo danh sách xe
cars = []

for i in range(10):
    reg = "ABC-" + str(i + 1)
    max_speed = random.randint(150, 200)
    new_car = Car(reg, max_speed)
    cars.append(new_car)


race_on = True

while race_on:

    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_on = False


print("Race result:")

for car in cars:
    print(car.registration_number, car.maximum_speed,
          car.current_speed, car.travelled_distance)