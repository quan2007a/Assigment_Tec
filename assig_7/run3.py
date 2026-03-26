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
        distance = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance


car1 = Car("ABC-123", 142)

car1.current_speed = 60
car1.travelled_distance = 2000

car1.drive(1.5)

print("Distance now:", car1.travelled_distance)