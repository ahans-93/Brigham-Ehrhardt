# Bab 16: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../16-chapter.md)

## Navigasi

- [16-1: Siklus konversi kas](#rumus-16-1)
- [16-2: Periode konversi persediaan](#rumus-16-2)
- [16-3: Rata-rata periode penagihan](#rumus-16-3)
- [16-4: Periode penundaan utang pemasok](#rumus-16-4)
- [16-5: Investasi dalam piutang](#rumus-16-5)
- [16-5a: Piutang dengan DSO](#rumus-16-5a)
- [16-6: Biaya nominal melepas diskon pemasok](#rumus-16-6)
- [U-16-01: EAR melepas diskon pemasok](#rumus-u-16-01)

<a id="rumus-16-1"></a>
## 16-1 — Siklus konversi kas

[PDF 700](../Financial_Management_Theory_and_Practice_15e.pdf#page=700)

$$
CCC=ICP+ACP-PDP
$$

**Variabel.** ICP: hari persediaan; ACP: hari penagihan; PDP: hari penundaan pembayaran pemasok.

**Penurunan dan logika.** Sejak kas dibayarkan, barang masih berada di persediaan lalu menjadi piutang; kredit pemasok membiayai sebagian waktu tersebut. Karena itu waktu kredit dikurangkan.

**Syarat penggunaan.** Ketiga periode memakai kalender dan basis aktivitas yang konsisten; ini ukuran rata-rata.

**Kekeliruan yang perlu dihindari.** CCC negatif dapat normal pada usaha yang menerima kas sebelum membayar pemasok; bukan kesalahan aritmetika.

**Contoh hitung.** Persediaan 50 hari, piutang 60 hari, utang 40 hari: CCC 70 hari.

```python
50+60-40
```
Hasil presisi mesin: `70`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-16-2"></a>
## 16-2 — Periode konversi persediaan

[PDF 701](../Financial_Management_Theory_and_Practice_15e.pdf#page=701)

$$
ICP=\frac{Inventory}{COGS/365}
$$

**Variabel.** Inventory: saldo persediaan pada biaya; COGS: HPP tahunan.

**Penurunan dan logika.** Saldo rupiah dibagi aliran biaya per hari menghasilkan jumlah hari. Rasio ini sama dengan 365 dibagi perputaran persediaan.

**Syarat penggunaan.** Gunakan saldo rata-rata bila musiman;365 dapat diganti kalender yang dinyatakan konsisten.

**Kekeliruan yang perlu dihindari.** Jangan membagi persediaan pada biaya dengan penjualan pada harga jual.

**Contoh hitung.** Persediaan 20, HPP 146 per tahun: ICP 50 hari.

```python
20/(146/365)
```
Hasil presisi mesin: `50`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-16-3"></a>
## 16-3 — Rata-rata periode penagihan

[PDF 701](../Financial_Management_Theory_and_Practice_15e.pdf#page=701)

$$
ACP=DSO=\frac{AR}{Sales/365}
$$

**Variabel.** AR: piutang usaha; Sales: penjualan kredit tahunan atau proksi penjualan buku.

**Penurunan dan logika.** Piutang berasal dari penjualan yang belum tertagih; saldo dibagi penjualan per hari mengukur waktu penagihan rata-rata.

**Syarat penggunaan.** Idealnya gunakan penjualan kredit neto dan piutang rata-rata; total penjualan hanya proksi.

**Kekeliruan yang perlu dihindari.** Pertumbuhan atau perubahan musiman dapat mengubah DSO tanpa perubahan perilaku bayar.

**Contoh hitung.** Piutang 30, penjualan 365: DSO 30 hari.

```python
30/(365/365)
```
Hasil presisi mesin: `30`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-16-4"></a>
## 16-4 — Periode penundaan utang pemasok

[PDF 702](../Financial_Management_Theory_and_Practice_15e.pdf#page=702)

$$
PDP=\frac{AP}{Purchases/365}\approx\frac{AP}{COGS/365}
$$

**Variabel.** AP: utang usaha; Purchases: pembelian kredit tahunan; COGS: pendekatan pembelian dalam buku.

**Penurunan dan logika.** Utang dibagi pembelian per hari memberi hari pembiayaan pemasok. Penggantian pembelian dengan HPP memerlukan persediaan relatif stabil.

**Syarat penggunaan.** Gunakan pembelian aktual jika perubahan persediaan material; pisahkan utang nonusaha.

**Kekeliruan yang perlu dihindari.** Kesamaan pembelian dan HPP bukan identitas pada usaha yang menumpuk persediaan.

**Contoh hitung.** Utang 12, pembelian 146 per tahun: PDP 30 hari.

```python
12/(146/365)
```
Hasil presisi mesin: `30`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-16-5"></a>
## 16-5 — Investasi dalam piutang

[PDF 707](../Financial_Management_Theory_and_Practice_15e.pdf#page=707)

$$
AR=(Sales/365)ACP
$$

**Variabel.** AR: saldo piutang; Sales/365: penjualan kredit per hari; ACP: hari penagihan.

**Penurunan dan logika.** Susun ulang 16-3 dengan mengalikan kedua sisi dengan penjualan harian.

**Syarat penggunaan.** Penjualan harian cukup seragam dan seluruh asumsi 16-3 berlaku.

**Kekeliruan yang perlu dihindari.** Saldo piutang bukan biaya pendanaan: biaya modal harus diterapkan terpisah.

**Contoh hitung.** Penjualan harian 1.000, ACP 30 hari: piutang 30.000.

```python
1000*30
```
Hasil presisi mesin: `30000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-16-5a"></a>
## 16-5a — Piutang dengan DSO

[PDF 709](../Financial_Management_Theory_and_Practice_15e.pdf#page=709)

$$
AR=(Sales/365)DSO
$$

**Variabel.** DSO sama dengan ACP; penjualan harian dan saldo memakai mata uang yang sama.

**Penurunan dan logika.** Ini varian notasi 16-5, bukan model piutang baru.

**Syarat penggunaan.** Penjualan seragam; gunakan profil bulanan untuk usaha musiman.

**Kekeliruan yang perlu dihindari.** DSO bukan persentase; masukkan jumlah hari.

**Contoh hitung.** Penjualan harian 32.000, DSO 60: saldo 1.920.000.

```python
32000*60
```
Hasil presisi mesin: `1920000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-16-6"></a>
## 16-6 — Biaya nominal melepas diskon pemasok

[PDF 712](../Financial_Management_Theory_and_Practice_15e.pdf#page=712)

$$
r_{nom}=\frac{d}{1-d}\frac{365}{N-D}
$$

**Variabel.** d: diskon dalam desimal; D: hari batas diskon; N: hari jatuh tempo neto.

**Penurunan dan logika.** Dengan tidak membayar 1-d pada D, pembeli meminjam 1-d dan membayar biaya d selama N-D hari. Annualisasi sederhana mengalikan jumlah periode setahun.

**Syarat penggunaan.** N>D dan 0<=d<1. Sumber menulis persentase dibagi 100-d; bentuk desimal ekuivalen.

**Kekeliruan yang perlu dihindari.** Ini APR nominal, bukan biaya efektif: EAR=(1+d/(1-d))^(365/(N-D))-1.

**Contoh hitung.** 2/10 net 30: biaya nominal 37,244898%.

```python
.02/.98*365/20
```
Hasil presisi mesin: `0.372448979592`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-16-01"></a>
## U-16-01 — EAR melepas diskon pemasok

[PDF 711](../Financial_Management_Theory_and_Practice_15e.pdf#page=711) · [PDF 712](../Financial_Management_Theory_and_Practice_15e.pdf#page=712)

$$
EAR=\left(1+\frac{d}{1-d}\right)^{365/(N-D)}-1
$$

**Variabel.** d: diskon desimal; N-D: masa kredit tambahan.

**Penurunan dan logika.** Compound biaya periodik 16-6, alih-alih annualisasi sederhana.

**Syarat penggunaan.** Siklus kredit dianggap dapat diulang; konvensi 365 konsisten.

**Kekeliruan yang perlu dihindari.** APRnominal 37,24% pada 2/10 net 30 berbeda dari EAR 44,59%.

**Contoh hitung.** 2/10 net 30: EAR 44,585293%.

```python
(1+.02/.98)**(365/20)-1
```
Hasil presisi mesin: `0.445852927312`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
