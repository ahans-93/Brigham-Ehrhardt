# Bab 4: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../04-chapter.md)

## Navigasi

- [4-1: Future value satu kas](#rumus-4-1)
- [4-2: Persamaan tanda kalkulator dua kas](#rumus-4-2)
- [4-3: Present value satu kas](#rumus-4-3)
- [4-4: Perpetuitas konstan](#rumus-4-4)
- [4-5: FV anuitas biasa](#rumus-4-5)
- [4-6: Persamaan kalkulator dengan anuitas](#rumus-4-6)
- [4-7: FV annuity due](#rumus-4-7)
- [4-8: PV anuitas biasa](#rumus-4-8)
- [4-9: PV annuity due](#rumus-4-9)
- [4-10: PV kas tidak seragam](#rumus-4-10)
- [4-11: FV kas tidak seragam](#rumus-4-11)
- [4-12: Periodic rate dari nominal APR](#rumus-4-12)
- [4-13: FV dengan compounding m kali](#rumus-4-13)
- [4-14: Effective annual rate](#rumus-4-14)
- [4-15: Real rate exact Fisher](#rumus-4-15)
- [U-4-01: Mencari tingkat dan waktu](#rumus-u-4-01)
- [U-4-02: Pinjaman amortisasi](#rumus-u-4-02)
- [U-4-03: Bunga sederhana dan continuous limit](#rumus-u-4-03)

<a id="rumus-4-1"></a>
## 4-1 — Future value satu kas

[PDF 180](../Financial_Management_Theory_and_Practice_15e.pdf#page=180) · [PDF 187](../Financial_Management_Theory_and_Practice_15e.pdf#page=187) · [PDF 191](../Financial_Management_Theory_and_Practice_15e.pdf#page=191)

$$
FV_N=PV(1+r)^N
$$

**Variabel.** r: bunga per periode; N: banyak interval dari kas awal ke tanggal penilaian.

**Penurunan dan logika.** Saldo berulang B(t+1)=Bt(1+r) memberi hasil perkalian (1+r) sebanyak N kali.

**Syarat penggunaan.** r konstan atau gunakan produk (1+rt) untuk rates berubah; tidak ada kas antara.

**Kekeliruan yang perlu dihindari.** N adalah selisih waktu, bukan sekadar label tahun akhir.

**Contoh hitung.** PV 100, r 10%, N 2: FV 121.

```python
100*1.1**2
```
Hasil presisi mesin: `121`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-2"></a>
## 4-2 — Persamaan tanda kalkulator dua kas

[PDF 182](../Financial_Management_Theory_and_Practice_15e.pdf#page=182)

$$
PV_{signed}(1+r)^N+FV_{signed}=0
$$

**Variabel.** PV dan FV bertanda menurut satu pihak: pembayaran dan penerimaan berlawanan tanda.

**Penurunan dan logika.** Pindahkan nilai kas akhir pada 4-1 ke ruas lain. Konvensi kalkulator memberi tanda berlawanan untuk pembayaran dan penerimaan.

**Syarat penggunaan.** Tidak ada PMT; r dan N sesuai periode.

**Kekeliruan yang perlu dihindari.** Ini tidak bertentangan dengan 4-1; perubahan tanda berasal dari konvensi arus kas, bukan nilai uang negatif secara ekonomi.

**Contoh hitung.** Pembayaran awal −100 dan penerimaan akhir 121 pada 10% dua periode memberi residual nol.

```python
-100*1.1**2+121
```
Hasil presisi mesin: `-1.42108547152e-14`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-3"></a>
## 4-3 — Present value satu kas

[PDF 187](../Financial_Management_Theory_and_Practice_15e.pdf#page=187)

$$
PV=FV_N/(1+r)^N
$$

**Variabel.** PV di sini adalah besaran nilai sekarang, bukan otomatis tanda input kalkulator.

**Penurunan dan logika.** Bagi kedua sisi 4-1 dengan (1+r)^N. Discounting adalah operasi kebalikan compounding.

**Syarat penggunaan.** r > −1 untuk discount factor positif pada model biasa.

**Kekeliruan yang perlu dihindari.** Kas pada tanggal berbeda tidak boleh dibandingkan tanpa menyamakan tanggal.

**Contoh hitung.** Kas 121 dua periode lagi, r 10%: PV 100.

```python
121/1.1**2
```
Hasil presisi mesin: `100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-4"></a>
## 4-4 — Perpetuitas konstan

[PDF 192](../Financial_Management_Theory_and_Practice_15e.pdf#page=192)

$$
PV=PMT/r
$$

**Variabel.** PMT pertama pada akhir periode 1 dan terus sama selamanya.

**Penurunan dan logika.** Jumlahkan deret geometri PMT/(1+r)+PMT/(1+r)^2+...; r > 0 menjamin konvergensi.

**Syarat penggunaan.** r positif dan kas konstan; pembayaran segera saat t 0 harus ditambahkan terpisah.

**Kekeliruan yang perlu dihindari.** Pada r=0 tidak ada PV finite untuk perpetuitas positif.

**Contoh hitung.** Kas tahunan 100 selamanya mulai tahun 1, r 10%: PV 1.000.

```python
100/.1
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-5"></a>
## 4-5 — FV anuitas biasa

[PDF 195](../Financial_Management_Theory_and_Practice_15e.pdf#page=195)

$$
FV_A=PMT[(1+r)^N-1]/r
$$

**Variabel.** PMT konstan pada akhir setiap periode 1 sampai N.

**Penurunan dan logika.** Compound setiap PMT menuju N lalu jumlahkan deret 1+(1+r)+...+(1+r)^(N−1).

**Syarat penggunaan.** r konstan; r=0 memakai limit N×PMT.

**Kekeliruan yang perlu dihindari.** Setoran terakhir tidak mendapat bunga lagi pada tanggal N.

**Contoh hitung.** Dua setoran akhir tahun 100, r 10%: FV 210.

```python
100*fvaf(.1,2)
```
Hasil presisi mesin: `210`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-6"></a>
## 4-6 — Persamaan kalkulator dengan anuitas

[PDF 195](../Financial_Management_Theory_and_Practice_15e.pdf#page=195)

$$
PV_s(1+r)^N+PMT_s\frac{(1+r)^N-1}{r}+FV_s=0
$$

**Variabel.** Subskrip s menandakan arus kas signed; PMT akhir periode.

**Penurunan dan logika.** Nyatakan semua kas pada tanggal N; jumlah kas awal dan PMT yang dikompaun diseimbangkan oleh kas akhir bertanda lawan.

**Syarat penggunaan.** Ordinary annuity; annuity due memerlukan faktor (1+r) pada komponen PMT.

**Kekeliruan yang perlu dihindari.** Mode BEGIN/END yang salah menimbulkan hasil berbeda walau nilai input sama.

**Contoh hitung.** PV −100, PMT −10 dua kali, r 10%, FV 142 menghasilkan residual nol.

```python
-100*1.1**2-10*fvaf(.1,2)+142
```
Hasil presisi mesin: `0`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-7"></a>
## 4-7 — FV annuity due

[PDF 196](../Financial_Management_Theory_and_Practice_15e.pdf#page=196)

$$
FV_{due}=FV_{ordinary}(1+r)
$$

**Variabel.** Jadwal due memindahkan setiap pembayaran satu periode lebih awal.

**Penurunan dan logika.** Setiap kas memperoleh satu periode bunga tambahan; faktor yang sama dapat dikeluarkan dari penjumlahan.

**Syarat penggunaan.** N dan tanggal penilaian sama; due dibayar pada t 0,..., N−1.

**Kekeliruan yang perlu dihindari.** Jangan mengganti N menjadi N+1 sekaligus mengalikan (1+r).

**Contoh hitung.** FV ordinary 210 pada r 10% memberi due 231.

```python
210*1.1
```
Hasil presisi mesin: `231`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-8"></a>
## 4-8 — PV anuitas biasa

[PDF 197](../Financial_Management_Theory_and_Practice_15e.pdf#page=197)

$$
PV_A=PMT[1-(1+r)^{-N}]/r
$$

**Variabel.** PMT dibayar akhir periode 1 sampai N.

**Penurunan dan logika.** Jumlahkan PV tiap pembayaran sebagai deret geometri, atau diskontokan FV 4-5 ke t 0.

**Syarat penggunaan.** r konstan; untuk r=0 gunakan N×PMT.

**Kekeliruan yang perlu dihindari.** Faktor ini menilai kas sebelum pembayaran pertama, bukan pada tanggal pembayaran pertama.

**Contoh hitung.** Dua penerimaan 100 dengan r 10% bernilai 173,553719.

```python
100*pvaf(.1,2)
```
Hasil presisi mesin: `173.553719008`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-9"></a>
## 4-9 — PV annuity due

[PDF 199](../Financial_Management_Theory_and_Practice_15e.pdf#page=199)

$$
PV_{due}=PV_{ordinary}(1+r)
$$

**Variabel.** Kas due mulai pada t 0, bukan t 1.

**Penurunan dan logika.** Memindahkan setiap kas satu periode lebih dekat mengurangi diskonto satu periode, sehingga mengalikan PV dengan (1+r).

**Syarat penggunaan.** Tanggal valuasi tetap; payment count sama.

**Kekeliruan yang perlu dihindari.** Pembayaran pertama due sudah bernilai penuh pada t 0.

**Contoh hitung.** Dua pembayaran due 100 pada r 10% bernilai 190,909091.

```python
100*pvaf(.1,2)*1.1
```
Hasil presisi mesin: `190.909090909`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-10"></a>
## 4-10 — PV kas tidak seragam

[PDF 203](../Financial_Management_Theory_and_Practice_15e.pdf#page=203)

$$
PV=\sum_{t=1}^{N}CF_t/(1+r)^t
$$

**Variabel.** CFt boleh berbeda setiap t; kas t 0 diperlakukan terpisah bila ada.

**Penurunan dan logika.** Prinsip aditivitas nilai: diskontokan masing-masing kas ke tanggal yang sama lalu jumlahkan.

**Syarat penggunaan.** r tunggal bila risiko/periode sesuai; otherwise gunakan discount factor spesifik.

**Kekeliruan yang perlu dihindari.** Jangan memakai faktor anuitas untuk rangkaian kas yang sebenarnya berubah.

**Contoh hitung.** CF 1 110 dan CF 2 121 dengan r 10% memberi PV 200.

```python
110/1.1+121/1.1**2
```
Hasil presisi mesin: `200`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-11"></a>
## 4-11 — FV kas tidak seragam

[PDF 205](../Financial_Management_Theory_and_Practice_15e.pdf#page=205)

$$
FV_N=\sum_{t=0}^{N}CF_t(1+r)^{N-t}
$$

**Variabel.** Kas t 0 termasuk dalam bentuk sumber ini; eksponen adalah sisa periode ke N.

**Penurunan dan logika.** Majukan masing-masing kas ke tanggal N melalui compounding dan jumlahkan.

**Syarat penggunaan.** r konstan; signed cash flow dapat dipakai untuk nilai neto.

**Kekeliruan yang perlu dihindari.** Kas pada t=N memakai eksponen nol, bukan satu.

**Contoh hitung.** CF 0=CF 1=CF 2=100, r 10%, N 2: FV 331.

```python
100*1.1**2+100*1.1+100
```
Hasil presisi mesin: `331`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-12"></a>
## 4-12 — Periodic rate dari nominal APR

[PDF 208](../Financial_Management_Theory_and_Practice_15e.pdf#page=208)

$$
r_{per}=r_{nom}/m
$$

**Variabel.** m: jumlah compounding periods per tahun; APR adalah nominal quotation.

**Penurunan dan logika.** Definisi nominal annual rate adalah m kali periodic rate.

**Syarat penggunaan.** Pembagian ini untuk APR nominal, bukan langsung untuk EAR.

**Kekeliruan yang perlu dihindari.** EAR 12% dibagi 12 bukan bunga bulanan efektif yang ekuivalen; gunakan akar untuk EAR.

**Contoh hitung.** APR 12%, m 12: bunga bulanan 1%.

```python
.12/12
```
Hasil presisi mesin: `0.01`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-13"></a>
## 4-13 — FV dengan compounding m kali

[PDF 209](../Financial_Management_Theory_and_Practice_15e.pdf#page=209)

$$
FV=PV(1+r_{nom}/m)^{mY}
$$

**Variabel.** Y: lama investasi dalam tahun; mY: jumlah periode.

**Penurunan dan logika.** Substitusikan periodic rate 4-12 dan period count mY ke 4-1.

**Syarat penggunaan.** APR dan frekuensi compounding diketahui; fraksi periode memerlukan konvensi yang ditetapkan.

**Kekeliruan yang perlu dihindari.** Membagi bunga tanpa mengalikan jumlah periode membuat jangka investasi salah.

**Contoh hitung.** PV 100, APR 12%, semesteran, Y 2: FV 126,247696.

```python
100*(1+.12/2)**4
```
Hasil presisi mesin: `126.247696`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-14"></a>
## 4-14 — Effective annual rate

[PDF 209](../Financial_Management_Theory_and_Practice_15e.pdf#page=209)

$$
EAR=(1+r_{nom}/m)^m-1
$$

**Variabel.** EAR: return satu tahun sesudah seluruh compounding.

**Penurunan dan logika.** Compound saldo satu unit selama m periode dan kurangi modal awal satu unit.

**Syarat penggunaan.** Tidak mencakup biaya tambahan kredit yang belum berada dalam arus kas kontrak.

**Kekeliruan yang perlu dihindari.** EAR berbeda dari APR ketika m>1 dan bunga bukan nol.

**Contoh hitung.** APR 12% semesteran: EAR 12,36%.

```python
(1+.12/2)**2-1
```
Hasil presisi mesin: `0.1236`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-4-15"></a>
## 4-15 — Real rate exact Fisher

[PDF 217](../Financial_Management_Theory_and_Practice_15e.pdf#page=217)

$$
r_{real}=(1+r_{nominal})/(1+\pi)-1
$$

**Variabel.** π: inflasi periode yang sama; nominal di sini return efektif, bukan APR yang belum disetarakan.

**Penurunan dan logika.** Pertumbuhan kekayaan nominal dibagi pertumbuhan tingkat harga memberi pertumbuhan daya beli.

**Syarat penggunaan.** Satuan periode dan basis nominal/real konsisten; 1+π>0.

**Kekeliruan yang perlu dihindari.** Nominal minus inflasi hanya pendekatan; tidak selalu persis sama.

**Contoh hitung.** Nominal 10% dan inflasi 5%: real 4,761905%.

```python
1.10/1.05-1
```
Hasil presisi mesin: `0.047619047619`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-4-01"></a>
## U-4-01 — Mencari tingkat dan waktu

[PDF 181](../Financial_Management_Theory_and_Practice_15e.pdf#page=181) · [PDF 182](../Financial_Management_Theory_and_Practice_15e.pdf#page=182) · [PDF 183](../Financial_Management_Theory_and_Practice_15e.pdf#page=183)

$$
r=(FV/PV)^{1/N}-1,\qquad N=\ln(FV/PV)/\ln(1+r)
$$

**Variabel.** PV, FV: besaran nilai positif untuk penyelesaian rasio; N: jumlah periode.

**Penurunan dan logika.** Ambil akar N dari FV/PV untukr; ambil log kedua sisi untuk N.

**Syarat penggunaan.** PV, FV>0; log 1+r terdefinisi dan bukan nol untuk formula N.

**Kekeliruan yang perlu dihindari.** Konvensi kas bertanda kalkulator perlu diubah menjadi rasio besaran positif dahulu.

**Contoh hitung.** PV 100, FV 121, N 2: r 10%.

```python
(121/100)**.5-1
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-4-02"></a>
## U-4-02 — Pinjaman amortisasi

[PDF 213](../Financial_Management_Theory_and_Practice_15e.pdf#page=213) · [PDF 214](../Financial_Management_Theory_and_Practice_15e.pdf#page=214)

$$
PMT=PV/pvaf(r,N),\quad I_t=rB_{t-1},\quad A_t=PMT-I_t,\quad B_t=B_{t-1}-A_t
$$

**Variabel.** Bt: saldo sesudah angsuran; At: pokok; It: bunga.

**Penurunan dan logika.** Samakan PV pinjaman dengan PV semua angsuran; bagi faktor anuitas. Saldo berkurang hanya oleh komponen pokok.

**Syarat penggunaan.** Bunga dan frekuensi angsuran sama; pembayaran akhir periode; r 0 memakai PMT=PV/N.

**Kekeliruan yang perlu dihindari.** Jangan menghitung bunga atas saldo setelah angsuran untuk pembayaran periode yang sama.

**Contoh hitung.** PV 100.000, r 6%, N 5: angsuran 23.739,640043.

```python
100000/pvaf(.06,5)
```
Hasil presisi mesin: `23739.6400431`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-4-03"></a>
## U-4-03 — Bunga sederhana dan continuous limit

[PDF 204](../Financial_Management_Theory_and_Practice_15e.pdf#page=204) · [PDF 205](../Financial_Management_Theory_and_Practice_15e.pdf#page=205) · [PDF 206](../Financial_Management_Theory_and_Practice_15e.pdf#page=206) · [PDF 207](../Financial_Management_Theory_and_Practice_15e.pdf#page=207)

$$
I=Prt,\quad FV_{simple}=P(1+rt),\quad FV_{continuous}=Pe^{rt}
$$

**Variabel.** P: pokok; r: annual rate sesuai konvensi; t: tahun/fraksi.

**Penurunan dan logika.** Simple interest tidak menambahkan bunga ke pokok. Compounding m kali setahun menuju exp(rt) saatm menuju tak hingga.

**Syarat penggunaan.** Day count dan basis bunga harus dinyatakan; continuousr bukan APRdenganm tertentu.

**Kekeliruan yang perlu dihindari.** Untuk periode lebih dari satu,1+rt berbeda dari(1+r)^t.

**Contoh hitung.** P 100, r 10%, t 2: FVsimple 120; continuous 122,140276.

```python
100*(1+.10*2)
```
Hasil presisi mesin: `120`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
