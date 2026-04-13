import numpy as np
import pandas as pd


def _rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def _macd(series: pd.Series) -> tuple[pd.Series, pd.Series, pd.Series]:
    ema_fast = series.ewm(span=12, adjust=False).mean()
    ema_slow = series.ewm(span=26, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal = macd.ewm(span=9, adjust=False).mean()
    hist = macd - signal
    return macd, signal, hist


def _atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high_low = df["high"] - df["low"]
    high_close = (df["high"] - df["close"].shift(1)).abs()
    low_close = (df["low"] - df["close"].shift(1)).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()

    # Returns
    for period in [1, 2, 3, 6, 12, 24]:
        work[f"return_{period}"] = work["close"].pct_change(period)

    work["log_return_1"] = np.log(work["close"]).diff(1)
    work["log_return_6"] = np.log(work["close"]).diff(6)
    work["log_return_24"] = np.log(work["close"]).diff(24)

    # Candle features
    work["close_open_pct"] = (work["close"] - work["open"]) / work["open"]
    work["high_low_pct"] = (work["high"] - work["low"]) / work["close"]
    work["upper_shadow"] = (work["high"] - work[["open", "close"]].max(axis=1)) / work["close"]
    work["lower_shadow"] = (work[["open", "close"]].min(axis=1) - work["low"]) / work["close"]
    work["body_size"] = (work["close"] - work["open"]).abs() / work["close"]

    # Rolling
    for window in [6, 12, 24, 48]:
        work[f"rolling_close_mean_{window}"] = work["close"].rolling(window).mean()
        work[f"rolling_return_std_{window}"] = work["return_1"].rolling(window).std()
        work[f"rolling_close_min_{window}"] = work["close"].rolling(window).min()
        work[f"rolling_close_max_{window}"] = work["close"].rolling(window).max()
        work[f"rolling_return_skew_{window}"] = work["return_1"].rolling(window).skew()
        work[f"rolling_return_kurt_{window}"] = work["return_1"].rolling(window).kurt()

    # Momentum and trend
    for period in [6, 12, 24]:
        work[f"roc_{period}"] = work["close"].pct_change(period)
        work[f"momentum_{period}"] = work["close"] - work["close"].shift(period)
        work[f"sma_{period}"] = work["close"].rolling(period).mean()
        work[f"ema_{period}"] = work["close"].ewm(span=period, adjust=False).mean()
        work[f"dist_sma_{period}"] = (work["close"] - work[f"sma_{period}"]) / work["close"]
        work[f"dist_ema_{period}"] = (work["close"] - work[f"ema_{period}"]) / work["close"]

    # Technical indicators
    work["rsi_14"] = _rsi(work["close"], period=14)
    macd, macd_signal, macd_hist = _macd(work["close"])
    work["macd"] = macd
    work["macd_signal"] = macd_signal
    work["macd_hist"] = macd_hist
    work["atr_14"] = _atr(work, period=14)

    rolling_mean_20 = work["close"].rolling(20).mean()
    rolling_std_20 = work["close"].rolling(20).std()
    bb_upper = rolling_mean_20 + 2 * rolling_std_20
    bb_lower = rolling_mean_20 - 2 * rolling_std_20
    work["bb_width"] = (bb_upper - bb_lower) / rolling_mean_20
    work["bb_position"] = (work["close"] - bb_lower) / (bb_upper - bb_lower)

    # Volume
    work["volume_return"] = work["volume"].pct_change(1)
    work["volume_mean_24"] = work["volume"].rolling(24).mean()
    work["volume_std_24"] = work["volume"].rolling(24).std()
    work["volume_zscore_24"] = (work["volume"] - work["volume_mean_24"]) / work["volume_std_24"]

    # Calendar features
    if not isinstance(work.index, pd.DatetimeIndex):
        raise ValueError("DataFrame index must be DatetimeIndex for calendar features.")
    hour = work.index.hour
    day = work.index.dayofweek
    work["hour_sin"] = np.sin(2 * np.pi * hour / 24)
    work["hour_cos"] = np.cos(2 * np.pi * hour / 24)
    work["dow_sin"] = np.sin(2 * np.pi * day / 7)
    work["dow_cos"] = np.cos(2 * np.pi * day / 7)
    work["is_weekend"] = (day >= 5).astype(int)

    # Selected lags
    lag_features = ["return_1", "return_6", "rsi_14", "macd_hist", "volume_zscore_24"]
    for col in lag_features:
        for lag in [1, 2, 3]:
            work[f"{col}_lag_{lag}"] = work[col].shift(lag)

    return work
