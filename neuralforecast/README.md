# NeuralForecast (PatchTST) for ETH

This folder contains a standalone pipeline that uses an advanced public architecture (`PatchTST`) from `neuralforecast` to predict ETH returns and evaluate trading-class accuracy (`sell/hold/buy`).

## 1. Install dependency

```powershell
pip install neuralforecast
```

## 2. Run on your raw ETH CSV

CSV must contain at least: `timestamp`, `close`.

```powershell
python neuralforecast/run_patchtst_eth.py --raw-csv "data/raw/ethusdt_1h.csv" --horizon-hours 6 --threshold 0.0075
```

## 3. Or run on existing prepared splits

Expected columns in each split: `timestamp`, `future_return`.

```powershell
python neuralforecast/run_patchtst_eth.py --train-csv "data/labeled/train_labeled.csv" --val-csv "data/labeled/val_labeled.csv" --test-csv "data/labeled/test_labeled.csv" --threshold 0.0075
```

## 4. Outputs

Saved by default to `reports/neuralforecast/`:

- `patchtst_metrics.json`
- `patchtst_classification_report.json`
- `patchtst_confusion_matrix.json`
- `patchtst_test_predictions.csv`

## 5. Notes

- The model predicts `future_return`.
- Predicted return is mapped to classes:
  - `sell (0)` when return `< -threshold`
  - `hold (1)` when `-threshold <= return <= threshold`
  - `buy (2)` when return `> threshold`
- Main quality metrics: `accuracy`, `balanced_accuracy`, `f1_macro`.
