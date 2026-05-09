# Sekcja 08 - Top-3 training, ensembles, uncertainty

- Zakres komorek w notebooku: `122` -> `128`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\top3_ensemble_metrics.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\top3_ensemble_summary.json` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\predictions` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\top3_fold_metrics_20260509_135846.csv` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
### `top3_ensemble_metrics.csv`
```text
rank,trial_number,cv_score_from_optuna,test_f1_macro,test_balanced_accuracy,test_accuracy,test_precision_macro,test_recall_macro
1,74,0.3975049075815675,0.3784874924286336,0.3923417367745629,0.404813373684969,0.3996496717782225,0.3923417367745629
2,21,0.3963765090422494,0.35757150088335937,0.3864420180341088,0.3625882692030552,0.4221464258734629,0.3864420180341088
3,72,0.3960468486413777,0.3719278897256982,0.40202330924663393,0.3955901426718547,0.4241132446094195,0.40202330924663393
```
### `top3_ensemble_summary.json`
```json
{
  "run_id": "20260509_135846",
  "n_sets": 3,
  "n_folds_per_set": 5,
  "metrics_file": "../reports/top3_ensemble_metrics_20260509_135846.csv",
  "fold_metrics_file": "../reports/top3_fold_metrics_20260509_135846.csv",
  "best_set_by_test_f1": {
    "rank": 1.0,
    "trial_number": 74.0,
    "cv_score_from_optuna": 0.3975049075815675,
    "test_f1_macro": 0.3784874924286336,
    "test_balanced_accuracy": 0.3923417367745629,
    "test_accuracy": 0.404813373684969,
    "test_precision_macro": 0.3996496717782225,
    "test_recall_macro": 0.3923417367745629
  }
}
```

## Komorka po komorce

### Cell 122 (markdown)
- Start: `## 08 - Top-3 training, ensembles, uncertainty`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 123 (markdown)
- Start: `### 1. Top-3 x 5-fold training and test prediction`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 124 (code)
- Start: `DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`
- Co robi kod: Skalowanie anti-leakage: fit na train, transform na val/test.
- Jak to jest wyliczane:
  - ensemble probability = srednia prawdopodobienstw z modeli foldowych
  - niepewnosc: entropia rozkladu prawdopodobienstw klas
  - niepewnosc margin = p1 - p2 (roznica 2 najwyzszych prawdopodobienstw)
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
- Zapisuje pliki:
  - `to_csv(ensemble_path, index=False)`
  - `to_csv(model_pred_path, index=False)`
  - `torch.save(...)`

### Cell 125 (markdown)
- Start: `### 2. Save final reports`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 126 (code)
- Start: `metrics_df = pd.DataFrame(metrics_rows).sort_values('rank')`
- Co robi kod: Agregacja metryk top-3 i zapis raport?w ko?cowych etapu ensemble.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(fold_metrics_path, index=False)`
  - `to_csv(latest_metrics_alias, index=False)`
  - `to_csv(metrics_path, index=False)`

### Cell 127 (markdown)
- Start: `### 3. Quick uncertainty summary`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 128 (code)
- Start: `summary_rows = []`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
