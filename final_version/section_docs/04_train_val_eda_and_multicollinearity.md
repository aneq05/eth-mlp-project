# Sekcja 04 - Train/Val EDA and multicollinearity

- Zakres komorek w notebooku: `58` -> `75`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\train_selected.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\val_selected.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\test_selected.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\selected_feature_columns.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\feature_selection_report.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\dropped_features_report.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\feature_target_mi.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\vif_table.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\eda\corr_heatmap_train_val.png` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
### `feature_selection_report.csv`
```text
metric,value
initial_feature_count,96
dropped_constant_count,0
dropped_corr_count,37
dropped_vif_count,21
final_selected_count,38
```

## Komorka po komorce

### Cell 58 (markdown)
- Start: `## 04 - Train/Val EDA and multicollinearity`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 59 (markdown)
- Start: `### 1. Histograms and pairplot (train+val only)`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 60 (code)
- Start: `# due to a large number of features (96) only a few histograms are displayed`
- Co robi kod: Definicja funkcji feature engineering (cechy techniczne, momentum, zmienno??, lags, rolling).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik wizualny: wykres PNG.

### Cell 61 (markdown)
- Start: `### Wnioski`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 62 (markdown)
- Start: `### 2. Feature covariance and high-correlation filter`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 63 (code)
- Start: `def drop_constant_features(df: pd.DataFrame, min_unique: int = 2):`
- Co robi kod: Filtracja cech sta?ych i silnie skorelowanych + heatmapa korelacji.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik wizualny: wykres PNG. Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 64 (markdown)
- Start: `#### Wnioski`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 65 (markdown)
- Start: `### 3. VIF analysis `
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 66 (code)
- Start: `def reduce_vif_features(`
- Co robi kod: Iteracyjna redukcja wielokolinearno?ci metod? VIF.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Log/stream: c:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\venv\Lib\site-packages\statsmodels\stats\outliers_influence.py:197: RuntimeWarning: divide by zero encountered in scalar divide |   vif = 1. / (1. - r_squared_i) Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 67 (markdown)
- Start: `### 4. Feature-target relation (train+val)`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 68 (code)
- Start: `X_mi = X_no_corr[kept_after_vif].copy()`
- Co robi kod: Analiza relacji cecha-target przez Mutual Information.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler). Wynik wizualny: wykres PNG.

### Cell 69 (markdown)
- Start: `#### Wnioski`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 70 (markdown)
- Start: `### 5. Final selected feature set & apply to train/val/test`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 71 (code)
- Start: `selected_features = kept_after_vif.copy()`
- Co robi kod: Budowa finalnej listy cech wej?ciowych i finalnych split?w cechowych.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 72 (markdown)
- Start: `#### Wnioski`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 73 (markdown)
- Start: `### 6. Saving artifacts`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 74 (code)
- Start: `TRAIN_SELECTED_OUT = PROCESSED_PATH + 'train_selected.csv'`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(DROP_LIST_OUT, index=False)`
  - `to_csv(MI_REPORT_OUT, index=False)`
  - `to_csv(SELECTED_FEATURES_OUT, index=False)`
  - `to_csv(SELECTION_REPORT_OUT, index=False)`
  - `to_csv(TEST_SELECTED_OUT, index=False)`
  - `to_csv(TRAIN_SELECTED_OUT, index=False)`
  - `to_csv(VAL_SELECTED_OUT, index=False)`
  - `to_csv(VIF_REPORT_OUT, index=False)`

### Cell 75 (code)
- Start: `train_df = train_selected.copy()`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
