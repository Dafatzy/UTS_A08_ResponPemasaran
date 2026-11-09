# Peta pemenuhan rubrik Milestone 1 (A–I) — Kelompok A08

| Rubrik | Bukti pada paket | Status audit |
|---|---|---|
| A. Problem formulation | BAB I: latar belakang, masalah klasifikasi biner, alasan, tujuan, target `y`, pendekatan classical ML, skenario prediksi, dan batasan. | Terpenuhi. |
| B. Dataset & data understanding | BAB II, `data/raw/bank-full.csv`, provenance, README dataset, kamus 16 prediktor, 45.211 × 17, unit observasi, target, audit kualitas. | Terpenuhi; bukti asal file didukung checksum silang sekunder, bukan checksum resmi UCI. |
| C. EDA & initial findings | BAB III, statistik deskriptif, distribusi target, `unknown`, `pdays=-1`, response rate `poutcome`, usia/saldo, distribusi target per blok, empat grafik EDA. | Terpenuhi. |
| D. Preprocessing | BAB IV: seleksi fitur pra-kontak, pipeline imputasi/encoding/scaling, penanganan sentinel `pdays`, dan pencegahan leakage per fold. | Terpenuhi dan dieksekusi dalam notebook. |
| E. Initial feature engineering | BAB IV: indikator `previously_contacted`, `days_since_previous_contact`, dan komparasi `pdays` mentah vs turunan. | Terpenuhi; perubahan AP kecil dan belum membuktikan peningkatan kuat. |
| F. Baseline & candidate models | BAB V: DummyClassifier, Logistic Regression, Decision Tree, Random Forest beserta konfigurasi awal. | Terpenuhi; model final memang belum wajib pada Milestone 1. |
| G. Evaluation design | BAB V: ordered holdout 80:20, TimeSeriesSplit 5-fold pada training, Average Precision serta metrik pelengkap. | Terpenuhi dengan keterbatasan timestamp dan jarak waktu yang dijelaskan. |
| H. Initial results & analysis | BAB V, `cross_validation_results.csv`, `test_set_results.csv`, `milestone1_experiment_summary.csv`, confusion matrix, kurva PR, analisis distribution shift. | Terpenuhi untuk eksperimen awal. |
| I. Documentation & next plan | Notebook, README, requirements, downloader, dataset, output CSV/grafik, manifest, checklist, rencana UAS di BAB V. | Terpenuhi; rubrik meminta notebook atau GitHub, sehingga notebook yang dapat dijalankan ulang sudah merupakan luaran yang sesuai. |

## Temuan utama yang harus dapat dijelaskan
1. Dataset berisi 45.211 observasi; kelas `no` 39.922 (88,302%) dan `yes` 5.289 (11,698%).
2. Audit menemukan 0 NaN, 0 baris duplikat penuh, 52.124 label `unknown`, dan 36.954 nilai `pdays=-1`.
3. Response rate `yes` menurut `poutcome`: success 64,73%; other 16,68%; failure 12,61%; unknown 9,16%. Ini asosiasi deskriptif, bukan sebab-akibat.
4. Proporsi `yes` naik dari 6,727% pada training menjadi 31,582% pada ordered holdout.
5. Logistic Regression memiliki Average Precision CV tertinggi (0,1089 ± 0,0945); pada holdout AP tertinggi Logistic Regression (0,5483), sedangkan F1 kelas `yes` tertinggi Decision Tree (0,2408). Tidak ada satu model yang unggul pada seluruh metrik.

## Catatan integritas
Angka berasal dari notebook dan output yang disertakan. File CSV dalam paket dicocokkan dengan SHA-256 yang tercatat pada data card publik sebagai bukti silang sekunder. Data card tersebut bukan penerbit dataset dan bukan checksum resmi UCI; sumber primer yang dirujuk tetap halaman UCI [1].
