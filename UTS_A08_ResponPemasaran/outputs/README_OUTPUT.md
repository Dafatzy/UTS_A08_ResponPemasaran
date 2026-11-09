# Artefak hasil eksperimen

Folder ini berisi output dari eksekusi notebook terhadap `data/raw/bank-full.csv` yang tercatat pada `data/raw/dataset_provenance.json` dan `run_metadata.json`.

- `audit_schema.csv`: nama kolom, tipe, dan validasi struktur.
- `target_distribution.csv`: jumlah/persentase kelas `no` dan `yes`.
- `quality_summary.csv`, `missing_by_column.csv`, `unknown_counts.csv`, `outlier_summary_iqr.csv`: audit kualitas data.
- `numeric_descriptive_statistics.csv`: statistik deskriptif numerik.
- `eda_initial_findings.csv`, `response_rate_by_poutcome.csv`, `target_rate_by_row_block.csv`: temuan EDA.
- `cross_validation_results.csv`: mean dan simpangan baku metrik pada TimeSeriesSplit 5-fold berbasis urutan baris.
- `test_set_results.csv`: metrik ordered holdout dan TN/FP/FN/TP.
- `milestone1_experiment_summary.csv`, `report_results_table.csv`: tabel komparasi untuk dirujuk laporan.
- `feature_engineering_comparison.csv`: perbandingan `pdays` mentah dan turunan.
- `ordered_split_summary.csv`, `ordered_cv_split_diagnostics.csv`: ukuran dan distribusi target per split/fold.
- `figures/`: grafik EDA, confusion matrix, precision-recall, dan perubahan proporsi target.
- `initial_results_interpretation.md`: interpretasi berbasis angka dari run ini.
- `run_metadata.json`, `manifest.csv`: informasi run, versi lingkungan, dan hash artefak.

Seluruh metrik yang dikutip pada laporan harus berasal dari satu run yang sama. Jika notebook dijalankan ulang, jangan mencampur output lama dan baru. Pastikan status eksperimen bernilai `completed` sebelum mengutip hasil.
