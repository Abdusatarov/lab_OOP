# ============================================================
# ООП: Паттерны Facade и State
# ============================================================

from abc import ABC, abstractmethod


# ============================================================
# ПАТТЕРН 1: FACADE — Умный дом
# ============================================================

class Light:
    def on(self):
        print("  [Свет] Включён")

    def off(self):
        print("  [Свет] Выключен")


class Thermostat:
    def set_temperature(self, t: int):
        print(f"  [Термостат] Температура установлена: {t}°C")


class SecuritySystem:
    def arm(self):
        print("  [Сигнализация] Включена (режим охраны)")

    def disarm(self):
        print("  [Сигнализация] Отключена")


class SmartHomeFacade:
    def __init__(self):
        self._light = Light()
        self._thermostat = Thermostat()
        self._security = SecuritySystem()

    def leave_home(self):
        print(">> LeaveHome: уходим из дома...")
        self._light.off()
        self._thermostat.set_temperature(16)
        self._security.arm()

    def arrive_home(self):
        print(">> ArriveHome: возвращаемся домой...")
        self._security.disarm()
        self._light.on()
        self._thermostat.set_temperature(22)


# ============================================================
# ПАТТЕРН 2: STATE — Заявка в службе поддержки
# ============================================================

class ITicketState(ABC):
    @abstractmethod
    def handle(self, ticket) -> None:
        pass


class NewState(ITicketState):
    def handle(self, ticket) -> None:
        print("  [NewState] Заявка создана и ожидает рассмотрения")
        ticket.state = InProgressState()


class InProgressState(ITicketState):
    def handle(self, ticket) -> None:
        print("  [InProgressState] Менеджер работает над заявкой")
        ticket.state = ResolvedState()


class ResolvedState(ITicketState):
    def handle(self, ticket) -> None:
        print("  [ResolvedState] Заявка закрыта")


class Ticket:
    def __init__(self):
        self.state = NewState()

    def next_state(self) -> None:
        self.state.handle(self)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("=" * 40)
    print("  Паттерн Facade — Умный дом")
    print("=" * 40)

    facade = SmartHomeFacade()
    facade.leave_home()
    print()
    facade.arrive_home()

    print()
    print("=" * 40)
    print("  Паттерн State — Служба поддержки")
    print("=" * 40)

    ticket = Ticket()

    print(">> Шаг 1:")
    ticket.next_state()

    print(">> Шаг 2:")
    ticket.next_state()

    print(">> Шаг 3:")
    ticket.next_state()