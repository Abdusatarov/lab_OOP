from __future__ import annotations


class Person:
    TotalCount = None
    _static_initialized = False

    def __init__(self, name: str, age: int):
        if not Person._static_initialized:
            Person.TotalCount = 0
            Person._static_initialized = True
            print("Person: статическая инициализация выполнена (TotalCount = 0).")

        self.Name = name
        self.Age = int(age)
        Person.TotalCount += 1


class MathUtils:
    @staticmethod
    def factorial(N: int) -> int:
        if N < 0:
            raise ValueError("Факториал определён только для неотрицательных чисел.")
        result = 1
        for i in range(2, N + 1):
            result *= i
        return result


class Counter:
    __count = 0

    def __init__(self):
        Counter.__count += 1

    @classmethod
    def get_count(cls) -> int:
        return cls.__count

class NumberUtils:
    @staticmethod
    def max(a: int, b: int, d: int) -> int:
        return max(a, b, d)


class DatabaseConnection:
    _initialized = False

    @classmethod
    def _static_init(cls):
        if not cls._initialized:
            print("Подключение к базе данных установлено (статическая инициализация).")
            cls._initialized = True

    @classmethod
    def connect(cls):
        cls._static_init()
        print("DatabaseConnection.connect() вызван — соединение активно.")


class StringUtils:
    @staticmethod
    def countchars(s: str) -> int:
        if s is None:
            return 0
        return len(s)


class AppSettings:
    ConfigVersion = "1.0.0"

    @staticmethod
    def oversimplification():
        print("ConfigVersion:", AppSettings.ConfigVersion)


class GameSettings:
    MaxPlayers = None
    _initialized = False

    @classmethod
    def _static_init(cls):
        if not cls._initialized:
            cls.MaxPlayers = 4
            cls._initialized = True
            print("GameSettings: статическая инициализация выполнена (MaxPlayers = 4).")

    @classmethod
    def printmaxplayers(cls):
        cls._static_init()
        print("MaxPlayers =", cls.MaxPlayers)


class TemperatureConverter:
    @staticmethod
    def celsiustofahrenheit(d: float) -> float:
        return (d * 9.0 / 5.0) + 32.0

    @staticmethod
    def fahrenheittocelsius(d: float) -> float:
        return (d - 32.0) * 5.0 / 9.0


# ----------------- Демонстрация работы -----------------
if __name__ == "__main__":
    print("1) Person и статическая инициализация:")
    p1 = Person("Алекс", 25)
    print("TotalCount после p1:", Person.TotalCount)
    p2 = Person("Мария", 30)
    print("TotalCount после p2:", Person.TotalCount)
    print()

    print("2) MathUtils.Factorial:")
    for n in (0, 1, 5, 8):
        print(f"{n}! = {MathUtils.factorial(n)}")
    print()

    print("3) Counter с приватным статическим полем:")
    c1 = Counter()
    cc2 = Counter()
    print("Количество созданных Counter объектов:", Counter.get_count())
    print()

    print("4) NumberUtils.Max:")
    print("max(3, 7, 5) =", NumberUtils.max(3, 7, 5))
    print()

    print("5) DatabaseConnection (статическая инициализация при первом обращении):")
    DatabaseConnection.connect()
    DatabaseConnection.connect()
    print()

    print("6) StringUtils.CountChars:")
    print("len('Hello') =", StringUtils.countchars("Hello"))
    print()

    print("7) AppSettings.DisplayConfigVersion:")
    AppSettings.oversimplification()
    print()

    print("8) GameSettings (статическая инициализация MaxPlayers = 4):")
    GameSettings.printmaxplayers()
    GameSettings.printmaxplayers()
    print()

    print("9) TemperatureConverter:")
    c = 25.0
    f = TemperatureConverter.celsiustofahrenheit(c)
    print(f"{c}C = {f}F")
    f2 = 77.0
    c2 = TemperatureConverter.fahrenheittocelsius(f2)
    print(f"{f2}F = {cc2:.2f}C")
    print()

    print("=== Демонстрация завершена ===")