# Dziennik szczeg??owy: 00_09_combined_pipeline_demo.ipynb

Dokument opisuje **ka?d? kom?rk?** notebooka: co robi, dlaczego zosta?a dodana i jaki da?a wynik.

## Najwa?niejsze wyniki globalne (z artefakt?w po pe?nym runie)

- Split 70/15/15 zosta? zachowany:
  - train: 32376 wierszy (0.7000), 2021-01-01 00:00:00+00:00 -> 2024-09-11 13:00:00+00:00
  - val: 6937 wierszy (0.1500), 2024-09-11 14:00:00+00:00 -> 2025-06-27 14:00:00+00:00
  - test: 6939 wierszy (0.1500), 2025-06-27 15:00:00+00:00 -> 2026-04-12 17:00:00+00:00
- Rozk?ad klas per split:
  - train | klasa 0: 8166 (0.2522)
  - train | klasa 1: 15349 (0.4741)
  - train | klasa 2: 8861 (0.2737)
  - val | klasa 0: 1884 (0.2716)
  - val | klasa 1: 3042 (0.4385)
  - val | klasa 2: 2011 (0.2899)
  - test | klasa 0: 1758 (0.2534)
  - test | klasa 1: 3352 (0.4831)
  - test | klasa 2: 1829 (0.2636)
- Selekcja cech: start=96, usuni?te corr=37, usuni?te vif=21, final=38.
- Skalowanie: robust (auto=robust), outlier_ratio=0.0552, cechy=38.
- Optuna: best_trial=74, best_CV_f1_macro=0.397505, trials_total=95, complete=14.
- Top-3 ensemble (test):
  - rank 1 (trial 74): f1_macro=0.378487, bal_acc=0.392342, acc=0.404813
  - rank 2 (trial 21): f1_macro=0.357572, bal_acc=0.386442, acc=0.362588
  - rank 3 (trial 72): f1_macro=0.371928, bal_acc=0.402023, acc=0.395590
- Testy statystyczne: wszystkie 3 pary maj? istotno?? McNemara po korekcie Holma.

## Cell 000 (markdown)
- **Tre??/Nag??wek:** `## Mapping to Lab6/7 Points (1-10)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 001 (code)
- **Pierwsza linia kodu:** `import os`
- **Co robi:** Importuje biblioteki potrzebne do ca?ego pipeline'u: przetwarzanie danych, wizualizacje, PyTorch, Optuna i testy statystyczne.
- **Dlaczego:** To centralny blok zale?no?ci; dzi?ki temu ka?da kolejna kom?rka korzysta z jednego, sp?jnego ?rodowiska wykonania.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 002 (code)
- **Pierwsza linia kodu:** `DATA_PATH = '../data/raw/ethusdt_1h.csv'`
- **Co robi:** Inicjalizuje ?cie?ki projektu (`data`, `reports`, `logs`, `checkpoints`), tworzy katalogi i ?aduje surowy CSV ETH do `raw_data`.
- **Dlaczego:** To uruchamia pipeline w trybie end-to-end w jednym notebooku i eliminuje konieczno?? r?cznego przygotowywania folder?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 003 (markdown)
- **Tre??/Nag??wek:** `## 00 - Data ingestion and quality`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 004 (markdown)
- **Tre??/Nag??wek:** `### 1. Raw data overview.`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 005 (code)
- **Pierwsza linia kodu:** `raw_data["timestamp"] = pd.to_datetime(raw_data["timestamp"], errors="coerce", utc=True)`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `raw_data["timestamp"] = pd.to_datetime(raw_data["timestamp"], errors="coerce", utc=True)`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 006 (markdown)
- **Tre??/Nag??wek:** `### Data description:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 007 (markdown)
- **Tre??/Nag??wek:** `### Thoughts about raw data:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 008 (markdown)
- **Tre??/Nag??wek:** `### 2. Data quality checks`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 009 (code)
- **Pierwsza linia kodu:** `quality_table = pd.DataFrame(`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `quality_table = pd.DataFrame(`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 010 (markdown)
- **Tre??/Nag??wek:** `### After thoughts:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 011 (markdown)
- **Tre??/Nag??wek:** `### 3. Timestamp checks`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 012 (code)
- **Pierwsza linia kodu:** `ts = pd.to_datetime(raw_data["timestamp"], utc=True, errors="coerce")`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `ts = pd.to_datetime(raw_data["timestamp"], utc=True, errors="coerce")`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 013 (markdown)
- **Tre??/Nag??wek:** `### Timestamp info`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 014 (markdown)
- **Tre??/Nag??wek:** `### 4. Candle integrity checks`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 015 (code)
- **Pierwsza linia kodu:** `num_df = raw_data.copy()`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `num_df = raw_data.copy()`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 016 (markdown)
- **Tre??/Nag??wek:** `### Candle thoughs:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 017 (markdown)
- **Tre??/Nag??wek:** `### Summary of notebook:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 018 (markdown)
- **Tre??/Nag??wek:** `## 01 - Cleaning and target definition`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 019 (markdown)
- **Tre??/Nag??wek:** `## Cleaning`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 020 (code)
- **Pierwsza linia kodu:** `def clean_ohlcv(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:`
- **Co robi:** Definiuje i uruchamia funkcj? czyszczenia OHLCV: walidacja/parsowanie czasu, usuwanie duplikat?w i b??dnych ?wiec, konwersje typ?w, porz?dkowanie indeksu czasowego.
- **Dlaczego:** Spe?nia punkt 1 instrukcji i przygotowuje sp?jne dane do budowy targetu i cech.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 021 (markdown)
- **Tre??/Nag??wek:** `### Thoughts after cleaning`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 022 (markdown)
- **Tre??/Nag??wek:** `## Target definition (3 classes)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 023 (markdown)
- **Tre??/Nag??wek:** `### Wnioski po definicji targetu`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 024 (code)
- **Pierwsza linia kodu:** `HORIZON = 6`
- **Co robi:** Definiuje wieloklasowy target (`0/1/2`) na bazie `future_return` dla zadanego horyzontu/progu i tworzy `labeled_df`.
- **Dlaczego:** Formalizuje problem klasyfikacyjny sieci neuronowej na sygna?y tradingowe.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 025 (markdown)
- **Tre??/Nag??wek:** `### Thoughts after target definition:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 026 (markdown)
- **Tre??/Nag??wek:** `## Class distribution & histogram `future_return``
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 027 (code)
- **Pierwsza linia kodu:** `class_counts = labeled_df["target"].value_counts().sort_index()`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `class_counts = labeled_df["target"].value_counts().sort_index()`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler). Wygenerowano wykres/obraz (PNG).

## Cell 028 (markdown)
- **Tre??/Nag??wek:** `### After thoughts:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 029 (markdown)
- **Tre??/Nag??wek:** `### Data saving`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 030 (code)
- **Pierwsza linia kodu:** `os.makedirs(CLEAN_PATH, exist_ok=True)`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `os.makedirs(CLEAN_PATH, exist_ok=True)`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 031 (markdown)
- **Tre??/Nag??wek:** `### Thoughts at the end of this notebook:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 032 (markdown)
- **Tre??/Nag??wek:** `## 02 - Chronological split and target EDA`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 033 (code)
- **Pierwsza linia kodu:** `if 'timestamp' not in labeled_df.columns and labeled_df.index.name == 'timestamp':`
- **Co robi:** Normalizuje struktur? `labeled_df` (je?li `timestamp` jest w indeksie, resetuje indeks), nast?pnie czy?ci i sortuje po czasie.
- **Dlaczego:** Zapobiega b??dom typu `KeyError: timestamp` i gwarantuje poprawny input do splitu czasowego.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 034 (markdown)
- **Tre??/Nag??wek:** `### Chronological split train/val/test`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 035 (code)
- **Pierwsza linia kodu:** `TRAIN_RATIO = 0.70`
- **Co robi:** Dzieli zbi?r chronologicznie na train/val/test i raportuje realne proporcje oraz zakresy czasu.
- **Dlaczego:** Chronologiczny split jest wymagany w time-series i chroni przed leakage.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).
- **Wynik liczbowy splitu:**
  - train: rows=32376, ratio=0.699991, start=2021-01-01 00:00:00+00:00, end=2024-09-11 13:00:00+00:00
  - val: rows=6937, ratio=0.149983, start=2024-09-11 14:00:00+00:00, end=2025-06-27 14:00:00+00:00
  - test: rows=6939, ratio=0.150026, start=2025-06-27 15:00:00+00:00, end=2026-04-12 17:00:00+00:00

## Cell 036 (markdown)
- **Tre??/Nag??wek:** `### Anti-leakage control (time)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 037 (code)
- **Pierwsza linia kodu:** `split_checks = pd.DataFrame({`
- **Co robi:** Tworzy raport anti-leakage: sprawdza, czy zakresy czasowe split?w nie nak?adaj? si? i czy kolejno?? jest poprawna.
- **Dlaczego:** To walidacja metodologiczna poprawno?ci podzia?u danych.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 038 (markdown)
- **Tre??/Nag??wek:** `### Target EDA: per split`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 039 (code)
- **Pierwsza linia kodu:** `def class_distribution(df: pd.DataFrame, split_name: str) -> pd.DataFrame:`
- **Co robi:** Liczy rozk?ad klas per split i wizualizuje proporcje klas na wykresie s?upkowym.
- **Dlaczego:** Pozwala oceni? niezbalansowanie klas i uzasadnia u?ycie wag klas/samplingu.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler). Wygenerowano wykres/obraz (PNG).
- **Wynik liczbowy rozk?adu klas:**
  - train | class 0: count=8166, ratio=0.2522
  - train | class 1: count=15349, ratio=0.4741
  - train | class 2: count=8861, ratio=0.2737
  - val | class 0: count=1884, ratio=0.2716
  - val | class 1: count=3042, ratio=0.4385
  - val | class 2: count=2011, ratio=0.2899
  - test | class 0: count=1758, ratio=0.2534
  - test | class 1: count=3352, ratio=0.4831
  - test | class 2: count=1829, ratio=0.2636

## Cell 040 (markdown)
- **Tre??/Nag??wek:** `### Split Timeline Visualization`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 041 (code)
- **Pierwsza linia kodu:** `plt.figure(figsize=(14, 2.8))`
- **Co robi:** Rysuje o? czasu split?w (train/val/test) dla kontroli chronologii i ci?g?o?ci podzia?u.
- **Dlaczego:** Wizualne potwierdzenie anti-leakage i poprawnego podzia?u czasowego.
- **Wynik z wykonania:** Wygenerowano wykres/obraz (PNG).

## Cell 042 (markdown)
- **Tre??/Nag??wek:** `### Data saving`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 043 (code)
- **Pierwsza linia kodu:** `TRAIN_OUT = LABELED_PATH + 'train_labeled.csv'`
- **Co robi:** Zapisuje splity `train_labeled.csv`, `val_labeled.csv`, `test_labeled.csv` oraz raporty splitu i rozk?adu klas.
- **Dlaczego:** Utrwala etap 02 jako artefakty wej?ciowe dla dalszych sekcji.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 044 (code)
- **Pierwsza linia kodu:** `train_split_df = train_df.copy()`
- **Co robi:** Tworzy aliasy zmiennych split?w (`train_split_df` itd.) pod kolejne sekcje feature engineering.
- **Dlaczego:** Ujednolica nazewnictwo mi?dzy etapami i zmniejsza ryzyko pomy?ek referencji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 045 (markdown)
- **Tre??/Nag??wek:** `## 03 - Feature engineering`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 046 (markdown)
- **Tre??/Nag??wek:** `### Minimal timestamp preparation`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 047 (code)
- **Pierwsza linia kodu:** `# Minimal preparation: parse timestamp and keep chronological order.`
- **Co robi:** Parsuje `timestamp` we wszystkich tabelach wej?ciowych etapu cech i tworzy podsumowanie zakres?w czasowych.
- **Dlaczego:** Przygotowuje dane do bezpiecznego feature engineeringu bez niesp?jno?ci czasowych.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 048 (markdown)
- **Tre??/Nag??wek:** `### Feature engineering function definitions`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 049 (markdown)
- **Tre??/Nag??wek:** `### Opis tworzonych cech`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 050 (markdown)
- **Tre??/Nag??wek:** `- RSI = Relative Strength Index`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 051 (code)
- **Pierwsza linia kodu:** `# Oblicza wskaźnik RSI na podstawie średnich wykładniczych wzrostów i spadków ceny z zadanego okresu.`
- **Co robi:** Definiuje funkcje in?ynierii cech technicznych (m.in. RSI, rolling, lag, wska?niki zmienno?ci i dynamiki ceny/volumenu).
- **Dlaczego:** Rozbudowuje przestrze? cech dla modelu MLP, aby wy?apywa? z?o?one wzorce rynkowe.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 052 (markdown)
- **Tre??/Nag??wek:** `### Feature construction and leakage control`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 053 (code)
- **Pierwsza linia kodu:** `work_df = labeled_df.copy()`
- **Co robi:** Buduje pe?ny zbi?r cech na danych czasowych, kontroluje potencjalny leakage i tworzy pr?bk? cech do inspekcji.
- **Dlaczego:** To etap przej?cia od etykiet do finalnych danych modelowych.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 054 (markdown)
- **Tre??/Nag??wek:** `### NaN/Inf report after lags/rolling and cleaning`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 055 (code)
- **Pierwsza linia kodu:** `inf_report = (`
- **Co robi:** Raportuje NaN/Inf po operacjach rolling/lag, czy?ci niesko?czono?ci i ko?cowe braki.
- **Dlaczego:** Chroni kolejne etapy przed b??dami numerycznymi i niestabilno?ci? treningu.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 056 (markdown)
- **Tre??/Nag??wek:** `### Cleaning data thoughts:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 057 (markdown)
- **Tre??/Nag??wek:** `### Assignment to existing splits from notebook 02`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 058 (code)
- **Pierwsza linia kodu:** `train_ts = set(train_split_df['timestamp'])`
- **Co robi:** Przypisuje wiersze cech do split?w po znacznikach czasu i sprawdza brak overlap?w mi?dzy splitami.
- **Dlaczego:** Zapewnia sp?jno?? splitu po feature engineeringu.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 059 (markdown)
- **Tre??/Nag??wek:** `### Quick feature report`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 060 (code)
- **Pierwsza linia kodu:** `model_feature_cols = [c for c in train_features.columns if c not in ['timestamp', 'target', 'future_return']]`
- **Co robi:** Tworzy szybki raport liczby cech, liczby wierszy i statystyk opisowych po in?ynierii cech.
- **Dlaczego:** Daje kontrol? jako?ci przed filtracj? korelacji/VIF.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 061 (markdown)
- **Tre??/Nag??wek:** `### Saving artifacts`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 062 (code)
- **Pierwsza linia kodu:** `FEATURES_FULL_OUT = PROCESSED_PATH + 'features_full.csv'`
- **Co robi:** Zapisuje pe?ne cechy i splity cechowe oraz list? kolumn cech do plik?w w `data/processed`.
- **Dlaczego:** Umo?liwia odtwarzalno?? i wykorzystanie tych samych cech w kolejnych etapach.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 063 (markdown)
- **Tre??/Nag??wek:** `### Final thoughts:`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 064 (code)
- **Pierwsza linia kodu:** `train_df = train_features.copy()`
- **Co robi:** Przepina aktywne `train_df/val_df/test_df` na wersje cechowe po notebooku 03.
- **Dlaczego:** Przygotowuje wej?cie do EDA wielokolinearno?ci z notebooka 04.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 065 (markdown)
- **Tre??/Nag??wek:** `## 04 - Train/Val EDA and multicollinearity`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 066 (markdown)
- **Tre??/Nag??wek:** `### Histograms and pairplot (train+val only)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 067 (code)
- **Pierwsza linia kodu:** `# due to a large number of features (96) only a few histograms are displayed`
- **Co robi:** Rysuje histogramy/pairplot wybranych cech train+val do jako?ciowej oceny rozk?ad?w.
- **Dlaczego:** To element EDA wymagany w punkcie 2 instrukcji.
- **Wynik z wykonania:** Wygenerowano wykres/obraz (PNG).

## Cell 068 (markdown)
- **Tre??/Nag??wek:** `#### Wnioski`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 069 (markdown)
- **Tre??/Nag??wek:** `### Feature covariance and high-correlation filter`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 070 (code)
- **Pierwsza linia kodu:** `def drop_constant_features(df: pd.DataFrame, min_unique: int = 2):`
- **Co robi:** Definiuje i uruchamia filtr cech sta?ych oraz silnie skorelowanych, tworzy macierz korelacji i heatmap?.
- **Dlaczego:** Redukuje redundancj? i przygotowuje dane do VIF.
- **Wynik z wykonania:** Wygenerowano wykres/obraz (PNG). Wygenerowano tabel?/element HTML (Styler).

## Cell 071 (markdown)
- **Tre??/Nag??wek:** `#### Wnioski`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 072 (markdown)
- **Tre??/Nag??wek:** `### VIF analysis `
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 073 (code)
- **Pierwsza linia kodu:** `def reduce_vif_features(`
- **Co robi:** Definiuje i wykonuje iteracyjne usuwanie cech o wysokim VIF, generuj?c tabel? VIF i list? cech usuni?tych.
- **Dlaczego:** Usuwa wielokolinearno??, co stabilizuje model i interpretacj?.
- **Wynik z wykonania:** Strumie? tekstu/log?w: c:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\venv\Lib\site-packages\statsmodels\stats\outliers_influence.py:197: RuntimeWarning: divide by zero encountered in scalar divide |   vif = 1. / (1. - r_squared_i) Wygenerowano tabel?/element HTML (Styler).

## Cell 074 (markdown)
- **Tre??/Nag??wek:** `### Feature-target relation (train+val)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 075 (code)
- **Pierwsza linia kodu:** `X_mi = X_no_corr[kept_after_vif].copy()`
- **Co robi:** Liczy mutual information cecha-target i buduje ranking top cech informacyjnych.
- **Dlaczego:** Potwierdza, ?e po filtrach zosta?y cechy nios?ce sygna? predykcyjny.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler). Wygenerowano wykres/obraz (PNG).

## Cell 076 (markdown)
- **Tre??/Nag??wek:** `#### Wnioski`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 077 (markdown)
- **Tre??/Nag??wek:** `### Final selected feature set & apply to train/val/test`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 078 (code)
- **Pierwsza linia kodu:** `selected_features = kept_after_vif.copy()`
- **Co robi:** Buduje finalny zestaw cech oraz finalne ramki `train_selected`, `val_selected`, `test_selected`.
- **Dlaczego:** To bezpo?rednie wej?cie do skalingu i modelowania.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).
- **Wynik liczbowy selekcji:** initial=96, dropped_corr=37, dropped_vif=21, final=38.

## Cell 079 (markdown)
- **Tre??/Nag??wek:** `#### Wnioski`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 080 (markdown)
- **Tre??/Nag??wek:** `### Saving artifacts`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 081 (code)
- **Pierwsza linia kodu:** `TRAIN_SELECTED_OUT = PROCESSED_PATH + 'train_selected.csv'`
- **Co robi:** Zapisuje artefakty selekcji cech: finalne splity, list? cech, raport selekcji, list? cech odrzuconych, raport MI i tabel? VIF.
- **Dlaczego:** Domyka punkt 2 instrukcji i zostawia ?lad audytowy dla obrony projektu.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 082 (code)
- **Pierwsza linia kodu:** `train_df = train_selected.copy()`
- **Co robi:** Wykonuje krok opisany przez kod rozpoczynaj?cy si? od: `train_df = train_selected.copy()`.
- **Dlaczego:** Kom?rka jest cz??ci? sekwencyjnego pipeline'u i przekazuje dane/ustawienia do kolejnych etap?w.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 083 (markdown)
- **Tre??/Nag??wek:** `## 05 - Scaling and DataLoaders`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 084 (markdown)
- **Tre??/Nag??wek:** `### Building X/y and choosing scaler`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 085 (code)
- **Pierwsza linia kodu:** `X_train = train_df[selected_features].to_numpy(dtype=np.float32)`
- **Co robi:** Tworzy macierze X/y, sprawdza finito??, estymuje outlier ratio i wybiera typ skalera (auto).
- **Dlaczego:** Przygotowuje dane numeryczne do modelu i uzasadnia wyb?r transformacji skali.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 086 (markdown)
- **Tre??/Nag??wek:** `### Anti-leakage scaling`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 087 (code)
- **Pierwsza linia kodu:** `# Fit scaler only on train, then transform val/test.`
- **Co robi:** Dopasowuje scaler tylko na train i transformuje val/test; tworzy raport skali.
- **Dlaczego:** To poprawna procedura anti-leakage dla danych czasowych.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 088 (markdown)
- **Tre??/Nag??wek:** `### Class imbalance setup`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 089 (code)
- **Pierwsza linia kodu:** `class_counts = np.bincount(y_train)`
- **Co robi:** Wyznacza liczno?ci klas i oblicza wagi klas do funkcji kosztu.
- **Dlaczego:** Kompensuje niezbalansowany target w treningu sieci.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 090 (markdown)
- **Tre??/Nag??wek:** `### Dataset and DataLoader`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 091 (code)
- **Pierwsza linia kodu:** `class TabularDataset(Dataset):`
- **Co robi:** Definiuje dataset tablicowy i DataLoadery; opcjonalnie umo?liwia samplowanie wa?one klasowo.
- **Dlaczego:** Spina etap przygotowania danych z API treningowym PyTorch.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 092 (markdown)
- **Tre??/Nag??wek:** `### Sanity check batches`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 093 (code)
- **Pierwsza linia kodu:** `x_batch, y_batch = next(iter(train_loader))`
- **Co robi:** Wykonuje sanity-check pojedynczego batcha (kszta?ty i zgodno?? etykiet).
- **Dlaczego:** Szybko wychwytuje ewentualne b??dy w konstrukcji DataLoadera przed kosztownym treningiem.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 094 (markdown)
- **Tre??/Nag??wek:** `### Save preprocessing artifacts`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 095 (code)
- **Pierwsza linia kodu:** `SCALER_OUT = PROCESSED_PATH + 'selected_scaler.pkl'`
- **Co robi:** Zapisuje scaler, wagi klas, tablice skalowane i podsumowanie preprocessingu do plik?w.
- **Dlaczego:** Daje pe?n? reprodukowalno?? etapu 05 oraz mo?liwo?? szybkiego wznowienia kolejnych etap?w.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).
- **Wynik liczbowy skalowania:** scaler=robust, outlier_ratio=0.055183, train_shape=[32326, 38], val_shape=[6937, 38], test_shape=[6939, 38].
- **Wagi klas:** {'0': 1.3216402960055604, '1': 0.7030295121898176, '2': 1.2181023438088778}

## Cell 096 (markdown)
- **Tre??/Nag??wek:** `## 06 - MLP training core (task points 3-6)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 097 (markdown)
- **Tre??/Nag??wek:** `### Reproducibility and training config`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 098 (code)
- **Pierwsza linia kodu:** `def set_seed(seed: int = 42):`
- **Co robi:** Ustawia seedy losowo?ci i tworzy konfiguracje treningu/modelu baseline MLP.
- **Dlaczego:** Kontroluje powtarzalno?? i parametry eksperymentu baseline.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 099 (markdown)
- **Tre??/Nag??wek:** `### Configurable MLP architecture (Task point 3)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 100 (code)
- **Pierwsza linia kodu:** `def build_activation(name: str) -> nn.Module:`
- **Co robi:** Definiuje aktywacje i konfigurowaln? architektur? MLP (warstwy ukryte, BN, dropout).
- **Dlaczego:** Realizuje punkt 3 instrukcji (architektura MLP).
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 101 (markdown)
- **Tre??/Nag??wek:** `### Train one epoch with gradient clipping (Task point 4)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 102 (code)
- **Pierwsza linia kodu:** `def train_one_epoch(`
- **Co robi:** Definiuje trening jednej epoki z gradient clippingiem.
- **Dlaczego:** Realizuje punkt 4 instrukcji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 103 (markdown)
- **Tre??/Nag??wek:** `### Validation at end of epoch (Task point 5)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 104 (code)
- **Pierwsza linia kodu:** `@torch.no_grad()`
- **Co robi:** Definiuje walidacj? jednej epoki i metryki klasyfikacyjne.
- **Dlaczego:** Realizuje punkt 5 instrukcji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 105 (markdown)
- **Tre??/Nag??wek:** `### Full training loop (Task point 6)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 106 (code)
- **Pierwsza linia kodu:** `def _is_improvement(curr: float, best: float, mode: str) -> bool:`
- **Co robi:** Definiuje pe?ny loop treningu: epoch train+val, early stopping, zapis najlepszego checkpointu i logowanie do CSV/TensorBoard.
- **Dlaczego:** Realizuje punkt 6 instrukcji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 107 (markdown)
- **Tre??/Nag??wek:** `### Run baseline training`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 108 (code)
- **Pierwsza linia kodu:** `device = torch.device(TRAINING_CONFIG['device'])`
- **Co robi:** Instancjonuje model baseline, strat? z wagami klas, optimizer i uruchamia pe?ny trening `fit_model`.
- **Dlaczego:** To wykonawcza kom?rka baseline MLP, z kt?rej pochodz? checkpoint i historia treningu.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 109 (markdown)
- **Tre??/Nag??wek:** `### Plot training curves and final validation summary`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 110 (code)
- **Pierwsza linia kodu:** `plt.figure(figsize=(12, 4))`
- **Co robi:** Rysuje krzywe treningowe i wy?wietla ko?cowe podsumowanie metryk walidacyjnych baseline.
- **Dlaczego:** Daje szybki obraz konwergencji i jako?ci baseline.
- **Wynik z wykonania:** Wygenerowano wykres/obraz (PNG). Wygenerowano tabel?/element HTML (Styler).

## Cell 111 (markdown)
- **Tre??/Nag??wek:** `## Shared helpers for Optuna and Top-3`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 112 (code)
- **Pierwsza linia kodu:** `def build_optimizer(name: str, model: nn.Module, lr: float, weight_decay: float):`
- **Co robi:** Definiuje helpery wsp??dzielone przez etapy 07-08: optimizer, scaler, class weights, ewaluacj? i parser top-3.
- **Dlaczego:** Redukuje duplikacj? i zapewnia sp?jno?? implementacji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 113 (code)
- **Pierwsza linia kodu:** `train_val_df = pd.concat([train_selected, val_selected], axis=0).sort_values('timestamp').reset_index(drop=True)`
- **Co robi:** Przygotowuje macierze train+val do objective Optuny.
- **Dlaczego:** To wej?cie do walidacji 5-fold w etapie HPO.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 114 (markdown)
- **Tre??/Nag??wek:** `## 07 - Optuna 5-fold CV (task point 7)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 115 (markdown)
- **Tre??/Nag??wek:** `## 2. Optuna config`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 116 (code)
- **Pierwsza linia kodu:** `DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`
- **Co robi:** Ustawia konfiguracj? Optuny: device, liczba fold?w, triali, epok, patience, storage i pruner.
- **Dlaczego:** Definiuje warunki eksperymentu HPO.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 117 (markdown)
- **Tre??/Nag??wek:** `## 3. Hyperparameter search space`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 118 (code)
- **Pierwsza linia kodu:** `def suggest_params(trial: optuna.Trial) -> dict:`
- **Co robi:** Definiuje przestrze? hiperparametr?w przeszukiwan? przez Optun?.
- **Dlaczego:** To zakres decyzji, kt?re maj? wp?yw na finaln? jako?? modelu.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 119 (markdown)
- **Tre??/Nag??wek:** `## 4. Objective with 5-fold TimeSeriesSplit (Task point 7)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 120 (code)
- **Pierwsza linia kodu:** `def objective(trial: optuna.Trial) -> float:`
- **Co robi:** Dopasowuje scaler tylko na train i transformuje val/test; tworzy raport skali.
- **Dlaczego:** To poprawna procedura anti-leakage dla danych czasowych.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 121 (markdown)
- **Tre??/Nag??wek:** `## 5. Run optimization`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 122 (code)
- **Pierwsza linia kodu:** `study = optuna.create_study(`
- **Co robi:** Tworzy/wznawia study i uruchamia `study.optimize`.
- **Dlaczego:** Uruchamia w?a?ciwe strojenie hiperparametr?w.
- **Wynik z wykonania:** Strumie? tekstu/log?w: [32m[I 2026-05-09 12:01:22,805][0m Using an existing study with name 'eth_mlp_optimization' instead of creating a new one.[0m | [32m[I 2026-05-09 12:02:31,072][0m Trial 65 pruned. [0m | [32m[I 2026-05-09 12:05:03,754][0m Trial 66 pruned. [0m | [32m[I 2026-05-09 12:05:40 Wygenerowano tabel?/element HTML (Styler).
- **Wynik liczbowy Optuna:** best_trial=74, best_value=0.397505, n_trials_total=95, n_trials_complete=14.

## Cell 123 (markdown)
- **Tre??/Nag??wek:** `## 6. Save summary and top-3 trials`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 124 (code)
- **Pierwsza linia kodu:** `trials_df = study.trials_dataframe(attrs=('number', 'value', 'state', 'params'))`
- **Co robi:** Zapisuje wyniki triali, wyci?ga top-3 i zapisuje podsumowania JSON/CSV.
- **Dlaczego:** Przygotowuje dane wej?ciowe dla treningu top-3 w etapie 08.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 125 (markdown)
- **Tre??/Nag??wek:** `## 7. Optional Optuna visual diagnostics`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 126 (code)
- **Pierwsza linia kodu:** `%pip install plotly`
- **Co robi:** Instaluje `plotly` (i sprawdza dost?pno?? pakiet?w) do renderowania wykres?w Optuny.
- **Dlaczego:** Bez tego wizualizacje `optuna.visualization` nie renderuj? si? poprawnie.
- **Wynik z wykonania:** Strumie? tekstu/log?w: Requirement already satisfied: plotly in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-project\venv\lib\site-packages (6.7.0) | Requirement already satisfied: narwhals>=1.15.1 in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-project\venv\lib\site-packages (from plotly Strumie? tekstu/log?w: [notice] A new release of pip is available: 24.2 -> 26.1.1 | [notice] To update, run: python.exe -m pip install --upgrade pip Strumie? tekstu/log?w: Requirement already satisfied: optuna in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-project\venv\lib\site-packages (4.8.0) | Requirement already satisfied: alembic>=1.5.0 in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-project\venv\lib\site-packages (from optuna) 

## Cell 127 (code)
- **Pierwsza linia kodu:** `fig1 = vis.plot_optimization_history(study)`
- **Co robi:** Rysuje wykres historii optymalizacji i wa?no?ci hiperparametr?w.
- **Dlaczego:** Umo?liwia interpretacj? procesu HPO, a nie tylko ko?cowego triala.
- **Wynik z wykonania:** Output techniczny obecny (wizualizacja/tabela), bez dodatkowego tekstu jawnego.

## Cell 128 (code)
- **Pierwsza linia kodu:** `top3_df = pd.read_csv(REPORTS_PATH + 'optuna_top3.csv')`
- **Co robi:** Wczytuje top-3 konfiguracje oraz przygotowuje train+val i test do finalnego treningu ensemble.
- **Dlaczego:** To start etapu 08 (punkty 8-9).
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 129 (markdown)
- **Tre??/Nag??wek:** `## 08 - Top-3 training, ensembles, uncertainty (task points 8-9)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 130 (markdown)
- **Tre??/Nag??wek:** `### Top-3 x 5-fold training and test prediction`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 131 (code)
- **Pierwsza linia kodu:** `DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`
- **Co robi:** Dopasowuje scaler tylko na train i transformuje val/test; tworzy raport skali.
- **Dlaczego:** To poprawna procedura anti-leakage dla danych czasowych.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 132 (markdown)
- **Tre??/Nag??wek:** `### Save final reports`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 133 (code)
- **Pierwsza linia kodu:** `metrics_df = pd.DataFrame(metrics_rows).sort_values('rank')`
- **Co robi:** Agreguje wyniki top-3, zapisuje raporty i aliasy latest do `reports/`.
- **Dlaczego:** Tworzy finalny raport jako?ci modeli ensemble.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).
- **Wynik liczbowy Top-3 ensemble:**
  - rank=1, trial=74, f1_macro=0.378487, bal_acc=0.392342, acc=0.404813
  - rank=2, trial=21, f1_macro=0.357572, bal_acc=0.386442, acc=0.362588
  - rank=3, trial=72, f1_macro=0.371928, bal_acc=0.402023, acc=0.395590

## Cell 134 (markdown)
- **Tre??/Nag??wek:** `### Quick uncertainty summary`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 135 (code)
- **Pierwsza linia kodu:** `summary_rows = []`
- **Co robi:** Agreguje statystyki niepewno?ci predykcji dla ka?dego ranku.
- **Dlaczego:** Daje dodatkow? ocen? jako?ci poza sam? trafno?ci? klasy.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 136 (markdown)
- **Tre??/Nag??wek:** `## 09 - Statistical tests and final report (task point 10)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 137 (code)
- **Pierwsza linia kodu:** `metrics_df = pd.read_csv(REPORTS_PATH + 'top3_ensemble_metrics.csv').sort_values('rank').reset_index(drop=True)`
- **Co robi:** Wczytuje metryki i `run_id` dla finalnej analizy statystycznej.
- **Dlaczego:** Gwarantuje sp?jno?? test?w z konkretnym runem predykcji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 138 (markdown)
- **Tre??/Nag??wek:** `## 1. Load ensemble predictions (3 sets) and align timestamps`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 139 (code)
- **Pierwsza linia kodu:** `def load_ensemble_predictions(rank: int, run_id: str) -> pd.DataFrame:`
- **Co robi:** Wczytuje predykcje 3 ensemble i wyr?wnuje je po timestampie.
- **Dlaczego:** To warunek poprawnego por?wnania parami tych samych obserwacji.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 140 (markdown)
- **Tre??/Nag??wek:** `## 2. Helper functions: bootstrap, McNemar, Holm correction`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 141 (code)
- **Pierwsza linia kodu:** `def bootstrap_metric_difference(`
- **Co robi:** Definiuje funkcje bootstrap, McNemar i korekt? Holma do test?w r??nic mi?dzy ensemble.
- **Dlaczego:** To formalna implementacja punktu 10 instrukcji.
- **Wynik z wykonania:** Brak bezpo?redniego outputu (kom?rka definiuje funkcje/zmienne albo przygotowuje kolejne kroki).

## Cell 142 (markdown)
- **Tre??/Nag??wek:** `## 3. Pairwise statistical comparison between 3 ensembles`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 143 (code)
- **Pierwsza linia kodu:** `y_true = preds[1]['y_true'].to_numpy(dtype=np.int64)`
- **Co robi:** Liczy statystyki por?wna? parami (r??nice metryk + przedzia?y ufno?ci + McNemar).
- **Dlaczego:** Odpowiada, czy r??nice jako?ci modeli s? istotne statystycznie.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).
- **Wynik liczbowy test?w statystycznych:**
  - rank1_vs_rank2: f1_diff=0.020991 [0.009525, 0.032369], mcnemar_p_holm=6.736e-12, significant=True
  - rank1_vs_rank3: f1_diff=0.006855 [-0.001958, 0.015716], mcnemar_p_holm=3.209e-02, significant=True
  - rank2_vs_rank3: f1_diff=-0.014137 [-0.025656, -0.002928], mcnemar_p_holm=9.131e-08, significant=True

## Cell 144 (markdown)
- **Tre??/Nag??wek:** `## 4. Multiple-comparison correction (Holm)`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 145 (code)
- **Pierwsza linia kodu:** `adj = holm_correction(mcnemar_pvals)`
- **Co robi:** Nak?ada korekt? Holma i wyznacza flagi istotno?ci po wielokrotnych por?wnaniach.
- **Dlaczego:** Chroni przed inflacj? b??du I rodzaju.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 146 (markdown)
- **Tre??/Nag??wek:** `## 5. Final ranking summary`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 147 (code)
- **Pierwsza linia kodu:** `rank_metrics = metrics_df[['rank', 'trial_number', 'test_f1_macro', 'test_balanced_accuracy', 'test_accuracy']].copy()`
- **Co robi:** Tworzy ko?cowy ranking ensemble po `test_f1_macro`.
- **Dlaczego:** Daje finaln? odpowied?, kt?ry zestaw HP jest najlepszy.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).

## Cell 148 (markdown)
- **Tre??/Nag??wek:** `## 6. Save statistical report artifacts`
- **Co robi:** Ustawia kontekst sekcji, opisuje decyzje metodologiczne albo komentuje wyniki poprzednich kom?rek.
- **Dlaczego:** Markdown buduje narracj? techniczn? projektu i u?atwia obron? (co, dlaczego, z jakim skutkiem).
- **Wynik:** Brak wyniku numerycznego; efektem jest dokumentacja i interpretacja.

## Cell 149 (code)
- **Pierwsza linia kodu:** `STAT_CSV = REPORTS_PATH + 'stat_tests_summary.csv'`
- **Co robi:** Zapisuje raporty test?w statystycznych i finalny ranking do CSV/JSON.
- **Dlaczego:** Domyka raport ko?cowy projektu i przygotowuje artefakty do obrony.
- **Wynik z wykonania:** Wygenerowano tabel?/element HTML (Styler).
