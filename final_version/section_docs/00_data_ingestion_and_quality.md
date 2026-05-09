# Sekcja 00 - Data ingestion and quality

- Zakres komorek w notebooku: `2` -> `15`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\raw\ethusdt_1h.csv` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
- Brak dodatkowego raportu liczbowego przypisanego tylko do tej sekcji.

## Komorka po komorce

### Cell 2 (markdown)
- Start: `## 00 - Data ingestion and quality`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 3 (markdown)
- Start: `### 1. Raw data overview.`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 4 (code)
- Start: `raw_data["timestamp"] = pd.to_datetime(raw_data["timestamp"], errors="coerce", utc=True)`
- Co robi kod: Normalizacja znacznika czasu (UTC), sortowanie i kontrola chronologii.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 5 (markdown)
- Start: `### Data description:`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 6 (markdown)
- Start: `### Thoughts about raw data:`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 7 (markdown)
- Start: `### 2. Data quality checks`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 8 (code)
- Start: `quality_table = pd.DataFrame(`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 9 (markdown)
- Start: `### After thoughts:`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 10 (markdown)
- Start: `### 3. Timestamp checks`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 11 (code)
- Start: `ts = pd.to_datetime(raw_data["timestamp"], utc=True, errors="coerce")`
- Co robi kod: Normalizacja znacznika czasu (UTC), sortowanie i kontrola chronologii.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 12 (markdown)
- Start: `### Timestamp info`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 13 (markdown)
- Start: `### 4. Candle integrity checks`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 14 (code)
- Start: `num_df = raw_data.copy()`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 15 (markdown)
- Start: `### Candle thoughs:`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.
