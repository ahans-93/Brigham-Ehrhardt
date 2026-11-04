# Bab 17: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../17-chapter.md)

## Navigasi

- [17-1: Paritas suku bunga tertutup](#rumus-17-1)
- [17-1a: Mencari return domestik tersirat](#rumus-17-1a)
- [17-2: Paritas daya beli satu barang](#rumus-17-2)
- [17-3: Kurs tersirat oleh PPP](#rumus-17-3)
- [17-4: Forward multiyear](#rumus-17-4)
- [U-17-01: Kuotasi timbal balik dan cross rate](#rumus-u-17-01)

<a id="rumus-17-1"></a>
## 17-1 — Paritas suku bunga tertutup

[PDF 760](../Financial_Management_Theory_and_Practice_15e.pdf#page=760)

$$
\frac{F}{S}=\frac{1+r_h}{1+r_f}
$$

**Variabel.** S, F: unit mata uang domestik per satu unit asing, spot dan forward; rh, rf: suku bunga untuk horizon sama.

**Penurunan dan logika.** Satu unit domestik ditanam langsung menjadi 1+rh. Konversi ke asing, investasi, lalu lindung nilai forward menghasilkan(1+rf)F/S. Tanpa arbitrase keduanya sama.

**Syarat penggunaan.** Aset berisiko sebanding, dapat dipinjam/ditanam, tanpa friksi material; suku bunga periodik.

**Kekeliruan yang perlu dihindari.** Balik kuotasi kurs berarti balik juga rasio. Forward bukan ramalan spot yang pasti.

**Contoh hitung.** S 15.000, rh 6%, rf 2%: forward 15.588,235294.

```python
15000*1.06/1.02
```
Hasil presisi mesin: `15588.2352941`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-17-1a"></a>
## 17-1a — Mencari return domestik tersirat

[PDF 760](../Financial_Management_Theory_and_Practice_15e.pdf#page=760)

$$
r_h=\frac{F}{S}(1+r_f)-1
$$

**Variabel.** Kuotasi langsung sumber F 1,00210 dan S 0,99443; rf 2% untuk 180 hari.

**Penurunan dan logika.** Susun ulang 17-1; faktor domestik harus sama dengan faktor investasi asing yang ditutup forward.

**Syarat penggunaan.** Return hasil adalah return 180 hari, baru kemudian annualisasi sesuai konvensi.

**Kekeliruan yang perlu dihindari.** Angka kurs sumber dibulatkan sehingga hasil dari angka tampilan sekitar 2,78675%, bukan angka presisi data mentah.

**Contoh hitung.** Kurs tampilan sumber menghasilkan rh sekitar 2,786722% per 180 hari.

```python
1.00210/.99443*1.02-1
```
Hasil presisi mesin: `0.0278672204177`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-17-2"></a>
## 17-2 — Paritas daya beli satu barang

[PDF 761](../Financial_Management_Theory_and_Practice_15e.pdf#page=761)

$$
P_h=P_f S
$$

**Variabel.** Ph, Pf: harga barang sebanding dalam mata uang domestik/asing; S: domestik per asing.

**Penurunan dan logika.** Konversi biaya membeli barang di luar negeri ke mata uang domestik; arbitrase barang menyamakan harga bila tanpa hambatan.

**Syarat penggunaan.** Barang identik dan dapat diperdagangkan; tarif, ongkos angkut, dan pajak membatasi kesetaraan.

**Kekeliruan yang perlu dihindari.** PPP bukan identitas kurs pasar pada setiap tanggal.

**Contoh hitung.** Harga asing 100, kurs 1,5: harga domestik 150.

```python
100*1.5
```
Hasil presisi mesin: `150`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-17-3"></a>
## 17-3 — Kurs tersirat oleh PPP

[PDF 761](../Financial_Management_Theory_and_Practice_15e.pdf#page=761)

$$
S=P_h/P_f
$$

**Variabel.** Ph dan Pf adalah harga barang atau indeks harga yang benar-benar sebanding.

**Penurunan dan logika.** Bagi 17-2 dengan Pf untuk memperoleh unit domestik per unit asing.

**Syarat penggunaan.** Pf positif; indeks harus memiliki basis konsisten bila digunakan.

**Kekeliruan yang perlu dihindari.** Jangan membagi dua indeks dengan tahun dasar berbeda tanpa normalisasi.

**Contoh hitung.** Ph 150 dan Pf 100: kurs 1,5.

```python
150/100
```
Hasil presisi mesin: `1.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-17-4"></a>
## 17-4 — Forward multiyear

[PDF 773](../Financial_Management_Theory_and_Practice_15e.pdf#page=773)

$$
F_t=S_0\left(\frac{1+r_h}{1+r_f}\right)^t
$$

**Variabel.** rh, rf: bunga efektif tahunan konstan; t: tahun.

**Penurunan dan logika.** Ulangi strategi arbitrase 17-1 selama t periode. Pada kurva bunga tidak datar gunakan faktor akumulasi masing-masing tenor.

**Syarat penggunaan.** Asumsi covered interest parity; forward terkunci bukan realisasi kurs mendatang.

**Kekeliruan yang perlu dihindari.** Jangan memakai forward yang sudah mengandung selisih bunga lalu menambahkan premium kurs lagi.

**Contoh hitung.** S 1,5, rh 6%, rf 4%, t 3: forward 1,588213331.

```python
1.5*(1.06/1.04)**3
```
Hasil presisi mesin: `1.58821333068`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-17-01"></a>
## U-17-01 — Kuotasi timbal balik dan cross rate

[PDF 750](../Financial_Management_Theory_and_Practice_15e.pdf#page=750) · [PDF 751](../Financial_Management_Theory_and_Practice_15e.pdf#page=751) · [PDF 752](../Financial_Management_Theory_and_Practice_15e.pdf#page=752) · [PDF 753](../Financial_Management_Theory_and_Practice_15e.pdf#page=753) · [PDF 754](../Financial_Management_Theory_and_Practice_15e.pdf#page=754)

$$
S_{B/A}=1/S_{A/B},\quad S_{A/C}=S_{A/B}S_{B/C}
$$

**Variabel.** SA/B: unit A per unit B; cocokkan unit sehingga B saling hapus.

**Penurunan dan logika.** Konversi mata uang mengikuti analisis dimensi, sama dengan perkalian faktor satuan.

**Syarat penggunaan.** Kurs tanpa bid/ask spread; dalam transaksi nyata gunakan sisi bid/ask yang tepat.

**Kekeliruan yang perlu dihindari.** Mengalikan dua kurs yangarahnya tidak sesuai menghasilkan unit salah meskipun angkanya masuk akal.

**Contoh hitung.** 15.000IDR/USD dan 1,1USD/EUR: 16.500IDR/EUR.

```python
15000*1.1
```
Hasil presisi mesin: `16500`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
