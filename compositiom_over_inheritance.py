class Engine:
    def start(self):
        return "Engine started"


class GPS:
    def navigate(self):
        return "Navigating..."


class Car:
    def __init__(self):
        self.engine = Engine()
        self.gps = GPS()

    def drive(self):
        print(self.engine.start())
        print(self.gps.navigate())
        print("Car is driving")


car = Car()
car.drive()
