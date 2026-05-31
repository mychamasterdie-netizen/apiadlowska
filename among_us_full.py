"""
Moduł among_us_full.py - Pełna implementacja gry Among Us z mechaniką poruszania się
Realistyczna gra z mapą, zadaniami, systemem głosowania i pełnym gameplayem
"""

import random
from base_app import BaseApp
from typing import List, Tuple, Dict


class Player:
    """
    Klasa reprezentująca gracza w grze Among Us.
    """

    def __init__(self, name: str, color: str, is_impostor: bool = False):
        """
        Inicjalizuje gracza.

        Args:
            name (str): Nazwa gracza
            color (str): Kolor gracza
            is_impostor (bool): Czy gracz jest impostorem
        """
        self.name = name
        self.color = color
        self.is_impostor = is_impostor
        self.x = 0
        self.y = 0
        self.alive = True
        self.tasks_completed = 0
        self.total_tasks = 3 if not is_impostor else 0
        self.in_meeting = False

    def __str__(self) -> str:
        """
        Reprezentacja tekstowa gracza.
        """
        status = "💀 DEAD" if not self.alive else "✓ ALIVE"
        role = "🔴 IMPOSTOR" if self.is_impostor else "👤 CREW"
        return f"{self.color:12} {self.name:12} | {role} | {status}"


class Room:
    """
    Klasa reprezentująca pokój na mapie.
    """

    def __init__(self, name: str, x: int, y: int):
        """
        Inicjalizuje pokój.

        Args:
            name (str): Nazwa pokoju
            x (int): Współrzędna X
            y (int): Współrzędna Y
        """
        self.name = name
        self.x = x
        self.y = y
        self.players_here = []

    def add_player(self, player: Player) -> None:
        """
        Dodaje gracza do pokoju.

        Args:
            player (Player): Gracz do dodania
        """
        if player not in self.players_here:
            self.players_here.append(player)

    def remove_player(self, player: Player) -> None:
        """
        Usuwa gracza z pokoju.

        Args:
            player (Player): Gracz do usunięcia
        """
        if player in self.players_here:
            self.players_here.remove(player)

    def get_players(self) -> List[Player]:
        """
        Zwraca listę graczy w pokoju.

        Returns:
            List[Player]: Lista graczy
        """
        return self.players_here


class Task:
    """
    Klasa reprezentująca zadanie dla crew memberów.
    """

    def __init__(self, name: str, description: str, room: str):
        """
        Inicjalizuje zadanie.

        Args:
            name (str): Nazwa zadania
            description (str): Opis zadania
            room (str): Pokój, gdzie jest zadanie
        """
        self.name = name
        self.description = description
        self.room = room
        self.completed = False

    def complete(self) -> None:
        """
        Oznacza zadanie jako ukończone.
        """
        self.completed = True


class AmongUsFullGame(BaseApp):
    """
    Pełna implementacja gry Among Us z poruszaniem się, zadaniami i głosowaniem.
    Gra edukacyjna ucząca pracy zespołowej, dedukcji i przetrwania.
    """

    def __init__(self):
        """
        Konstruktor gry Among Us.
        """
        super().__init__("Among Us Full v3.0", 768)
        self.players = []
        self.rooms = []
        self.current_player = None
        self.impostor = None
        self.round_number = 0
        self.emergency_calls = 0
        self.game_state = "playing"  # playing, voting, ended
        self.game_message = ""
        self.dead_bodies = []

    def _create_map(self) -> None:
        """
        Tworzy mapę gry z różnymi pokojami.
        """
        self.rooms = [
            Room("🏠 CAFETERIA", 5, 5),
            Room("🔧 ENGINE ROOM", 2, 2),
            Room("🛡️  SHIELDS", 8, 2),
            Room("🧪 LABORATORY", 8, 8),
            Room("🚪 ELECTRICAL", 2, 8),
            Room("☠️  MEDBAY", 5, 2)
        ]

    def _create_players(self) -> None:
        """
        Tworzy graczy na mapie.
        """
        colors = ["Red", "Blue", "Green", "Yellow", "Pink", "Orange"]
        names = ["Adam", "Bia", "Cezary", "Dorota", "Ewa", "Filip"]

        for i in range(6):
            is_impostor = (i == random.randint(0, 5))
            player = Player(names[i], colors[i], is_impostor)
            player.x = random.randint(2, 8)
            player.y = random.randint(2, 8)
            self.players.append(player)

            if is_impostor:
                self.impostor = player

            # Dodaj gracza do pokoju
            for room in self.rooms:
                if abs(player.x - room.x) < 1 and abs(player.y - room.y) < 1:
                    room.add_player(player)

        self.current_player = self.players[0]

    def _create_tasks(self) -> List[Task]:
        """
        Tworzy listę zadań dla crew memberów.

        Returns:
            List[Task]: Lista zadań
        """
        return [
            Task("Aktywacja Tarcz", "Kliknij przełączniki w Shields", "🛡️  SHIELDS"),
            Task("Naprawa Silnika", "Napraw kod w Engine Room", "🔧 ENGINE ROOM"),
            Task("Skanowanie Medyczne", "Przejdź skan w Medbay", "☠️  MEDBAY")
        ]

    def start(self) -> None:
        """
        Inicjalizuje pełną grę Among Us.
        """
        self.is_running = True
        self._create_map()
        self._create_players()

        print("\n" + "*" * 70)
        print("* AMONG US FULL v3.0 - INTERACTIVE GAMEPLAY *".center(70))
        print("*" * 70)
        print("\n🚀 WITAJ W KOSMICZNEJ STACJI!")
        print("\nTwoim zadaniem:")
        if self.current_player.is_impostor:
            print("  ⚠️  JESTEŚ IMPOSTOREM! Wyeliminuj crew memberów bez zostania złapanym.")
            print("  • Poruszaj się po stacji")
            print("  • Sabotuj systemy")
            print("  • Ukryj swoje czyny")
        else:
            print("  ✓ JESTEŚ CREW MEMBEREM! Wykonaj zadania i znaleź impostora.")
            print("  • Poruszaj się po stacji (wasd)")
            print("  • Wykonaj przydzielone zadania")
            print("  • Zgłaszaj podejrzane działania")

        print("\n📋 GRACZE:")
        for player in self.players:
            role = "🔴 IMPOSTOR (TAJNE!)" if (player == self.current_player and player.is_impostor) else "👤 CREW"
            print(f"  {player.color:12} - {player.name:12} ({role})")

        print("\nKOMANDY RUCHU: w/a/s/d")
        print("AKCJE: e (wykonaj zadanie), r (zgłoś ciało), v (wezwij spotkanie)")
        print("\n")
        input("Naciśnij Enter aby zacząć grę...")

    def render(self) -> None:
        """
        Rysuje interfejs gry.
        """
        self._clear_screen()
        print("\n" + "=" * 70)
        print("AMONG US - MAPA STACJI".center(70))
        print("=" * 70 + "\n")

        # Rysuj mapę
        self._draw_map()

        print("\n" + "-" * 70)
        print("👤 TWÓJ GRACZ:")
        print(f"  {self.current_player}")

        print("\n🏠 GRACZE W TWOJEJ OKOLICY:")
        current_room = self._get_current_room()
        if current_room:
            nearby_players = [p for p in current_room.get_players() if p.alive and p != self.current_player]
            if nearby_players:
                for player in nearby_players:
                    print(f"  {player.name:12} ({player.color})")
            else:
                print("  Brak graczy w pobliżu")

        print("\n📊 STATUS MISJI:")
        crew_alive = sum(1 for p in self.players if p.alive and not p.is_impostor)
        impostor_alive = sum(1 for p in self.players if p.alive and p.is_impostor)
        print(f"  Crew alive: {crew_alive} | Impostorów: {impostor_alive}")

        if self.game_message:
            print(f"\n💬 {self.game_message}")
            self.game_message = ""

        print("\n" + "-" * 70)
        print("KOMENDY: w/a/s/d (porusz), e (zadanie), r (ciało), v (spotkanie), q (wyjście)")

    def _draw_map(self) -> None:
        """
        Rysuje mapę stacji.
        """
        # Wysokość i szerokość mapy
        map_width = 12
        map_height = 10

        # Inicjalizuj mapę
        map_grid = [["." for _ in range(map_width)] for _ in range(map_height)]

        # Dodaj pokoje
        for room in self.rooms:
            if 0 <= room.x < map_width and 0 <= room.y < map_height:
                map_grid[room.y][room.x] = "█"

        # Dodaj graczy
        for player in self.players:
            if player.alive and 0 <= player.x < map_width and 0 <= player.y < map_height:
                if player == self.current_player:
                    map_grid[player.y][player.x] = "●"  # Ty
                elif player.is_impostor and not (player == self.current_player and player.is_impostor):
                    map_grid[player.y][player.x] = "○"  # Inni (impostora nie widać)
                else:
                    map_grid[player.y][player.x] = "◉"  # Crew memberowie

        # Rysuj mapę
        print("   ", end="")
        for i in range(map_width):
            print(f"{i} ", end="")
        print("\n")

        for y in range(map_height):
            print(f"{y:2} ", end="")
            for x in range(map_width):
                print(f"{map_grid[y][x]} ", end="")
            print()

        print("\nLegenda: ● = Ty, ◉ = Crew, ○ = Inni, █ = Pokój, . = Pusta przestrzeń")

    def _get_current_room(self) -> 'Room':
        """
        Zwraca pokój, w którym znajduje się gracz.

        Returns:
            Room: Pokój gracza lub None
        """
        for room in self.rooms:
            if abs(self.current_player.x - room.x) < 1.5 and abs(self.current_player.y - room.y) < 1.5:
                return room
        return None

    def _move_player(self, dx: int, dy: int) -> None:
        """
        Przesuwa gracza na mapie.

        Args:
            dx (int): Zmiana X
            dy (int): Zmiana Y
        """
        old_room = self._get_current_room()

        new_x = max(0, min(11, self.current_player.x + dx))
        new_y = max(0, min(9, self.current_player.y + dy))

        self.current_player.x = new_x
        self.current_player.y = new_y

        new_room = self._get_current_room()

        if old_room != new_room:
            if old_room:
                old_room.remove_player(self.current_player)
            if new_room:
                new_room.add_player(self.current_player)
                self.game_message = f"Wszedłeś do {new_room.name}"

    def _kill_player(self, victim: Player) -> None:
        """
        Eliminuje gracza (tylko dla impostora).

        Args:
            victim (Player): Ofiara
        """
        if not self.current_player.is_impostor:
            self.game_message = "⚠️  Tylko impostor może eliminować!"
            return

        current_room = self._get_current_room()
        if victim not in current_room.get_players():
            self.game_message = "⚠️️  Ten gracz nie jest w pobliżu!"
            return

        victim.alive = False
        self.dead_bodies.append(victim)
        self.game_message = f"☠️  {victim.name} został wyeliminowany!"

    def _report_body(self) -> None:
        """
        Zgłasza znalezione ciało.
        """
        current_room = self._get_current_room()
        if not current_room:
            self.game_message = "⚠️  Nie jesteś w pokoju!"
            return

        found_bodies = [b for b in self.dead_bodies if abs(b.x - self.current_player.x) < 2 and abs(b.y - self.current_player.y) < 2]

        if not found_bodies:
            self.game_message = "⚠️  Brak ciał w pobliżu!"
            return

        self.game_message = f"☠️  Znaleźliśmy ciało! Wezwanie spotkania kryzysowego..."
        self._start_meeting()

    def _start_meeting(self) -> None:
        """
        Rozpoczyna spotkanie głosowania.
        """
        self.game_state = "voting"
        print("\n" + "=" * 70)
        print("SPOTKANIE KRYZYSOWE!".center(70))
        print("=" * 70)

        print("\n👥 WSZYSCY GRACZE:")
        for i, player in enumerate(self.players, 1):
            status = "💀 DEAD" if not player.alive else "✓ ALIVE"
            print(f"  {i}. {player.name:12} ({player.color:12}) {status}")

        print("\nKto jest impostorem? (Wpisz numer 1-6):")
        try:
            choice = int(input("\nTwój głos: ")) - 1
            if 0 <= choice < len(self.players):
                chosen_player = self.players[choice]
                self._vote_out_player(chosen_player)
            else:
                self.game_message = "⚠️  Błędny numer!"
        except ValueError:
            self.game_message = "⚠️  Wpisz liczbę!"

        self.game_state = "playing"

    def _vote_out_player(self, player: Player) -> None:
        """
        Wyrzuca gracza z głosowania.

        Args:
            player (Player): Gracz do wyrzucenia
        """
        if player.is_impostor:
            print(f"\n✓ POPRAWNIE! {player.name} był impostorem!")
            print("Crew wygrywa! Statek wrócił do domu bezpiecznie.")
            self.is_running = False
        else:
            print(f"\n✗ BŁĄD! {player.name} był crew memberem!")
            print(f"{player.name} został wyrzucony z statku...")
            player.alive = False
            self._check_win_condition()

    def _check_win_condition(self) -> None:
        """
        Sprawdza warunki wygranej.
        """
        crew_alive = sum(1 for p in self.players if p.alive and not p.is_impostor)
        impostor_alive = sum(1 for p in self.players if p.alive and p.is_impostor)

        if impostor_alive == 0:
            print("\n✓ CREW ZWYCIĘŻA! Wszyscy impostorzy wyrzuceni!")
            self.is_running = False
        elif crew_alive <= impostor_alive:
            print("\n✗ IMPOSTOR ZWYCIĘŻA! Przejął kontrolę nad stacją!")
            self.is_running = False

    def update(self) -> None:
        """
        Aktualizuje stan gry.
        """
        try:
            command = input("\n> ").strip().lower()

            if command == "w":
                self._move_player(0, -1)
            elif command == "s":
                self._move_player(0, 1)
            elif command == "a":
                self._move_player(-1, 0)
            elif command == "d":
                self._move_player(1, 0)
            elif command == "e":
                self.game_message = "✓ Wykonujesz zadanie..."
                self.current_player.tasks_completed += 1
            elif command == "r":
                self._report_body()
            elif command == "v":
                self._start_meeting()
            elif command == "q":
                self.is_running = False
            else:
                self.game_message = "⚠️  Nieznana komenda!"

        except Exception as e:
            self.game_message = f"⚠️  Błąd: {e}"

    @staticmethod
    def _clear_screen() -> None:
        """
        Czyści ekran.
        """
        for _ in range(50):
            print()
