"""
In object-oriented programming (OOP), a class is a blueprint for creating objects (instances).
It defines attributes (data) and methods (behavior) that the instances will have. You then
instantiate (create) objects from the class; each object holds its own data while sharing the
class's methods.

В объектно-ориентированном программировании класс — это шаблон для создания объектов.
Класс определяет свойства (данные) и методы (поведение). Создавая экземпляры класса, вы
получаете объекты с собственными значениями полей, которые используют общие методы класса.
"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def print_fields(self):
        print("Book: ", self.title, " by ", self.author, ", Pages: ", self.pages)


class Student:
    def __init__(self, name, age, grades, student_id=None):
        self.name = name
        self.age = age
        self.grades = grades
        self.__student_id = student_id

    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def print_info(self):
        print("Name: ", self.name)
        if self.age >= 18:
            print("Age: ", self.age)
        print("Average: ", self.average_grade())

    def equals(self, other):
        return self.name == other.name and self.age == other.age and self.grades == other.grades


student1 = Student("Aybek", 20, [5, 4, 3])
student1.print_info()

if student1 is not None:
    student1.print_info()

print(student1.average_grade())

# student1 = None
# student1.print_info()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        return "Meow"


class Dog(Animal):
    def speak(self):
        return "Woof"


cat = Cat("Murky")
dog = Dog("Bobi")

print(cat.speak())
print(dog.speak())

s1 = Student("Aybek", 20, grades=[4, 5, 3, 5], student_id=12345)
s2 = Student("Aybek", 18, grades=[4, 5, 3, 5], student_id=12345)
s3 = Student("Dana", 17, grades=[5, 5, 5], student_id=54321)

print(s1.equals(s2))  # False
print(s1.equals(s3))  # False


class Room:
    def __init__(self, name, number):
        # Protected
        self._name = name
        # Private
        self.__number = number

    def set_data(self, name, number):
        if isinstance(name, str) and isinstance(number, int):
            # Protected
            self._name = name
            # Private
            self.__number = number
        else:
            print("Типы данных неверный")

    def out(self):
        return self._name, self.__number


pt = Room("Aybek", 12)
print(pt.out())
pt.set_data("Samat", 100)
print(pt.out())
pt.set_data("Asia", 24)
print(pt.out())
