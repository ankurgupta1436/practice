#* Vehicle → Abstract class

from tracemalloc import start


# Car / Bike → Inherit from Vehicle

# __fuel → Encapsulation (private variable)

# start() → Polymorphism (different behavior for Car & Bike)

# car, bike → Objects



from abc import ABC, abstractmethod

# ===============================
# Abstraction
# ===============================
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass


# ===============================
# Encapsulation + Inheritance
# ===============================
class Car(Vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand)
        self.__fuel = fuel     # private variable (encapsulation)

    def start(self):
        if self.__fuel > 0:
            print(f"{self.brand} car started")
        else:
            print(f"{self.brand} has no fuel")

    def drive(self):
        self.__fuel -= 1
        print(f"Driving... Fuel left: {self.__fuel}")

    def get_fuel(self):
        return self.__fuel


class Bike(Vehicle):
    def start(self):
        print(f"{self.brand} bike started")


# ===============================
# Polymorphism
# ===============================
def start_vehicle(vehicle):
    vehicle.start()   # same method, different behavior


# ===============================
# Object creation
# ===============================
car = Car("Tesla", 3)
bike = Bike("Yamaha")

start_vehicle(car)
car.drive()
print("Fuel:", car.get_fuel())

start_vehicle(bike)
