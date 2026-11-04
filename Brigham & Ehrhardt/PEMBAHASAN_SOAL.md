# Pembahasan ulang soal sumber dan pemeriksaan hitung

[Daftar isi](SUMMARY.md) · [Register rumus](RUMUS_DAN_DERIVASI.md) · [Appendix A sumber](27-appendix-a.md)

Bagian ini membahas ulang beberapa soal asli yang data dan solusinya terbaca pada sumber. Ini bukan kunci jawaban lengkap seluruh soal buku. Input diambil dari bab terkait dan Appendix A; langkah dihitung ulang dengan Python pada pemeriksaan numerik. Nomor halaman di sini adalah halaman PDF, bukan nomor halaman cetak. Tidak ada angka tarif pajak ilustratif yang diperlakukan sebagai ketentuan pajak saat ini.

## Bab 2, ST-1: Cole Furnaces — PDF 1078

Data dalam jutaan dolar: EBIT 5; D&A 1; bunga 1; tarif pajak soal 40%; aset lancar operasi 14; kewajiban lancar operasi 4; aset operasi jangka panjang 15; modal operasi tahun sebelumnya 24; WACC 10%.

1. EBT = EBIT − bunga = 5 − 1 = 4.
2. Pajak laba dalam model = 40% × 4 = 1,6; NI = 4 − 1,6 = **2,4**.
3. NCF sederhana = NI + D&A = 2,4 + 1 = **3,4**.
4. NOPAT = EBIT(1 − T) = 5 × 60% = **3**.
5. NOWC = 14 − 4 = **10**; modal operasi total = 10 + 15 = **25**.
6. Investasi neto modal operasi = 25 − 24 = **1**.
7. FCF = 3 − 1 = **2**.
8. ROIC menggunakan basis modal dalam soal = 3 / 25 = **12%**.
9. EVA = 3 − 25 × 10% = **0,5**.

NI berbeda dari NOPAT karena NI sudah mengandung pengaruh bunga. NCF sederhana berbeda dari FCF karena FCF memperhitungkan investasi operasi. Menambahkan D&A kembali sekaligus memakai perubahan aset operasi neto tanpa penyesuaian yang konsisten dapat menggandakan penyesuaian depresiasi.

## Bab 3, ST-1: Argent — PDF 1078–1079

Utang berbunga 120; seluruh liabilities 150; common equity 210, semuanya jutaan. Total aset = liabilities + equity = **360**. Debt/assets = 120/360 = **33,3333%**. Debt/equity = 120/210 = **57,1429%**.

Jika 150 dipakai sebagai numerator debt/assets, hasilnya 41,6667%, tetapi itu merupakan liabilities/assets. Perbedaan definisi numerator adalah inti soal, bukan pembulatan.

## Bab 3, ST-2: merekonstruksi neraca dan DuPont — PDF 1079–1080

Data dalam jutaan: penjualan 14.600; DSO 40 hari; cash 400; quick ratio 2; current ratio 3; net fixed assets 4.300; NI 730; ROE 12,5%.

| Langkah | Perhitungan | Hasil |
|---|---|---:|
| AR | 40 × 14.600 / 365 | 1.600 |
| CL | (cash + AR) / quick ratio | 1.000 |
| CA | current ratio × CL | 3.000 |
| Inventory, dengan komposisi CA sederhana soal | CA − cash − AR | 1.000 |
| Assets | CA + net fixed assets | 7.300 |
| ROA | 730 / 7.300 | 10% |
| Equity | 730 / 12,5% | 5.840 |
| Long-term debt, sesuai klaim dalam soal | 7.300 − 1.000 − 5.840 | 460 |
| Equity multiplier | 7.300 / 5.840 | 1,25 |
| Net margin | 730 / 14.600 | 5% |
| Asset turnover | 14.600 / 7.300 | 2 kali |

Pemeriksaan DuPont: 5% × 2 × 1,25 = **12,5%**, sama dengan ROE input. Pemeriksaan neraca: 1.000 + 460 + 5.840 = **7.300**. Rekonstruksi inventory dan long-term debt di atas mengikuti komposisi sederhana soal, bukan asumsi umum bahwa semua perusahaan hanya memiliki akun-akun tersebut.

## Bab 4, ST-1: garis waktu dan compounding — PDF 1080–1081

### a. Satu setoran tumbuh dari tahun 1 ke tahun 4

Setoran 1.000 pada tahun 1, bunga tahunan 8%, dinilai pada tahun 4. Jumlah periode adalah 4 − 1 = **3**, bukan 4. FV = 1.000 × 1,08³ = **1.259,712**, dibulatkan **1.259,71**.

### b. Nominal 8% dengan compounding kuartalan

Untuk jangka tiga tahun yang sama: bunga per kuartal 8%/4 = 2%; jumlah periode 3 × 4 = 12. FV = 1.000 × 1,02¹² = **1.268,2418**, dibulatkan **1.268,24**. Nilainya melebihi compounding tahunan karena bunga memperoleh bunga lebih sering.

### c. Empat setoran akhir tahun sebesar 250

FV pada akhir tahun keempat = 250 × [(1,08⁴ − 1)/0,08] = **1.126,528**, dibulatkan **1.126,53**. Setoran pertama memperoleh bunga tiga tahun, yang terakhir tidak memperoleh bunga sebelum tanggal penilaian.

### d. Setoran tahunan untuk mencapai 1.259,712

PMT = 1.259,712 / [(1,08⁴ − 1)/0,08] = **279,5563**, dibulatkan **279,56**. Keempat setoran dimulai pada akhir tahun pertama; jangan memakai faktor anuitas due.

## Bab 4, ST-2: menyamakan tanggal pembanding — PDF 1081–1083

Untuk mencapai 1.000 pada tahun 4 melalui setoran tunggal pada tahun 1 dengan bunga 8%: PV pada tahun 1 = 1.000/1,08³ = **793,8322**.

Alternatif empat setoran akhir tahun 1–4: PMT = 1.000/[(1,08⁴ − 1)/0,08] = **221,9208**. Nilai sekarang keempat setoran pada tahun 0 adalah **735,0299**, tetapi nilainya pada tahun 1 adalah 735,0299 × 1,08 = **793,8322**.

Tawaran 750 yang dibayar pada tahun 1 harus dibandingkan dengan 793,8322 pada tahun 1. Membandingkannya dengan 735,0299 pada tahun 0 mencampur tanggal dan memberi kesimpulan salah. Pada tahun 4, 750 × 1,08³ = **944,784**, belum mencapai 1.000.

Tingkat bunga untuk mengubah 750 pada tahun 1 menjadi 1.000 pada tahun 4: (1.000/750)^(1/3) − 1 = **10,0642%**.

## Bab 4, ST-3: ekuivalensi quoted rates — PDF 1083

Bank A menawarkan nominal 8%, compounding kuartalan. EAR = 1,02⁴ − 1 = **8,243216%**. Agar bank B dengan compounding bulanan setara:

$$APR_B=12[(1+0.08243216)^{1/12}-1]$$

Hasilnya **7,9472515%**, sekitar **7,95%** jika memakai angka EAR penuh. Teks solusi sumber menampilkan sekitar 7,94% karena pembulatan hasil antara. Selisih tersebut dicatat, bukan dipaksa sama dengan menurunkan presisi perhitungan. Menggunakan 8,24% yang sudah dibulatkan sebagai EAR memberi sekitar 7,9443%.

## Bab 5, ST-1 bagian b–c: obligasi premium — PDF 1083–1084

Nominal 1.000; kupon tahunan 12% dibayar semesteran; sisa 25 tahun; quoted YTM 10% nominal dengan periode semester. C = 60; y = 5%; n = 50.

$$P=60\frac{1-1.05^{-50}}{0.05}+1000(1.05)^{-50}$$

Harga = **1.182,5593**, dibulatkan **1.182,56**. Current yield = 120/1.182,5593 = **10,1475%**. Perbedaan dengan quoted YTM 10% sesuai dengan obligasi premium yang bergerak menuju par dalam kondisi yield tetap. Kutipan current-yield-plus-capital-gain dalam sumber merupakan pemisahan yield model; untuk return holding-period aktual gunakan kas dan harga pada tanggal yang benar.

## Bab 6, ST-2: beta portofolio dan CAPM — PDF 1086

Bobot awal 60%, 25%, 10%, 5%; beta masing-masing 0,70, 0,90, 1,30, 1,50. Beta portofolio = 0,60×0,70 + 0,25×0,90 + 0,10×1,30 + 0,05×1,50 = **0,85**.

Dengan risk-free 6% dan premium pasar 5% sesuai input soal, required return = 6% + 0,85×5% = **10,25%**.

Setelah bobot menjadi 50%, 25%, 10%, 15%, beta = **0,93**, dan required return = **10,65%**. Return yang diminta naik 0,40 poin persentase karena porsi aset beta tinggi bertambah. Hasil tersebut bukan ramalan bahwa realisasi return pasti naik sebesar itu.

## Bab 7, ST-1: mencari pertumbuhan dividen — PDF 1086

P0 = 36; D0 = 2,40; required return 12%. Gunakan dividen berikutnya, sehingga:

$$36=\frac{2.40(1+g)}{0.12-g}$$

36×0,12 − 36g = 2,40 + 2,40g, sehingga 1,92 = 38,40g dan **g = 5%**. Dengan kebijakan dan parameter yang tetap, harga ekspektasian pada tahun 5 = 36×1,05⁵ = **45,9461**, dibulatkan **45,95**. Ini adalah harga pada tahun 5, belum termasuk dividen yang diterima selama lima tahun dalam penghitungan total return.

## Batas pembahasan

Pembahasan di atas baru mencakup sembilan kelompok soal sumber. Appendix A memuat solusi self-test lain dan Appendix B memuat jawaban akhir soal terpilih. Keduanya sudah disimpan sebagai teks sumber, tetapi tidak boleh dinyatakan sebagai pembahasan langkah demi langkah yang baru diverifikasi untuk seluruh soal. INVENTARIS_SUMBER.md menyediakan lokasi kandidat nomor dan self-test agar pekerjaan lanjutan dapat dilacak.
