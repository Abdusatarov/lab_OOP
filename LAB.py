"""
Library Management System
Объектілі бағдарланған программалау (SFT6002-105-L)
Final Project
"""

from abc import ABC, abstractmethod


# ============================================================
# АБСТРАКТІЛІ БАЗАЛЫҚ КЛАСС — Person
# ============================================================

class Person(ABC):
    """
    Абстрактілі базалық класс.
    Барлық адамдарға (Reader, Librarian) ортақ интерфейс береді.
    """

    def __init__(self, name: str):
        self._name = name  # Инкапсуляция: _ (жабық атрибут)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Аты бос болмауы керек!")
        self._name = value.strip()

    @abstractmethod
    def role(self) -> str:
        """Абстрактілі метод — әр ұрпақта өз іске асуы болады."""
        pass

    def show_info(self) -> str:
        """Полиморфизм: role() әрбір ұрпақтың өз нұсқасын шақырады."""
        return f"[{self.role()}] Аты: {self._name}"

    def __str__(self):
        return self.show_info()


# ============================================================
# Reader — Person-нан мұраланады
# ============================================================

class Reader(Person):
    """
    Кітапхана оқырманы.
    Мұрагерлік: Person -> Reader
    """

    def __init__(self, name: str, reader_id: int):
        super().__init__(name)
        self._reader_id = reader_id          # Инкапсуляция
        self._borrowed_books: list = []       # Алынған кітаптар тізімі

    @property
    def reader_id(self) -> int:
        return self._reader_id

    @property
    def borrowed_books(self) -> list:
        return list(self._borrowed_books)    # Тізімнің көшірмесін береміз

    def role(self) -> str:
        return "Оқырман"                      # Полиморфизм

    def borrow_book(self, book_title: str):
        if book_title in self._borrowed_books:
            raise ValueError(f"'{book_title}' кітабы қазірдің өзінде алынған!")
        self._borrowed_books.append(book_title)

    def return_book(self, book_title: str):
        if book_title not in self._borrowed_books:
            raise ValueError(f"'{book_title}' кітабы алынбаған!")
        self._borrowed_books.remove(book_title)

    def show_info(self) -> str:
        base = super().show_info()
        return f"{base} | ID: {self._reader_id} | Алынған кітаптар: {len(self._borrowed_books)}"


# ============================================================
# Librarian — Person-нан мұраланады
# ============================================================

class Librarian(Person):
    """
    Кітапхана қызметкері.
    Мұрагерлік: Person -> Librarian
    """

    def __init__(self, name: str, employee_id: str = "L-001"):
        super().__init__(name)
        self._employee_id = employee_id      # Инкапсуляция

    @property
    def employee_id(self) -> str:
        return self._employee_id

    def role(self) -> str:
        return "Кітапханашы"                  # Полиморфизм

    def show_info(self) -> str:
        base = super().show_info()
        return f"{base} | Қызметкер ID: {self._employee_id}"


# ============================================================
# Book — Кітап класы
# ============================================================

class Book:
    """
    Кітапты сипаттайтын класс.
    Инкапсуляция: жабық атрибуттар + property арқылы қол жеткізу.
    """

    def __init__(self, title: str, author: str, year: int, isbn: str = ""):
        self._title = title
        self._author = author
        self._year = year
        self._isbn = isbn
        self._is_available = True

    # --- Propertyлер (Инкапсуляция) ---

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if value < 1000 or value > 2100:
            raise ValueError("Жыл дұрыс мәнде болуы керек (1000-2100)!")
        self._year = value

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def is_available(self) -> bool:
        return self._is_available

    def mark_borrowed(self):
        if not self._is_available:
            raise ValueError(f"'{self._title}' кітабы қазір қолжетімді емес!")
        self._is_available = False

    def mark_returned(self):
        self._is_available = True

    def __str__(self):
        status = "Бар" if self._is_available else "Берілген"
        return (f"📖 '{self._title}' | Автор: {self._author} | "
                f"Жыл: {self._year} | Статус: {status}")

    def __repr__(self):
        return f"Book(title='{self._title}', author='{self._author}', year={self._year})"


# ============================================================
# Library — Кітапхана класы (негізгі класс)
# ============================================================

class Library:
    """
    Кітапхананы басқарушы класс.
    Кітаптар мен оқырмандарды басқарады.
    """

    def __init__(self, name: str):
        self._name = name
        self._books: list[Book] = []
        self._readers: list[Reader] = []
        self._staff: list[Librarian] = []

    @property
    def name(self) -> str:
        return self._name

    # ============ КІТАПТАРМЕН ЖҰМЫС ============

    def add_book(self, book: Book):
        """Кітап қосу."""
        if not isinstance(book, Book):
            raise TypeError("Тек Book типіндегі объект қосуға болады!")
        self._books.append(book)
        print(f"✅ Кітап қосылды: '{book.title}'")

    def remove_book(self, title: str) -> bool:
        """Кітапты атауы бойынша жою."""
        for book in self._books:
            if book.title.lower() == title.lower():
                self._books.remove(book)
                print(f"🗑️ Кітап жойылды: '{title}'")
                return True
        print(f"❌ '{title}' кітабы табылмады!")
        return False

    def search_by_title(self, query: str) -> list[Book]:
        """Атауы бойынша іздеу."""
        result = [b for b in self._books if query.lower() in b.title.lower()]
        return result

    def search_by_author(self, author: str) -> list[Book]:
        """Автор бойынша іздеу."""
        result = [b for b in self._books if author.lower() in b.author.lower()]
        return result

    def sort_by_year(self, reverse: bool = False) -> list[Book]:
        """Жылы бойынша сорттау."""
        return sorted(self._books, key=lambda b: b.year, reverse=reverse)

    def list_books(self):
        """Барлық кітаптар тізімі."""
        if not self._books:
            print("📚 Кітапхана бос.")
            return
        print(f"\n{'='*55}")
        print(f"  📚 {self._name} — Кітаптар тізімі ({len(self._books)} кітап)")
        print(f"{'='*55}")
        for i, book in enumerate(self._books, 1):
            print(f"  {i}. {book}")
        print(f"{'='*55}\n")

    def list_available_books(self):
        """Тек қолжетімді кітаптар."""
        available = [b for b in self._books if b.is_available]
        print(f"\n✅ Қолжетімді кітаптар: {len(available)} дана")
        for b in available:
            print(f"   - {b}")

    # ============ ОҚЫРМАНДАРМЕН ЖҰМЫС ============

    def add_reader(self, reader: Reader):
        """Оқырман қосу."""
        if not isinstance(reader, Reader):
            raise TypeError("Тек Reader типіндегі объект қосуға болады!")
        # ID бірегейлігін тексеру
        for r in self._readers:
            if r.reader_id == reader.reader_id:
                raise ValueError(f"ID={reader.reader_id} бар оқырман бұрын тіркелген!")
        self._readers.append(reader)
        print(f"✅ Оқырман тіркелді: {reader.name} (ID: {reader.reader_id})")

    def remove_reader(self, reader_id: int) -> bool:
        """Оқырманды жою."""
        for reader in self._readers:
            if reader.reader_id == reader_id:
                if reader.borrowed_books:
                    raise ValueError(f"Оқырманда {len(reader.borrowed_books)} қайтарылмаған кітап бар!")
                self._readers.remove(reader)
                print(f"🗑️ Оқырман жойылды: {reader.name}")
                return True
        print(f"❌ ID={reader_id} оқырман табылмады!")
        return False

    def list_readers(self):
        """Барлық оқырмандар тізімі."""
        if not self._readers:
            print("👥 Оқырмандар жоқ.")
            return
        print(f"\n{'='*55}")
        print(f"  👥 Оқырмандар тізімі ({len(self._readers)} адам)")
        print(f"{'='*55}")
        for i, reader in enumerate(self._readers, 1):
            print(f"  {i}. {reader.show_info()}")
        print(f"{'='*55}\n")

    # ============ ҚЫЗМЕТКЕРЛЕРМЕН ЖҰМЫС ============

    def add_librarian(self, librarian: Librarian):
        """Кітапханашы қосу."""
        self._staff.append(librarian)
        print(f"✅ Қызметкер қосылды: {librarian.name}")

    def list_staff(self):
        """Қызметкерлер тізімі."""
        if not self._staff:
            print("👤 Қызметкерлер жоқ.")
            return
        print(f"\n👤 Қызметкерлер тізімі:")
        for s in self._staff:
            print(f"   - {s.show_info()}")

    # ============ КІТАП БЕРУДЕГİ ОПЕРАЦИЯЛАР ============

    def borrow_book(self, reader_id: int, book_title: str):
        """Оқырманға кітап беру."""
        reader = self._find_reader(reader_id)
        book = self._find_book_by_title(book_title)

        if reader is None:
            raise ValueError(f"ID={reader_id} оқырман табылмады!")
        if book is None:
            raise ValueError(f"'{book_title}' кітабы табылмады!")

        book.mark_borrowed()
        reader.borrow_book(book.title)
        print(f"📤 '{book.title}' кітабы {reader.name}-ге берілді.")

    def return_book(self, reader_id: int, book_title: str):
        """Кітапты қабылдау."""
        reader = self._find_reader(reader_id)
        book = self._find_book_by_title(book_title)

        if reader is None:
            raise ValueError(f"ID={reader_id} оқырман табылмады!")
        if book is None:
            raise ValueError(f"'{book_title}' кітабы табылмады!")

        book.mark_returned()
        reader.return_book(book.title)
        print(f"📥 '{book.title}' кітабы қайтарылды ({reader.name}).")

    # ============ ЖЕКЕ КӨМЕКШІ ӘДІСТЕР ============

    def _find_reader(self, reader_id: int):
        for r in self._readers:
            if r.reader_id == reader_id:
                return r
        return None

    def _find_book_by_title(self, title: str):
        for b in self._books:
            if b.title.lower() == title.lower():
                return b
        return None

    def show_statistics(self):
        """Кітапхана статистикасы."""
        available = sum(1 for b in self._books if b.is_available)
        borrowed = len(self._books) - available
        print(f"\n{'='*55}")
        print(f"  📊 {self._name} — Статистика")
        print(f"{'='*55}")
        print(f"  Барлық кітаптар   : {len(self._books)}")
        print(f"  Қолжетімді        : {available}")
        print(f"  Берілген          : {borrowed}")
        print(f"  Оқырмандар        : {len(self._readers)}")
        print(f"  Қызметкерлер      : {len(self._staff)}")
        print(f"{'='*55}\n")


# ============================================================
# ПОЛИМОРФИЗМ ДЕМОНСТРАЦИЯСЫ
# ============================================================

def demonstrate_polymorphism(people: list):
    """
    Полиморфизм: Reader және Librarian бір тізімде,
    show_info() әр объектіде өзінше жұмыс істейді.
    """
    print("\n🔄 Полиморфизм демонстрациясы:")
    print("-" * 40)
    for person in people:
        print(person.show_info())
    print("-" * 40)


# ============================================================
# НЕГІЗГІ БАҒДАРЛАМА (main)
# ============================================================

def main():
    print("=" * 55)
    print("  📚 КІТАПХАНА БАСҚАРУ ЖҮЙЕСІ")
    print("  Library Management System")
    print("=" * 55)

    # --- Кітапхана құру ---
    library = Library("Орталық Кітапхана")

    # --- Қызметкерлер қосу ---
    librarian1 = Librarian("Айгүл Сейткали", "L-001")
    library.add_librarian(librarian1)

    # --- Кітаптар қосу ---
    print("\n📖 Кітаптар қосылуда...")
    books = [
        Book("Абай жолы", "Мұхтар Әуезов", 1942),
        Book("Қан мен тер", "Әбдіжәміл Нұрпейісов", 1961),
        Book("Python программалау", "Марк Лутц", 2013),
        Book("Clean Code", "Роберт Мартин", 2008),
        Book("The Pragmatic Programmer", "Дэвид Томас", 1999),
        Book("Батыр Баян", "Ілияс Жансүгіров", 1934),
    ]
    for book in books:
        library.add_book(book)

    # --- Оқырмандар тіркеу ---
    print("\n👥 Оқырмандар тіркелуде...")
    readers = [
        Reader("Алихан Сейткали", 1001),
        Reader("Дана Қасымова", 1002),
        Reader("Бекзат Нұрлан", 1003),
    ]
    for reader in readers:
        library.add_reader(reader)

    # --- Тізімдерді көрсету ---
    library.list_books()
    library.list_readers()
    library.list_staff()

    # --- Кітап беру ---
    print("\n📤 Кітап беру операциялары:")
    library.borrow_book(1001, "Абай жолы")
    library.borrow_book(1002, "Python программалау")
    library.borrow_book(1001, "Clean Code")

    # --- Іздеу ---
    print("\n🔍 'Python' бойынша іздеу:")
    results = library.search_by_title("Python")
    for b in results:
        print(f"   {b}")

    print("\n🔍 'Мұхтар Әуезов' авторы бойынша іздеу:")
    results = library.search_by_author("Мұхтар Әуезов")
    for b in results:
        print(f"   {b}")

    # --- Жылы бойынша сорттау ---
    print("\n📅 Жылы бойынша сорттау (өсу реті):")
    sorted_books = library.sort_by_year()
    for b in sorted_books:
        print(f"   {b}")

    # --- Кітап қайтару ---
    print("\n📥 Кітап қайтару:")
    library.return_book(1001, "Абай жолы")

    # --- Кітап жою ---
    print("\n🗑️ Кітап жою:")
    library.remove_book("Батыр Баян")

    # --- Статистика ---
    library.show_statistics()

    # --- Полиморфизм демонстрациясы ---
    all_people = [
        Reader("Алихан Сейткали", 1001),
        Librarian("Айгүл Сейткали"),
        Reader("Дана Қасымова", 1002),
    ]
    demonstrate_polymorphism(all_people)

    # --- Қате өңдеу (Exception Handling) ---
    print("\n⚠️ Қате өңдеу (Exception Handling) мысалдары:")
    try:
        library.borrow_book(9999, "Абай жолы")
    except ValueError as e:
        print(f"   ValueError: {e}")

    try:
        library.borrow_book(1002, "Python программалау")  # Бұрын берілген
    except ValueError as e:
        print(f"   ValueError: {e}")

    try:
        r = Reader("", 2000)  # Бос ат
    except ValueError as e:
        print(f"   ValueError: {e}")

    try:
        bad_book = Book("Test", "Author", 500)  # Дұрыс емес жыл
        bad_book.year = 500
    except ValueError as e:
        print(f"   ValueError: {e}")

    print("\n✅ Бағдарлама сәтті аяқталды!")


if __name__ == "__main__":
    main()