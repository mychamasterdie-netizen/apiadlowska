from datetime import datetime


class SystemLogger:
    """
    Klasa do logowania zdarzeń systemowych.
    Przechowuje historię wszystkich akcji wykonanych w systemie.
    """

    def __init__(self):
        """
        Konstruktor logera systemowego.
        Inicjalizuje pustą listę historii.
        """
        self.history: list[str] = []

    def log_event(self, message: str) -> None:
        """
        Loguje zdarzenie z czasem jego wystąpienia.

        Args:
            message (str): Treść zdarzenia do zalogowania
        """
        current_time = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{current_time}] {message}"
        self.history.append(formatted_message)

    def print_all_logs(self) -> None:
        """
        Wyświetla całą historię logów na ekranie.
        Czyści ekran i wypisuje każdy wpis z listy historii.
        """
        self._clear_screen()
        print("\n" + "=" * 70)
        print("HISTORIA ZDARZEŃ SYSTEMOWYCH".center(70))
        print("=" * 70 + "\n")

        if not self.history:
            print("Brak zdarzeń do wyświetlenia.\n")
        else:
            for log_entry in self.history:
                print(log_entry)

        print("\n" + "=" * 70)
        input("Naciśnij Enter aby powrócić do menu...")

    @staticmethod
    def _clear_screen() -> None:
        """
        Czyści ekran poprzez wydrukowanie pustych linii.
        """
        for _ in range(100):
            print()


class Profile:
    """
    Klasa bazowa reprezentująca profil użytkownika w systemie.
    Zarządza danymi dostępu i uprawnieniami.
    """

    def __init__(self, username: str, password: str):
        """
        Konstruktor profilu użytkownika.

        Args:
            username (str): Nazwa użytkownika
            password (str): Hasło użytkownika
        """
        self.username = username
        self.password = password
        self.allowed_apps = ["kalkulator"]

    def verify_password(self, password: str) -> bool:
        """
        Weryfikuje czy podane hasło jest poprawne.

        Args:
            password (str): Hasło do weryfikacji

        Returns:
            bool: True jeśli hasło jest poprawne, False w przeciwnym razie
        """
        return self.password == password

    def has_access_to_app(self, app_name: str) -> bool:
        """
        Sprawdza czy użytkownik ma dostęp do aplikacji.

        Args:
            app_name (str): Nazwa aplikacji

        Returns:
            bool: True jeśli użytkownik ma dostęp, False w przeciwnym razie
        """
        return app_name in self.allowed_apps


class AdminProfile(Profile):
    """
    Klasa reprezentująca profil administratora systemu.
    Dziedziczy po Profile i rozszerza jego funkcjonalność.
    """

    def __init__(self, username: str, password: str):
        """
        Konstruktor profilu administratora.
        Wywołuje konstruktor klasy bazowej i rozszerza uprawnienia.

        Args:
            username (str): Nazwa administratora
            password (str): Hasło administratora
        """
        super().__init__(username, password)
        self.account_type = "ROOT"
        self.allowed_apps.extend(["codebreaker", "crawler"])

    def __str__(self) -> str:
        """
        Zwraca sformatowany opis profilu administratora.

        Returns:
            str: Informacje o koncie administratora
        """
        return f"[{self.account_type}] {self.username} - Dostęp do aplikacji: {', '.join(self.allowed_apps)}"
