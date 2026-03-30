# 1. Animal, Dog, Cat
class Animal:
    def speak(self):
        print("...")  # базовый звук


class Dog(Animal):
    def speak(self):
        print("Гав")


class Cat(Animal):
    def speak(self):
        print("Мяу")


# 2. Shape, Circle, Square (с полем color в родителе)
class Shape:
    def __init__(self, color: str = "без цвета"):
        self.color = color

    def draw(self):
        print("Рисую фигуру")  # базовый вариант


class Circle(Shape):
    def draw(self):
        print("Рисую ", self.color.upper(), " круг")


class Square(Shape):
    def draw(self):
        print("Рисую ", self.color.upper(), " квадрат")


# 3. Figure, Rectangle, Triangle (area)
class Figure:
    def area(self) -> float:
        return 0.0


class RectangleFigure(Figure):
    def __init__(self, d: float, b: float):
        self.a = float(d)
        self.b = float(b)

    def area(self) -> float:
        return self.a * self.b


class TriangleFigure(Figure):
    def __init__(self, base: float, height: float):
        self.base = float(base)
        self.height = float(height)

    def area(self) -> float:
        return 0.5 * self.base * self.height


# 4. Human, Russian, English, German, MuteHuman
class Human:
    def sayHello(self):
        print("Hello!")


class Russian(Human):
    def sayHello(self):
        print("Привет!")


class English(Human):
    def sayHello(self):
        print("Hello!")


class German(Human):
    def sayHello(self):
        print("Guten Tag!")


class MuteHuman(Human):
    pass


# 5. Transport, Plane, Ship
class Transport:
    def __init__(self, speed_kmh: float):
        self.speed_kmh = float(speed_kmh)

    def showSpeed(self):
        print("Скорость:", self.speed_kmh, "км/ч")


class Plane(Transport):
    def showSpeed(self):
        print("Скорость:", self.speed_kmh, "км/ч")


class Ship(Transport):
    def showSpeed(self):
        knots = self.speed_kmh / 1.852
        print("Скорость:", round(knots, 2), "узлов")


# 6. Account, TaxFreeAccount, PenaltyAccount
class Account:
    def __init__(self, balance: float = 0.0):
        self._balance = float(balance)

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств.")
        self._balance -= amount
        print("Снято", amount, ". Остаток:", self._balance)

    def get_balance(self):
        return self._balance


class TaxFreeAccount(Account):
    pass


class PenaltyAccount(Account):
    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")

        commission = amount * 0.05
        total = amount + commission

        if total > self._balance:
            raise ValueError("Недостаточно средств с учётом комиссии.")

        self._balance -= total
        print("Снято", amount, "+ комиссия", round(commission, 2), ". Остаток:", self._balance)


# 7. Bird
class Bird:
    def fly(self):
        print("Птица летит")


class Eagle(Bird):
    def fly(self):
        print("Лечу высоко")


class Penguin(Bird):
    def fly(self):
        print("Я не умею летать, я иду")


def make_bird_fly(b: Bird):
    b.fly()


# 8. Printer
class Printer:
    def printText(self, text: str):
        print(text)


class UpperPrinter(Printer):
    def printText(self, text: str):
        print(text.upper())


class BracketPrinter(Printer):
    def printText(self, text: str):
        print("[", text, "]")


# 9. Enemy
class Enemy:
    def __init__(self, hp: float):
        self.hp = float(hp)

    def takeDamage(self, amount: float):
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self.hp -= amount
        print("Получил", amount, "урона. HP теперь", self.hp)


class Slime(Enemy):
    pass


class ArmoredEnemy(Enemy):
    def takeDamage(self, amount: float):
        effective = amount / 2.0

        if effective < 0:
            raise ValueError("Урон не может быть отрицательным.")

        self.hp -= effective
        print("Бронированный: получил", effective, "(из", amount, "). HP теперь", self.hp)


def attack(target: Enemy):
    target.takeDamage(10.0)


# 10. Worker
class Worker:
    def work(self):
        print("Я выполняю базовую работу")


class Manager(Worker):
    def work(self):
        super().work()
        print("... и раздаю указания")


# ----------------- Демонстрация -----------------
if __name__ == "__main__":
    print("1) Animal polymorphism:")
    animals = [Dog(), Cat()]
    for a in animals:
        a.speak()
    print()

    print("2) Shape + color inheritance:")
    shapes = [Circle("красный"), Square("синий")]
    for s in shapes:
        s.draw()
    print()

    print("3) Figure areas sum:")
    figures = [RectangleFigure(3, 4), TriangleFigure(10, 5), RectangleFigure(2, 2)]
    total_area = 0.0
    for f in figures:
        ar = f.area()
        print("Площадь фигуры:", ar)
        total_area += ar
    print("Суммарная площадь:", total_area)
    print()

    print("4) Human greetings:")
    ppl = [Russian(), English(), German(), MuteHuman()]
    for p in ppl:
        p.sayHello()
    print()

    print("5) Transport speed units:")
    transports = [Plane(900), Ship(37)]
    for t in transports:
        t.showSpeed()
    print()

    print("6) Account withdraw:")
    accounts = [TaxFreeAccount(1000.0), PenaltyAccount(1000.0)]
    for acc in accounts:
        try:
            acc.withdraw(100.0)
        except ValueError as e:
            print("Ошибка:", e)
    print()

    print("7) Bird fly:")
    make_bird_fly(Eagle())
    make_bird_fly(Penguin())
    print()

    print("8) Printers:")
    printers = [Printer(), UpperPrinter(), BracketPrinter()]
    for pr in printers:
        pr.printText("Hello, world")
    print()

    print("9) Enemies:")
    enemies = [Slime(50), ArmoredEnemy(50)]
    for e in enemies:
        attack(e)
    print()

    print("10) Worker and Manager:")
    w = Worker()
    m = Manager()
    w.work()
    m.work()