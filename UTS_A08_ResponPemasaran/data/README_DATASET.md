# Dataset Bank Marketing

File yang digunakan pada eksperimen: `data/raw/bank-full.csv`.

Sumber yang ditetapkan: [UCI Machine Learning Repository — Bank Marketing, ID 222](https://archive.ics.uci.edu/dataset/222/bank+marketing). Arsip resmi: https://archive.ics.uci.edu/static/public/222/bank+marketing.zip.

Versi yang digunakan adalah `bank-full.csv` (versi penuh legacy): 45.211 observasi, 16 prediktor, dan satu target `y` (17 kolom total). Delimiter CSV adalah titik koma (`;`). Jangan menggantinya dengan `bank.csv` (sampel) atau `bank-additional-full.csv` (versi lain dengan jumlah fitur berbeda).

File di paket ini berukuran 4.610.348 byte dan memiliki SHA-256:

```text
d1513ec63b385506f7cfce9f2c5caa9fe99e7ba4e8c3fa264b3aaf0f849ed32d
```

Hash tersebut cocok dengan checksum pada data card publik pihak ketiga yang mencatat pengambilan melalui HTTPS dari arsip resmi UCI. Ini adalah verifikasi silang sekunder, bukan checksum resmi UCI. Arsip ZIP UCI dari unduhan kelompok tidak disimpan bersama paket, sehingga tingkat bukti asal file dijelaskan secara transparan pada `data/raw/dataset_provenance.json` dan `VERIFIKASI_DATASET.md`.

Untuk memperoleh ulang file secara langsung dari UCI, jalankan `python download_dataset.py` dari root proyek. Skrip mengunduh arsip resmi, mengekstrak `bank-full.csv` dari `bank.zip`, memvalidasi jumlah baris dan skema, lalu membuat provenance baru.

Lisensi yang tercantum pada halaman UCI adalah CC BY 4.0. Cantumkan atribusi Moro, Rita, dan Cortez (2014).
