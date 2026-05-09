# Sekcja 02 - Chronological split and target EDA

- Zakres komorek w notebooku: `26` -> `38`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\labeled\train_labeled.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\labeled\val_labeled.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\labeled\test_labeled.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\labeled\split_summary.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\labeled\class_distribution_per_split.csv` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
### `split_summary.csv`
```text
split,rows,ratio_real,start,end
train,32376,0.6999913517253308,2021-01-01 00:00:00+00:00,2024-09-11 13:00:00+00:00
val,6937,0.1499827034506616,2024-09-11 14:00:00+00:00,2025-06-27 14:00:00+00:00
test,6939,0.1500259448240076,2025-06-27 15:00:00+00:00,2026-04-12 17:00:00+00:00
```
### `class_distribution_per_split.csv`
```text
split,target,count,ratio
train,0,8166,0.2522
train,1,15349,0.4741
train,2,8861,0.2737
val,0,1884,0.2716
val,1,3042,0.4385
val,2,2011,0.2899
test,0,1758,0.2534
test,1,3352,0.4831
test,2,1829,0.2636
```

## Komorka po komorce

### Cell 26 (markdown)
- Start: `## 02 - Chronological split and target EDA`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 27 (code)
- Start: `if 'timestamp' not in labeled_df.columns and labeled_df.index.name == 'timestamp':`
- Co robi kod: Normalizacja znacznika czasu (UTC), sortowanie i kontrola chronologii.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 28 (markdown)
- Start: `### 1. Chronological split train/val/test`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 29 (code)
- Start: `TRAIN_RATIO = 0.70`
- Co robi kod: Chronologiczny podzia? train/val/test i raport zakres?w czasowych.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 30 (markdown)
- Start: `### 2. Anti-leakage control (time)`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 31 (code)
- Start: `split_checks = pd.DataFrame({`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 32 (markdown)
- Start: `### 3. Target EDA: per split`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 33 (code)
- Start: `def class_distribution(df: pd.DataFrame, split_name: str) -> pd.DataFrame:`
- Co robi kod: Wyliczenie rozk?ad?w klas i proporcji klas per split.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler). Wynik wizualny: wykres PNG.

### Cell 34 (markdown)
- Start: `### 4. Split Timeline Visualization`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 35 (code)
- Start: `plt.figure(figsize=(14, 2.8))`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik wizualny: wykres PNG.

### Cell 36 (markdown)
- Start: `### 5. Data saving`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 37 (code)
- Start: `TRAIN_OUT = LABELED_PATH + 'train_labeled.csv'`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(CLASS_REPORT_OUT, index=False)`
  - `to_csv(SPLIT_SUMMARY_OUT, index=False)`
  - `to_csv(TEST_OUT, index=False)`
  - `to_csv(TRAIN_OUT, index=False)`
  - `to_csv(VAL_OUT, index=False)`

### Cell 38 (code)
- Start: `train_split_df = train_df.copy()`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
