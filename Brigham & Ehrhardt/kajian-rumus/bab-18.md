# Bab 18: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../18-chapter.md)

## Navigasi

- [18-1: Kepemilikan investor baru](#rumus-18-1)
- [18-1a: Jumlah saham untuk target kepemilikan](#rumus-18-1a)
- [18-2: Nilai ekuitas sesudah IPO](#rumus-18-2)
- [18-3: Harga penawaran konsisten dengan nilai](#rumus-18-3)
- [18-4: Porsi investor untuk jumlah dana tertentu](#rumus-18-4)
- [U-18-01: Spread underwriting dan underpricing](#rumus-u-18-01)

<a id="rumus-18-1"></a>
## 18-1 — Kepemilikan investor baru

[PDF 795](../Financial_Management_Theory_and_Practice_15e.pdf#page=795)

$$
f=\frac{n_{new}}{n_{new}+n_{existing}}
$$

**Variabel.** nnew: saham baru diterbitkan; nexisting: saham sebelum emisi; f: fraksi kepemilikan baru.

**Penurunan dan logika.** Bagi saham yang dibeli dengan total saham sesudah emisi.

**Syarat penggunaan.** Satu kelas saham dengan hak setara; saham treasury, opsi, dan konversi harus ditentukan basisnya.

**Kekeliruan yang perlu dihindari.** Penjualan saham lama oleh pendiri tidak menambah saham beredar atau kas perusahaan.

**Contoh hitung.** Saham lama 80, baru 20: kepemilikan 20%.

```python
20/(20+80)
```
Hasil presisi mesin: `0.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-18-1a"></a>
## 18-1a — Jumlah saham untuk target kepemilikan

[PDF 795](../Financial_Management_Theory_and_Practice_15e.pdf#page=795)

$$
n_{new}=\frac{f n_{existing}}{1-f}
$$

**Variabel.** f: target kepemilikan investor baru dalam desimal.

**Penurunan dan logika.** Kalikan 18-1 dengan total saham lalu pindahkan f nnew ke sisi kiri.

**Syarat penggunaan.** 0<=f<1; basis saham harus konsisten.

**Kekeliruan yang perlu dihindari.** Menerbitkan 20% dari jumlah lama hanya memberi 16,67% dari jumlah baru.

**Contoh hitung.** Target 20%, saham lama 80: terbitkan 20.

```python
.2*80/(1-.2)
```
Hasil presisi mesin: `20`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-18-2"></a>
## 18-2 — Nilai ekuitas sesudah IPO

[PDF 795](../Financial_Management_Theory_and_Practice_15e.pdf#page=795)

$$
V_{post}=V_{pre}+P_{offer}(1-F)n_{new}
$$

**Variabel.** F: spread penjamin emisi; Poffer: harga penawaran; Vpre: nilai sebelum dana baru.

**Penurunan dan logika.** Nilai lama ditambah penerimaan neto emisi; spread mengurangi kas yang masuk.

**Syarat penggunaan.** Tidak ada perubahan nilai operasi lain atau biaya tetap tambahan; jika ada, kurangkan juga.

**Kekeliruan yang perlu dihindari.** F di sini spread, bukan forward kurs bab 17.

**Contoh hitung.** Vpre 100, harga 10, saham baru 2, spread 5%: Vpost 119.

```python
100+10*(1-.05)*2
```
Hasil presisi mesin: `119`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-18-3"></a>
## 18-3 — Harga penawaran konsisten dengan nilai

[PDF 796](../Financial_Management_Theory_and_Practice_15e.pdf#page=796)

$$
P_{offer}=\frac{V_{pre}}{F n_{new}+n_{existing}}
$$

**Variabel.** Variabel mengikuti 18-1 dan 18-2; F dalam desimal.

**Penurunan dan logika.** Tetapkan harga per saham=Ppost=Vpost/(nexisting+nnew), substitusi 18-2, lalu kumpulkan suku P di kiri.

**Syarat penggunaan.** Model harga wajar tanpa underpricing tambahan; kelas saham setara.

**Kekeliruan yang perlu dihindari.** Membagi Vpre dengan jumlah saham sesudah emisi mengabaikan tambahan kas.

**Contoh hitung.** Vpre 100, saham lama 10, baru 2, F 5%: harga 9,900990099.

```python
100/(.05*2+10)
```
Hasil presisi mesin: `9.90099009901`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-18-4"></a>
## 18-4 — Porsi investor untuk jumlah dana tertentu

[PDF 796](../Financial_Management_Theory_and_Practice_15e.pdf#page=796)

$$
f=\frac{Investment}{(1-F)Investment+V_{pre}}
$$

**Variabel.** Investment: pembayaran bruto investor; F: spread; penyebut: nilai pascaemisi.

**Penurunan dan logika.** Investor meminta klaim senilai dana bruto yang dibayar; perusahaan menerima dana neto setelah spread.

**Syarat penggunaan.** Nilai saham baru sama dengan harga penawaran; biaya lain belum diperhitungkan.

**Kekeliruan yang perlu dihindari.** Jangan menaruh investasi neto di pembilang jika investor membayar bruto.

**Contoh hitung.** Investasi 20, Vpre 100, F 5%: porsi 16,806723%.

```python
20/(.95*20+100)
```
Hasil presisi mesin: `0.168067226891`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-18-01"></a>
## U-18-01 — Spread underwriting dan underpricing

[PDF 793](../Financial_Management_Theory_and_Practice_15e.pdf#page=793) · [PDF 794](../Financial_Management_Theory_and_Practice_15e.pdf#page=794) · [PDF 800](../Financial_Management_Theory_and_Practice_15e.pdf#page=800) · [PDF 801](../Financial_Management_Theory_and_Practice_15e.pdf#page=801)

$$
NetProceeds=P_{offer}n(1-F)-FixedCosts,\quad InitialReturn=P_{close}/P_{offer}-1
$$

**Variabel.** F: spread; Pclose: harga pasar setelah emisi.

**Penurunan dan logika.** Spread mengurangi penerimaan emiten; initial return mengukur keuntungan harga investor IPO. Keduanya biaya/konsep berbeda.

**Syarat penggunaan.** Jumlah saham primer dansekunder dipisahkan.

**Kekeliruan yang perlu dihindari.** Harga saham naik pada hari pertama bukan kas tambahan diterima emiten.

**Contoh hitung.** Poffer 10, Pclose 12: initial return 20%.

```python
12/10-1
```
Hasil presisi mesin: `0.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
