# ETH MLP Project

Pipeline do predykcji sygnalu `sell / hold / buy` dla ETHUSDT (interwal 1h) z uzyciem:

- PyTorch (MLP)
- Optuna (HPO)
- TensorBoard (monitoring)

## Struktura

```text
eth-mlp-project/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/
├── src/
├── logs/
│   ├── tensorboard/
│   └── optuna/
├── checkpoints/
├── reports/
│   └── figures/
├── requirements.txt
└── README.md
```

## Szybki start

1. Wejdz do katalogu projektu:

```powershell
cd C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project
```

2. Zainstaluj zaleznosci:

```powershell
pip install -r requirements.txt
```

3. Uruchom TensorBoard:

```powershell
tensorboard --logdir logs/tensorboard
```

## Kolejnosc prac

1. `notebooks/01_data_download_and_cleaning.ipynb` - pobranie i cleaning danych.
2. `notebooks/02_eda.ipynb` - EDA i analiza klas.
3. `notebooks/03_feature_engineering.ipynb` - cechy + target.
4. `src/` - pipeline treningowy i inferencja.
5. `notebooks/04_results_analysis.ipynb` - analiza wynikow i wykresy.

## Notatki metodologiczne (time series)

- Split danych wykonujemy chronologicznie.
- Walidacja wielokrotna to walk-forward / TimeSeriesSplit.
- Skaler fitowany tylko na train fold.
- Niezbalansowanie klas obslugujemy wagami w `CrossEntropyLoss`.
