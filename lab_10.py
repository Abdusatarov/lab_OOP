"""
Паттерны ООП: Адаптер и Стратегия
==================================
6 заданий — полная реализация на Python
"""
from __future__ import annotations
import re
from abc import ABC, abstractmethod


# ═══════════════════════════════════════════════════════════════════════════
#  ЗАДАНИЕ 1 — АДАПТЕР: Конвертер данных для Legacy-системы (JSON → XML)
# ═══════════════════════════════════════════════════════════════════════════

class LegacyXMLReporter:
    """Старая библиотека — принимает только XML-строку."""
    def generate_report(self, xml_string: str) -> str:
        return f"[Legacy Report]\n{xml_string}"


class JsonToXmlAdapter:
    """
    Адаптер: принимает dict (JSON-объект), конвертирует в XML
    и передаёт в LegacyXMLReporter.
    """

    def __init__(self):
        self._reporter = LegacyXMLReporter()

    def generate_report(self, data: dict) -> str:
        xml = self._dict_to_xml(data, root="report")
        return self._reporter.generate_report(xml)

    def _dict_to_xml(self, data: dict | list | str | int | float,
                     root: str = "item") -> str:
        if isinstance(data, dict):
            inner = "".join(self._dict_to_xml(v, k) for k, v in data.items())
            return f"<{root}>{inner}</{root}>"
        if isinstance(data, list):
            inner = "".join(self._dict_to_xml(item, "item") for item in data)
            return f"<{root}>{inner}</{root}>"
        return f"<{root}>{data}</{root}>"


def demo_task1():
    print("═" * 60)
    print("ЗАДАНИЕ 1 — АДАПТЕР: JSON → XML Legacy-репортер")
    print("═" * 60)

    json_data = {
        "order_id": 42,
        "customer": "B.Alia",
        "items": ["laptop", "mouse"],
        "total": 1500.00
    }

    adapter = JsonToXmlAdapter()
    print(adapter.generate_report(json_data))
    print()


# ═══════════════════════════════════════════════════════════════════════════
#  ЗАДАНИЕ 2 — СТРАТЕГИЯ: Гибкая система скидок в магазине
# ═══════════════════════════════════════════════════════════════════════════

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float, quantity: int) -> float:
        """Возвращает итоговую цену после применения скидки."""


class NoDiscount(DiscountStrategy):
    def calculate(self, price: float, quantity: int) -> float:
        return price


class HolidayDiscount(DiscountStrategy):
    """Праздничная скидка: фиксированные −15%."""

    def calculate(self, price: float, quantity: int) -> float:
        return price * 0.85


class WholesaleDiscount(DiscountStrategy):
    """Оптовая скидка: −10%, но только при quantity > 5."""

    def calculate(self, price: float, quantity: int) -> float:
        if quantity > 5:
            return price * 0.90
        return price


class Order:
    def __init__(self, price: float, quantity: int,
                 strategy: DiscountStrategy = None):
        self.price = price
        self.quantity = quantity
        self._strategy = strategy or NoDiscount()

    def set_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def total(self) -> float:
        return self._strategy.calculate(self.price * self.quantity,
                                        self.quantity)


def demo_task2():
    print("═" * 60)
    print("ЗАДАНИЕ 2 — СТРАТЕГИЯ: Система скидок")
    print("═" * 60)

    order = Order(price=200.0, quantity=6)

    order.set_strategy(NoDiscount())
    print(f"Без скидки (6 × 200):          {order.total():.2f} ₸")

    order.set_strategy(HolidayDiscount())
    print(f"Праздничная −15%:               {order.total():.2f} ₸")

    order.set_strategy(WholesaleDiscount())
    print(f"Оптовая −10% (кол-во > 5):     {order.total():.2f} ₸")

    order2 = Order(price=200.0, quantity=3, strategy=WholesaleDiscount())
    print(f"Оптовая −10% (кол-во ≤ 5):    {order2.total():.2f} ₸  ← скидка не применяется")
    print()


# ═══════════════════════════════════════════════════════════════════════════
#  ЗАДАНИЕ 3 — АДАПТЕР: Универсальный медиаплеер
# ═══════════════════════════════════════════════════════════════════════════

class MediaPlayer(ABC):
    """Целевой интерфейс — умеет воспроизводить только .mp3."""

    @abstractmethod
    def play(self, filename: str) -> str:
        pass


class Mp3Player(MediaPlayer):
    def play(self, filename: str) -> str:
        return f"[MP3Player] Воспроизведение: {filename}"


# --- Сторонние плагины (adaptees) ----------------------------------------

class VlcPlugin:
    def play_vlc(self, filename: str) -> str:
        return f"[VLC Plugin] Открываю файл: {filename}"


class Mp4Plugin:
    def render_mp4(self, filename: str) -> str:
        return f"[MP4 Plugin] Декодирую видео: {filename}"


# --- Адаптеры -------------------------------------------------------------

class VlcAdapter(MediaPlayer):
    def __init__(self):
        self._vlc = VlcPlugin()

    def play(self, filename: str) -> str:
        if not filename.endswith(".vlc"):
            raise ValueError("Vlc_Adapter поддерживает только .vlc")
        return self._vlc.play_vlc(filename)


class Mp4Adapter(MediaPlayer):
    def __init__(self):
        self._mp4 = Mp4Plugin()

    def play(self, filename: str) -> str:
        if not filename.endswith(".mp4"):
            raise ValueError("Mp4Adapter поддерживает только .mp4")
        return self._mp4.render_mp4(filename)


class UniversalPlayer:
    """Основной плеер — выбирает нужный адаптер автоматически."""

    _adapters: dict[str, MediaPlayer] = {}

    def register(self, extension: str, player: MediaPlayer):
        self._adapters[extension.lower()] = player

    def play(self, filename: str) -> str:
        ext = filename.rsplit(".", 1)[-1].lower()
        player = self._adapters.get(ext)
        if player is None:
            return f"Формат .{ext} не поддерживается"
        return player.play(filename)


def demo_task3():
    print("═" * 60)
    print("ЗАДАНИЕ 3 — АДАПТЕР: Универсальный медиаплеер")
    print("═" * 60)

    player = UniversalPlayer()
    player.register("mp3", Mp3Player())
    player.register("vlc", VlcAdapter())
    player.register("mp4", Mp4Adapter())

    for f in ["song.mp3", "movie.vlc", "clip.mp4", "doc.avi"]:
        print(player.play(f))
    print()


# ═══════════════════════════════════════════════════════════════════════════
#  ЗАДАНИЕ 4 — СТРАТЕГИЯ: Мульти-шлюз платежей
# ═══════════════════════════════════════════════════════════════════════════

class PaymentStrategy(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> bool:
        pass

    @abstractmethod
    def confirm(self, amount: float) -> str:
        pass


class BankCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self._card = f"****{card_number[-4:]}"

    def authorize(self, amount: float) -> bool:
        print(f"  [BankCard] Авторизация карты {self._card} на {amount:.2f}₸...")
        return True  # упрощение

    def confirm(self, amount: float) -> str:
        return f"  [BankCard] Транзакция {amount:.2f}₸ подтверждена по карте {self._card}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self._email = email

    def authorize(self, amount: float) -> bool:
        print(f"  [PayPal] Вход в аккаунт {self._email}...")
        return True

    def confirm(self, amount: float) -> str:
        return f"  [PayPal] Платёж {amount:.2f}₸ выполнен через {self._email}"


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet: str):
        self._wallet = wallet

    def authorize(self, amount: float) -> bool:
        print(f"  [Crypto] Подписание транзакции из кошелька {self._wallet[:8]}...")
        return True

    def confirm(self, amount: float) -> str:
        return f"  [Crypto] Смарт-контракт выполнен: {amount:.2f}₸ → {self._wallet[:8]}…"


class Checkout:
    """Контекст — делегирует платёж выбранной стратегии."""

    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_payment_method(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def pay(self, amount: float):
        if self._strategy.authorize(amount):
            print(self._strategy.confirm(amount))
        else:
            print("  Платёж отклонён.")


def demo_task4():
    print("═" * 60)
    print("ЗАДАНИЕ 4 — СТРАТЕГИЯ: Мульти-шлюз платежей")
    print("═" * 60)

    checkout = Checkout(BankCardPayment("1234567890123456"))
    print("Оплата картой:")
    checkout.pay(3500.00)

    checkout.set_payment_method(PayPalPayment("user@example.com"))
    print("Оплата через PayPal:")
    checkout.pay(3500.00)

    checkout.set_payment_method(CryptoPayment("0xABCDEF1234567890ABCDEF"))
    print("Оплата криптовалютой:")
    checkout.pay(3500.00)
    print()


# ═══════════════════════════════════════════════════════════════════════════
#  ЗАДАНИЕ 5 — АДАПТЕР: Контроллер «Умного дома»
# ═══════════════════════════════════════════════════════════════════════════

class TemperatureSensor(ABC):
    """Единый интерфейс датчика температуры."""

    @abstractmethod
    def get_celsius(self) -> float:
        pass


# --- Три несовместимых датчика (adaptees) ---------------------------------

class SensorA:
    """Датчик A: возвращает int в Цельсиях."""

    def read_temp(self) -> int:
        return 22


class SensorB:
    """Датчик B: возвращает строку вида '25C'."""

    def fetch_data(self) -> str:
        return "25C"


class SensorC:
    """Датчик C: возвращает float в Фаренгейтах."""

    def get_fahrenheit(self) -> float:
        return 77.0  # = 25°C


# --- Адаптеры -------------------------------------------------------------

class SensorAAdapter(TemperatureSensor):
    def __init__(self, sensor: SensorA):
        self._sensor = sensor

    def get_celsius(self) -> float:
        return float(self._sensor.read_temp())


class SensorBAdapter(TemperatureSensor):
    def __init__(self, sensor: SensorB):
        self._sensor = sensor

    def get_celsius(self) -> float:
        raw = self._sensor.fetch_data()          # "25C"
        return float(raw.rstrip("C"))


class SensorCAdapter(TemperatureSensor):
    def __init__(self, sensor: SensorC):
        self._sensor = sensor

    def get_celsius(self) -> float:
        fahrenheit = self._sensor.get_fahrenheit()
        return (fahrenheit - 32) * 5 / 9


class SmartHomeController:
    def __init__(self, sensors: list[TemperatureSensor]):
        self._sensors = sensors

    def average_temperature(self) -> float:
        readings = [s.get_celsius() for s in self._sensors]
        return sum(readings) / len(readings)

    def report(self) -> str:
        readings = [s.get_celsius() for s in self._sensors]
        lines = [f"  Датчик {i + 1}: {t:.1f}°C" for i, t in enumerate(readings)]
        lines.append(f"  Средняя: {sum(readings) / len(readings):.1f}°C")
        return "\n".join(lines)


def demo_task5():
    print("═" * 60)
    print("ЗАДАНИЕ 5 — АДАПТЕР: Контроллер умного дома")
    print("═" * 60)

    sensors: list[TemperatureSensor] = [
        SensorAAdapter(SensorA()),   # int → float
        SensorBAdapter(SensorB()),   # "25C" → float
        SensorCAdapter(SensorC()),   # °F → °C
    ]

    controller = SmartHomeController(sensors)
    print(controller.report())
    print()


# ═══════════════════════════════════════════════════════════════════════════
#  ЗАДАНИЕ 6 — СТРАТЕГИЯ: Динамическая валидация по регионам
# ═══════════════════════════════════════════════════════════════════════════

class ValidationStrategy(ABC):
    @abstractmethod
    def validate_phone(self, phone: str) -> bool:
        pass

    @abstractmethod
    def validate_postal(self, code: str) -> bool:
        pass

    @property
    @abstractmethod
    def country(self) -> str:
        pass


class KazakhstanValidation(ValidationStrategy):
    """Казахстан: телефон +7(XXX)XXX-XX-XX, индекс 6 цифр."""

    @property
    def country(self) -> str:
        return "Казахстан"

    def validate_phone(self, phone: str) -> bool:
        return bool(re.fullmatch(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", phone))

    def validate_postal(self, code: str) -> bool:
        return bool(re.fullmatch(r"\d{6}", code))


class USAValidation(ValidationStrategy):
    """США: телефон +1-XXX-XXX-XXXX, ZIP-код 5 цифр (или 5+4)."""

    @property
    def country(self) -> str:
        return "США"

    def validate_phone(self, phone: str) -> bool:
        return bool(re.fullmatch(r"\+1-\d{3}-\d{3}-\d{4}", phone))

    def validate_postal(self, code: str) -> bool:
        return bool(re.fullmatch(r"\d{5}(-\d{4})?", code))


class GermanyValidation(ValidationStrategy):
    """Германия: телефон +49 XXX XXXXXXX, индекс 5 цифр."""

    @property
    def country(self) -> str:
        return "Германия"

    def validate_phone(self, phone: str) -> bool:
        return bool(re.fullmatch(r"\+49 \d{3,5} \d{5,8}", phone))

    def validate_postal(self, code: str) -> bool:
        return bool(re.fullmatch(r"\d{5}", code))


class Validator:
    """Контекст — мгновенно переключает стратегию валидации."""

    def __init__(self, strategy: ValidationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ValidationStrategy):
        self._strategy = strategy
        print(f"  → Стратегия переключена на: {strategy.country}")

    def validate(self, phone: str, postal: str) -> dict:
        return {
            "country":  self._strategy.country,
            "phone":    self._strategy.validate_phone(phone),
            "postal":   self._strategy.validate_postal(postal),
        }


def demo_task6():
    print("═" * 60)
    print("ЗАДАНИЕ 6 — СТРАТЕГИЯ: Динамическая валидация по регионам")
    print("═" * 60)

    validator = Validator(KazakhstanValidation())

    test_cases = [
        (KazakhstanValidation(), "+7(701)234-56-78", "050010"),
        (USAValidation(),        "+1-800-555-1234",  "90210"),
        (GermanyValidation(),    "+49 030 12345678", "10115"),
        # Намеренно неверные данные
        (KazakhstanValidation(), "+1-800-555-1234",  "ABC"),
    ]

    for strategy, phone, postal in test_cases:
        validator.set_strategy(strategy)
        result = validator.validate(phone, postal)
        phone_ok = "✓" if result["phone"] else "✗"
        postal_ok = "✓" if result["postal"] else "✗"
        print(f"  Телефон {phone_ok}: {phone:<25}  Индекс {postal_ok}: {postal}")

    print()


# ═══════════════════════════════════════════════════════════════════════════
#  ТОЧКА ВХОДА
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    demo_task1()
    demo_task2()
    demo_task3()
    demo_task4()
    demo_task5()
    demo_task6()
