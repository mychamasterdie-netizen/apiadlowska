Projekt sem_lo2 - rozszerzona wersja (poziom 6)

Instrukcja uruchomienia:

1. Przejdź do katalogu repozytorium i zgałąź sem_lo2:
   git fetch origin
   git checkout sem_lo2

2. (opcjonalnie) Stwórz i aktywuj wirtualne środowisko
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate   # Windows

3. Zainstaluj zależności:
   pip install -r sem_lo2/requirements.txt

4. Wygeneruj dane startowe:
   python -m sem_lo2.seed_data

5. Uruchom program:
   python -m sem_lo2.main

Użytkownicy startowi:
 - admin / adminpass (rola: admin)
 - seller / sellerpass (rola: seller)
 - purchaser / purchaserpass (rola: purchaser)

Uwagi:
- Wszystkie dane trzymane są w sem_lo2/data/*.json
- Raport tekstowy generowany jest jako company_report.txt w katalogu gdzie uruchomisz program
