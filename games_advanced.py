"""
Moduł games_advanced.py - Zaawansowane gry w systemie RetroOS
Zawiera implementacje bardziej złożonych gier edukacyjnych i rozrywkowych
"""

import random
from base_app import BaseApp


class AmongUsGame(BaseApp):
    """
    Gra symulująca Among Us - znaleźć impostora wśród członków załogi.
    Gra edukacyjna o dedukcji logicznej i analizie zachowań.
    """

    def __init__(self):
        """
        Konstruktor gry Among Us.
        """
        super().__init__("Among Us Simulator v2.0", 512)
        self.crew_members = []
        self.impostor_index = 0
        self.current_round = 0
        self.max_rounds = 3
        self.crew_votes = []
        self.game_message = ""
        self.suspicion_levels = {}

    def _create_crew(self) -> None:
        """
        Tworzy załogę z losowymi członkami.
        Jeden z nich jest impostorem.
        """
        names = ["Red", "Blue", "Green", "Yellow", "Pink", "Orange", "Purple", "Cyan", "Lime", "White"]
        crew_size = 8
        selected_names = random.sample(names, crew_size)

        self.crew_members = selected_names
        self.impostor_index = random.randint(0, crew_size - 1)

        # Inicjalizuj poziomy podejrzenia
        for member in self.crew_members:
            self.suspicion_levels[member] = random.randint(10, 40)

    def start(self) -> None:
        """
        Inicjalizuje grę Among Us.
        """
        self.is_running = True
        self.current_round = 0
        self._create_crew()

        print("\n" + "*" * 70)
        print("* AMONG US SIMULATOR v2.0 *".center(70))
        print("*" * 70)
        print("\nWitaj w kosmicznej grze Among Us!")
        print("Twojąm zadaniem jest zidentyfikować impostora wśród członków załogi.")
        print("\nFakty:")
        print(f"  • Załoga składa się z {len(self.crew_members)} członków")
        print(f"  • Jeden z nich jest impostorem (sabotażystą)")
        print(f"  • Musisz go odkryć na podstawie wskazówek i podejrzenia")
        print(f"  • Będziesz miał(-a) {self.max_rounds} rundy do głosowania")
        print("\nPowodzenia! 🚀\n")

    def render(self) -> None:
        """
        Rysuje interfejs gry.
        """
        print("\n" + "=" * 70)
        print(f"RUNDA {self.current_round + 1}/{self.max_rounds}".center(70))
        print("=" * 70)

        print("\n📋 ZAŁOGA KOSMICZNA:")
        print("-" * 70)

        for i, member in enumerate(self.crew_members):
            suspicion = self.suspicion_levels[member]
            bar_length = 20
            filled = int((suspicion / 100) * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"{i + 1}. {member:12} [Podejrzenie: {bar}] ({suspicion}%)")

        if self.game_message:
            print(f"\n{self.game_message}")
            self.game_message = ""

        print("\n" + "-" * 70)
        print("Wybierz członka załogi do głosowania (1-8):")

    def update(self) -> None:
        """
        Aktualizuje stan gry.
        Obsługuje głosowanie gracza.
        """
        try:
            user_input = input("\nTwój wybór (1-8): ").strip()
            choice = int(user_input) - 1

            if choice < 0 or choice >= len(self.crew_members):
                self.game_message = "⚠️  Błąd: Wybierz numer między 1 a 8!"
                return

            chosen_member = self.crew_members[choice]

            print(f"\n🔍 Głosujesz na usunięcie: {chosen_member}")
            input("Naciśnij Enter aby kontynuować...")

            if choice == self.impostor_index:
                self._on_impostor_found(chosen_member)
                self.is_running = False
            else:
                self._on_wrong_vote(chosen_member)
                self.current_round += 1

                if self.current_round >= self.max_rounds:
                    self._on_game_over_loss()
                    self.is_running = False

        except ValueError:
            self.game_message = "⚠️  Błąd: Wpisz liczbę!"

    def _on_impostor_found(self, member: str) -> None:
        """
        Obsługuje znalezienie impostora.

        Args:
            member (str): Nazwa znalezionego impostora
        """
        print("\n" + "=" * 70)
        print("* ZWYCIĘSTWO! *".center(70))
        print("=" * 70)
        print(f"\n✓ Poprawnie zidentyfikowałeś(-aś) impostora!")
        print(f"🔴 {member} był(-a) sabotażystą!\n")
        print("Załoga jest bezpieczna! Statek wrócił do domu.")
        print("=" * 70 + "\n")

    def _on_wrong_vote(self, member: str) -> None:
        """
        Obsługuje błędne głosowanie.

        Args:
            member (str): Nazwa usuniętego członka
        """
        impostor = self.crew_members[self.impostor_index]
        print(f"\n❌ {member} nie był(-a) impostorem!")
        print(f"   {member} opuścił(-a) statek.\n")

        # Impostor sabotuje - podnosi podejrzenie innych
        print("🔴 Impostor sabotuje system!")
        for i, other_member in enumerate(self.crew_members):
            if i != self.impostor_index:
                increase = random.randint(5, 15)
                self.suspicion_levels[other_member] += increase
                self.suspicion_levels[other_member] = min(100, self.suspicion_levels[other_member])

    def _on_game_over_loss(self) -> None:
        """
        Obsługuje przegraną grę.
        """
        impostor = self.crew_members[self.impostor_index]
        print("\n" + "=" * 70)
        print("* KONIEC GRY - PRZEGRANA! *".center(70))
        print("=" * 70)
        print(f"\n✗ Nie zdołałeś(-aś) zidentyfikować impostora!")
        print(f"🔴 Impostorem był(-a): {impostor}\n")
        print("Impostor przejął kontrolę nad statkiem!")
        print("Wszyscy członkowie załogi zostali wyeliminowani.")
        print("=" * 70 + "\n")


class MinesweeperGame(BaseApp):
    """
    Klasyczna gra Minesweeper - znaleźć wszystkie miny bez ich aktywacji.
    Gra logiczna ucząca myślenia strategicznego.
    """

    def __init__(self):
        """
        Konstruktor gry Minesweeper.
        """
        super().__init__("Minesweeper Classic v1.8", 256)
        self.grid_size = 5
        self.mines_count = 5
        self.board = []
        self.revealed = []
        self.flags = []
        self.game_message = ""

    def _create_board(self) -> None:
        """
        Tworzy planszę z minami.
        """
        # Inicjalizuj planszę
        self.board = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.revealed = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.flags = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # Losowo umieść miny
        mines_placed = 0
        while mines_placed < self.mines_count:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)

            if self.board[row][col] != -1:  # -1 oznacza minę
                self.board[row][col] = -1
                mines_placed += 1

        # Oblicz liczby
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col] != -1:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < self.grid_size and 0 <= nc < self.grid_size:
                                if self.board[nr][nc] == -1:
                                    count += 1
                    self.board[row][col] = count

    def start(self) -> None:
        """
        Inicjalizuje grę Minesweeper.
        """
        self.is_running = True
        self._create_board()

        print("\n" + "*" * 70)
        print("* MINESWEEPER CLASSIC v1.8 *".center(70))
        print("*" * 70)
        print("\nWitaj w grze Minesweeper!")
        print("Odkryj wszystkie bezpieczne pola bez aktywacji min.")
        print(f"\nPlanszą: {self.grid_size}x{self.grid_size}")
        print(f"Liczba min: {self.mines_count}")
        print("\nKomendy:")
        print("  reveal X Y  - Odkryj pole")
        print("  flag X Y    - Oznacz flagą (podejrzenie miny)")
        print("  unflag X Y  - Usuń flagę\n")

    def render(self) -> None:
        """
        Rysuje planszę gry.
        """
        print("\n" + "=" * 70)
        print("MINESWEEPER".center(70))
        print("=" * 70 + "\n")

        # Wyświetl numery kolumn
        print("    ", end="")
        for col in range(self.grid_size):
            print(f"{col + 1} ", end="")
        print("\n")

        # Wyświetl planszę
        for row in range(self.grid_size):
            print(f" {row + 1}: ", end="")
            for col in range(self.grid_size):
                if self.flags[row][col]:
                    print("🚩", end=" ")
                elif not self.revealed[row][col]:
                    print("■", end=" ")
                else:
                    cell = self.board[row][col]
                    if cell == -1:
                        print("💣", end=" ")
                    elif cell == 0:
                        print("·", end=" ")
                    else:
                        print(cell, end=" ")
            print()

        if self.game_message:
            print(f"\n{self.game_message}")
            self.game_message = ""

        print("\n" + "-" * 70)
        print("Wpisz komendę (reveal X Y, flag X Y, unflag X Y):")

    def update(self) -> None:
        """
        Aktualizuje stan gry.
        """
        try:
            user_input = input("\n> ").strip().split()

            if len(user_input) < 3:
                self.game_message = "⚠️  Błąd: Wpisz komendę (np: reveal 1 1)"
                return

            command = user_input[0].lower()
            col = int(user_input[1]) - 1
            row = int(user_input[2]) - 1

            if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
                self.game_message = f"⚠️  Błąd: Współrzędne poza zakresem (1-{self.grid_size})"
                return

            if command == "reveal":
                self._reveal_cell(row, col)
            elif command == "flag":
                self.flags[row][col] = True
                self.game_message = f"🚩 Oznaczono pole ({col + 1}, {row + 1})"
            elif command == "unflag":
                self.flags[row][col] = False
                self.game_message = f"Usunięto flagę z pola ({col + 1}, {row + 1})"
            else:
                self.game_message = "⚠️  Nieznana komenda!"

        except ValueError:
            self.game_message = "⚠️  Błąd: Wpisz liczby!"

    def _reveal_cell(self, row: int, col: int) -> None:
        """
        Odkrywa pole na planszy.

        Args:
            row (int): Wiersz
            col (int): Kolumna
        """
        if self.revealed[row][col]:
            self.game_message = "⚠️  To pole już zostało odkryte!"
            return

        self.revealed[row][col] = True

        if self.board[row][col] == -1:
            self._on_mine_hit()
        else:
            self._check_win_condition()

    def _on_mine_hit(self) -> None:
        """
        Obsługuje trafieniw na minę.
        """
        print("\n" + "=" * 70)
        print("* KONIEC GRY - PRZEGRANA! *".center(70))
        print("=" * 70)
        print("\n💥 BOOOM! Trafiłeś(-aś) na minę!\n")
        self.is_running = False

    def _check_win_condition(self) -> None:
        """
        Sprawdza czy gracz wygrał.
        """
        revealed_count = sum(row.count(True) for row in self.revealed)
        safe_cells = (self.grid_size * self.grid_size) - self.mines_count

        if revealed_count == safe_cells:
            print("\n" + "=" * 70)
            print("* ZWYCIĘSTWO! *".center(70))
            print("=" * 70)
            print(f"\n✓ Gratulacje! Odkryłeś(-aś) wszystkie bezpieczne pola!")
            print("Wszystkie miny zidentyfikowane!\n")
            print("=" * 70 + "\n")
            self.is_running = False


class CodingChallengeGame(BaseApp):
    """
    Gra edukacyjna - rozwiązuj zagadki programistyczne.
    Uczy logicznego myślenia i podstaw algorytmiki.
    """

    def __init__(self):
        """
        Konstruktor gry.
        """
        super().__init__("Coding Challenge v1.5", 384)
        self.challenges = []
        self.current_challenge = 0
        self.score = 0
        self.game_message = ""

    def _create_challenges(self) -> None:
        """
        Tworzy listę wyzwań programistycznych.
        """
        self.challenges = [
            {
                "title": "WYZWANIE 1: Suma liczb",
                "desc": "Ile wynosi suma liczb od 1 do 100?",
                "answer": 5050,
                "hint": "Użyj wzoru: n * (n + 1) / 2"
            },
            {
                "title": "WYZWANIE 2: Liczba Fibonacciego",
                "desc": "Jaka jest 10. liczba Fibonacciego? (ciąg: 1, 1, 2, 3, 5, 8...)",
                "answer": 55,
                "hint": "Każda liczba to suma dwóch poprzednich"
            },
            {
                "title": "WYZWANIE 3: Konwersja binarnie",
                "desc": "Ile wynosi liczba 15 w systemie binarnym? (wpisz bez '0b')",
                "answer": "1111",
                "hint": "Dziel przez 2 i zbieraj reszty"
            },
            {
                "title": "WYZWANIE 4: Operacja logiczna",
                "desc": "Wynik: (5 > 3) AND (2 == 2) = ?",
                "answer": "True",
                "hint": "TRUE = 1, FALSE = 0. AND wymaga obu warunków"
            },
            {
                "title": "WYZWANIE 5: Silnia",
                "desc": "Ile wynosi silnia z 5? (5! = 5 * 4 * 3 * 2 * 1)",
                "answer": 120,
                "hint": "Mnóż: 5 * 4 * 3 * 2 * 1"
            }
        ]

    def start(self) -> None:
        """
        Inicjalizuje grę.
        """
        self.is_running = True
        self.current_challenge = 0
        self.score = 0
        self._create_challenges()

        print("\n" + "*" * 70)
        print("* CODING CHALLENGE v1.5 *".center(70))
        print("*" * 70)
        print("\nWitaj w wyzwaniach programistycznych!")
        print("Rozwiąż zagadki z zakresu algorytmiki i logiki.")
        print(f"\nWyzwań do rozwiązania: {len(self.challenges)}")
        print("Za każde poprawne rozwiązanie otrzymasz 1 punkt.\n")

    def render(self) -> None:
        """
        Rysuje aktualny stan.
        """
        if self.current_challenge >= len(self.challenges):
            return

        challenge = self.challenges[self.current_challenge]

        print("\n" + "=" * 70)
        print(challenge["title"].center(70))
        print("=" * 70)
        print(f"\n{challenge['desc']}\n")
        print(f"💡 Podpowiedź: {challenge['hint']}\n")

        if self.game_message:
            print(f"{self.game_message}\n")
            self.game_message = ""

        print("-" * 70)
        print("Twoja odpowiedź:")

    def update(self) -> None:
        """
        Aktualizuje stan gry.
        """
        challenge = self.challenges[self.current_challenge]
        user_input = input("\n> ").strip()

        # Konwertuj odpowiedź na odpowiedni typ
        expected_answer = challenge["answer"]
        is_correct = False

        try:
            if isinstance(expected_answer, int):
                user_answer = int(user_input)
                is_correct = user_answer == expected_answer
            else:
                user_answer = str(user_input).lower()
                is_correct = user_answer == str(expected_answer).lower()
        except ValueError:
            user_answer = str(user_input).lower()
            is_correct = user_answer == str(expected_answer).lower()

        if is_correct:
            print(f"\n✓ POPRAWNIE! Odpowiedź to: {expected_answer}")
            self.score += 1
        else:
            print(f"\n✗ BŁĘDNIE! Prawidłowa odpowiedź to: {expected_answer}")

        self.current_challenge += 1

        if self.current_challenge >= len(self.challenges):
            input("\nNaciśnij Enter aby zobaczyć wyniki...")
            self._display_results()
            self.is_running = False
        else:
            input("\nNaciśnij Enter aby przejść do następnego wyzwania...")

    def _display_results(self) -> None:
        """
        Wyświetla wyniki.
        """
        total = len(self.challenges)
        percentage = (self.score / total) * 100

        print("\n" + "=" * 70)
        print("WYNIKI WYZWAŃ PROGRAMISTYCZNYCH".center(70))
        print("=" * 70)
        print(f"\nWynik: {self.score}/{total} poprawnych")
        print(f"Procent: {percentage:.1f}%")

        if percentage >= 100:
            print("\n🌟 FENOMENALNIE! Jesteś mistrzem algorytmiki!")
        elif percentage >= 80:
            print("\n⭐ ŚWIETNIE! Masz solidne umiejętności programistyczne!")
        elif percentage >= 60:
            print("\n✓ DOBRZE! Kontynuuj naukę algorytmiki!")
        else:
            print("\n📚 Potrzebujesz więcej praktyki z algorytmami!")

        print("=" * 70 + "\n")
