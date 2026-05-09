# Sekcja 06 - MLP training core

- Zakres komorek w notebooku: `89` -> `106`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\checkpoints` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\logs` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
- Brak dodatkowego raportu liczbowego przypisanego tylko do tej sekcji.

## Komorka po komorce

### Cell 89 (markdown)
- Start: `## 06 - MLP training core`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 90 (markdown)
- Start: `### 1. Reproducibility and training config`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 91 (code)
- Start: `def set_seed(seed: int = 42):`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 92 (markdown)
- Start: `### 2. MLP architecture`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 93 (code)
- Start: `def build_activation(name: str) -> nn.Module:`
- Co robi kod: Definicja konfigurowalnej architektury MLP.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 94 (markdown)
- Start: `### 3. Train one epoch with gradient clipping`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 95 (code)
- Start: `def train_one_epoch(`
- Co robi kod: Definicja treningu 1 epoki (z gradient clipping).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 96 (markdown)
- Start: `### 4. Validation at end of epoch`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 97 (code)
- Start: `@torch.no_grad()`
- Co robi kod: Definicja walidacji 1 epoki oraz metryk jako?ci.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 98 (markdown)
- Start: `### 5. Full training loop`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 99 (code)
- Start: `def _is_improvement(curr: float, best: float, mode: str) -> bool:`
- Co robi kod: Pe?na p?tla treningowa (early stopping, checkpoint best model, logowanie TensorBoard/CSV).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
- Zapisuje pliki:
  - `to_csv(history_csv_path, index=False)`
  - `torch.save(...)`

### Cell 100 (markdown)
- Start: `### 6. Run baseline training`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 101 (code)
- Start: `device = torch.device(TRAINING_CONFIG['device'])`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 102 (markdown)
- Start: `### 7. Plot training curves and final validation summary`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 103 (code)
- Start: `plt.figure(figsize=(12, 4))`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik wizualny: wykres PNG. Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 104 (markdown)
- Start: `## Shared helpers for Optuna and Top-3`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 105 (code)
- Start: `def build_optimizer(name: str, model: nn.Module, lr: float, weight_decay: float):`
- Co robi kod: Wyliczenie wag klas dla niezbalansowanej klasyfikacji.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 106 (code)
- Start: `train_val_df = pd.concat([train_selected, val_selected], axis=0).sort_values('timestamp').reset_index(drop=True)`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).
