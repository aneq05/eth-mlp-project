# ETH MLP Project

Pipeline do predykcji sygnalu `sell / hold / buy` dla ETHUSDT (interwal 1h) z uzyciem:

- PyTorch (MLP)
- Optuna (HPO)
- TensorBoard (monitoring)

Notebooki zostaja tylko do prezentacji i raportu. Caly pipeline treningowy jest uruchamiany skryptami.

## Struktura

```text
eth-mlp-project/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/                      # tylko prezentacja i EDA do zaliczenia
├── scripts/                        # entrypointy pipeline'u
│   ├── run_prepare_data.py
│   ├── run_optuna.py
│   ├── run_top3.py
│   ├── run_evaluate.py
│   └── run_all.py
├── src/
│   ├── core/                       # config, utilsy
│   ├── data/                       # loading, cleaning, split, dataset
│   ├── features/                   # feature engineering, target, scaling, selection
│   ├── modeling/                   # MLP, train/validate/fit, optuna helpers, inference
│   ├── evaluation/                 # metrics, testy statystyczne
│   └── pipelines/                  # logika etapow E2E
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

```powershell
cd C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project
pip install -r requirements.txt
```

## Uruchamianie etapowe (zalecane)

1. Przygotowanie danych (cleaning + features + target + split):

```powershell
python scripts/run_prepare_data.py --raw-csv "C:\sciezka\do\ethusdt_1h.csv" --horizon 6 --threshold 0.0075
```

2. Optuna z 5-fold walk-forward:

```powershell
python scripts/run_optuna.py --n-trials 30 --epochs 20 --patience 5 --n-splits 5 --device cpu
```

3. Trening top-3 i ensemble na test:

```powershell
python scripts/run_top3.py --epochs 50 --patience 10 --device cpu
```

4. Raporty ewaluacyjne (confusion matrix + classification report):

```powershell
python scripts/run_evaluate.py
```

## Uruchomienie end-to-end

```powershell
python scripts/run_all.py --raw-csv "C:\sciezka\do\ethusdt_1h.csv" --n-trials 30 --device cpu
```

## TensorBoard

```powershell
tensorboard --logdir logs/tensorboard
```

## Dokumentacja danych

Szczegolowy opis uzytego zbioru danych znajduje sie w:

- `reports/data_description.md`

## Notatki metodologiczne (time series)

- Split danych wykonujemy chronologicznie.
- Walidacja wielokrotna to walk-forward (`TimeSeriesSplit`).
- Skaler fitowany tylko na train fold.
- Niezbalansowanie klas obslugujemy wagami w `CrossEntropyLoss`.
