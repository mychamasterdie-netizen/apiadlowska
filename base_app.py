from abc import ABC, abstractmethod


class BaseApp(ABC):
    """
    Klasa bazowa dla wszystkich aplikacji (gier) w systemie RetroOS.
    Definiuje architekturę i wymusza implementację kluczowych metod.
    """

    def __init__(self, name: str, ram_required: int):
        """
        Konstruktor klasy bazowej.

        Args:
            name (str): Nazwa aplikacji
            ram_required (int): Ilość RAM-u wymagana do uruchomienia (w MB)
        """
        self.__name = name
        self.__ram_required = ram_required
        self.is_running = False

    @property
    def name(self) -> str:
        """
        Getter dla nazwy aplikacji (read-only).
        Próba przypisania wartości wyrzuci błąd AttributeError.

        Returns:
            str: Nazwa aplikacji
        """
        return self.__name

    @property
    def ram_required(self) -> int:
        """
        Getter dla wymagań RAM (read-only).
        Próba przypisania wartości wyrzuci błąd AttributeError.

        Returns:
            int: Ilość wymaganego RAM-u w MB
        """
        return self.__ram_required

    @abstractmethod
    def start(self) -> None:
        """
        Metoda abstrakcyjna do inicjalizacji aplikacji.
        Każda gra musi ją zaimplementować.
        """
        pass

    @abstractmethod
    def update(self) -> None:
        """
        Metoda abstrakcyjna do aktualizacji stanu aplikacji.
        Obsługuje logikę gry i dane wejściowe od użytkownika.
        Każda gra musi ją zaimplementować.
        """
        pass

    @abstractmethod
    def render(self) -> None:
        """
        Metoda abstrakcyjna do rysowania interfejsu aplikacji.
        Wyświetla ekran gry.
        Każda gra musi ją zaimplementować.
        """
        pass
