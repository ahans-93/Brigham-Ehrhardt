# Kajian manual persamaan — Brigham & Ehrhardt 15e

[Daftar isi buku](../SUMMARY.md) · [Catatan koreksi dan konvensi](CATATAN_KRITIS.md)

**236 persamaan bernomor unik**, termasuk 25 varian a/b, diperiksa dari tampilan PDF dan dikaji satu per satu. Ada 244 lokasi tampil karena beberapa persamaan dicetak ulang. **44 keluarga rumus tambahan** membahas rasio tanpa nomor, perhitungan tabel, serta formalisasi konsep pada bab yang tidak memiliki persamaan bernomor.

Setiap entri memuat persamaan LaTeX, arti variabel, penurunan atau rekonsiliasi, syarat, kesalahan penggunaan, dan contoh numerik. Angka contoh baru dipilih untuk menguji mekanisme; contoh substitusi sumber ditandai dalam uraian. Contoh bukan salinan seluruh soal akhir bab.

Rujukan PDF memakai nomor halaman berkas (1–1.221), bukan nomor cetak. Untuk bab utama, halaman cetak = halaman PDF − 37. Klik rujukan PDF atau cari halaman tersebut pada PDF asli. Rujukan keluarga tanpa nomor adalah konteks pembahasan; beberapa formula diberi bentuk matematis oleh penyusun dan dilabeli demikian.

## Peta cakupan

| Bab | Bernomor | Keluarga tambahan | Kajian |
|---|---:|---:|---|
| 1 | 1 | 0 | [Bab 1](bab-01.md) |
| 2 | 20 | 0 | [Bab 2](bab-02.md) |
| 3 | 3 | 14 | [Bab 3](bab-03.md) |
| 4 | 15 | 3 | [Bab 4](bab-04.md) |
| 5 | 9 | 1 | [Bab 5](bab-05.md) |
| 6 | 20 | 1 | [Bab 6](bab-06.md) |
| 7 | 23 | 0 | [Bab 7](bab-07.md) |
| 8 | 13 | 1 | [Bab 8](bab-08.md) |
| 9 | 13 | 0 | [Bab 9](bab-09.md) |
| 10 | 6 | 2 | [Bab 10](bab-10.md) |
| 11 | 0 | 6 | [Bab 11](bab-11.md) |
| 12 | 5 | 0 | [Bab 12](bab-12.md) |
| 13 | 0 | 1 | [Bab 13](bab-13.md) |
| 14 | 3 | 2 | [Bab 14](bab-14.md) |
| 15 | 22 | 0 | [Bab 15](bab-15.md) |
| 16 | 7 | 1 | [Bab 16](bab-16.md) |
| 17 | 5 | 1 | [Bab 17](bab-17.md) |
| 18 | 5 | 1 | [Bab 18](bab-18.md) |
| 19 | 1 | 1 | [Bab 19](bab-19.md) |
| 20 | 4 | 1 | [Bab 20](bab-20.md) |
| 21 | 33 | 0 | [Bab 21](bab-21.md) |
| 22 | 3 | 1 | [Bab 22](bab-22.md) |
| 23 | 0 | 4 | [Bab 23](bab-23.md) |
| 24 | 0 | 2 | [Bab 24](bab-24.md) |
| 25 | 23 | 0 | [Bab 25](bab-25.md) |
| 26 | 2 | 1 | [Bab 26](bab-26.md) |

## Audit cakupan dan hitung

- Status hitung: **PASS**, 298 pemeriksaan numerik dan identitas lintas metode.
- [Data kajian](formula-review.json): seluruh uraian, ekspresi perhitungan, dan hasil pembanding.
- [Lokasi persamaan](equation-locations.json): nomor, halaman, dan posisi label di PDF, termasuk cetak ulang.
- [Hasil verifikasi](verification-results.json): hasil tiap contoh dan identitas; tidak ada nomor yang hilang, berlebih, atau ganda.
- Jalankan `python verify_formula_review.py --write-report` dari root repository. Hanya memakai Python standard library, tanpa jaringan.

## Metode dan batas cakupan

Label persamaan ditelusuri pada margin kanan seluruh halaman bab utama PDF 40–1.077, lalu tampilan persamaan diperiksa. Perluasan pencarian mencakup akhiran a/b; nomor yang tercetak ulang tidak dianggap rumus baru. Kajian ditulis manual berdasarkan bentuk persamaan dan konteks, bukan diturunkan otomatis dari OCR. Script hanya menyusun dokumen dari catatan kurasi dan menghitung ulang angka.

Cakupan selesai yang dapat diaudit adalah seluruh 236 label persamaan bernomor yang ditemukan di 26 bab utama. Keluarga tambahan memperluas pembahasan, tetapi bukan klaim bahwa setiap baris aritmetika tanpa nomor, setiap sel spreadsheet, tabel, grafik, atau seluruh solusi soal telah ditulis ulang satu per satu. Appendix C telah diperiksa sebagai ringkasan pembanding; Appendix A/B memuat penerapan ulang dan jawaban, bukan inventaris rumus baru. Bab web 27–30 dan Excel Tool Kits tidak ada sebagai berkas terpisah dalam PDF ini.

Hasil numerik yang lulus menguji contoh serta identitas yang dinyatakan; itu tidak menggantikan penilaian asumsi ekonomi. Gunakan catatan kritis khusus untuk 2-7, 2-12a, 8-4/5, 21-6/8, 25-16, dan 26-1.
