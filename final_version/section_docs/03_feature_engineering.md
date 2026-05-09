# Sekcja 03 - Feature engineering

- Zakres komorek w notebooku: `39` -> `57`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\features_full.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\train_features.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\val_features.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\test_features.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\feature_columns.csv` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
- Brak dodatkowego raportu liczbowego przypisanego tylko do tej sekcji.

## Komorka po komorce

### Cell 39 (markdown)
- Start: `## 03 - Feature engineering`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 40 (markdown)
- Start: `### 1. Timestamp checks`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 41 (code)
- Start: `for name, df in [('labeled', labeled_df), ('train', train_split_df), ('val', val_split_df), ('test', test_split_df)]:`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 42 (markdown)
- Start: `### 2. Feature engineering function definitions`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 43 (markdown)
- Start: `| Nazwa cechy / grupa | Z czego powstaje (jak liczona) | Co wnosi do modelu |`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 44 (markdown)
- Start: `- RSI = Relative Strength Index`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 45 (code)
- Start: `# Oblicza wskaźnik RSI na podstawie średnich wykładniczych wzrostów i spadków ceny z zadanego okresu.`
- Co robi kod: Definicja funkcji feature engineering (cechy techniczne, momentum, zmienno??, lags, rolling).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 46 (markdown)
- Start: `### 3. Feature construction and leakage control`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 47 (code)
- Start: `work_df = labeled_df.copy()`
- Co robi kod: Budowa pe?nego zbioru cech na danych z targetem oraz kontrola leakage.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 48 (markdown)
- Start: `### 4. NaN/Inf report after feature engineering`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 49 (code)
- Start: `inf_report = (`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 50 (markdown)
- Start: `### Cleaning data thoughts:`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 51 (markdown)
- Start: `### 5. Assignment to existing splits from part 02`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 52 (code)
- Start: `train_ts = set(train_split_df['timestamp'])`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 53 (markdown)
- Start: `### 6. Quick feature report`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 54 (code)
- Start: `model_feature_cols = [c for c in train_features.columns if c not in ['timestamp', 'target', 'future_return']]`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 55 (markdown)
- Start: `### 7. Saving artifacts`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 56 (code)
- Start: `FEATURES_FULL_OUT = PROCESSED_PATH + 'features_full.csv'`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(FEATURES_FULL_OUT, index=False)`
  - `to_csv(FEATURE_LIST_OUT, index=False)`
  - `to_csv(TEST_FEATURES_OUT, index=False)`
  - `to_csv(TRAIN_FEATURES_OUT, index=False)`
  - `to_csv(VAL_FEATURES_OUT, index=False)`

### Cell 57 (code)
- Start: `train_df = train_features.copy()`
- Co robi kod: Normalizacja znacznika czasu (UTC), sortowanie i kontrola chronologii.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
