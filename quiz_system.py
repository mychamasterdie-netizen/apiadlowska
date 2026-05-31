"""
Moduł quiz_system.py - System quizów edukacyjnych
Zawiera pytania z zakresu informatyki na poziomie 1 LO
"""

import random
from typing import List, Tuple, Dict


class QuizQuestion:
    """
    Klasa reprezentująca jedno pytanie quizowe.
    Zawiera treść, opcje odpowiedzi i prawidłową odpowiedź.
    """

    def __init__(self, question: str, options: List[str], correct_answer: int, explanation: str):
        """
        Konstruktor pytania quizowego.

        Args:
            question (str): Treść pytania
            options (List[str]): Lista opcji odpowiedzi (4 opcje: A, B, C, D)
            correct_answer (int): Indeks prawidłowej odpowiedzi (0-3)
            explanation (str): Wyjaśnienie prawidłowej odpowiedzi
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation

    def display(self, question_number: int) -> None:
        """
        Wyświetla pytanie w formacie tekstowym.

        Args:
            question_number (int): Numer pytania w quizie
        """
        print("\n" + "=" * 70)
        print(f"PYTANIE {question_number}".center(70))
        print("=" * 70)
        print(f"\n{self.question}\n")

        letters = ['A', 'B', 'C', 'D']
        for i, option in enumerate(self.options):
            print(f"  {letters[i]}) {option}")

    def check_answer(self, user_answer: int) -> Tuple[bool, str]:
        """
        Sprawdza czy odpowiedź użytkownika jest poprawna.

        Args:
            user_answer (int): Indeks wybranej przez użytkownika opcji (0-3)

        Returns:
            Tuple[bool, str]: (czy odpowiedź poprawna, wyjaśnienie)
        """
        is_correct = user_answer == self.correct_answer
        letters = ['A', 'B', 'C', 'D']

        if is_correct:
            result = f"✓ POPRAWNIE! Odpowiedź to {letters[self.correct_answer]}: {self.options[self.correct_answer]}\n"
        else:
            result = f"✗ BŁĘDNIE! Wybrałeś {letters[user_answer]}, a prawidłowa odpowiedź to {letters[self.correct_answer]}: {self.options[self.correct_answer]}\n"

        result += f"WYJAŚNIENIE: {self.explanation}"
        return is_correct, result


class ComputerScienceQuiz:
    """
    Klasa zarządzająca quizem z informatyki.
    Zawiera pytania, liczy punkty i wyświetla wyniki.
    """

    def __init__(self):
        """
        Konstruktor quizu.
        Inicjalizuje bazę pytań edukacyjnych.
        """
        self.questions = self._create_questions()
        self.score = 0
        self.total_questions = 0
        self.answered = 0

    def _create_questions(self) -> List[QuizQuestion]:
        """
        Tworzy bazę pytań z informatyki na poziomie 1 LO.

        Returns:
            List[QuizQuestion]: Lista wszystkich pytań
        """
        questions = [
            QuizQuestion(
                "Jaki jest główny zadaniem CPU (procesora)?",
                [
                    "Przechowywanie danych na dysku",
                    "Wykonywanie instrukcji i sterowanie pracą komputera",
                    "Wyświetlanie obrazu na monitorze",
                    "Wzmacnianie sygnału internetowego"
                ],
                1,
                "Procesor to mózg komputera - wykonuje wszystkie instrukcje programów i koordynuje pracę innych komponentów."
            ),
            QuizQuestion(
                "Co oznacza skrót RAM?",
                [
                    "Read And Modify",
                    "Random Access Memory - pamięć o dostępie swobodnym",
                    "Rapid Automatic Machine",
                    "Resource Allocation Manager"
                ],
                1,
                "RAM to pamięć operacyjna - szybka, ale nietrwała. Jej zawartość traci się po wyłączeniu komputera."
            ),
            QuizQuestion(
                "Ile bitów ma jeden bajt?",
                [
                    "4 bity",
                    "8 bitów",
                    "16 bitów",
                    "32 bity"
                ],
                1,
                "1 bajt = 8 bitów. Bit to najmniejsza jednostka informacji (0 lub 1)."
            ),
            QuizQuestion(
                "Co to jest system operacyjny?",
                [
                    "Program do edycji tekstu",
                    "Oprogramowanie zarządzające zasobami komputera i umożliwiające uruchamianie aplikacji",
                    "Antywirus chroniący komputer",
                    "Gra komputerowa"
                ],
                1,
                "System operacyjny (np. Windows, Linux, macOS) to pośrednik między użytkownikiem a sprzętem komputera."
            ),
            QuizQuestion(
                "Jaka jest główna różnica między twardym dyskiem HDD a SSD?",
                [
                    "SSD jest droższy, ale wolniejszy",
                    "HDD używa wirujących talerzy, SSD używa pamięci elektronicznej - SSD jest szybszy",
                    "HDD może przechowywać więcej danych",
                    "Nie ma różnicy w wydajności"
                ],
                1,
                "SSD (Solid State Drive) nie ma ruchomych części, dlatego jest szybszy i bardziej niezawodny niż HDD."
            ),
            QuizQuestion(
                "Co to jest bit?",
                [
                    "Mała gra komputerowa",
                    "Najmniejsza jednostka informacji (0 lub 1)",
                    "Rodzaj antywirusa",
                    "Program do edycji grafiki"
                ],
                1,
                "Bit (ang. binary digit) to najmniejsza jednostka danych. Komputer operuje na bitach - każdy bit to 0 lub 1."
            ),
            QuizQuestion(
                "Jaki jest porządek rosnący jednostek pamięci?",
                [
                    "B < KB < MB < GB < TB",
                    "KB < B < MB < GB < TB",
                    "MB < KB < B < GB < TB",
                    "TB < GB < MB < KB < B"
                ],
                0,
                "Prawidłowy porządek: Bajt (B) < Kilobajt (KB) < Megabajt (MB) < Gigabajt (GB) < Terabajt (TB)"
            ),
            QuizQuestion(
                "Co to jest algorytm?",
                [
                    "Rodzaj wirusa komputerowego",
                    "Sekwencja kroków do rozwiązania problemu",
                    "Plik danych",
                    "Kod zdalnego dostępu"
                ],
                1,
                "Algorytm to dokładnie zdefiniowana procedura do rozwiązania problemu. Jest fundamentem programowania."
            ),
            QuizQuestion(
                "Ile wynosi 1 GB w MB?",
                [
                    "100 MB",
                    "512 MB",
                    "1024 MB",
                    "2048 MB"
                ],
                2,
                "1 GB = 1024 MB. System binarny używa potęg liczby 2, a nie dziesiętnych."
            ),
            QuizQuestion(
                "Co to jest kompilator?",
                [
                    "Antywirusowy program ochronny",
                    "Program zamieniający kod źródłowy na kod maszynowy",
                    "Edytor tekstu dla programistów",
                    "Narzędzie do zarządzania plikami"
                ],
                1,
                "Kompilator tłumaczy kod źródłowy (napisany przez człowieka) na kod maszynowy, który procesor może wykonać."
            ),
        ]
        return questions

    def get_random_questions(self, count: int = 5) -> List[QuizQuestion]:
        """
        Losowo wybiera pytania z bazy.

        Args:
            count (int): Ile pytań wylosować

        Returns:
            List[QuizQuestion]: Lista wylosowanych pytań
        """
        self.total_questions = min(count, len(self.questions))
        return random.sample(self.questions, self.total_questions)

    def add_score(self, points: int) -> None:
        """
        Dodaje punkty do wyniku.

        Args:
            points (int): Liczba punktów do dodania
        """
        self.score += points

    def get_percentage(self) -> float:
        """
        Oblicza procent poprawnych odpowiedzi.

        Returns:
            float: Procent poprawnych odpowiedzi
        """
        if self.total_questions == 0:
            return 0.0
        return (self.score / self.total_questions) * 100

    def display_results(self) -> None:
        """
        Wyświetla podsumowanie wyników quizu.
        """
        percentage = self.get_percentage()
        print("\n" + "=" * 70)
        print("PODSUMOWANIE QUIZU".center(70))
        print("=" * 70)
        print(f"\nWynik: {self.score}/{self.total_questions} poprawnych odpowiedzi")
        print(f"Procent: {percentage:.1f}%")

        if percentage >= 90:
            rating = "DOSKONALE! 🌟🌟🌟"
        elif percentage >= 75:
            rating = "BARDZO DOBRZE! 🌟🌟"
        elif percentage >= 60:
            rating = "DOBRZE! 🌟"
        elif percentage >= 50:
            rating = "PRZYZWOICIE"
        else:
            rating = "POTRZEBUJESZ WIĘCEJ NAUKI"

        print(f"Ocena: {rating}")
        print("=" * 70 + "\n")


class ProgrammingBasicsQuiz:
    """
    Klasa quizu dotyczącego podstaw programowania.
    """

    def __init__(self):
        """
        Konstruktor quizu programowania.
        """
        self.questions = self._create_programming_questions()
        self.score = 0
        self.total_questions = 0

    def _create_programming_questions(self) -> List[QuizQuestion]:
        """
        Tworzy pytania o podstawach programowania.

        Returns:
            List[QuizQuestion]: Lista pytań
        """
        questions = [
            QuizQuestion(
                "Co to jest zmienna w programowaniu?",
                [
                    "Przyciski na klawiaturze",
                    "Pojemnik na dane z przypisaną nazwą",
                    "Rodzaj błędu programu",
                    "Urządzenie peryferyjne"
                ],
                1,
                "Zmienna to pojemnik przechowujący wartość, którą możemy używać i zmieniać w programie."
            ),
            QuizQuestion(
                "Do czego służy pętla (loop) w programie?",
                [
                    "Do przesłania wiadomości",
                    "Do powtarzania określonego fragmentu kodu",
                    "Do tworzenia kopii zapasowych",
                    "Do łączenia z internetem"
                ],
                1,
                "Pętla pozwala na automatyczne powtarzanie kodu - zamiast pisać go wielokrotnie."
            ),
            QuizQuestion(
                "Co to jest funkcja (procedure) w kodzie?",
                [
                    "Błąd w programie",
                    "Blok kodu wykonujący konkretne zadanie, które można wielokrotnie wywoływać",
                    "Opcja w menu programu",
                    "Nazwa zmiennej"
                ],
                1,
                "Funkcja to powtórnie używany blok kodu. Pozwala na organizację i reużywalność kodu."
            ),
            QuizQuestion(
                "Co to jest instrukcja warunkowa (if/else)?",
                [
                    "Polecenie wyłączenia komputera",
                    "Wyświetlanie komunikatu błędu",
                    "Struktury decyzyjne - wykonują kod na podstawie warunku",
                    "Rodzaj pamięci komputera"
                ],
                2,
                "If/else pozwala na wykonanie różnych akcji w zależności od spełnienia warunku."
            ),
            QuizQuestion(
                "Jaki jest cel debugowania programu?",
                [
                    "Dodawanie nowych funkcji",
                    "Szybszenie programu",
                    "Wyszukiwanie i usuwanie błędów",
                    "Zmiana nazwy pliku"
                ],
                2,
                "Debugowanie to proces szukania i naprawiania błędów w kodzie. Jest kluczowe dla jakości oprogramowania."
            ),
        ]
        return questions

    def get_random_questions(self, count: int = 5) -> List[QuizQuestion]:
        """
        Losowo wybiera pytania.

        Args:
            count (int): Liczba pytań

        Returns:
            List[QuizQuestion]: Wylosowane pytania
        """
        self.total_questions = min(count, len(self.questions))
        return random.sample(self.questions, self.total_questions)

    def add_score(self, points: int) -> None:
        """
        Dodaje punkty.

        Args:
            points (int): Punkty do dodania
        """
        self.score += points

    def get_percentage(self) -> float:
        """
        Oblicza procent poprawnych odpowiedzi.

        Returns:
            float: Procent
        """
        if self.total_questions == 0:
            return 0.0
        return (self.score / self.total_questions) * 100

    def display_results(self) -> None:
        """
        Wyświetla wyniki.
        """
        percentage = self.get_percentage()
        print("\n" + "=" * 70)
        print("WYNIKI QUIZU PROGRAMOWANIA".center(70))
        print("=" * 70)
        print(f"\nWynik: {self.score}/{self.total_questions}")
        print(f"Procent: {percentage:.1f}%")

        if percentage >= 90:
            rating = "ŚWIETNIE! Już znasz podstawy! 🎓"
        elif percentage >= 75:
            rating = "DOBRZE! Kontynuuj naukę"
        elif percentage >= 60:
            rating = "ŚREDNIO - powtórz materiał"
        else:
            rating = "Potrzebujesz więcej nauki"

        print(f"Ocena: {rating}")
        print("=" * 70 + "\n")
