class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)