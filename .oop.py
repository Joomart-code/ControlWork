class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Ошибка")

    def get_age(self):
        return self.__age
p = Person()
p.set_age(25)
print(f"Возраст: {p.get_age()}")
p.set_age(-5)
print(f"Возраст после ошибки: {p.get_age()}")

print("-----------------")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())

print("-----------------")

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))



from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
print("-----------------")
class Rectangle(Shape):
    def __init__(self, shirina, visota):
        self.shirina = shirina
        self.visota = visota

    def area(self):
        return self.shirina * self.visota

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Площадь круга: S = π * r^2
        return math.pi * (self.radius ** 2)

rect = Rectangle(10, 5)
circle = Circle(7)
print(f"Площадь прямоугольника:{rect.area()}")
print(f"Площадь круга: {circle.area():.2f}")