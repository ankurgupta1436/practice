class Vehicle:

    def start(self):
        raise NotImplementedError("Subclass must implement this method")

    def stop(self):
        raise NotImplementedError("Subclass must implement this method")


class Car(Vehicle):

    def start(self):
        print("Car starts with a key.")

    def stop(self):
        print("Car stops using brakes.")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with self-start button.")

    def stop(self):
        print("Bike stops using hand brakes.")


# Creating objects
c = Car()
b = Bike()

c.start()
c.stop()

b.start()
b.stop()