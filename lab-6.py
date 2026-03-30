from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi
from pathlib import Path


# 1. Base contract "Playable"
class Playable(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class MusicPlayer(Playable):
    def play(self) -> None:
        print("MusicPlayer: play music")

    def stop(self) -> None:
        print("MusicPlayer: stop music")


class VideoPlayer(Playable):
    def play(self) -> None:
        print("VideoPlayer: play video")

    def stop(self) -> None:
        print("VideoPlayer: stop video")


def run_playable(device: Playable) -> None:
    device.play()
    device.stop()


# 2. Charging devices
class Chargeable(ABC):
    @abstractmethod
    def charge(self) -> None:
        pass


class Smartphone(Chargeable):
    def charge(self) -> None:
        print("Smartphone is charging")


class Laptop(Chargeable):
    def charge(self) -> None:
        print("Laptop is charging")


class ElectricCar(Chargeable):
    def charge(self) -> None:
        print("Electric car is charging")


class Chair:
    pass


def charge_supported_devices(devices: list[object]) -> None:
    for device in devices:
        if isinstance(device, Chargeable):
            device.charge()


# 3. Different shapes, one perimeter
class HasPerimeter(ABC):
    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Circle(HasPerimeter):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(HasPerimeter):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Hexagon(HasPerimeter):
    def __init__(self, side: float) -> None:
        self.side = side

    def get_perimeter(self) -> float:
        return 6 * self.side


def find_max_perimeter(shape: list[HasPerimeter]) -> HasPerimeter:
    if not shape:
        raise ValueError("shapes list must not be empty")
    return max(shape, key=lambda shape_1: shape_1.get_perimeter())


# 4. Multiple interfaces
class Swimmable(ABC):
    @abstractmethod
    def swim(self) -> None:
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass


class Duck(Swimmable, Flyable):
    def swim(self) -> None:
        print("Duck is swimming")

    def fly(self) -> None:
        print("Duck is flying")


class Fish(Swimmable):
    def swim(self) -> None:
        print("Fish is swimming")


# 5. Notification system (Messenger)
class Sender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        pass


class EmailSender(Sender):
    def send(self, message: str, recipient: str) -> None:
        print(f"Email to {recipient}: {message}")


class TelegramBot(Sender):
    def send(self, message: str, recipient: str) -> None:
        print(f"Telegram message to {recipient}: {message}")


class SmsService(Sender):
    def send(self, message: str, recipient: str) -> None:
        print(f"SMS to {recipient}: {message}")


def notify(sender: Sender, message: str, recipient: str) -> None:
    sender.send(message, recipient)


# 6. Sorting (object comparison)
@dataclass
class Product:
    name: str
    price: float

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price


# 7. Data storage
class Repository(ABC):
    @abstractmethod
    def save(self, data: str) -> int:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        pass


class MemoryRepository(Repository):
    def __init__(self) -> None:
        self._storage: dict[int, str] = {}
        self._next_id = 1

    def save(self, data: str) -> int:
        item_id = self._next_id
        self._storage[item_id] = data
        self._next_id += 1
        return item_id

    def delete(self, item_id: int) -> bool:
        return self._storage.pop(item_id, None) is not None


class FileRepository(Repository):
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)
        self.file_path.touch(exist_ok=True)
        self._next_id = self._calculate_next_id()

    def _calculate_next_id(self) -> int:
        max_id = 0
        for line in self.file_path.read_text(encoding="utf-8").splitlines():
            if "|" not in line:
                continue
            raw_id, _ = line.split("|", 1)
            if raw_id.isdigit():
                max_id = max(max_id, int(raw_id))
        return max_id + 1

    def save(self, data: str) -> int:
        item_id = self._next_id
        with self.file_path.open("a", encoding="utf-8") as file:
            file.write(f"{item_id}|{data}\n")
        self._next_id += 1
        return item_id

    def delete(self, item_id: int) -> bool:
        lines = self.file_path.read_text(encoding="utf-8").splitlines()
        kept: list[str] = []
        removed = False
        for line in lines:
            if line.startswith(f"{item_id}|"):
                removed = True
                continue
            kept.append(line)

        self.file_path.write_text(
            "\n".join(kept) + ("\n" if kept else ""),
            encoding="utf-8",
        )
        return removed


def demo_repository(repository: Repository) -> None:
    first_id = repository.save("first value")
    second_id = repository.save("second value")
    print(f"Saved IDs: {first_id}, {second_id}")
    print(f"Delete first ID -> {repository.delete(first_id)}")


if __name__ == "__main__":
    print("1) Playable")
    run_playable(MusicPlayer())
    run_playable(VideoPlayer())

    print("\n2) Chargeable")
    mixed_devices: list[object] = [Smartphone(), Chair(), Laptop(), ElectricCar()]
    charge_supported_devices(mixed_devices)

    print("\n3) HasPerimeter")
    shapes: list[HasPerimeter] = [Circle(5), Rectangle(8, 3), Hexagon(4)]
    max_shape = find_max_perimeter(shapes)
    print(f"Max perimeter: {max_shape.get_perimeter():.2f}")

    print("\n4) Multiple interfaces")
    duck = Duck()
    fish = Fish()
    flyers: list[Flyable] = [duck]
    swimmers: list[Swimmable] = [duck, fish]
    for flyer in flyers:
        flyer.fly()
    for swimmer in swimmers:
        swimmer.swim()

    print("\n5) Sender")
    chosen_sender: Sender = TelegramBot()
    notify(chosen_sender, "Your order is ready", "@user123")

    print("\n6) Product sorting")
    products = [
        Product("Keyboard", 50.0),
        Product("Mouse", 25.0),
        Product("Monitor", 200.0),
    ]
    products.sort()
    for product in products:
        print(f"{product.name}: {product.price}")

    print("\n7) Repository")
    # One-line switch of implementation:
    storage: Repository = MemoryRepository()
    # storage: Repository = FileRepository("storage.txt")
    demo_repository(storage)
