# Status kajian dan arsip

Pembaruan: 4 November 2026.

| Komponen | Hasil terverifikasi |
|---|---|
| Sumber | Financial Management: Theory and Practice, 15e; Cengage 2017; ISBN 978-1-305-63229-5 |
| PDF asli | 18.123.922 byte; 1.221 halaman; tetap tersimpan di repository |
| Teks sumber | Seluruh penanda halaman 1–1.221; 34 bagian Markdown, termasuk 26 bab utama dan lampiran |
| Kajian persamaan bernomor | **Selesai untuk 236 label unik** pada 26 bab utama, termasuk 25 varian a/b; 244 lokasi tampil karena cetak ulang |
| Isi tiap kajian | Rumus LaTeX, variabel, penurunan/rekonsiliasi, syarat, kekeliruan penggunaan, contoh numerik, dan rujukan PDF |
| Pendamping rumus | 44 catatan rasio, rumus tanpa nomor, perhitungan tabel, dan formalisasi konsep |
| Appendix C | Seluruh 13 halaman isi persamaan diperiksa sebagai ringkasan pembanding; tidak dianggap inventaris lengkap bab utama |
| Uji hitung baru | **298/298 lulus**: 280 contoh dan 18 identitas/pemeriksaan lintas metode; tidak ada nomor kajian hilang, berlebih, atau ganda |
| Uji hitung sebelumnya | 42 pemeriksaan contoh dan soal terpilih tetap tersedia terpisah |
| Seluruh soal akhir bab/self-test | **Belum seluruhnya dibahas manual**; pembahasan sebelumnya mencakup sembilan kelompok soal sumber |
| Semua baris aritmetika tanpa nomor/sel spreadsheet | Tidak diklaim diperiksa satu per satu; catatan tambahan mengelompokkan keluarga rumus |
| Rekonstruksi semua tabel dan grafik | Belum selesai; periksa PDF untuk tata letak/visual sumber |
| Web Chapters 27–30, Web Extensions, Excel Tool Kits | Materi eksternal tidak tersedia sebagai berkas mandiri dalam PDF yang diberikan |
| Format dokumentasi | Markdown dengan navigasi GitBook; situs GitBook/Jekyll live belum diterbitkan |
| Publikasi | `git push connected main:main` melalui adaptor GitHub terautentikasi; lihat PUSH_TRANSPORT.md di root |

## Membaca dan menguji kajian

Buka [indeks kajian manual](kajian-rumus/README.md) dan [catatan kritis](kajian-rumus/CATATAN_KRITIS.md). Rujukan nomor halaman menggunakan halaman berkas PDF; pada bab utama nomor cetak = nomor PDF − 37.

```powershell
python verify_formula_review.py --write-report
python verify_calculations.py
```

Perintah dijalankan dari root repository, tanpa jaringan dan tanpa paket Python tambahan. Pemeriksaan numerik menguji contoh yang dinyatakan dan identitas lintas metode; bukan bukti bahwa asumsi model berlaku untuk semua perusahaan.

## Integritas arsip

SHA-256 PDF asli: `1638b312422c14a3b870c27fd16f4498ba5ed3de8cb63ea278ad1ab4862ce56c`.

Unggahan ulang terbaru diperiksa identitas edisi, ISBN, jumlah halaman, ukuran, dan konten terpilih. PDF arsip dipertahankan; pembandingan byte demi byte terhadap objek unggahan ulang tidak diklaim. Teks ekstraksi lama tetap menyimpan struktur per halaman; simbol atau tabel yang rusak dalam ekstraksi harus dirujuk ke PDF dan kajian terpisah.

Koneksi HTTPS langsung terminal ke github.com:443 belum diperbaiki. Adaptor sesi menghubungkan permintaan Git dengan koneksi GitHub yang diotorisasi dan memverifikasi SHA remote sebelum menyatakan push sukses. Login browser tidak otomatis memberi autentikasi Git permanen. Tidak ada password/token disimpan di materi.

## Pembaruan dari dua file kompilasi v2

Sebanyak 197 entri kiriman sudah dipetakan; tersedia 12 kelompok kajian pendamping dan 50 entri dengan penjelasan/koreksi khusus. Seluruh 30 pemeriksaan numerik tambahan lulus, dan 340 pemeriksaan sebelumnya tetap lulus. Kajian lama dipertahankan. Lihat [status integrasi](kompilasi-v2/README.md). Markdown masukan dan ekstraksi lengkap isi Word disertakan. Pada 5 November 2026, berkas Word asli dan Markdown/LaTeX terbaru juga telah ditambahkan; lihat [arsip asli](kompilasi-v2/sumber/unggahan-2026-11-05/README.md). Pekerjaan ini tidak mengubah status penyelesaian seluruh soal buku.
