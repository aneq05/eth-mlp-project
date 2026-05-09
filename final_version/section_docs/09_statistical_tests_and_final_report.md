# Sekcja 09 - Statistical tests and final report

- Zakres komorek w notebooku: `129` -> `142`

## Pliki i artefakty tej sekcji
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\stat_tests_summary.csv` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\stat_tests_summary.json` (istnieje)
- `C:\Users\ankap\OneDrive\Desktop\PROJEKTY\nn\eth-mlp-project\reports\final_ensemble_ranking.csv` (istnieje)

## Wyniki liczbowe / raporty (jesli dostepne)
### `stat_tests_summary.csv`
```text
pair,f1_mean_diff,f1_ci_low,f1_ci_high,balacc_mean_diff,balacc_ci_low,balacc_ci_high,acc_mean_diff,acc_ci_low,acc_ci_high,mcnemar_n01,mcnemar_n10,mcnemar_chi2,mcnemar_p,mcnemar_p_holm,mcnemar_significant_0_05,f1_diff_significant_by_ci,balacc_diff_significant_by_ci,acc_diff_significant_by_ci
rank1_vs_rank2,0.0209914525451512,0.00952485484893875,0.03236913701797281,0.005950659469275903,-0.006156746446532152,0.01729922221559291,0.042264879665657874,0.03040783974636113,0.05419008502666084,1012,719,49.257076834199886,2.245204022699454e-12,6.735612068098362e-12,True,True,False,True
rank1_vs_rank3,0.006854541161760293,-0.0019584489209521325,0.015715588433048957,-0.009335280436643249,-0.018197008253903316,-0.00031866872308186726,0.009556420233463037,0.0010051880674448567,0.01801772589710332,464,400,4.59375,0.0320887339782312,0.0320887339782312,True,False,True,True
rank2_vs_rank3,-0.014136911383390903,-0.025656057392253274,-0.0029276182620708705,-0.015285939905919154,-0.027059421686187135,-0.0030316672467542655,-0.032708459432194845,-0.04424268626603256,-0.020604553970312744,755,984,29.89304197814836,4.565482880636296e-08,9.130965761272591e-08,True,True,True,True
```

## Komorka po komorce

### Cell 129 (markdown)
- Start: `## 09 - Statistical tests and final report`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 130 (code)
- Start: `metrics_df = pd.read_csv(REPORTS_PATH + 'top3_ensemble_metrics.csv').sort_values('rank').reset_index(drop=True)`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 131 (markdown)
- Start: `### 1. Load ensemble predictions (3 sets) and align timestamps`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 132 (code)
- Start: `def load_ensemble_predictions(rank: int, run_id: str) -> pd.DataFrame:`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 133 (markdown)
- Start: `### 2. Helper functions: bootstrap, McNemar, Holm correction`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 134 (code)
- Start: `def bootstrap_metric_difference(`
- Co robi kod: Definicja test?w statystycznych (bootstrap, McNemar, Holm correction).
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Brak outputu (komorka definicyjna lub przygotowawcza).

### Cell 135 (markdown)
- Start: `### 3. Pairwise statistical comparison between 3 ensembles`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 136 (code)
- Start: `y_true = preds[1]['y_true'].to_numpy(dtype=np.int64)`
- Co robi kod: Por?wnanie par modeli ensemble i estymacja istotno?ci r??nic.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 137 (markdown)
- Start: `### 4. Multiple-comparison correction (Holm)`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 138 (code)
- Start: `adj = holm_correction(mcnemar_pvals)`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 139 (markdown)
- Start: `### 5. Final ranking summary`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 140 (code)
- Start: `rank_metrics = metrics_df[['rank', 'trial_number', 'test_f1_macro', 'test_balanced_accuracy', 'test_accuracy']].copy()`
- Co robi kod: Wykonanie kroku pomocniczego w ramach bie??cej sekcji pipeline.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).

### Cell 141 (markdown)
- Start: `### 6. Save statistical report artifacts`
- Rola: opis metodologii / komentarz interpretacyjny / naglowek etapu.
- Znaczenie: pomaga powiazac kod z wymaganiami projektu i interpretacja wynikow.

### Cell 142 (code)
- Start: `STAT_CSV = REPORTS_PATH + 'stat_tests_summary.csv'`
- Co robi kod: Zapis ko?cowych raport?w statystycznych i rankingu modeli.
- Jak to jest wyliczane: krok proceduralny (przeksztalcenie danych / trenowanie / zapis), bez osobnego wzoru matematycznego w tej komorce.
- Wynik uruchomienia: Wynik tabelaryczny/wizualny: HTML (np. Styler).
- Zapisuje pliki:
  - `to_csv(RANKING_CSV, index=False)`
  - `to_csv(STAT_CSV, index=False)`
