from __future__ import annotations
from typing import TypeVar, Generic
import threading

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

