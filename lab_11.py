"""
OOP Patterns: Singleton, Observer, Factory Method
All tasks in one file
"""

from abc import ABC, abstractmethod


# ════════════════════════════════════════════════
# 1. Government — Singleton
# ════════════════════════════════════════════════
class Government:
    _instance = None

    def __new__(cls, president_name=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, president_name=None):
        if not self._initialized and president_name is not None:
            self.president_name = president_name
            self._initialized = True

    @staticmethod
    def get_instance(president_name=None):
        return Government(president_name)


# ════════════════════════════════════════════════
# 2. NewsAgency — Observer
# ════════════════════════════════════════════════
class Subscriber:

    t = 0

    @classmethod
    def update(cls, news):
        print("Subscriber = " + str(cls.t) , news)
        cls.t += 1


class NewsAgency:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def publish_news(self, headline):
        news = f"Срочная новость! {headline}"
        for subscriber in self._subscribers:
            subscriber.update(news)


# ════════════════════════════════════════════════
# 3. Transport — Factory Method
# ════════════════════════════════════════════════
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "Delivery by truck"


class Ship(Transport):
    def deliver(self):
        return "Delivery by ship"


class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass


class TruckFactory(TransportFactory):
    def create_transport(self):
        return Truck()


class ShipFactory(TransportFactory):
    def create_transport(self):
        return Ship()


def transport_client(factory: TransportFactory):
    transport = factory.create_transport()
    print("[Transport]", transport.deliver())


# ════════════════════════════════════════════════
# 4. AppSettings — Singleton
# ════════════════════════════════════════════════
class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "Light"
            cls._instance.language = "EN"
        return cls._instance

    @staticmethod
    def get_instance():
        return AppSettings()

    def update_settings(self, theme=None, language=None):
        if theme:
            self.theme = theme
        if language:
            self.language = language


# ════════════════════════════════════════════════
# 5. Smart Home — Observer
# ════════════════════════════════════════════════
class TemperatureSensor:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def subscribe(self, observer):
        self._observers.append(observer)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self._notify()

    def _notify(self):
        for observer in self._observers:
            observer.update(self._temperature)


class AirConditioner:
    def update(self, temperature):
        state = "ON" if temperature > 25 else "OFF"
        print(f"[AC] {state}")


class Heater:
    def update(self, temperature):
        state = "ON" if temperature < 15 else "OFF"
        print(f"[Heater] {state}")


# ════════════════════════════════════════════════
# 6. UI — Factory Method
# ════════════════════════════════════════════════
class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        return "Windows Button"


class HTMLButton(Button):
    def render(self):
        return "HTML Button"


class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        pass

    def render_window(self):
        button = self.create_button()
        print("[UI]", button.render())


class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()


# ════════════════════════════════════════════════
# TEST ALL
# ════════════════════════════════════════════════
if __name__ == "__main__":

    print("\n--- 1. Government ---")
    g1 = Government.get_instance("Tokayev")
    g2 = Government.get_instance("Other")
    print(g1.president_name)
    print(g2.president_name)
    print("Same instance:", g1 is g2)

    print("\n--- 2. NewsAgency ---")
    agency = NewsAgency()
    for i in range(10):
        s1 = Subscriber()
        agency.subscribe(s1)
    agency.publish_news("New headline released")

    print("\n--- 3. Transport ---")
    transport_client(TruckFactory())
    transport_client(ShipFactory())

    print("\n--- 4. AppSettings ---")
    s1 = AppSettings.get_instance()
    s2 = AppSettings.get_instance()
    s1.update_settings(theme="Dark", language="RU")
    print(s2.theme, s2.language)

    print("\n--- 5. Smart Home ---")
    sensor = TemperatureSensor()
    sensor.subscribe(AirConditioner())
    sensor.subscribe(Heater())
    sensor.set_temperature(10)
    sensor.set_temperature(30)

    print("\n--- 6. UI ---")
    dialog = WindowsDialog()
    dialog.render_window()
    dialog = WebDialog()
    dialog.render_window()