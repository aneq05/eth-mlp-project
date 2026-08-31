# Final Report

## 1. Objective

The project explores whether a tabular neural network can classify short-term ETHUSDT market states into `sell`, `hold`, and `buy` classes using hourly OHLCV-derived features.

The main goal is methodological: build a time-series-aware ML workflow that avoids the most common leakage mistakes and can be inspected both as a final notebook and as reusable Python code.

## 2. Data

The dataset is an ETHUSDT 1h Binance spot snapshot with `46,258` rows from `2021-01-01 00:00:00 UTC` to `2026-04-12 23:00:00 UTC`.

The raw schema contains OHLCV prices, quote volume, trade count, and taker-buy volume fields. Data quality checks found no missing values, no duplicate timestamps, and no candle consistency errors. A small number of zero-volume rows and missing hourly timestamps were handled as part of the cleaning workflow.

See `reports/data_description.md` for the full data note.

## 3. Target

The target is based on the future close-to-close return:

```text
future_return_t = close[t + 6 hours] / close[t] - 1
```

The implementation resolves the horizon by timestamp. For the default configuration, the future close must exist exactly at `timestamp + 6 hours`; observations crossing missing hourly timestamps are dropped before modeling.

Default labels:

- `sell = 0`: future return below `-0.0075`
- `hold = 1`: future return between `-0.0075` and `+0.0075`
- `buy = 2`: future return above `+0.0075`

The split is chronological and preserves the temporal order of observations. A purge gap equal to the prediction horizon is inserted between train/validation/test segments.

## 4. Modeling Workflow

The modular pipeline contains:

1. Raw OHLCV loading and cleaning.
2. Feature engineering.
3. Threshold-based target generation.
4. Chronological train/validation/test split.
5. Feature filtering fit inside each CV fold and final-training split using constant-feature removal, correlation filtering, and optional VIF reduction.
6. Scaling fit only on training folds.
7. MLP training in PyTorch with class-weighted cross-entropy.
8. Optuna hyperparameter search with seeded sampling and purged walk-forward cross-validation.
9. Top-3 completed-trial retraining and mean-probability ensembling.
10. Majority-class, Logistic Regression, and Random Forest baselines.
11. Test-set evaluation and moving-block bootstrap comparison against the CV-best single model.

## 5. Results

The canonical run is `canonical_seed42`, generated with a run-local data directory and run-local Optuna database. VIF reduction was disabled for the canonical run after correlation filtering, as it added substantial computational cost without being essential for the MLP pipeline.

```bash
python scripts/run_all.py --run-id canonical_seed42 --raw-csv data/raw/ethusdt_1h.csv --n-trials 30 --seed 42 --reset-study --bootstrap-block-size 24 --no-vif --device cpu
```

| Model | Macro F1 | Balanced accuracy |
| --- | ---: | ---: |
| Majority baseline | 0.2168 | 0.3333 |
| Logistic Regression | 0.3945 | 0.3970 |
| Random Forest | 0.4149 | 0.4233 |
| CV-best MLP | 0.4096 | 0.4195 |
| MLP Ensemble | 0.4121 | 0.4213 |

Best Optuna CV macro F1 was `0.4017` for trial `19`. The MLP ensemble slightly improved over the CV-best MLP on the test set, but the Random Forest baseline remained marginally stronger on macro F1 and balanced accuracy. This is an important result: the neural network is evaluated against simpler baselines rather than assumed to be superior.

The moving-block bootstrap comparison of MLP Ensemble vs CV-best MLP gives macro F1 mean difference `+0.0027` with 95% CI `[-0.0072, +0.0131]` using 24-hour blocks.

The generated metrics are stored in `reports/canonical_results.json`; the matching full run artifacts are stored under the ignored `reports/runs/canonical_seed42/` directory.

For the final public snapshot, keep the full run directory out of git and promote only compact canonical artifacts such as `reports/canonical_results.json`, `reports/canonical_confusion_matrix.png`, and refreshed README metrics.

## 6. What Worked

- Chronological splitting and walk-forward validation make the workflow more realistic than random splitting.
- Class weighting helps address the dominant `hold` class.
- The ensemble provides a structured way to combine the best Optuna configurations.
- Separating the final notebook from `src/` and `scripts/` makes the project easier to review on GitHub.

## 7. Limitations

- No transaction costs, slippage, latency, or portfolio simulation are included.
- Labels are sensitive to the chosen horizon and threshold.
- The model only uses engineered OHLCV-style tabular features.
- Market regimes change; historical test performance may not transfer to future periods.
- The project does not implement live trading, exchange integration, or risk management.

## 8. Conclusion

The project is best presented as an educational ML pipeline for financial time-series classification. Its strongest part is the methodology and code organization: data checks, leakage-aware splitting, modular training scripts, hyperparameter search, and honest reporting of noisy results.
