# Paket UTS Machine Learning — Milestone 1: Bank Marketing (Kelompok A08)

## Status paket
Paket ini berisi laporan DOCX/PDF lima BAB, notebook eksperimen yang menyimpan output eksekusi, CSV `bank-full.csv`, artefak EDA/evaluasi, arsip output, dokumentasi, dan checklist. Angka pada laporan dapat ditelusuri ke file CSV dalam `outputs/`.

**Catatan data:** file yang disertakan berukuran 4.610.348 byte, berbentuk 45.211 × 17, dan SHA-256-nya cocok dengan checksum pada data card publik pihak ketiga yang merekam pengambilan melalui HTTPS dari arsip UCI. Ini merupakan verifikasi silang sekunder, bukan checksum resmi UCI. Detail lengkap ada di `VERIFIKASI_DATASET.md` dan `data/raw/dataset_provenance.json`.
## A08 ResponPemesanan
anggota Kelompok:
- M.Alief Mufthi – 231111319 
- Dafa Aditya Nazwan Priyadi – 231111548 
- M.Sendy Aulia – 231111455

## Isi paket
- `Laporan_Milestone1_Bank_Marketing_A08.docx` — laporan editable, lima BAB.
- `Laporan_Milestone1_Bank_Marketing_A08.pdf` — PDF laporan yang dikumpulkan.
- `notebook/Notebook_Eksperimen_Bank_Marketing_FINAL.ipynb` — notebook dengan 13 sel kode yang telah dieksekusi dan tanpa output error.
- `data/raw/bank-full.csv` — dataset mentah yang dianalisis.
- `data/raw/dataset_provenance.json` — ukuran, target, SHA-256, dan tingkat verifikasi sumber.
- `data/README_DATASET.md` — keterangan versi dan cara memperoleh dataset.
- `outputs/` — audit, EDA, hasil CV, ordered holdout, perbandingan fitur, grafik, interpretasi, dan manifest output.
- `bank_marketing_outputs.zip` — arsip isi folder `outputs/`.
- `download_dataset.py`, `requirements.txt` — alat unduh dan dependensi.
- `PETA_RUBRIK_A-I.md`, `CHECKLIST_PENGUMPULAN.md` — peta pemenuhan rubrik dan pengecekan pengumpulan.
- `references/REFERENSI.md` — referensi yang dipakai, termasuk data card sekunder yang dirujuk untuk checksum.
- `MANIFEST_SHA256.csv` — hash seluruh file paket selain manifest itu sendiri.

## Dataset dan skenario
- Sumber primer: [UCI Bank Marketing, dataset ID 222](https://archive.ics.uci.edu/dataset/222/bank+marketing).
- Versi: `bank-full.csv`, bukan `bank.csv` sampel atau `bank-additional-full.csv`.
- Ukuran: 45.211 baris × 17 kolom (16 prediktor + target `y`).
- Delimiter: titik koma (`;`).
- Target: `y`; `no` = 0 dan `yes` = 1.
- Lisensi UCI: CC BY 4.0; cantumkan atribusi Moro, Rita, dan Cortez (2014).

## Metodologi utama
- Supervised binary classification pada data tabular.
- Skenario prediksi: sebelum kontak telemarketing saat ini dilakukan.
- Fitur yang dikeluarkan dari model inti: `duration`, `campaign`, `day`, `month`, dan `contact`, karena nilainya merekam kontak/kampanye saat ini atau belum tentu tersedia sebelum kontak.
- Feature engineering: `pdays` menjadi indikator status pernah dihubungi dan jumlah hari valid.
- Preprocessing: `Pipeline`/`ColumnTransformer`, one-hot encoding, imputasi jika diperlukan, dan scaling numerik untuk Logistic Regression.
- Baseline: DummyClassifier (`most_frequent`). Kandidat: Logistic Regression, Decision Tree, dan Random Forest.
- Split: 80% awal menurut urutan baris untuk training, 20% akhir untuk ordered holdout. CV: TimeSeriesSplit 5-fold pada training.
- Metrik utama awal: Average Precision kelas `yes`; pelengkap: precision, recall, F1, balanced accuracy, ROC-AUC, accuracy, confusion matrix.

## Temuan utama run yang dilaporkan
- Target: `no` 39.922 (88,302%); `yes` 5.289 (11,698%).
- Audit: 0 NaN, 0 duplikat penuh, 52.124 label `unknown`, dan 36.954 baris `pdays=-1`.
- Proporsi `yes` pada training 6,727%; holdout 31,582%.
- Logistic Regression memiliki Average Precision CV tertinggi (0,1089 ± 0,0945). Pada holdout, AP tertinggi Logistic Regression (0,5483), sedangkan F1 kelas `yes` tertinggi Decision Tree (0,2408). Belum ditetapkan model final.
- Perubahan prevalensi di sepanjang urutan sumber membatasi interpretasi hasil. CSV tidak memuat timestamp lengkap per baris.

## Cara menjalankan ulang (Google Colab)
1. Unggah notebook dari `notebook/` ke Google Colab.
2. Unggah `bank-full.csv` ketika diminta, atau biarkan notebook mencoba mengunduh arsip UCI.
3. Pilih `Runtime > Run all`.
4. Pastikan ukuran 45.211 × 17, distribusi target, dan validasi skema sesuai.
5. Unduh folder `outputs/` atau `bank_marketing_outputs.zip`.

## Cara menjalankan ulang (lokal)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python download_dataset.py
```
Buka notebook dari folder `notebook/` dengan working directory root proyek. Notebook dan downloader menggunakan `data/raw/bank-full.csv`.

## Batasan penting
- TimeSeriesSplit menjaga urutan baris, tetapi jarak waktu antarbaris tidak dapat dipastikan setara karena tidak ada timestamp lengkap.
- Tidak tersedia ID unik untuk memastikan identitas nasabah lintasbaris.
- Distribusi target berubah besar antara bagian awal dan akhir urutan data.
- Dataset berasal dari satu institusi dan kampanye historis di Portugal; generalisasi ke bank/negara/periode lain belum dibuktikan.
- Hasil klasifikasi bukan bukti kausal peningkatan keuntungan atau efektivitas kampanye.

## Identitas dan tanggung jawab kelompok
Sampul sudah mencantumkan Kelompok A08, Program Studi Teknik Informatika, dan nama/NIM tiga anggota. Nama universitas, fakultas, atau dosen pengampu hanya perlu ditambahkan jika template resmi kampus mewajibkannya. Semua anggota harus memahami dan dapat menjelaskan kontribusi masing-masing.
