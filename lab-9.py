from __future__ import annotations
from typing import TypeVar
import threading

T = TypeVar("T")


# __Задание-1____________________________________________________
# Singleton — Государственный реестр

class Government:
    _instance: Government = None

    def __init__(self, president_name: str):
        self.president_name = president_name

    @classmethod
    def get_instance(cls, president_name: str) -> Government:
        if cls._instance is None:
            cls._instance = cls(president_name)
        return cls._instance


# __Задание-2____________________________________________________
# Observer — Логика рассылки новостей

class Observer:
    def update(self, news: str):
        pass


class NewsAgency:
    def __init__(self):
        self._subscribers: list[Observer] = []

    def subscribe(self, observer: Observer):
        self._subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        self._subscribers.remove(observer)

    def publish_headline(self, headline: str):
        for subscriber in self._subscribers:
            subscriber.update(headline)


class Subscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, news: str):
        print(f"{self.name} получил: Срочная новость! -> {news}")


# __Задание-3____________________________________________________
# Factory Method — Транспортный цех

class Transport:
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print("Доставка грузовиком по суше")


class Ship(Transport):
    def deliver(self):
        print("Доставка кораблём по морю")


class LogisticsFactory:
    def create_transport(self) -> Transport:
        raise NotImplementedError

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()


class TruckFactory(LogisticsFactory):
    def create_transport(self) -> Transport:
        return Truck()


class ShipFactory(LogisticsFactory):
    def create_transport(self) -> Transport:
        return Ship()


# __Задание-4____________________________________________________
# Singleton — Глобальные настройки приложения

class AppSettings:
    instance: AppSettings = None

    def __init__(self):
        self.theme = "Light"
        self.language = "Русский"

    @classmethod
    def get_instance(cls) -> AppSettings:
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def set_theme(self, theme: str):
        self.theme = theme

    def set_language(self, language: str):
        self.language = language

    def print_settings(self):
        print(f"Тема: {self.theme} | Язык: {self.language}")


# __Задание-5____________________________________________________
# Observer — Умный дом

class TempObserver:
    def on_temperature_changed(self, temperature: int):
        pass


class TemperatureSensor:
    def __init__(self):
        self._observers: list[TempObserver] = []
        self._temperature = 0

    def add_observer(self, observer: TempObserver):
        self._observers.append(observer)

    def set_temperature(self, temp: int):
        self._temperature = temp
        print(f"\n Температура изменилась: {temp}°C")
        for observer in self._observers:
            observer.on_temperature_changed(temp)


class AirConditioner(TempObserver):
    def on_temperature_changed(self, temperature: int):
        if temperature > 25:
            print("  Кондиционер: ВКЛЮЧЁН (жарко!)")
        else:
            print("  Кондиционер: выключен")


class Heater(TempObserver):
    def on_temperature_changed(self, temperature: int):
        if temperature < 15:
            print("  Обогреватель: ВКЛЮЧЁН (холодно!)")
        else:
            print("  Обогреватель: выключен")


# __Задание-6____________________________________________________
# Factory Method — Кроссплатформенный UI

class Button:
    def render(self):
        pass

    def on_click(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("Отрисовка Windows-кнопки")

    def on_click(self):
        print("Windows-кнопка нажата!")


class HTMLButton(Button):
    def render(self):
        print("Отрисовка HTML-кнопки")

    def on_click(self):
        print("HTML-кнопка нажата!")


class Dialog:
    def create_button(self) -> Button:
        raise NotImplementedError

    def render_dialog(self):
        button = self.create_button()
        button.render()
        button.on_click()


class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()


# __Задание-7____________________________________________________
# Singleton — Безопасный в многопоточности
#
# class Singleton:
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:          ← оба потока проходят сюда одновременно
#             cls._instance = super().__new__(cls)
#     return cls._instance
#


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:              # Проверка 1: быстрая, без блокировки
            with cls._lock:                    # Блокировка — только при первом создании
                if cls._instance is None:      # Проверка 2: внутри блока — безопасно
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = []


# _______________________________________________________________

if __name__ == "__main__":

    # __Задание-1__
    print("=== Задание 1: Государственный реестр ===")
    g1 = Government.get_instance("Иванов")
    g2 = Government.get_instance("Петров")     # попытка "создать второе правительство"
    print(g1.president_name)                   # Иванов
    print(g2.president_name)                   # Иванов — имя не изменилось
    print(g1 is g2)                            # True — один и тот же объект

    # __Задание-2__
    print("\n=== Задание 2: Рассылка новостей ===")
    agency = NewsAgency()
    alice = Subscriber("Алиса")
    bob = Subscriber("Боб")
    agency.subscribe(alice)
    agency.subscribe(bob)
    agency.publish_headline("Землетрясение магнитудой 6.5!")

    # __Задание-3__
    print("\n=== Задание 3: Транспортный цех ===")
    for factory in [TruckFactory(), ShipFactory()]:
        factory.plan_delivery()

    # __Задание-4__
    print("\n=== Задание 4: Глобальные настройки ===")
    s1 = AppSettings.get_instance()
    s1.print_settings()                        # Тема: Light | Язык: Русский

    s2 = AppSettings.get_instance()
    s2.set_theme("Dark")
    s2.set_language("English")

    s1.print_settings()                        # Тема: Dark | Язык: English (изменилось!)
    print(s1 is s2)                            # True


    # __Задание-5__
    print("\n=== Задание 5: Умный дом ===")
    sensor = TemperatureSensor()
    sensor.add_observer(AirConditioner())
    sensor.add_observer(Heater())
    sensor.set_temperature(30)                 # жарко  → кондиционер вкл
    sensor.set_temperature(20)                 # норма  → оба выкл
    sensor.set_temperature(10)                 # холодно → обогреватель вкл

    # __Задание-6__
    print("\n=== Задание 6: Кроссплатформенный UI ===")
    platform = "web"                           # попробуйте "windows"
    dialog = WindowsDialog() if platform == "windows" else WebDialog()
    dialog.render_dialog()

    # __Задание-7__
    print("\n=== Задание 7: Потокобезопасный Singleton ===")
    results = []

    def get_instance():
        results.append(Singleton())

    threads = [threading.Thread(target=get_instance) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    ids = [id(obj) for obj in results]
    print(f"Все id одинаковы: {len(set(ids)) == 1}")  # True
