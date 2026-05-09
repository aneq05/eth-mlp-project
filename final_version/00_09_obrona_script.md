# 00_09 Combined Notebook - Wersja Na Obrone

Ten dokument to skrot prezentacyjny do notebooka:
`final_version/00_09_combined_pipeline_demo.ipynb`

Cel: szybko i pewnie przejsc przez wszystkie wymagania z `Lab6_7-1.pdf` podczas obrony.

## 1) Data cleaning (Punkt 1)
- Komorki: `018-021` (sekcja 01).
- Co pokazac:
  - funkcja `clean_ohlcv(...)` (komorka 020),
  - raport czyszczenia (duplikaty, NaN, invalid candles).
- Co powiedziec (gotowiec):
  - "Najpierw zrobilam czyszczenie surowych danych OHLCV: parsowanie timestamp, usuniecie duplikatow i rekordow niespojnych rynkowo."
  - "Dzieki temu dalsze etapy pracuja na wiarygodnym zbiorze czasowym."

## 2) EDA + split + analiza cech + VIF + scaling (Punkt 2)
- Komorki:
  - split i leakage: `033-043` (sekcja 02),
  - feature engineering: `047-062` (sekcja 03),
  - EDA korelacje + VIF + MI: `067-081` (sekcja 04),
  - scaling: `085-095` (sekcja 05).
- Co pokazac:
  - chronologiczny split 70/15/15,
  - histogramy/pairplot i heatmapa korelacji,
  - redukcja cech po korelacji i VIF,
  - fit scalera tylko na train.
- Kluczowe wyniki:
  - split: train=32376, val=6937, test=6939,
  - cechy: 96 -> 38 (usuniete corr=37, vif=21),
  - wybrany scaler: `robust`, outlier ratio ~0.055.
- Co powiedziec:
  - "Split jest chronologiczny, wiec nie przeciekam informacja z przyszlosci."
  - "Po engineeringu i filtrach zostawiam 38 najbardziej uzytecznych cech, co stabilizuje model."

## 3) MLP configurable architecture (Punkt 3)
- Komorki: `099-100` (sekcja 06).
- Co pokazac:
  - `MLPClassifier` z parametrami: `hidden_dims`, `activation`, `dropout`, `batchnorm`.
- Co powiedziec:
  - "Architektura jest konfigurowalna i potem strojona przez Optune."

## 4) train_one_epoch + gradient clipping (Punkt 4)
- Komorki: `101-102`.
- Co pokazac:
  - funkcja `train_one_epoch(...)`,
  - linia `clip_grad_norm_`.
- Co powiedziec:
  - "Kazda epoka treningu ma gradient clipping, co zabezpiecza przed exploding gradients."

## 5) validate_one_epoch (Punkt 5)
- Komorki: `103-104`.
- Co pokazac:
  - `validate_one_epoch(...)` i metryki (`f1_macro`, `balanced_accuracy`, `accuracy`).
- Co powiedziec:
  - "Walidacja jest oddzielona od treningu, bez aktualizacji wag (`@torch.no_grad()`)."

## 6) Full fit loop + best checkpoint + logging (Punkt 6)
- Komorki: `105-108`.
- Co pokazac:
  - `fit_model(...)`: early stopping, monitor metryki, zapis najlepszego modelu,
  - logi do CSV i TensorBoard,
  - baseline run (komorka 108) i wykresy (110).
- Co powiedziec:
  - "Model zapisuje najlepszy checkpoint na walidacji, a przebieg treningu loguje do TensorBoard."

## 7) Optuna 5-fold time-series CV (Punkt 7)
- Komorki: `115-124` (+ 127 wykresy).
- Co pokazac:
  - `suggest_params(...)`,
  - `objective(...)` z `TimeSeriesSplit(n_splits=5)`,
  - `study.optimize(...)`.
- Kluczowy wynik:
  - best trial: `74`, best CV `f1_macro ~ 0.3975`.
- Co powiedziec:
  - "HPO robie na 5-fold CV czasowym, bez losowego seedowania splitow w objective, zgodnie z instrukcja."

## 8) Trening top-3 konfiguracji w 5-fold (Punkt 8)
- Komorki: `128-133`.
- Co pokazac:
  - petla po `top3_df`,
  - 5 foldow na kazdy zestaw,
  - zapisy checkpointow i logow.
- Co powiedziec:
  - "Dla trzech najlepszych konfiguracji trenuje po 5 modeli, lacznie 15 modeli."

## 9) Predykcja test + srednia odpowiedz i niepewnosc (Punkt 9)
- Komorki: `131-135`.
- Co pokazac:
  - ensemble mean probabilities,
  - metryki testowe,
  - niepewnosc: entropy, margin, mean_prob_std.
- Kluczowe wyniki (test):
  - rank1: f1_macro=0.3785, bal_acc=0.3923, acc=0.4048,
  - rank2: f1_macro=0.3576, bal_acc=0.3864, acc=0.3626,
  - rank3: f1_macro=0.3719, bal_acc=0.4020, acc=0.3956.
- Co powiedziec:
  - "Finalna decyzja modelu to ensemble z 5 foldow; dodatkowo raportuje pewnosc predykcji."

## 10) Testy statystyczne miedzy ensemble (Punkt 10)
- Komorki: `139-149`.
- Co pokazac:
  - bootstrap roznic metryk,
  - McNemar,
  - korekta Holma,
  - finalny ranking.
- Kluczowe wyniki:
  - wszystkie pary maja istotne roznice McNemara po korekcie Holma.
- Co powiedziec:
  - "Porownanie modeli nie opiera sie tylko na metrykach punktowych, ale na testach istotnosci."

---

## Szybki plan 30-min wystapienia
1. Cel + dane (2 min)
2. Cleaning + target (4 min)
3. Split + EDA + feature pipeline (8 min)
4. MLP + train/val/fit (5 min)
5. Optuna + top3 ensemble (7 min)
6. Testy statystyczne + wnioski (4 min)

## 5 gotowych odpowiedzi na trudne pytania
1. "Dlaczego nie random split?"
- "Bo to szereg czasowy; random split powodowalby leakage z przyszlosci."

2. "Dlaczego `f1_macro` jako glowna metryka?"
- "Klasy sa niezbalansowane, a `f1_macro` rowno traktuje wszystkie klasy."

3. "Po co VIF skoro jest korelacja?"
- "Korelacja wycina zaleznosci parami, VIF wykrywa wielokolinearnosc wielowymiarowa."

4. "Po co ensemble z foldow?"
- "Srednia po 5 modelach zmniejsza wariancje i daje stabilniejsze predykcje."

5. "Skad pewnosc, ze roznice modeli sa realne?"
- "Sprawdzam to testami bootstrap + McNemar z korekta Holma."

## Checklista przed obrona
- Otwarty notebook: `final_version/00_09_combined_pipeline_demo.ipynb`
- Otwarty dziennik: `final_version/00_09_combined_pipeline_demo_journal.md`
- Otwarta sciaga: `final_version/00_09_obrona_script.md`
- TensorBoard path: `logs/tensorboard`
- Finalne raporty: `reports/top3_ensemble_metrics.csv`, `reports/stat_tests_summary.csv`
