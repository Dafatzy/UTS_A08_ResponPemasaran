# Catatan verifikasi dataset

## Dataset yang digunakan
- File: `data/raw/bank-full.csv`
- Sumber primer proyek: UCI Bank Marketing, dataset ID 222 — https://archive.ics.uci.edu/dataset/222/bank+marketing
- Versi: `bank-full.csv` (legacy full)
- Bentuk: 45.211 baris × 17 kolom (16 prediktor + target `y`)
- Ukuran file: 4,610,348 byte
- SHA-256: `d1513ec63b385506f7cfce9f2c5caa9fe99e7ba4e8c3fa264b3aaf0f849ed32d`
- Target: `no` = 39.922 dan `yes` = 5.289

## Tingkat bukti sumber
1. Struktur, ukuran, nama kolom, label target, dan hash file telah diperiksa pada salinan yang disertakan.
2. SHA-256 di atas cocok persis dengan checksum pada data card publik pihak ketiga yang mencatat pengambilan file melalui HTTPS dari arsip resmi UCI: https://github.com/raederhans/ca6003-bankmarketing/blob/main/notes/data_card.md.
3. Data card tersebut merupakan bukti silang sekunder, bukan checksum resmi yang diterbitkan atau ditandatangani UCI. Arsip ZIP yang diunduh kelompok tidak disimpan pada run ini. Oleh karena itu, paket tidak menyatakan autentikasi sumber resmi yang lebih kuat daripada bukti yang tersedia.

## Catatan integritas
CSV disertakan dalam byte asli yang hash-nya cocok dengan provenance dan metadata run. Jangan mengedit atau menyimpan ulang CSV dari spreadsheet karena perubahan line ending/encoding dapat mengubah SHA-256. Bila dibutuhkan bukti akuisisi primer, unduh arsip resmi dari URL UCI di atas dan jalankan `python download_dataset.py`; skrip membuat provenance baru termasuk hash ZIP sumber.
