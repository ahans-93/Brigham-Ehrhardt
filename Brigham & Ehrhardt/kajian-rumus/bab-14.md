# Bab 14: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../14-chapter.md)

## Navigasi

- [14-1: Residual distribution model](#rumus-14-1)
- [14-2: Saham yang dibeli kembali](#rumus-14-2)
- [14-3: Saham tersisa setelah repurchase](#rumus-14-3)
- [U-14-01: Payout dan retention](#rumus-u-14-01)
- [U-14-02: Stock split](#rumus-u-14-02)

<a id="rumus-14-1"></a>
## 14-1 — Residual distribution model

[PDF 616](../Financial_Management_Theory_and_Practice_15e.pdf#page=616)

$$
Distribution=NI-w_E\times CapitalBudget
$$

**Variabel.** wE: porsi ekuitas target untuk membiayai investasi; NI: dana laba yang tersedia dalam model.

**Penurunan dan logika.** Pertahankan laba sebesar kebutuhan ekuitas untuk proyek yang diterima; sisanya dapat didistribusikan.

**Syarat penggunaan.** Capital budget sudah dipilih berdasarkan nilai dan risiko; target struktur modal sesuai.

**Kekeliruan yang perlu dihindari.** Hasil negatif menunjukkan kebutuhan pembiayaan ekuitas yang belum tercukupi, bukan pembayaran dividen negatif.

**Contoh hitung.** NI 100, budget 100, equityratio 60% memberi distribution 40.

```python
100-.6*100
```
Hasil presisi mesin: `40`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-14-2"></a>
## 14-2 — Saham yang dibeli kembali

[PDF 626](../Financial_Management_Theory_and_Practice_15e.pdf#page=626)

$$
n_{rep}=Cash_{rep}/P_{rep}
$$

**Variabel.** Prep: harga aktual/adil per saham pada transaksi model.

**Penurunan dan logika.** Pembayaran dibagi harga per unit menghasilkan jumlah unit yang dibeli.

**Syarat penggunaan.** Model sumber mengasumsikan repurchase itu sendiri pada harga fair tidak mengubah harga; efek informasi kebijakan dinilai terpisah.

**Kekeliruan yang perlu dihindari.** Harga sebelum pengumuman tidak otomatis sama dengan harga sesaat sebelum pelaksanaan.

**Contoh hitung.** Kasrepurchase 200 dan harga 20 membeli 10 saham.

```python
200/20
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-14-3"></a>
## 14-3 — Saham tersisa setelah repurchase

[PDF 626](../Financial_Management_Theory_and_Practice_15e.pdf#page=626)

$$
n_{post}=n_{prior}-Cash_{rep}/P_{rep}=n_{prior}(1-Cash_{rep}/E_{prior})
$$

**Variabel.** Eprior=nprior×Prep pada saat basis harga ditetapkan.

**Penurunan dan logika.** Kurangi saham repurchase dari jumlah awal; substitusi Prep=Eprior/nprior memberi bentuk faktor.

**Syarat penggunaan.** Harga fair dan nilai equity prior konsisten dengan kas yang masih ada sebelum transaksi.

**Kekeliruan yang perlu dihindari.** Mengurangi kas dari ekuitas tetapi tidak mengurangi jumlah saham akan salah menghitung harga pasca-repurchase.

**Contoh hitung.** n 100, Eprior 2000, Cashrep 200 menghasilkan 90 saham.

```python
100*(1-200/2000)
```
Hasil presisi mesin: `90`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-14-01"></a>
## U-14-01 — Payout dan retention

[PDF 607](../Financial_Management_Theory_and_Practice_15e.pdf#page=607) · [PDF 608](../Financial_Management_Theory_and_Practice_15e.pdf#page=608) · [PDF 609](../Financial_Management_Theory_and_Practice_15e.pdf#page=609) · [PDF 610](../Financial_Management_Theory_and_Practice_15e.pdf#page=610)

$$
Payout=D/NI,\quad b=1-Payout,\quad g=bROE
$$

**Variabel.** D: dividen common; NI: laba common; b: laba ditahan sebagai proporsi.

**Penurunan dan logika.** Laba ditahan menopang pertumbuhan equity jika ROE danpendanaan stabil; kaitkan dengan 9-11.

**Syarat penggunaan.** NI positif; basis ROE dan timing perlu sesuai model.

**Kekeliruan yang perlu dihindari.** Repurchase bukan dividen; total payout harus memasukkan buyback neto bila itulah ukuran yang dipilih.

**Contoh hitung.** NI 100, D 40: b 60%; ROE 15% memberi g 9%.

```python
(1-40/100)*.15
```
Hasil presisi mesin: `0.09`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-14-02"></a>
## U-14-02 — Stock split

[PDF 631](../Financial_Management_Theory_and_Practice_15e.pdf#page=631) · [PDF 632](../Financial_Management_Theory_and_Practice_15e.pdf#page=632) · [PDF 633](../Financial_Management_Theory_and_Practice_15e.pdf#page=633)

$$
n_{after}=kn_{before},\quad P_{after}=P_{before}/k
$$

**Variabel.** k: rasio pemecahan, misalnya 2 untuk 2-for-1.

**Penurunan dan logika.** Jumlah klaim bertambah secara proporsional sementara nilai total teoritis tetap pada saat split tanpa informasi baru.

**Syarat penggunaan.** Tidak ada perubahan nilai ekonomi atau kas akibat tindakan split itu sendiri.

**Kekeliruan yang perlu dihindari.** Harga pasar sesudah pengumuman dapat bergerak; formula hanya penyesuaian mekanis.

**Contoh hitung.** 100 saham, harga 40, split 2: 200 saham, harga 20.

```python
40/2
```
Hasil presisi mesin: `20`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
