from typing import TypeVar, Generic

T = TypeVar("T")


# __Задание-1____________________________________________________

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = 0

    def division(self):
        # try:
        #     self.sum = self.a / self.b
        #     return self.sum
        # except ZeroDivisionError:
        #     return "«Ошибка: деление на ноль!»"
        if self.a == 0 or self.b == 0:
            return "«Ошибка: деление на ноль!»"
        else:
            self.sum = self.a / self.b
            return self.sum


# __Задание-2____________________________________________________

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value


# __Задание-3____________________________________________________

class List:
    Number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, index):
        self.index = index

    def get(self):
        try:
            return self.Number_list[int(self.index)]
        except ValueError:
            print("Ввёл не число")
        except IndexError:
            print("Индекс вышел за границы")


# __Задание-4____________________________________________________

class Utils:

    @staticmethod
    def getFirstElement(items: list[T]):
        if items is None or len(items) == 0:
            raise ValueError("Список пустой или None")
        return items[0]


# __Задание-5____________________________________________________

def infinite():
    return infinite()


# __Задание-6____________________________________________________

class DataRepository(Generic[T]):

    def __init__(self):
        self.data = []

    def findElement(self, index: int):
        try:
            return self.data[index]
        except IndexError:
            raise IndexError("Индекс вне диапазона")

    def addSafely(self, item):
        try:
            if item is None:
                raise ValueError
            self.data.append(item)
        except ValueError:
            print("Нельзя добавить None")


# _______________________________________________________________

if __name__ == "__main__":
    # __Задание-1__
    A = int(input())
    B = int(input())
    Sum = Division(A, B)
    print(Sum.division())

    # __Задание-2__
    B1 = Box("Hello")
    B2 = Box(15)
    print(B1.get())
    print(B2.get())

    # __Задание-3__
    obj = List("2")
    print(obj.get())  # 3
    obj1 = List("abc")
    print(obj1.get())  # Ввёл не число
    obj2 = List("100")
    print(obj2.get())  # Индекс вышел за границы

    # __Задание-4__
    ob_1 = Utils()
    ob_2 = Utils()
    print(ob_1.getFirstElement([1, 2, 3]))
    # print(ob_2.getFirstElement([]))

    # __Задание-5__
    try:
        infinite()
    except RecursionError:
        print("Поймана ошибка: бесконечная рекурсия")

    # __Задание-6__
    repo = DataRepository[int]()  # репозиторий для int

    repo.addSafely(10)
    repo.addSafely(20)

    print(repo.findElement(1))  # 20
    # print(repo.findElement(5))
