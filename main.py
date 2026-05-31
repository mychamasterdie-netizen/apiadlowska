from hardware import VirtualMachine
from system_uzytkownikow import SystemLogger, AdminProfile
from apps_package import CodeBreakerGame, NetCrawlerRPG
from apps_extended import ComputerScienceQuizApp, ProgrammingQuizApp, NetworkSecurityLab
from games_advanced import AmongUsGame, MinesweeperGame, CodingChallengeGame


def clear_screen() -> None:
    """
    Czyści ekran poprzez wydrukowanie pustych linii.
    """
    for _ in range(60):
        print()


def display_main_menu() -> None:
    """
    Wyświetla główne menu systemu.
    """
    print("\n" + "=" * 70)
    print("RETRO OS - TERMINAL".center(70))
    print("=" * 70)
    print("\nDostępne komendy:")
    print("  [apps]           - Wyświetl dostępne aplikacje")
    print("  [run NAZWA]      - Uruchom aplikację (np: run codebreaker)")
    print("  [logs]           - Wyświetl historię zdarzeń")
    print("  [whoami]         - Wyświetl bieżącego użytkownika")
    print("  [shutdown]       - Wyłącz system")
    print("\n" + "=" * 70)


def display_user_info(user: AdminProfile) -> None:
    """
    Wyświetla informacje o zalogowanym użytkowniku.

    Args:
        user (AdminProfile): Aktualny profil użytkownika
    """
    print(f"\nZalogowany użytkownik: {user}")


def display_available_apps(system_apps: dict) -> None:
    """
    Wyświetla listę dostępnych aplikacji z ich wymaganiami RAM.

    Args:
        system_apps (dict): Słownik dostępnych aplikacji
    """
    print("\n" + "=" * 70)
    print("DOSTĘPNE APLIKACJE".center(70))
    print("=" * 70 + "\n")

    categories = {
        "🎮 GRY LOGICZNE": ["codebreaker", "crawler", "minesweeper"],
        "📚 QUIZY EDUKACYJNE": ["csquiz", "progquiz"],
        "🔐 BEZPIECZEŃSTWO": ["networksec"],
        "🚀 GRY ZAAWANSOWANE": ["amongus", "codingchallenge"]
    }

    for category, apps in categories.items():
        print(f"{category}:")
        for app_name in apps:
            if app_name in system_apps:
                app = system_apps[app_name]
                print(f"  📱 {app.name}")
                print(f"     Wymagania RAM: {app.ram_required}MB")
                print(f"     Komenda: run {app_name}")
        print()

    print("=" * 70)


def run_application(app_name: str, machine: VirtualMachine, logger: SystemLogger,
                    system_apps: dict, current_user: AdminProfile) -> bool:
    """
    Uruchamia wybraną aplikację z obsługą alokacji RAM.

    Args:
        app_name (str): Nazwa aplikacji do uruchomienia
        machine (VirtualMachine): Maszyna wirtualna
        logger (SystemLogger): Logger systemowy
        system_apps (dict): Słownik aplikacji
        current_user (AdminProfile): Aktualny użytkownik

    Returns:
        bool: True jeśli aplikacja została uruchomiona, False w przeciwnym razie
    """
    if app_name not in system_apps:
        print(f"\n✗ Błąd: Aplikacja '{app_name}' nie istnieje.")
        return False

    if not current_user.has_access_to_app(app_name):
        print(f"\n✗ Błąd: Brak dostępu do aplikacji '{app_name}'.")
        logger.log_event(f"ODMOWA DOSTĘPU: Próba uruchomienia {app_name} przez {current_user.username}")
        return False

    app = system_apps[app_name]

    # Sprawdź dostępność RAM
    if not machine.ram.allocate(app.ram_required):
        print(f"\n✗ Błąd: Brak wystarczającej ilości RAM!")
        print(f"  Wymagane: {app.ram_required}MB")
        print(f"  Dostępne: {machine.ram.total - machine.ram.used}MB")
        logger.log_event(f"BRAK PAMIĘCI: Nie można uruchomić {app.name} (brak {app.ram_required}MB)")
        return False

    # Alokacja udana - uruchom aplikację
    logger.log_event(f"URUCHOMIONO: {app.name}")
    print(f"\n✓ Uruchamianie aplikacji: {app.name}...\n")

    app.start()

    # Główna pętla aplikacji
    while app.is_running:
        app.render()
        app.update()

    # Zwolnij RAM i zaloguj zamknięcie
    machine.ram.free(app.ram_required)
    logger.log_event(f"ZAMKNIĘTO: {app.name}")
    print(f"\n✓ Aplikacja {app.name} zamknięta.")
    input("Naciśnij Enter aby powrócić do menu...")

    return True


def main() -> None:
    """
    Główna funkcja programu.
    Uruchamia pętlę głównego systemu operacyjnego RetroOS.
    """
    # Inicjalizacja systemu
    machine = VirtualMachine("Ryzen 9", 4.0, 1024)
    logger = SystemLogger()
    current_user = AdminProfile("Root_Hacker", "admin123")

    # Rozszerzona baza aplikacji ze wszystkimi grami i quizami
    system_apps = {
        # Gry logiczne
        "codebreaker": CodeBreakerGame(),
        "crawler": NetCrawlerRPG(),
        "minesweeper": MinesweeperGame(),
        
        # Quizy edukacyjne
        "csquiz": ComputerScienceQuizApp(),
        "progquiz": ProgrammingQuizApp(),
        
        # Bezpieczeństwo
        "networksec": NetworkSecurityLab(),
        
        # Gry zaawansowane
        "amongus": AmongUsGame(),
        "codingchallenge": CodingChallengeGame()
    }

    # Rozszerz dostęp admina do wszystkich aplikacji
    current_user.allowed_apps = list(system_apps.keys())

    # Włącz system
    machine.power_status = True
    logger.log_event("Włączono system operacyjny RetroOS")
    logger.log_event(f"Zalogowano użytkownika: {current_user.username}")
    logger.log_event(f"Dostępne aplikacje: {len(system_apps)}")

    print("\n" + "*" * 70)
    print("* RETRO OS - WELCOME *".center(70))
    print("*" * 70)
    print("\nSystem uruchomiony pomyślnie.")
    print(f"Dostępnych aplikacji: {len(system_apps)}")
    input("Naciśnij Enter aby kontynuować...")

    # Główna pętla systemu
    while machine.power_status:
        clear_screen()
        print(machine.get_system_status())
        display_main_menu()
        display_user_info(current_user)

        user_input = input("\n$ ").strip().lower()

        # Obsługa komend
        if user_input == "apps":
            display_available_apps(system_apps)
            input("\nNaciśnij Enter aby powrócić do menu...")

        elif user_input == "logs":
            logger.print_all_logs()

        elif user_input == "whoami":
            clear_screen()
            display_user_info(current_user)
            input("\nNaciśnij Enter aby powrócić do menu...")

        elif user_input.startswith("run "):
            app_name = user_input[4:].strip()
            clear_screen()
            run_application(app_name, machine, logger, system_apps, current_user)

        elif user_input == "shutdown":
            logger.log_event("Wyłączono system RetroOS")
            machine.power_status = False
            clear_screen()
            print("\n" + "*" * 70)
            print("* SYSTEM SHUTDOWN *".center(70))
            print("*" * 70)
            print("\nDziękuję za korzystanie z RetroOS!")
            print("System wyłączony bezpiecznie.\n")

        else:
            print(f"\n✗ Nieznana komenda: '{user_input}'")
            print("Wpisz jedną z dostępnych komend z głównego menu.")
            input("\nNaciśnij Enter aby kontynuować...")


if __name__ == "__main__":
    """
    Punkt wejścia do programu.
    """
    main()
