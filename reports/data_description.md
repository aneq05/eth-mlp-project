# Data Description

## Dataset

- File: `data/raw/ethusdt_1h.csv`
- Instrument: `ETHUSDT`
- Market: Binance spot
- Interval: `1h`
- Rows: `46,258`
- Time range: `2021-01-01 00:00:00 UTC` to `2026-04-12 23:00:00 UTC`

Each row is one hourly candle. The interval does not mean that the dataset covers one hour; it means every observation summarizes one hour of trading activity.

## Source

The raw data was assembled from Binance Data Vision public kline archives:

- monthly klines: `https://data.binance.vision/data/spot/monthly/klines/ETHUSDT/1h/`
- daily klines: `https://data.binance.vision/data/spot/daily/klines/ETHUSDT/1h/`

The repository includes a CSV snapshot so the final notebook and pipeline can be inspected without repeating the download step.

## Schema

| Column | Description |
| --- | --- |
| `timestamp` | Candle open time in UTC |
| `open` | Opening price |
| `high` | Highest price during the hour |
| `low` | Lowest price during the hour |
| `close` | Closing price |
| `volume` | Base asset volume in ETH |
| `quote_asset_volume` | Quote asset volume in USDT |
| `number_of_trades` | Number of trades |
| `taker_buy_base_asset_volume` | Aggressor buy volume in ETH |
| `taker_buy_quote_asset_volume` | Aggressor buy volume in USDT |

## Quality Checks

The original raw-data audit found:

- missing values: `0`
- duplicate rows: `0`
- duplicate timestamps: `0`
- candles where `high < max(open, close)`: `0`
- candles where `low > min(open, close)`: `0`
- negative volume: `0`
- rows with `volume = 0`: `2`
- rows with `number_of_trades = 0`: `2`
- missing hourly timestamps in the full range: `14`

The dataset is suitable for this educational modeling workflow after basic cleaning and chronological splitting.

## Target Definition

The classification target is derived from the future close-to-close return:

```text
future_return_t = close[t + horizon] / close[t] - 1
```

The horizon is timestamp-based. For example, `horizon = 6` means `timestamp + 6 hours`, not simply the sixth following row. Rows whose exact future timestamp is missing are excluded.

Default project settings:

- `horizon = 6`
- `threshold = 0.0075`
- `sell = 0` when `future_return < -threshold`
- `hold = 1` when `-threshold <= future_return <= threshold`
- `buy = 2` when `future_return > threshold`

The exact class distribution is generated during data preparation and saved to `reports/runs/<run-id>/data_prep_metadata.json`. Generated labeled and processed datasets are intentionally not committed, so the public repository does not mix stale artifacts with the current pipeline.

## Limitations

- Binance spot ETHUSDT is used as a practical proxy for ETH/USD market behavior.
- No transaction costs, slippage, latency, or exchange execution constraints are modeled.
- The labels are threshold-dependent and should be re-evaluated for any different trading horizon or market regime.
