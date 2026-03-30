from abc import ABC, abstractmethod
from math import pi

#__Задание-1____________________________________________________
class Animal:
    totalitarianism = 0

    def __init__(self, name):
        self.name = name
        self.energy = 100

    def speak(self):
        Animal.totalitarianism += 1
        self.energy -= 5
    def info(self):
        print(f"{self.name} says {Animal.totalitarianism}")

class Dog(Animal):
    # def speak(self):
    #     print("Гав")
    #     super().speak()
    #     for i in range(self.energy):
    #         print("Гав")

    def speak(self):
        while self.energy > 0:
            print("Гав")
            super().speak()
    def infor(self):
        print(self.energy)


class Cat(Animal):
    def speak(self):
        while self.energy >= 10:
            print("Мяу")
            super().speak()
        print("Кот спит")
        self.energy = 100
    def infor(self):
        print(self.energy)

#__Задание-2____________________________________________________
class Employee:
    def __init__(self, baseSalary, performanceRating):
        self.__baseSalary = baseSalary
        self._performanceRating = performanceRating

    def calculateSalary(self):
        return self.__baseSalary * self._performanceRating

    def _get_base_salary(self):
        return self.__baseSalary

class Manager(Employee):
    def __init__(self, baseSalary, performanceRating, subordinates):
        super().__init__(baseSalary, performanceRating)
        self.subordinates = subordinates

    def calculateSalary(self):
        base = super().calculateSalary()
        bonus = 10 * self._get_base_salary() * self.subordinates
        return base + bonus


class Developer(Employee):
    def __init__(self, baseSalary, performanceRating, languageComplexity):
        super().__init__(baseSalary, performanceRating)
        self.languageComplexity = languageComplexity

    def calculateSalary(self):
        base = super().calculateSalary()
        if self._performanceRating > 3:
            return base * self.languageComplexity
        return base

#__Задание-3____________________________________________________
class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def scale(self, factor):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        if radius >= 0:
            self.radius = radius
        else:
            self.radius = 0

    def area(self):
        return pi * self.radius ** 2

    def scale(self, factor):
        self.radius *= factor

class Rectangle(Shape):
    def __init__(self, width, height):
        if width >= 0:
            self.width = width
        else:
            self.width = 0
        if height >= 0:
            self.height = height
        else:
            self.height = 0

    def area(self):
        return self.width * self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

def scale_shapes(Shapes):
    for shape in Shapes:
        if shape.area() > 100:
            factor = 2.0
        else:
            factor = 0.5

        shape.scale(factor)

#__Задание-4____________________________________________________
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def copy(cls, other):
        return cls(other.name, other.age)

class Document:

    def __init__(self, data):
        self.data = data

    @classmethod
    def copy(cls, other):
        return cls(other.data.copy())

class Buffer:

    def __init__(self, size):
        self.data = [0] * size

    @classmethod
    def copy(cls, other):
        new_buffer = cls(len(other.data))
        new_buffer.data = other.data.copy()
        return new_buffer

    def assign(self, other):
        self.data = other.data.copy()



if __name__ == "__main__":
    print("программа")

    # __Задание-1__
    Bob = Dog("Bob")
    Bob.speak()
    Bob.info()

    Muse = Cat("Muse")
    Muse.speak()
    Muse.info()
    Bob.infor()
    Muse.infor()

    #__Задание-2__
    # manager = Manager(1000, 4, 3)
    # developer = Developer(900, 4, 1.2)
    #
    # print(manager.calculateSalary())
    # print(developer.calculateSalary())

    # __Задание-3__
    # shapes = [Circle(6), Rectangle(4, 9), Rectangle(20, 6)]
    # scale_shapes(shapes)

    # __Задание-4__

    # __Задание-4.1__
    # p1 = Person("Miko", 30)
    # p2 = Person.copy(p1)
    # p2.name = "Aybek"
    # print("Original:", p1.name)
    # print("Copy:", p2.name)

    # __Задание-4.2__
    # d1 = Document([1, 2, 3, 4])
    # d2 = Document.copy(d1)
    # d2.data[0] = 100
    # print("Original:", d1.data)
    # print("Copy:", d2.data)

    # __Задание-4.3__
    # b1 = Buffer(5)
    # b2 = Buffer.copy(b1)
    # b1.data[0] = 100
    # b3 = Buffer(3)
    # print(b3.data)
    # b3.assign(b1)
    # print(b1.data, b2.data, b3.data)