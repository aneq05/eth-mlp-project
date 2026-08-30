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
10. Test-set evaluation and bootstrap comparison against the CV-best single model.

## 5. Results

Historical prediction CSVs and metric summaries from earlier pipeline revisions were removed from version control. A fresh canonical run should be generated with the current leakage-aware pipeline before presenting final model results.

The recommended command is:

```bash
python scripts/run_all.py --run-id canonical_seed42 --raw-csv data/raw/ethusdt_1h.csv --n-trials 30 --seed 42 --reset-study --device cpu
```

The generated metrics will be written to `reports/runs/canonical_seed42/final_results_summary.json`.

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
