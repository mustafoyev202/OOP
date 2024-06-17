class Vehicle:
    def general_usage(self):
        print("General Usage:transportation")


class Car(Vehicle):
    def __init__(self):
        print("Car")
        self.wheel = 4
        self.has_root = True

    def special_usage(self):
        self.general_usage()
        print("Special Usage:vacation with family")


class Motorcycle(Vehicle):
    def __init__(self):
        print("Motorcycle")
        self.has_root = False
        self.wheel = 2

    def special_usage(self):
        self.general_usage()
        print("Special Usage:motorcycle")


c = Car()
c.special_usage()

print(isinstance(c, Car))
print(issubclass(Car, Vehicle))



# MultiInheritance

class Father():
    def gardening(self):
        print("Gardening")


class Mother():
    def cooking(self):
        print("Cooking")


class Child(Father, Mother):
    def sports(self):
        print("Sports")


c = Child()
c.gardening()
c.cooking()
c.sports()
