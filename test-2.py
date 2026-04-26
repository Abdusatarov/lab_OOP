from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")

class Singleton:


    _instance = None
    def __new__(cls, self):
        self.theme = "Light"
        self.language = "Русский"
        if cls._instance is None:
            cls._instance = cls
        return cls._instance


    def set_theme(self, theme: str):
        self.theme = theme

    def set_language(self, language: str):
        self.language = language

    def print_settings(self):
        print(f"Тема: {self.theme} | Язык: {self.language}")

if __name__ == "__main__":
    singleton = Singleton()
    singleton.print_settings()

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
