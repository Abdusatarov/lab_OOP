from __future__ import annotations
import math

class Car:
    def __init__(self, make: str, year: int, price: float):
        if year < 0:
            raise ValueError("Год не может быть отрицательным.")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.__make = make
        self.__year = int(year)
        self.__price = float(price)

    def get_make(self) -> str:
        return self.__make

    def get_year(self) -> int:
        return self.__year

    def get_price(self) -> float:
        return self.__price

    def set_make(self, make: str):
        self.__make = make

    def set_year(self, year: int):
        if year < 0:
            raise ValueError("Год не может быть отрицательным.")
        self.__year = int(year)

    def set_price(self, price: float):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self.__price = float(price)

    def display(self):
        print("Марка: ", self.__make, " , Год: ", self.__year, " , Цена: ", self.__price)


class Employee:
    def __init__(self, name: str, age: int, salary: float = 50000.0):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        self.__name = name
        self.__age = int(age)
        self.__salary = float(salary)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.__age = int(age)

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, salary: float):
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        self.__salary = float(salary)

    def annual_salary(self) -> float:
        return self.__salary * 12

    def display_info(self):
        print("Имя:", self.__name, ", Возраст:", self.__age, ", Зарплата (мес):", self.__salary)


class Rectangle:
    def __init__(self, length=0.0, width=0.0):
        self._length = 0.0
        self._width = 0.0
        self.set_length(length)
        self.set_width(width)

    # сеттеры
    def set_length(self, value):
        if value < 0:
            raise ValueError("Длина не может быть отрицательной")
        self._length = float(value)

    def set_width(self, value):
        if value < 0:
            raise ValueError("Ширина не может быть отрицательной")
        self._width = float(value)

    # геттеры
    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    # методы
    def perimeter(self):
        return 2 * (self._length + self._width)

    def area(self):
        return self._length * self._width

    def get_diagonal(self):
        return math.sqrt(self._length ** 2 + self._width ** 2)

    def display_info(self):
        print("Длина:", self._length)
        print("Ширина:", self._width)
        print("Площадь:", self.area())
        print("Периметр:", self.perimeter())
        print("Диагональ:", self.get_diagonal())

    def __repr__(self):
        return "Rectangle -> Длина: " + str(self._length) + ", Ширина: " + str(self._width)


class BankAccount:
    def __init__(self, initial_balance=0.0, annual_rate_percent=0.0):
        self.__balance = 0.0
        self.__annual_rate = 0.0
        self.set_balance(initial_balance)
        self.set_annual_rate(annual_rate_percent)

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.__balance = float(value)

    def set_annual_rate(self, value):
        if value < 0:
            raise ValueError("Ставка не может быть отрицательной")
        self.__annual_rate = float(value)

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной.")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств.")
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

    def apply_interest_to_balance(self):
        self.__accrue_interest()

    def __accrue_interest(self):
        interest = self.__balance * (self.__annual_rate / 100.0)
        self.__balance += interest


class Product:
    def __init__(self, name: str, price: float, stock: int):
        self._name = name
        self._price = 0.0
        self._stock = 0
        self.set_price(price)
        self.set_stock(stock)

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def set_price(self, value: float):
        if value < 0:
            raise ValueError("Цена не может быть ниже нуля.")
        self._price = float(value)

    def get_stock(self) -> int:
        return self._stock

    def set_stock(self, value: int):
        if value < 0:
            raise ValueError("Количество на складе не может быть отрицательным.")
        self._stock = int(value)

    def change_price(self, new_price: float):
        self.set_price(new_price)

    def change_stock(self, new_stock: int):
        self.set_stock(new_stock)

    def display(self):
        print("Товар: ", self._name, ", Цена: ", self._price, ", В наличии: ", self._stock)


class Book:
    def __init__(self, title: str = "", author: str = "", price: float = 0.0, pages: int = 0):
        self._title = title
        self._author = author
        self._price = float(price)
        self._pages = int(pages)

    def get_info(self) -> str:
        return "Название: " + str(self._title) + ", Автор: " + str(self._author) + ", Цена: " + str(self._price) + ", Страниц: " + str(self._pages)

    def get_price(self) -> float:
        return self._price

def create_book_default() -> Book:
    return Book()

def create_book_with_details(title: str, author: str, price: float, pages: int) -> Book:
    return Book(title, author, price, pages)

def compare_books_by_price(book1: Book, book2: Book) -> int:
    """
    Возвращает:
      1 если book1 дороже,
     -1 если book2 дороже,
      0 если равны
    """
    if not isinstance(book1, Book) or not isinstance(book2, Book):
        raise TypeError("Оба аргумента должны быть Book.")
    if book1.get_price() > book2.get_price():
        return 1
    if book1.get_price() < book2.get_price():
        return -1
    return 0


if __name__ == "__main__":
    print("=== Car ===")
    car = Car("Toyota", 2010, 700000.0)
    car.display()
    car.set_price(650000.0)
    print("Новая цена:", car.get_price())
    print()

    print("=== Employee ===")
    emp = Employee("Ольга", 30)
    emp.display_info()
    print("Годовая зарплата:", emp.annual_salary())
    emp.set_salary(60000.0)
    emp.display_info()
    print("Новая годовая зарплата:", emp.annual_salary())
    print()

    print("=== Rectangle ===")
    r1 = Rectangle(3, 4)
    r2 = Rectangle(3, 4)
    r1.display_info()
    print(r2, "Площадь:", r2.area(),"Периметр:", r2.perimeter(), "Диагональ:", r2.get_diagonal())
    # Rectangle(-1, 3)
    print()

    print("=== BankAccount ===")
    acc = BankAccount(1000.0, 5.0)
    print("Баланс до процентов:", acc.get_balance())
    acc.apply_interest_to_balance()
    print("Баланс после начисления процентов:", acc.get_balance())
    acc.deposit(500.0)
    print("Баланс после депозита 500:", acc.get_balance())
    try:
        acc.withdraw(10000.0)
    except ValueError as e:
        print("Ожидаемая ошибка при снятии:", e)
    print()

    print("=== Product ===")
    prod = Product("Карандаш", 10.0, 100)
    prod.display()
    prod.change_price(12.5)
    prod.change_stock(120)
    prod.display()
    print()

    print("=== Book ===")
    b1 = create_book_with_details("Война и мир", "Л. Толстой", 500.0, 1200)
    b2 = create_book_with_details("Маленький принц", "А. де Сент-Экзюпери", 300.0, 120)
    b3 = create_book_default()
    print(b3.get_info())
    print(b1.get_info())
    print("Сравнение по цене (1 если b1 дороже):", compare_books_by_price(b1, b2))
    print()

    print("=== Все проверки пройдены ===")
