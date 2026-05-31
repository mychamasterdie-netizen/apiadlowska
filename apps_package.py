import random
from base_app import BaseApp


class CodeBreakerGame(BaseApp):
    """
    Gra "Szyfrator Sieciowy" - zgadywanie losowego kodu.
    Gracz ma ograniczoną liczbę prób aby odgadnąć trzycyfrowy kod.
    """

    def __init__(self):
        """
        Konstruktor gry CodeBreaker.
        Inicjalizuje parametry gry poprzez konstruktor klasy bazowej.
        """
        super().__init__("Szyfrator Sieciowy v1.0", 256)
        self.secret_code = 0
        self.attempts_left = 0

    def start(self) -> None:
        """
        Inicjalizuje grę.
        Ustawia flagę działania, generuje losowy kod i resetuje licznik prób.
        """
        self.is_running = True
        self.secret_code = random.randint(100, 999)
        self.attempts_left = 5
        print("\n" + "*" * 60)
        print("* SZYFRATOR SIECIOWY v1.0 *".center(60))
        print("*" * 60)
        print("\nWitaj w szyfratorze sieciowym!")
        print("Twoim zadaniem jest odgadnąć trzycyfrowy kod.")
        print(f"Masz {self.attempts_left} prób.")
        print("Wskaźniki: 'Za niski' lub 'Za wysoki' będą Ci pomocne.\n")

    def render(self) -> None:
        """
        Rysuje interfejs gry.
        Wyświetla ramkę, pozostałe próby i prośbę o wpisanie kodu.
        """
        print("\n" + "-" * 50)
        print(f"Pozostałe próby: {self.attempts_left}")
        print("-" * 50)
        print("\nPodaj trzycyfrowy kod (100-999):")

    def update(self) -> None:
        """
        Aktualizuje stan gry na podstawie danych wejściowych.
        Obsługuje błędy wpisania i logikę porównywania kodu.
        """
        try:
            user_input = input("> ")
            user_code = int(user_input)

            if user_code < 100 or user_code > 999:
                print("\n⚠️  Błąd: Kod musi być między 100 a 999!")
                return

            if user_code == self.secret_code:
                print("\n✓ SUKCES! Odgadłeś kod!")
                print(f"Prawidłowy kod to: {self.secret_code}")
                print(f"Odgadłeś w {6 - self.attempts_left} próbie(ach)!\n")
                self.is_running = False
            elif user_code < self.secret_code:
                print("\n↑ Sygnał za niski - kod jest większy")
                self.attempts_left -= 1
            else:
                print("\n↓ Sygnał za wysoki - kod jest mniejszy")
                self.attempts_left -= 1

            if self.attempts_left == 0 and self.is_running:
                print("\n✗ PORAŻKA! Skończyły się próby!")
                print(f"Prawidłowy kod to był: {self.secret_code}\n")
                self.is_running = False

        except ValueError:
            print("\n✗ Błąd: Podaj cyfry!")


class NetCrawlerRPG(BaseApp):
    """
    Gra RPG "Net Crawler" - walka z Zaporami Sieciowymi w wirtualnym lochu.
    Gracz ma 100 HP i musi pokonywać coraz silniejszych wrogów.
    """

    def __init__(self):
        """
        Konstruktor gry NetCrawler.
        Inicjalizuje parametry gry poprzez konstruktor klasy bazowej.
        """
        super().__init__("Net Crawler RPG v2.1", 512)
        self.player_hp = 100
        self.current_layer = 1
        self.enemy_hp = 0
        self.enemy_max_hp = 0
        self.game_message = ""

    def start(self) -> None:
        """
        Inicjalizuje grę RPG.
        Wituje gracza i przygotowuje pierwszego przeciwnika.
        """
        self.is_running = True
        self.player_hp = 100
        self.current_layer = 1
        print("\n" + "*" * 60)
        print("* NET CRAWLER RPG v2.1 *".center(60))
        print("*" * 60)
        print("\nWitaj w cyfrowym labiryncie!")
        print("Twoim zadaniem jest pokonać Zapory Sieciowe.")
        print("Z każdą warstwą wrogowie są coraz silniejsi.\n")
        self._spawn_enemy()

    def _spawn_enemy(self) -> None:
        """
        Generuje nowego przeciwnika (Zaporę Sieciową).
        Siła przeciwnika rośnie wraz z warstwą.
        """
        base_hp = 30 + (self.current_layer - 1) * 20
        self.enemy_max_hp = random.randint(base_hp - 5, base_hp + 5)
        self.enemy_hp = self.enemy_max_hp
        self.game_message = f"\n⚡ Pojawiła się Zapora Sieciowa poziomu {self.current_layer}!"

    def _draw_hp_bar(self, current: int, maximum: int, label: str) -> str:
        """
        Rysuje pasek zdrowia w postaci tekstowej.

        Args:
            current (int): Aktualna wartość HP
            maximum (int): Maksymalna wartość HP
            label (str): Etykieta paska (np. "GRACZ" lub "WRÓG")

        Returns:
            str: Sformatowany pasek zdrowia
        """
        if maximum <= 0:
            return ""
        bar_length = 30
        filled = int((current / maximum) * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        percentage = (current / maximum) * 100
        return f"{label}: [{bar}] {current}/{maximum} HP ({percentage:.0f}%)"

    def render(self) -> None:
        """
        Rysuje interfejs gry RPG.
        Wyświetla stany zdrowia, informacje o warstwie i dostępne akcje.
        """
        print("\n" + "=" * 60)
        print(f"WARSTWA: {self.current_layer}".center(60))
        print("=" * 60)

        # Wyświetl pasek zdrowia gracza
        player_bar = self._draw_hp_bar(self.player_hp, 100, "GRACZ")
        print(f"\n{player_bar}")

        # Wyświetl pasek zdrowia wroga
        enemy_bar = self._draw_hp_bar(self.enemy_hp, self.enemy_max_hp, "WRÓG  ")
        print(f"{enemy_bar}")

        # Wyświetl komunikat gry
        if self.game_message:
            print(f"\n{self.game_message}")
            self.game_message = ""

        # Wyświetl menu akcji
        print("\n" + "-" * 60)
        print("CO CHCESZ ZROBIĆ?")
        print("-" * 60)
        print("1. Wyślij pakiet atakujący")
        print("2. Uruchom skrypt naprawczy")
        print("3. Uciekaj (zakończy grę)")
        print("-" * 60)

    def update(self) -> None:
        """
        Aktualizuje stan gry RPG.
        Obsługuje akcje gracza: ataki, leczenie, ucieczkę.
        """
        try:
            user_input = input("\nTwoja akcja [1/2/3]: ").strip()

            if user_input == "1":  # Atak
                self._player_attack()
                if self.is_running and self.enemy_hp > 0:
                    self._enemy_attack()
            elif user_input == "2":  # Leczenie
                self._player_heal()
                if self.is_running and self.enemy_hp > 0:
                    self._enemy_attack()
            elif user_input == "3":  # Ucieczka
                print("\n✗ Opuściłeś dungeon. Gra zakończy się.")
                self.is_running = False
            else:
                print("\n⚠️  Nieznana akcja! Wpisz 1, 2 lub 3.")

        except Exception as e:
            print(f"\n✗ Błąd: {e}")

    def _player_attack(self) -> None:
        """
        Wykonuje atak gracza na wroga.
        Losuje obrażenia i aplikuje je wrogowi.
        """
        damage = random.randint(15, 30)
        self.enemy_hp -= damage
        self.game_message = f"\n⚔️  Wysłałeś pakiet! Zadałeś {damage} obrażeń!"

        if self.enemy_hp <= 0:
            self._on_enemy_defeated()

    def _player_heal(self) -> None:
        """
        Gracz uruchamia skrypt naprawczy (leczenie).
        Przywraca losową ilość zdrowia.
        """
        heal_amount = random.randint(20, 35)
        old_hp = self.player_hp
        self.player_hp = min(self.player_hp + heal_amount, 100)
        actual_heal = self.player_hp - old_hp
        self.game_message = f"\n💚 Uruchomiłeś skrypt naprawczy! Wróciło {actual_heal} HP!"

    def _enemy_attack(self) -> None:
        """
        Wróg atakuje gracza.
        Losuje obrażenia i aplikuje je graczowi.
        """
        damage = random.randint(8, 18)
        self.player_hp -= damage
        self.game_message += f" Zapora kontrattakuje! Otrzymałeś {damage} obrażeń!"

        if self.player_hp <= 0:
            self._on_player_defeated()

    def _on_enemy_defeated(self) -> None:
        """
        Obsługuje pokonanie wroga.
        Przechodzi do następnej warstwy lub kończy grę w zwycięstwie.
        """
        self.game_message = "\n✓ ZWYCIĘSTWO! Pokonałeś Zaporę Sieciową!"
        self.current_layer += 1

        if self.current_layer > 5:
            print(self.game_message)
            print("\n" + "*" * 60)
            print("* KONIEC GRY - WYGRAŁEŚ! *".center(60))
            print("*" * 60)
            print(f"\nPokonałeś wszystkie 5 warstw dungeomu!")
            print(f"Twoje finalne HP: {self.player_hp}/100\n")
            self.is_running = False
        else:
            self._spawn_enemy()

    def _on_player_defeated(self) -> None:
        """
        Obsługuje śmierć gracza.
        Kończy grę w porażce.
        """
        print("\n" + "*" * 60)
        print("* KONIEC GRY - PRZEGRAŁEŚ! *".center(60))
        print("*" * 60)
        print(f"\nZostałeś pokonany na warstwie {self.current_layer}.")
        print(f"Dotarłeś do {self.current_layer} warstwy dungeonu.\n")
        self.is_running = False
