class RAM:
    """
    Klasa symulująca pamięć RAM komputera.
    Zarządza alokacją i dealokacją pamięci.
    """

    def __init__(self, total_capacity: int):
        """
        Konstruktor klasy RAM.

        Args:
            total_capacity (int): Całkowita pojemność RAM-u w MB
        """
        self.total = total_capacity
        self.used = 0

    def allocate(self, amount: int) -> bool:
        """
        Próbuje przydzielić określoną ilość RAM-u.

        Args:
            amount (int): Ilość RAM-u do przydzielenia w MB

        Returns:
            bool: True jeśli alokacja się powiodła, False w przeciwnym razie
        """
        if self.used + amount <= self.total:
            self.used += amount
            return True
        return False

    def free(self, amount: int) -> None:
        """
        Zwalnia określoną ilość RAM-u.
        Zabezpiecza przed spadnięciem poniżej zera.

        Args:
            amount (int): Ilość RAM-u do zwolnienia w MB
        """
        self.used = max(0, self.used - amount)

    def get_status(self) -> str:
        """
        Zwraca string z informacją o stanie pamięci.

        Returns:
            str: Sformatowany opis stanu RAM-u
        """
        return f"{self.used}MB / {self.total}MB"


class CPU:
    """
    Klasa symulująca procesor komputera.
    """

    def __init__(self, model: str, base_clock: float):
        """
        Konstruktor klasy CPU.

        Args:
            model (str): Model procesora (np. "Intel Core i7")
            base_clock (float): Częstotliwość taktowania w GHz
        """
        self.model = model
        self.base_clock = base_clock
        self.temperature = 40.0  # Temperatura w stopniach Celsjusza

    def get_status(self) -> str:
        """
        Zwraca string z informacją o stanie procesora.

        Returns:
            str: Sformatowany opis stanu CPU
        """
        return f"{self.model} @ {self.base_clock}GHz ({self.temperature}°C)"


class VirtualMachine:
    """
    Klasa reprezentująca wirtualny komputer.
    Implementuje kompozycję: posiada RAM i CPU jako części składowe.
    """

    def __init__(self, cpu_model: str, cpu_clock: float, ram_capacity: int):
        """
        Konstruktor wirtualnego komputera.

        Args:
            cpu_model (str): Model procesora
            cpu_clock (float): Częstotliwość taktowania CPU w GHz
            ram_capacity (int): Całkowita pojemność RAM-u w MB
        """
        self.ram = RAM(ram_capacity)
        self.cpu = CPU(cpu_model, cpu_clock)
        self.power_status = False

    def get_system_status(self) -> str:
        """
        Generuje kompletny raport o stanie systemu.
        Pobiera dane ze wszystkich komponentów i tworzy sformatowany string.

        Returns:
            str: Pełny status systemu z informacjami o CPU i RAM-ie
        """
        cpu_status = self.cpu.get_status()
        ram_status = self.ram.get_status()
        return f"[SYSTEM STATUS] Procesor: {cpu_status} | RAM: {ram_status}"
