"""
Moduł apps_extended.py - Rozszerzenie aplikacji o quizy edukacyjne
Integruje system quizów z RetroOS
"""

from base_app import BaseApp
from quiz_system import ComputerScienceQuiz, ProgrammingBasicsQuiz
import random


class ComputerScienceQuizApp(BaseApp):
    """
    Aplikacja quizu z informatyki dla 1 LO.
    Uczy podstawowe pojęcia z informatyki poprzez interaktywne pytania.
    """

    def __init__(self):
        """
        Konstruktor aplikacji quizu.
        Inicjalizuje parametry poprzez klasę bazową.
        """
        super().__init__("Informatyka Quiz v1.0", 128)
        self.quiz = ComputerScienceQuiz()
        self.current_questions = []
        self.current_question_index = 0
        self.game_message = ""

    def start(self) -> None:
        """
        Inicjalizuje grę quizową.
        Losuje pytania i wyświetla wprowadzenie.
        """
        self.is_running = True
        self.current_questions = self.quiz.get_random_questions(5)
        self.current_question_index = 0
        self.quiz.score = 0

        print("\n" + "*" * 70)
        print("* INFORMATYKA QUIZ v1.0 *".center(70))
        print("*" * 70)
        print("\nWitaj w quizie z informatyki!")
        print("Będziesz odpowiadać na pytania dotyczące komputerów i technologii.")
        print("Za każdą poprawną odpowiedź otrzymasz 1 punkt.")
        print("\nPytań do rozwiązania: " + str(self.quiz.total_questions))
        print("\nOdpowiedzz wpisując A, B, C lub D\n")

    def render(self) -> None:
        """
        Rysuje aktualny stan quizu.
        Wyświetla pytanie i opcje odpowiedzi.
        """
        if self.current_question_index >= len(self.current_questions):
            return

        question = self.current_questions[self.current_question_index]
        question.display(self.current_question_index + 1)

        if self.game_message:
            print(f"\n{self.game_message}")
            self.game_message = ""

        print("\nTwoja odpowiedź (A/B/C/D):")

    def update(self) -> None:
        """
        Aktualizuje stan quizu.
        Przetwarza odpowiedź użytkownika i przechodzi do następnego pytania.
        """
        try:
            user_input = input("> ").strip().upper()

            # Walidacja odpowiedzi
            if user_input not in ['A', 'B', 'C', 'D']:
                self.game_message = "⚠️  Błąd: Wpisz A, B, C lub D!"
                return

            # Konwersja litery na indeks (A=0, B=1, C=2, D=3)
            answer_index = ord(user_input) - ord('A')

            # Sprawdzenie odpowiedzi
            question = self.current_questions[self.current_question_index]
            is_correct, explanation = question.check_answer(answer_index)

            print(f"\n{explanation}\n")

            if is_correct:
                self.quiz.add_score(1)

            self.quiz.answered += 1
            self.current_question_index += 1

            # Jeśli to było ostatnie pytanie
            if self.current_question_index >= len(self.current_questions):
                input("Naciśnij Enter aby zobaczyć wyniki...")
                self.quiz.display_results()
                self.is_running = False
            else:
                input("Naciśnij Enter aby przejść do następnego pytania...")

        except ValueError:
            self.game_message = "⚠️  Błąd: Wpisz A, B, C lub D!"


class ProgrammingQuizApp(BaseApp):
    """
    Aplikacja quizu o podstawach programowania.
    Uczy koncepcji programistyczne poprzez pytania.
    """

    def __init__(self):
        """
        Konstruktor aplikacji.
        """
        super().__init__("Programowanie Quiz v1.5", 256)
        self.quiz = ProgrammingBasicsQuiz()
        self.current_questions = []
        self.current_question_index = 0
        self.game_message = ""

    def start(self) -> None:
        """
        Inicjalizuje quiz programowania.
        """
        self.is_running = True
        self.current_questions = self.quiz.get_random_questions(5)
        self.current_question_index = 0
        self.quiz.score = 0

        print("\n" + "*" * 70)
        print("* PROGRAMOWANIE QUIZ v1.5 *".center(70))
        print("*" * 70)
        print("\nWitaj w quizie o programowaniu!")
        print("Nauczysz się podstawowych koncepcji programistycznych.")
        print("Za każdą poprawną odpowiedź otrzymasz 1 punkt.")
        print(f"\nPytań do rozwiązania: {self.quiz.total_questions}\n")

    def render(self) -> None:
        """
        Rysuje aktualny stan quizu.
        """
        if self.current_question_index >= len(self.current_questions):
            return

        question = self.current_questions[self.current_question_index]
        question.display(self.current_question_index + 1)

        if self.game_message:
            print(f"\n{self.game_message}")
            self.game_message = ""

        print("\nTwoja odpowiedź (A/B/C/D):")

    def update(self) -> None:
        """
        Aktualizuje stan quizu.
        """
        try:
            user_input = input("> ").strip().upper()

            if user_input not in ['A', 'B', 'C', 'D']:
                self.game_message = "⚠️  Błąd: Wpisz A, B, C lub D!"
                return

            answer_index = ord(user_input) - ord('A')

            question = self.current_questions[self.current_question_index]
            is_correct, explanation = question.check_answer(answer_index)

            print(f"\n{explanation}\n")

            if is_correct:
                self.quiz.add_score(1)

            self.current_question_index += 1

            if self.current_question_index >= len(self.current_questions):
                input("Naciśnij Enter aby zobaczyć wyniki...")
                self.quiz.display_results()
                self.is_running = False
            else:
                input("Naciśnij Enter aby przejść do następnego pytania...")

        except ValueError:
            self.game_message = "⚠️  Błąd: Wpisz A, B, C lub D!"


class NetworkSecurityLab(BaseApp):
    """
    Aplikacja laboratorium bezpieczeństwa sieciowego.
    Gra edukacyjna o chronieniu danych w sieci.
    """

    def __init__(self):
        """
        Konstruktor aplikacji.
        """
        super().__init__("Network Security Lab v1.2", 384)
        self.scenario = 0
        self.correct_actions = 0
        self.game_message = ""

    def start(self) -> None:
        """
        Inicjalizuje laboratorium.
        """
        self.is_running = True
        self.scenario = 0
        self.correct_actions = 0

        print("\n" + "*" * 70)
        print("* NETWORK SECURITY LAB v1.2 *".center(70))
        print("*" * 70)
        print("\nWitaj w laboratorium bezpieczeństwa sieciowego!")
        print("Poznasz zagrożenia internetowe i jak się przed nimi bronić.")
        print("W każdym scenariuszu wybierz bezpieczną akcję.\n")

    def render(self) -> None:
        """
        Wyświetla scenariusz bezpieczeństwa.
        """
        scenarios = [
            {
                "title": "SCENARIUSZ 1: Podejrzany Email",
                "desc": "Otrzymujesz email od 'banku' z linkiem do potwierdzenia danych.",
                "options": [
                    "Klikniesz w link i podasz dane",
                    "Nie klikniesz, sprawdzisz adres nadawcy i kontaktujesz bank",
                    "Przechyliś wiadomość do spamu",
                    "Prześlij email wszystkim znajomym"
                ],
                "correct": 1
            },
            {
                "title": "SCENARIUSZ 2: Hasło",
                "desc": "Jak powinno wyglądać bezpieczne hasło?",
                "options": [
                    "123456",
                    "MojImie2024",
                    "X9#kL2@pQ7mNzV (duże litery, małe, cyfry, znaki specjalne)",
                    "password"
                ],
                "correct": 2
            },
            {
                "title": "SCENARIUSZ 3: WiFi Publiczny",
                "desc": "Łączysz się z WiFi w kawiarni. Co robisz, aby być bezpieczny?",
                "options": [
                    "Normalnie robisz wszystko, co zwykle",
                    "Nie wchodzisz na strony z hasłami i logami",
                    "Używasz VPN do szyfrowania połączenia",
                    "Wyłączasz WiFi i używasz 4G"
                ],
                "correct": 2
            }
        ]

        if self.scenario < len(scenarios):
            s = scenarios[self.scenario]\n            print(\"\\n\" + \"=\" * 70)
            print(s[\"title\"].center(70))
            print(\"=\" * 70)
            print(f\"\\n{s['desc']}\\n\")

            for i, option in enumerate(s[\"options\"]):
                print(f\"  {i+1}. {option}\")

            if self.game_message:
                print(f\"\\n{self.game_message}\")

    def update(self) -> None:
        """
        Przetwarza wybór użytkownika.
        """
        scenarios = [
            {
                "title": "SCENARIUSZ 1: Podejrzany Email",
                "desc": "Otrzymujesz email od 'banku' z linkiem do potwierdzenia danych.",
                "options": [
                    "Klikniesz w link i podasz dane",
                    "Nie klikniesz, sprawdzisz adres nadawcy i kontaktujesz bank",
                    "Przechyliś wiadomość do spamu",
                    "Prześlij email wszystkim znajomym"
                ],
                "correct": 1
            },
            {
                "title": "SCENARIUSZ 2: Hasło",
                "desc": "Jak powinno wyglądać bezpieczne hasło?",
                "options": [
                    "123456",
                    "MojImie2024",
                    "X9#kL2@pQ7mNzV (duże litery, małe, cyfry, znaki specjalne)",
                    "password"
                ],
                "correct": 2
            },
            {
                "title": "SCENARIUSZ 3: WiFi Publiczny",
                "desc": "Łączysz się z WiFi w kawiarni. Co robisz, aby być bezpieczny?",
                "options": [
                    "Normalnie robisz wszystko, co zwykle",
                    "Nie wchodzisz na strony z hasłami i logami",
                    "Używasz VPN do szyfrowania połączenia",
                    "Wyłączasz WiFi i używasz 4G"
                ],
                "correct": 2
            }
        ]

        try:
            user_input = input("\\nTwój wybór (1/2/3/4): \").strip()
            choice = int(user_input) - 1

            if choice < 0 or choice >= 4:
                self.game_message = "⚠️  Błąd: Wybierz 1, 2, 3 lub 4!"
                return

            scenario = scenarios[self.scenario]

            if choice == scenario[\"correct\"]:
                print(f\"\\n✓ POPRAWNIE! To bezpieczna akcja.\")
                self.correct_actions += 1
            else:
                correct_option = scenario[\"options\"][scenario[\"correct\"]]
                print(f\"\\n✗ BŁĘDNIE! Prawidłowa odpowiedź to: {correct_option}\")

            self.scenario += 1

            if self.scenario >= len(scenarios):
                input(\"\\nNaciśnij Enter aby zobaczyć wyniki...\")
                self._display_results()
                self.is_running = False
            else:
                input(\"\\nNaciśnij Enter aby przejść do następnego scenariusza...\")

        except ValueError:
            self.game_message = \"⚠️  Błąd: Wpisz liczbę!\"\n\n    def _display_results(self) -> None:\n        \"\"\"\n        Wyświetla wyniki laboratorium.\n        \"\"\"\n        total = 3\n        percentage = (self.correct_actions / total) * 100\n\n        print(\"\\n\" + \"=\" * 70)\n        print(\"WYNIKI LABORATORIUM\".center(70))\n        print(\"=\" * 70)\n        print(f\"\\nPoprawne odpowiedzi: {self.correct_actions}/{total}\")\n        print(f\"Procent: {percentage:.1f}%\")\n\n        if percentage >= 100:\n            print(\"\\n🛡️  DOSKONAŁY BEZPIECZEŃŚMY! Jesteś ekspertem!\")\n        elif percentage >= 66:\n            print(\"\\n✓ DOBRZE! Znasz podstawy bezpieczeństwa.\")\n        else:\n            print(\"\\n⚠️  Przypomnij sobie zasady bezpieczeństwa online.\")\n\n        print(\"=\" * 70 + \"\\n\")\n"