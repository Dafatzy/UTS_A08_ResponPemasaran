# Checklist sebelum pengumpulan UTS — Kelompok A08

## Luaran wajib dosen
- [x] Laporan Milestone 1 tersedia dalam PDF lima BAB: `Laporan_Milestone1_Bank_Marketing_A08.pdf`.
- [x] Notebook eksperimen tersedia: `notebook/Notebook_Eksperimen_Bank_Marketing_FINAL.ipynb`.
- [x] Dataset atau petunjuk sumber tersedia: `data/raw/bank-full.csv`, `data/README_DATASET.md`, dan `VERIFIKASI_DATASET.md`.
- [x] Tabel hasil eksperimen tersedia: `outputs/milestone1_experiment_summary.csv` dan `outputs/report_results_table.csv`.
- [x] Rencana pengembangan pasca-UTS menuju UAS tersedia pada BAB V laporan.

## Pemeriksaan teknis yang telah dilakukan
- [x] Dataset memiliki ukuran 45.211 baris × 17 kolom; target berisi 39.922 `no` dan 5.289 `yes`.
- [x] CSV dalam paket disimpan dengan byte yang SHA-256-nya sama dengan provenance dan metadata run.
- [x] 13 sel kode notebook memiliki execution count; tidak ditemukan output error pada notebook yang disertakan.
- [x] Audit kualitas, empat grafik EDA, temuan, tabel CV, ordered holdout, confusion matrix, kurva PR, dan perbandingan feature engineering tersedia.
- [x] Angka laporan dapat dilacak ke output run pada folder `outputs/`.
- [x] `bank_marketing_outputs.zip` dibuat dari folder `outputs/` yang disertakan.
- [x] README, notebook, downloader, dan direktori data menggunakan path `data/raw/`.
- [x] Manifest SHA-256 dibuat ulang dari isi paket; manifest tidak memasukkan hash dirinya sendiri.
- [x] Sampul mencantumkan Kelompok A08, Program Studi Teknik Informatika, tiga nama anggota, dan NIM.

## Yang hanya perlu dilakukan kelompok bila diwajibkan pedoman kampus
- [ ] Tambahkan nama universitas, fakultas, dan dosen pengampu jika template resmi meminta data tersebut. Informasi ini tidak diisi karena belum diberikan.
- [ ] Setiap anggota membaca laporan dan mampu menjelaskan bagian/kontribusinya, pemilihan fitur, preprocessing, model, metrik, perubahan distribusi, serta batasan validasi.
- [ ] Pastikan PDF final mengikuti ketentuan ukuran kertas dan logo pada template kampus (jika ada ketentuan khusus yang belum diberikan).

## Batasan yang wajib dipahami saat presentasi
Dataset tidak memiliki ID unik nasabah maupun timestamp lengkap per baris. TimeSeriesSplit mempertahankan urutan baris, tetapi tidak menjamin interval kalender antar-fold sama. Proporsi kelas `yes` berubah besar antara training dan holdout. Hasil merupakan eksperimen awal, bukan bukti kausal atau jaminan generalisasi operasional.
