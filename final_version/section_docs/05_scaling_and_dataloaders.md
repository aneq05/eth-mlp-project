# Sekcja 05 - Scaling and DataLoaders

- Zakres komorek w notebooku: `76` -> `88`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\selected_scaler.pkl` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\class_weights.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\scaled_arrays.npz` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\data\processed\scaling_dataloaders_summary.json` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
### `scaling_dataloaders_summary.json`
```json
{
  "scaler_type": "robust",
  "auto_scaler": "robust",
  "train_outlier_ratio_iqr": 0.05518289009661442,
  "selected_feature_count": 38,
  "train_shape": [
    32326,
    38
  ],
  "val_shape": [
    6937,
    38
  ],
  "test_shape": [
    6939,
    38
  ],
  "batch_size": 128,
  "use_weighted_sampler": false,
  "class_weights": {
    "0": 1.3216402960055604,
    "1": 0.7030295121898176,
    "2": 1.2181023438088778
  }
}
```

## Komorka po komorce

### Cell 76 (markdown)
- Start: `## 05 - Scaling and DataLoaders`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 77 (markdown)
- Start: `### 1. Building X/y and choosing scaler`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 78 (code)
- Start: `X_train = train_df[selected_features].to_numpy(dtype=np.float32)`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 79 (markdown)
- Start: `### 2. Anti-leakage scaling`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 80 (code)
- Start: `# Fit scaler only on train, then transform val/test.`
- Co robi kod: Skalowanie anti-leakage: fit na train, transform na val/test.
- Jak to jest wyliczane:
  - skaler dopasowany tylko na train: X_train_scaled = fit_transform(X_train), val/test = transform
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 81 (markdown)
- Start: `### 3. Class imbalance setup`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 82 (code)
- Start: `class_counts = np.bincount(y_train)`
- Co robi kod: Wyliczenie wag klas dla niezbalansowanej klasyfikacji.
- Jak to jest wyliczane:
  - class_weight_c = N / (K * n_c)
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 83 (markdown)
- Start: `### 4. Dataset and DataLoader`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 84 (code)
- Start: `class TabularDataset(Dataset):`
- Co robi kod: Definicja datasetu tablicowego i DataLoader?w PyTorch.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 85 (markdown)
- Start: `### 5. Sanity check batches`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 86 (code)
- Start: `x_batch, y_batch = next(iter(train_loader))`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 87 (markdown)
- Start: `### 6. Save preprocessing artifacts`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 88 (code)
- Start: `SCALER_OUT = PROCESSED_PATH + 'selected_scaler.pkl'`
- Co robi kod: Zapis artefakt?w preprocessingu (scaler, arrays, class weights, summary).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(CLASS_WEIGHTS_OUT, index=False)`
