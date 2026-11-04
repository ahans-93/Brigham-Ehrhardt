# Bab 20: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../20-chapter.md)

## Navigasi

- [20-1: Pemisahan obligasi dengan warrant](#rumus-20-1)
- [20-2: Harga konversi](#rumus-20-2)
- [20-3: Rasio konversi](#rumus-20-3)
- [20-4: Nilai straight debt convertible](#rumus-20-4)
- [U-20-01: Conversion value dan warrant intrinsic value](#rumus-u-20-01)

<a id="rumus-20-1"></a>
## 20-1 — Pemisahan obligasi dengan warrant

[PDF 862](../Financial_Management_Theory_and_Practice_15e.pdf#page=862)

$$
P_{package}=B_{straight}+W_{package}
$$

**Variabel.** Bstraight: nilai obligasi tanpa warrant; Wpackage: nilai semua warrant dalam paket.

**Penurunan dan logika.** Harga paket adalah penjumlahan nilai klaim yang dapat dipisahkan; nilai warrant menjadi residual.

**Syarat penggunaan.** Harga kedua komponen pada tanggal dan basis yang sama.

**Kekeliruan yang perlu dihindari.** Residual semua warrant dibagi jumlah warrant untuk mendapat nilai per warrant.

**Contoh hitung.** Harga 1.000, obligasi 829,728726: warrant total 170,271274.

```python
1000-bond(80,1000,.10,20)
```
Hasil presisi mesin: `170.271274395`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-20-2"></a>
## 20-2 — Harga konversi

[PDF 867](../Financial_Management_Theory_and_Practice_15e.pdf#page=867)

$$
P_c=\frac{Par}{CR}
$$

**Variabel.** Par: nilai nominal obligasi; CR: saham yang diterima per obligasi.

**Penurunan dan logika.** Harga konversi adalah nominal yang dikorbankan untuk setiap saham.

**Syarat penggunaan.** Gunakan rasio konversi yang berlaku sesudah penyesuaian kontrak.

**Kekeliruan yang perlu dihindari.** Pc bukan harga pasar obligasi dibagi saham.

**Contoh hitung.** Par 1.000, CR 18: Pc 55,555556.

```python
1000/18
```
Hasil presisi mesin: `55.5555555556`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-20-3"></a>
## 20-3 — Rasio konversi

[PDF 868](../Financial_Management_Theory_and_Practice_15e.pdf#page=868)

$$
CR=\frac{1000}{P_c}\quad\text{(par 1000)}
$$

**Variabel.** Pc: harga konversi; untuk nominal lain ganti 1.000 dengan Par.

**Penurunan dan logika.** Susun ulang 20-2 untuk CR.

**Syarat penggunaan.** Nilai nominal dan mata uang konsisten.

**Kekeliruan yang perlu dihindari.** Angka 1.000 pada sumber adalah nominal contoh, bukan konstanta semua obligasi.

**Contoh hitung.** Nominal 1.000, Pc 50: CR 20 saham.

```python
1000/50
```
Hasil presisi mesin: `20`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-20-4"></a>
## 20-4 — Nilai straight debt convertible

[PDF 869](../Financial_Management_Theory_and_Practice_15e.pdf#page=869)

$$
B_0=\sum_{t=1}^{N}\frac{I}{(1+r_d)^t}+\frac{M}{(1+r_d)^N}
$$

**Variabel.** I: kupon per periode; M: nominal jatuh tempo; rd: yield utang serupa tanpa hak konversi.

**Penurunan dan logika.** Diskontokan pembayaran kontraktual sebagai obligasi biasa; hak konversi dinilai terpisah.

**Syarat penggunaan.** Risiko kredit dan tenor pembanding sebanding; sesuaikan frekuensi kupon.

**Kekeliruan yang perlu dihindari.** Jangan memakai yield convertible yang sudah mencakup nilai opsi sebagai rd obligasi biasa.

**Contoh hitung.** Kupon 80, nominal 1.000, rd 10%,20 tahun: B 0829,728726.

```python
bond(80,1000,.10,20)
```
Hasil presisi mesin: `829.728725605`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-20-01"></a>
## U-20-01 — Conversion value dan warrant intrinsic value

[PDF 861](../Financial_Management_Theory_and_Practice_15e.pdf#page=861) · [PDF 862](../Financial_Management_Theory_and_Practice_15e.pdf#page=862) · [PDF 868](../Financial_Management_Theory_and_Practice_15e.pdf#page=868) · [PDF 869](../Financial_Management_Theory_and_Practice_15e.pdf#page=869)

$$
CV=CR\,S,\quad W_{intrinsic}=\max(S-K,0)
$$

**Variabel.** CR: saham per obligasi; S: harga saham; K: exercise price per warrant untuk satu saham.

**Penurunan dan logika.** Konversi menyerahkan obligasi untuksaham; warrant melibatkan pembayaran kas exercise sehingga payoff berbeda.

**Syarat penggunaan.** Periksa jumlah saham per warrant dan dilusi; nilai intrinsik tidak memasukkan nilai waktu.

**Kekeliruan yang perlu dihindari.** Convertible tidak selalu sama denganstraight bond+call sederhana karena callability, credit, dan interaksi konversi.

**Contoh hitung.** CR 20, S 60: conversion value 1.200.

```python
20*60
```
Hasil presisi mesin: `1200`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
