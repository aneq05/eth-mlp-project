# Opis Uzywanych Danych (ETHUSDT 1h)

## 1. Zbior danych

- Plik: `data/raw/ethusdt_1h.csv`
- Instrument: `ETHUSDT` (Ethereum kwotowane w USDT, praktyczny proxy USD)
- Interwal: `1h` (jedna obserwacja = jedna swieca godzinowa)
- Liczba rekordow: `46,258`
- Zakres czasu (UTC): `2021-01-01 00:00:00` -> `2026-04-12 23:00:00`

## 2. Zrodlo danych

Dane zostaly pobrane z publicznego archiwum Binance Data Vision:

- monthly klines: `https://data.binance.vision/data/spot/monthly/klines/ETHUSDT/1h/`
- daily klines: `https://data.binance.vision/data/spot/daily/klines/ETHUSDT/1h/`

Do projektu pobrano historie od 2021 roku do biezacego okresu i zapisano jako pojedynczy plik CSV.

## 3. Schemat kolumn

- `timestamp` - czas otwarcia swiecy w UTC
- `open` - cena otwarcia
- `high` - cena maksymalna
- `low` - cena minimalna
- `close` - cena zamkniecia
- `volume` - wolumen bazowy (ETH)
- `quote_asset_volume` - wolumen w aktywie kwotowanym (USDT)
- `number_of_trades` - liczba transakcji
- `taker_buy_base_asset_volume` - wolumen kupna agresora (ETH)
- `taker_buy_quote_asset_volume` - wolumen kupna agresora (USDT)

## 4. Jak interpretowac interwal 1h

`1h` nie oznacza "danych z jednej godziny". Oznacza, ze kazdy rekord opisuje **jedna godzine handlu**.  
Caly plik zawiera kolejne godziny, godzina po godzinie, przez wiele lat.

## 5. Kontrola jakosci danych (surowy plik)

Wykonane kontrole:

- braki (`NaN`) w kolumnach: `0`
- duplikaty rekordow: `0`
- duplikaty timestamp: `0`
- niespojnosc swiec:
  - `high < max(open, close)`: `0`
  - `low > min(open, close)`: `0`
- ujemny wolumen: `0`
- rekordy z `volume = 0`: `2`
- rekordy z `number_of_trades = 0`: `2`
- brakujace godziny w calym zakresie: `14` (glownie 2021)

Wniosek: zbior jest dobry jakosciowo i nadaje sie do modelowania po standardowym cleaningu.

## 6. Wykorzystanie w projekcie

Zbior sluzy do budowy celu klasyfikacyjnego `sell / hold / buy`:

- horyzont: np. `h = 6` godzin
- zwrot przyszly: `future_return_t = close[t+h] / close[t] - 1`
- etykiety:
  - `sell` gdy `future_return_t < -tau`
  - `hold` gdy `-tau <= future_return_t <= +tau`
  - `buy` gdy `future_return_t > +tau`

Przy `h=6` i `tau=0.0075` klasy sa sensownie rozlozone (ok. 25-47-27), co dobrze pasuje do klasyfikacji wieloklasowej.

## 7. Ograniczenia

- Dane pochodza z rynku spot (Binance), a nie bezposrednio z feedu brokera CFD.
- USDT jest traktowane jako praktyczny proxy USD.
- W raporcie nalezy to jawnie opisac w sekcji "zrodlo danych i ograniczenia".
