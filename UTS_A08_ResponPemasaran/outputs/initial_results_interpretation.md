# Analisis Hasil Eksperimen Awal (berdasarkan run dataset ini)

## 1. Distribusi target dan baseline
Dataset berisi 45,211 baris. Kelas `no` berjumlah 39,922 (88.302%), sedangkan kelas `yes` berjumlah 5,289 (11.698%). Distribusi tidak seimbang; karena itu accuracy saja tidak cukup. DummyClassifier menjadi pembanding minimum.
Pada cross-validation berbasis urutan, baseline Dummy memperoleh Average Precision 0.0744; kandidat dengan AP CV tertinggi adalah Logistic Regression sebesar 0.1089 (simpangan baku 0.0945). Variasi antar-fold cukup besar sehingga hasil awal perlu dibaca hati-hati.

## 2. Kualitas data
Audit menemukan 0 sel NaN dan 0 baris duplikat penuh. Label literal `unknown` berjumlah 52,124 pada beberapa fitur kategorikal; nilai ini bukan NaN sehingga dipertahankan sebagai kategori. Nilai `pdays=-1` berjumlah 36,954 (81.737%) dan diartikan sebagai belum pernah dihubungi pada kampanye sebelumnya.

## 3. Temuan EDA dan implikasi
Tingkat respons (`y=yes`) menurut `poutcome` berbeda: kategori success 64.73%, other 16.68%, failure 12.61%, dan unknown 9.16%. `poutcome` merupakan riwayat kampanye sebelumnya dan layak dianalisis sebagai prediktor, tetapi asosiasi ini bukan bukti sebab-akibat.
Median usia kelas no adalah 39.0 tahun dan kelas yes 38.0 tahun. Median balance kelas no adalah 417.0, sedangkan kelas yes 733.0. Perbedaan deskriptif tersebut tidak membuktikan pengaruh kausal dan belum tentu cukup untuk memisahkan kelas.

## 4. Perubahan distribusi berdasarkan urutan sumber
Proporsi `yes` pada bagian training 80% awal adalah 6.727%, sedangkan pada holdout 20% akhir adalah 31.582% (selisih +24.855 poin persentase). Ini merupakan perubahan distribusi yang besar. UCI menyebut `bank-full.csv` tersusun berdasarkan tanggal, tetapi tidak menyediakan timestamp lengkap di setiap baris; karena itu pergeseran ini dilaporkan sebagai perubahan menurut urutan baris sumber, bukan sebagai estimasi perubahan pada tanggal kalender tertentu.
Proporsi kelas positif pada sepuluh blok urutan baris bergerak dari 2.99% pada blok pertama menjadi 47.09% pada blok terakhir. Model yang dilatih pada periode awal menghadapi karakteristik target yang berbeda pada holdout akhir. Perbedaan besar antara skor CV dan holdout harus dipahami dalam konteks pergeseran ini.

## Catatan pembacaan Average Precision baseline
Pada ordered holdout, Average Precision DummyClassifier sebesar 0.3158 sama dengan prevalensi kelas yes pada holdout (31.582%). Strategi `most_frequent` memberikan skor konstan untuk kelas positif sehingga Average Precision pada skor yang seluruhnya seri mengikuti prevalensi kelas positif. Karena itu, nilai ini menjadi acuan dasar; kandidat dibandingkan terhadapnya, tetapi hasil tetap harus dibaca bersama perubahan distribusi target dan metrik threshold default.

## 5. Hasil kandidat pada ordered holdout
Holdout melaporkan performa pada bagian akhir data dan tidak digunakan untuk tuning/pemilihan model. Logistic Regression memiliki Average Precision holdout tertinggi di antara model yang diuji, sedangkan Decision Tree memiliki F1 kelas yes tertinggi; perbedaan ini menunjukkan trade-off dan belum cukup untuk menetapkan model final. Recall kelas yes seluruh kandidat masih rendah, sehingga banyak kasus yes terlewat pada threshold default.

                model  accuracy  precision_yes  recall_yes   f1_yes  average_precision   tn  fp   fn  tp
Dummy - most frequent  0.684176       0.000000    0.000000 0.000000           0.315824 6187   0 2856   0
  Logistic Regression  0.694349       0.707207    0.054972 0.102014           0.548281 6122  65 2699 157
        Decision Tree  0.693907       0.555696    0.153711 0.240812           0.472583 5836 351 2417 439
        Random Forest  0.686608       0.576389    0.029062 0.055333           0.463979 6126  61 2773  83

## 6. Dampak feature engineering `pdays`
Average Precision CV Logistic Regression berubah dari 0.107582 (pdays mentah) menjadi 0.108878 (fitur turunan), selisih +0.001297. Perubahan ini kecil dan tidak menunjukkan peningkatan yang kuat. Pertahankan transformasi sebagai eksperimen yang terdokumentasi, tetapi jangan menyatakan bahwa transformasi terbukti meningkatkan model.

## 7. Kesimpulan sementara dan pekerjaan lanjutan
Eksperimen awal berhasil dijalankan, tetapi belum menghasilkan model final yang dapat direkomendasikan. Laporan Milestone 1 pada paket ini telah diselaraskan dengan angka dari run yang sama. Pekerjaan lanjutan menuju UAS adalah (1) menelaah penyebab perubahan distribusi target sepanjang urutan sumber; (2) melakukan analisis sensitivitas dengan protokol stratified random split secara terpisah dan tidak menggantikan evaluasi berurutan; (3) mengevaluasi class weighting serta threshold hanya menggunakan validasi training; (4) melakukan analisis error FP/FN per segmen; dan (5) menguji stabilitas kandidat dengan validasi yang dirancang tanpa menggunakan holdout untuk tuning. Tidak boleh memilih konfigurasi hanya dari skor holdout.