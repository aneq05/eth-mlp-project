# Sekcja 01 - Cleaning and target definition

- Zakres komorek w notebooku: `16` -> `25`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\clean\eth_clean.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\labeled\eth_labeled.csv` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
- Brak dodatkowego raportu liczbowego przypisanego tylko do tej sekcji.

## Komorka po komorce

### Cell 16 (markdown)
- Start: `## 01 - Cleaning and target definition`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 17 (markdown)
- Start: `### 1. Cleaning`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 18 (code)
- Start: `def clean_ohlcv(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:`
- Co robi kod: Definicja funkcji czyszczenia OHLCV: usuwanie brak?w, duplikat?w i niesp?jnych ?wiec.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 19 (markdown)
- Start: `### Target definition (3 classes)`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 20 (code)
- Start: `HORIZON = 6`
- Co robi kod: Definicja targetu klasyfikacyjnego 3-klasowego (sell/hold/buy) na bazie future_return.
- Jak to jest wyliczane:
  - future_return = close(t+h) / close(t) - 1
  - target=0 gdy future_return < -threshold; target=1 w przedziale; target=2 gdy > threshold
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 21 (markdown)
- Start: `### 3. Class distribution & histogram `future_return``
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 22 (code)
- Start: `class_counts = labeled_df["target"].value_counts().sort_index()`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler). Wynik wizualny: wykres PNG.

### Cell 23 (markdown)
- Start: `### After thoughts:`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 24 (markdown)
- Start: `### 4. Data saving`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 25 (code)
- Start: `os.makedirs(CLEAN_PATH, exist_ok=True)`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(CLEAN_FILE, index=False)`
  - `to_csv(LABELED_FILE, index=False)`
