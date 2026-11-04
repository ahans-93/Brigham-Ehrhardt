# Bab 10: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../10-chapter.md)

## Navigasi

- [10-1: Net present value proyek](#rumus-10-1)
- [10-2: Internal rate of return](#rumus-10-2)
- [10-2a: MIRR dengan kas masuk dan keluar terpisah](#rumus-10-2a)
- [10-2b: MIRR dalam bentuk terminal value](#rumus-10-2b)
- [10-3: Profitability index](#rumus-10-3)
- [10-4: Payback dengan fraksi tahun](#rumus-10-4)
- [U-10-01: Payback dan discounted payback](#rumus-u-10-01)
- [U-10-02: Equivalent annual annuity](#rumus-u-10-02)

<a id="rumus-10-1"></a>
## 10-1 — Net present value proyek

[PDF 454](../Financial_Management_Theory_and_Practice_15e.pdf#page=454)

$$
NPV=\sum_{t=0}^{N}CF_t/(1+r)^t
$$

**Variabel.** CF 0: investasi awal signed; r: biaya modal sesuai risiko proyek.

**Penurunan dan logika.** Nilai kas masuk dan keluar pada tanggal sama dijumlahkan. Kas t 0 tidak didiskontokan karena eksponennya nol.

**Syarat penggunaan.** Arus kas incremental setelah pajak, opportunity cost, efek samping, dan reinvestasi dimasukkan; sunk cost dikeluarkan.

**Kekeliruan yang perlu dihindari.** Laba akuntansi bukan kas proyek. Untuk proyek saling eksklusif, perbedaan skala/waktu dapat membuat peringkat IRR berbeda dari NPV.

**Contoh hitung.** CF 0−100, CF 1=121, r 10% menghasilkan NPV 10.

```python
-100+121/1.1
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-10-2"></a>
## 10-2 — Internal rate of return

[PDF 457](../Financial_Management_Theory_and_Practice_15e.pdf#page=457)

$$
\sum_{t=0}^{N}CF_t/(1+IRR)^t=0
$$

**Variabel.** IRR: akar tingkat diskonto yang membuat NPV nol.

**Penurunan dan logika.** Ganti r pada 10-1 dengan variabel yang dicari dan cari akar numeriknya.

**Syarat penggunaan.** Arus kas konvensional biasanya memiliki satu akar relevan. Perubahan tanda berulang dapat menimbulkan lebih dari satu atau tidak ada IRR.

**Kekeliruan yang perlu dihindari.** Aturan IRR>cost of capital perlu kehati-hatian untuk financing cash flows dan proyek nonkonvensional.

**Contoh hitung.** Investasi 100 sekarang dan penerimaan 121 satu tahun lagi: IRR 21%.

```python
irr([-100,121])
```
Hasil presisi mesin: `0.21`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-10-2a"></a>
## 10-2a — MIRR dengan kas masuk dan keluar terpisah

[PDF 465](../Financial_Management_Theory_and_Practice_15e.pdf#page=465)

$$
\sum_{t=0}^{N}\frac{COF_t}{(1+r_f)^t}=\frac{\sum_{t=0}^{N}CIF_t(1+r_{re})^{N-t}}{(1+MIRR)^N}
$$

**Variabel.** COF, CIF: besaran positif kas keluar/masuk; rf: finance rate; rre: reinvestment rate. Sumber memakai r yang sama untuk kedua rate.

**Penurunan dan logika.** Tarik seluruh biaya ke 0 dan majukan seluruh manfaat keN; cari return tunggal yang menghubungkan PVcost dengan terminal manfaat.

**Syarat penggunaan.** PVcost>0, TVbenefit>0, N>0; rate eksternal ditetapkan secara konsisten.

**Kekeliruan yang perlu dihindari.** Jangan memakai COF negatif sebagai denominator pada akar MIRR. IRR dan MIRR berbeda karena asumsi timing reinvestasi.

**Contoh hitung.** Outlay 100 pada 0, inflow 110 pada 1, T 2, reinvestment 10% memberi TV 121 dan MIRR 10%.

```python
mirr([-100,110,0],.1,.1)
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-10-2b"></a>
## 10-2b — MIRR dalam bentuk terminal value

[PDF 465](../Financial_Management_Theory_and_Practice_15e.pdf#page=465)

$$
MIRR=(TV/PV_{cost})^{1/N}-1
$$

**Variabel.** TV: manfaat yang sudah dikompaun keN; PVcost: biaya positif pada 0.

**Penurunan dan logika.** Susun ulang PVcost=TV/(1+MIRR)^N dari 10-2a, lalu ambil akar N.

**Syarat penggunaan.** Model dan domain 10-2a; bukan rate yang dicari dengan mengubah reinvestment rate menjadi MIRR itu sendiri.

**Kekeliruan yang perlu dihindari.** Jika salah satu sisi nol/negatif, formula akar standar tidak otomatis bermakna.

**Contoh hitung.** TV 121, PVcost 100, N 2 memberi 10%.

```python
(121/100)**.5-1
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-10-3"></a>
## 10-3 — Profitability index

[PDF 466](../Financial_Management_Theory_and_Practice_15e.pdf#page=466)

$$
PI=\frac{\sum_{t=1}^{N}CF_t/(1+r)^t}{InitialCost},\quad InitialCost=-CF_0>0
$$

**Variabel.** Denominator: besaran positif biaya awal pada kasus investasi awal tunggal.

**Penurunan dan logika.** Bandingkan PV manfaat setelah t 0 dengan dana awal; pada kasus sederhana PI=1+NPV/Initial Cost.

**Syarat penggunaan.** Untuk beberapa outlay atau kendala proyek indivisible, definisi serta pemilihan portofolio harus diperjelas.

**Kekeliruan yang perlu dihindari.** Buku memakai simbol CF 0 pada denominator sambil menyebut Initial cost. Jika CF 0 signed negatif dari 10-1, gunakan −CF 0 agar PI tidak terbalik tandanya.

**Contoh hitung.** Kas 121 setahun, r 10%, biaya 100: PI 1,1.

```python
(121/1.1)/100
```
Hasil presisi mesin: `1.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-10-4"></a>
## 10-4 — Payback dengan fraksi tahun

[PDF 467](../Financial_Management_Theory_and_Practice_15e.pdf#page=467)

$$
Payback=k+UnrecoveredCost_k/CF_{k+1}
$$

**Variabel.** k: tahun penuh terakhir sebelum biaya pulih.

**Penurunan dan logika.** Akumulasikan kas tanpa diskonto sampai sisa biaya dapat ditutup; fraksi merupakan interpolasi dalam tahun pemulihan.

**Syarat penggunaan.** Kas selama tahun pemulihan diasumsikan merata untuk interpretasi fraksi waktu.

**Kekeliruan yang perlu dihindari.** Jika kas benar-benar hanya diterima pada akhir tahun, tanggal pulih diskretnya berbeda. Payback juga mengabaikan kas setelah pemulihan.

**Contoh hitung.** Biaya 100, kas tahun 1=40 dan tahun 2=80: payback 1,75 tahun.

```python
1+(100-40)/80
```
Hasil presisi mesin: `1.75`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-10-01"></a>
## U-10-01 — Payback dan discounted payback

[PDF 455](../Financial_Management_Theory_and_Practice_15e.pdf#page=455) · [PDF 456](../Financial_Management_Theory_and_Practice_15e.pdf#page=456) · [PDF 457](../Financial_Management_Theory_and_Practice_15e.pdf#page=457) · [PDF 458](../Financial_Management_Theory_and_Practice_15e.pdf#page=458)

$$
PB=k+\frac{Unrecovered_k}{CF_{k+1}}
$$

**Variabel.** k: tahun penuh sebelum investasi tertutup; sisa modal dibagi kas tahun penutupan.

**Penurunan dan logika.** Akumulasikan kas sampai tanda kumulatif berubah; interpolasi fraksi tahun. Discounted PB memakai PV setiap kas.

**Syarat penggunaan.** Interpolasi mengasumsikan kas tahun penutup mengalir seragam; jika hanya di akhir tahun, gunakan tanggal aktual.

**Kekeliruan yang perlu dihindari.** Payback mengabaikan kas setelah cutoff dan ordinary PB mengabaikan nilai waktu uang.

**Contoh hitung.** Investasi 100, kas 40 per tahun: PB 2+(20/40)=2,5 tahun.

```python
2+20/40
```
Hasil presisi mesin: `2.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-10-02"></a>
## U-10-02 — Equivalent annual annuity

[PDF 483](../Financial_Management_Theory_and_Practice_15e.pdf#page=483) · [PDF 484](../Financial_Management_Theory_and_Practice_15e.pdf#page=484) · [PDF 485](../Financial_Management_Theory_and_Practice_15e.pdf#page=485)

$$
EAA=NPV/pvaf(r,N)
$$

**Variabel.** EAA: nilai tahunan ekuivalen proyek; N: umur ekonomis.

**Penurunan dan logika.** Cari anuitas yang PV-nya sama dengan NPV. Untuk biaya saja, gunakan EAC=PVcost/pvaf.

**Syarat penggunaan.** Perbandingan umur berbeda perlu layanan setara dan asumsi pengulangan yang masuk akal.

**Kekeliruan yang perlu dihindari.** EAA bukan asumsi bahwa kas aktual proyek setiap tahun sama.

**Contoh hitung.** NPV 100, r 10%, N 3: EAA 40,21148.

```python
100/pvaf(.10,3)
```
Hasil presisi mesin: `40.2114803625`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
