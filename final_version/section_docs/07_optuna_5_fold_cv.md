# Sekcja 07 - Optuna 5-fold CV

- Zakres komorek w notebooku: `107` -> `121`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\logs\optuna\optuna.db` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\optuna_trials.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\optuna_top3.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\optuna_summary.json` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
### `optuna_summary.json`
```json
{
  "study_name": "eth_mlp_optimization",
  "best_trial_number": 74,
  "best_value": 0.39750490758156753,
  "best_params": {
    "n_layers": 2,
    "hidden_dim_1": 320,
    "hidden_dim_2": 352,
    "dropout": 0.38602540514996175,
    "activation": "leaky_relu",
    "use_batchnorm": false,
    "optimizer": "adam",
    "lr": 0.0017426803787583814,
    "weight_decay": 0.00018073848892979683,
    "batch_size": 32,
    "scaler_type": "standard",
    "clip_grad_norm": 2.32356923645467
  },
  "n_trials_total": 95,
  "n_trials_complete": 14,
  "top3": [
    {
      "rank": 1,
      "trial_number": 74,
      "value": 0.39750490758156753,
      "params": {
        "n_layers": 2,
        "hidden_dim_1": 320,
        "hidden_dim_2": 352,
        "dropout": 0.38602540514996175,
        "activation": "leaky_relu",
        "use_batchnorm": false,
        "optimizer": "adam",
        "lr": 0.0017426803787583814,
        "weight_decay": 0.00018073848892979683,
        "batch_size": 32,
        "scaler_type": "standard",
        "clip_grad_norm": 2.32356923645467
      }
    },
```

## Komorka po komorce

### Cell 107 (markdown)
- Start: `## 07 - Optuna 5-fold CV`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 108 (markdown)
- Start: `### 1. Optuna config`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 109 (code)
- Start: `DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 110 (markdown)
- Start: `### 2. Hyperparameter search space`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 111 (code)
- Start: `def suggest_params(trial: optuna.Trial) -> dict:`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 112 (markdown)
- Start: `### 3. Objective with 5-fold TimeSeriesSplit`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 113 (code)
- Start: `def objective(trial: optuna.Trial) -> float:`
- Co robi kod: Skalowanie anti-leakage: fit na train, transform na val/test.
- Jak to jest wyliczane:
  - score triala = srednia F1_macro po foldach time-series CV
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 114 (markdown)
- Start: `### 4. Run optimization`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 115 (code)
- Start: `study = optuna.create_study(`
- Co robi kod: Uruchomienie Optuna HPO na walidacji 5-fold time-series.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Log/stream: [32m[I 2026-05-09 12:01:22,805][0m Using an existing study with name 'eth_mlp_optimization' instead of creating a new one.[0m | [32m[I 2026-05-09 12:02:31,072][0m Trial 65 pruned. [0m | [32m[I 2026-05-09 12:05:03,754][0m Trial 66 pr Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 116 (markdown)
- Start: `### 5. Save summary and top-3 trials`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 117 (code)
- Start: `trials_df = study.trials_dataframe(attrs=('number', 'value', 'state', 'params'))`
- Co robi kod: Zapis wynik?w HPO oraz wyb?r top-3 triali do etapu ko?cowego.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(REPORTS_PATH + 'optuna_top3.csv', index=False)`
  - `to_csv(REPORTS_PATH + 'optuna_trials.csv', index=False)`

### Cell 118 (markdown)
- Start: `### 6. Optional Optuna visual diagnostics`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 119 (code)
- Start: `%pip install plotly`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Log/stream: Requirement already satisfied: plotly in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-project\venv\lib\site-packages (6.7.0) | Requirement already satisfied: narwhals>=1.15.1 in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-pro Log/stream: [notice] A new release of pip is available: 24.2 -> 26.1.1 | [notice] To update, run: python.exe -m pip install --upgrade pip Log/stream: Requirement already satisfied: optuna in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-project\venv\lib\site-packages (4.8.0) | Requirement already satisfied: alembic>=1.5.0 in c:\users\ankap\onedrive\desktop\projekty\nn\eth-mlp-proje

### Cell 120 (code)
- Start: `fig1 = vis.plot_optimization_history(study)`
- Co robi kod: Wizualizacja przebiegu HPO i wa?no?ci hiperparametr?w (Plotly/Optuna).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Output techniczny obecny (bez jawnych warto?ci tekstowych).

### Cell 121 (code)
- Start: `top3_df = pd.read_csv(REPORTS_PATH + 'optuna_top3.csv')`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
