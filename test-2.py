from typing import TypeVar, Generic


T = TypeVar("T")

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

repo = DataRepository[int]()   # репозиторий для int

repo.addSafely(10)
repo.addSafely(20)

print(repo.findElement(1))   # 20
# print(repo.findElement(5))