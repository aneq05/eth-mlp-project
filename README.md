# ETH MLP Trading Signal Classifier

Small academic machine-learning project for classifying short-term ETH/USDT market states into `sell`, `hold`, and `buy` signals from hourly OHLCV data.

The original deliverable was a Jupyter notebook prepared for a university assignment. The project was later refactored into a modular Python package and reproducible command-line pipelines. In this repository, the notebook is kept as a historical submission artifact, while `src/` and `scripts/` are the source of truth for the portfolio version.

## Project Highlights

- Time-series-aware train/validation/test split, with no random shuffling across time.
- Multiclass target based on future return over a configurable horizon.
- Feature engineering and feature selection for tabular MLP input.
- Optuna search with walk-forward cross-validation.
- Top-3 model retraining and mean-probability ensemble.
- Evaluation with macro F1, balanced accuracy, confusion matrices, and bootstrap comparisons.

This is a learning/research project, not trading advice or a production trading system.

## Repository Layout

```text
eth-mlp-project/
|-- data/
|   |-- raw/                  # raw ETHUSDT 1h CSV snapshot
|   |-- clean/                # cleaned CSV snapshot
|   |-- labeled/              # labeled train/val/test CSV snapshots
|   `-- processed/            # engineered/scaled data snapshots
|-- notebooks/
|   `-- original_submission.ipynb
|-- scripts/                  # command-line pipeline entrypoints
|-- src/                      # reusable Python package code
|   |-- core/
|   |-- data/
|   |-- features/
|   |-- modeling/
|   |-- evaluation/
|   `-- pipelines/
|-- reports/                  # data notes, result summaries, metrics, figures
|-- tests/                    # lightweight unit tests
`-- requirements.txt
```

## Data

The included dataset is an ETHUSDT hourly OHLCV snapshot from Binance Data Vision:

- instrument: `ETHUSDT`
- interval: `1h`
- rows: `46,258`
- date range: `2021-01-01 00:00:00 UTC` to `2026-04-12 23:00:00 UTC`
- source folders:
  - `https://data.binance.vision/data/spot/monthly/klines/ETHUSDT/1h/`
  - `https://data.binance.vision/data/spot/daily/klines/ETHUSDT/1h/`

More details are in `reports/data_description.md`.

## Method

For each timestamp `t`, the project computes a future return:

```text
future_return_t = close[t + horizon] / close[t] - 1
```

With the default configuration:

- horizon: `6` hours
- threshold: `0.0075`
- labels:
  - `0`: sell, when future return is below `-threshold`
  - `1`: hold, when future return is within `[-threshold, +threshold]`
  - `2`: buy, when future return is above `+threshold`

The model is a feed-forward MLP trained with weighted cross-entropy to reduce the impact of class imbalance.

## Results Snapshot

The best recorded run is intentionally reported conservatively. Crypto return direction is noisy, and the model should be read as an ML experiment rather than a deployable strategy.

| Rank | Optuna CV macro F1 | Test macro F1 | Test balanced accuracy | Test accuracy |
| ---: | -----------------: | ------------: | ---------------------: | ------------: |
| 1 | 0.3999 | 0.3751 | 0.3942 | 0.3943 |
| 2 | 0.3997 | 0.3712 | 0.3944 | 0.4071 |
| 3 | 0.3975 | 0.3798 | 0.3905 | 0.4003 |

See `reports/final_report.md` and the CSV/JSON files under `reports/` for the preserved experiment outputs.

## Quick Start

Create a fresh environment. Do not reuse a committed or copied virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run The Pipeline

Prepare the data:

```bash
python scripts/run_prepare_data.py --raw-csv data/raw/ethusdt_1h.csv --horizon 6 --threshold 0.0075
```

Run Optuna search:

```bash
python scripts/run_optuna.py --n-trials 30 --epochs 20 --patience 5 --n-splits 5 --device cpu
```

Train the top-3 models and ensemble:

```bash
python scripts/run_top3.py --epochs 50 --patience 10 --device cpu
```

Generate evaluation figures and reports:

```bash
python scripts/run_evaluate.py
```

Or run everything end-to-end:

```bash
python scripts/run_all.py --raw-csv data/raw/ethusdt_1h.csv --n-trials 30 --device cpu
```

## Notebook Version

`notebooks/original_submission.ipynb` contains the original notebook-based version prepared for the university assignment.

The implementation was later refactored into the modular `src/` package and reproducible command-line pipelines under `scripts/`. The notebook and package are intentionally not maintained as two identical copies of the same code.

## Development

Install the project dependencies and run the lightweight tests:

```bash
pip install -r requirements.txt
python -m unittest discover -s tests
```

Run a syntax check without training:

```bash
python -m compileall -q src scripts tests
```

## Notes And Limitations

- The split is chronological; validation uses walk-forward folds.
- Scalers are fit only on training folds to avoid leakage.
- The target is threshold-based and sensitive to horizon/threshold choices.
- No transaction costs, slippage, latency, or portfolio simulation are modeled.
- Results should not be interpreted as a profitable trading strategy.
