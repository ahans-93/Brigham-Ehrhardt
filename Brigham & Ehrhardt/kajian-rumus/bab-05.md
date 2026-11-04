# Bab 5: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../05-chapter.md)

## Navigasi

- [5-1: Nilai obligasi kupon tahunan](#rumus-5-1)
- [5-1a: Harga par: menjumlahkan kas obligasi sumber](#rumus-5-1a)
- [5-1b: Harga par dengan faktor anuitas](#rumus-5-1b)
- [5-2: Nilai obligasi kupon semesteran](#rumus-5-2)
- [5-3: Mencari YTM](#rumus-5-3)
- [5-4: Mencari yield to call](#rumus-5-4)
- [5-5: Komponen current dan capital gains yield](#rumus-5-5)
- [5-6: Dekomposisi tingkat bunga](#rumus-5-6)
- [5-7: Rata-rata inflation premium](#rumus-5-7)
- [U-5-01: Fisher exact dan perkiraan](#rumus-u-5-01)

<a id="rumus-5-1"></a>
## 5-1 — Nilai obligasi kupon tahunan

[PDF 238](../Financial_Management_Theory_and_Practice_15e.pdf#page=238)

$$
P_B=C\sum_{t=1}^{N}(1+y)^{-t}+F(1+y)^{-N}
$$

**Variabel.** C: kupon kas per tahun; F: par yang dilunasi pada maturity; y: required yield tahunan.

**Penurunan dan logika.** Pisahkan kontrak menjadi anuitas kupon dan pembayaran pokok tunggal, lalu jumlahkan PV keduanya.

**Syarat penggunaan.** Kas kontraktual pasti dalam model atau yield mencerminkan risikonya; tingkat dan tenor konstan.

**Kekeliruan yang perlu dihindari.** Coupon rate menentukan C, sedangkan yield menentukan discount factor. Keduanya bukan angka yang otomatis sama.

**Contoh hitung.** C 100, F 1000, y 10%, N 3 menghasilkan harga par 1.000.

```python
bond(100,1000,.1,3)
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-1a"></a>
## 5-1a — Harga par: menjumlahkan kas obligasi sumber

[PDF 239](../Financial_Management_Theory_and_Practice_15e.pdf#page=239)

$$
P=\sum_{t=1}^{15}90/(1.09)^t+1000/(1.09)^{15}=1000
$$

**Variabel.** Kupon 90, par 1000, tenor 15 tahun, yield 9%.

**Penurunan dan logika.** Discount tiap kupon dan pokok secara langsung; coupon rate sama dengan yield sehingga harga par.

**Syarat penggunaan.** Pembayaran tahunan dan tanggal valuasi sesuai model 5-1.

**Kekeliruan yang perlu dihindari.** Kesamaan harga par tidak berlaku bila yield berubah walaupun coupon rate kontraktual tetap 9%.

**Contoh hitung.** Rangkaian 14kas 90 dan kasakhir 1090 bernilai 1000.

```python
pv_stream([90]*14+[1090],.09)
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-1b"></a>
## 5-1b — Harga par dengan faktor anuitas

[PDF 239](../Financial_Management_Theory_and_Practice_15e.pdf#page=239)

$$
P=90\frac{1-1.09^{-15}}{.09}+1000(1.09)^{-15}=1000
$$

**Variabel.** Dua komponen adalah PV kupon dan PV pokok.

**Penurunan dan logika.** Ganti penjumlahan kupon 5-1a dengan closed-form annuity factor; hasil harus sama sebelum pembulatan.

**Syarat penggunaan.** Gunakan presisi penuh; angka komponen pada buku dibulatkan.

**Kekeliruan yang perlu dihindari.** Selisih akibat pembulatan intermediate bukan formula yang berbeda.

**Contoh hitung.** PV kupon ditambah pokok tetap 1000.

```python
90*pvaf(.09,15)+1000/1.09**15
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-2"></a>
## 5-2 — Nilai obligasi kupon semesteran

[PDF 245](../Financial_Management_Theory_and_Practice_15e.pdf#page=245)

$$
P_B=\sum_{t=1}^{2N}\frac{C/2}{(1+y_{nom}/2)^t}+\frac{F}{(1+y_{nom}/2)^{2N}}
$$

**Variabel.** C: kupon tahunan; yNom: quoted yield nominal dengan basis semester.

**Penurunan dan logika.** Ubah unit menjadi semester: bagi kupon dan yield nominal dua, kalikan banyak tahun dua.

**Syarat penggunaan.** Tanggal valuasi tepat sesudah kupon untuk bentuk dasar; accrued interest dan periode pecahan perlu perlakuan tambahan.

**Kekeliruan yang perlu dihindari.** Jangan membagi EAR dua jika input yang tersedia adalah yield efektif tahunan.

**Contoh hitung.** Kupon 100 per tahun, F 1000, quoted 10%, N 2 tahun: harga 1.000.

```python
bond(50,1000,.05,4)
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-3"></a>
## 5-3 — Mencari YTM

[PDF 246](../Financial_Management_Theory_and_Practice_15e.pdf#page=246)

$$
P_{market}=\sum_{t=1}^{N}\frac C{(1+YTM)^t}+\frac F{(1+YTM)^N}
$$

**Variabel.** YTM adalah akar persamaan harga terhadap yield; price, coupon, par dan tenor diketahui.

**Penurunan dan logika.** Balik 5-1 secara numerik. Untuk kas obligasi standar positif, harga turun monoton ketika yield naik sehingga akar pada domain yang relevan unik.

**Syarat penggunaan.** Diasumsikan pembayaran sampai maturity sesuai kontrak. Return terealisasi juga dipengaruhi default, penjualan, dan reinvestasi.

**Kekeliruan yang perlu dihindari.** YTM bukan coupon rate kecuali harga par pada model standar.

**Contoh hitung.** Harga 1000, C 100, F 1000, N 3: YTM 10%.

```python
ytm(1000,100,1000,3)
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-4"></a>
## 5-4 — Mencari yield to call

[PDF 248](../Financial_Management_Theory_and_Practice_15e.pdf#page=248)

$$
P=\sum_{t=1}^{N_c}\frac C{(1+YTC)^t}+\frac{CallPrice}{(1+YTC)^{N_c}}
$$

**Variabel.** Nc: periode sampai tanggal call yang diasumsikan; call price mengganti maturity par.

**Penurunan dan logika.** Gunakan PV kas yang berakhir pada call, lalu cari yield yang menyamakan PV dengan market price.

**Syarat penggunaan.** Tanggal dan harga call benar; model mengondisikan pada call, bukan menjamin call terjadi.

**Kekeliruan yang perlu dihindari.** Memakai maturity tenor bersama call price mencampur dua skenario kontrak.

**Contoh hitung.** Harga 1000, C 100, call 1000 setelah 2 tahun: YTC 10%.

```python
ytm(1000,100,1000,2)
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-5"></a>
## 5-5 — Komponen current dan capital gains yield

[PDF 249](../Financial_Management_Theory_and_Practice_15e.pdf#page=249)

$$
CurrentYield+CapitalGainsYield\approx YTM
$$

**Variabel.** Current yield=C/P 0; capital gains yield adalah perubahan harga per P 0 dengan konvensi horizon yang dinyatakan.

**Penurunan dan logika.** Return holding-period satu tahun selalu [C+P 1−P 0]/P 0. Di bawah model yield tetap dengan pembayaran tahunan yang sesuai, return ini merekonsiliasi ke required yield.

**Syarat penggunaan.** Sumber menulis kesamaan. Untuk coupon subannual, reinvestasi, dirty/clean price dan horizon lain, konvensinya harus disetarakan sebelum menyamakan ke quoted YTM.

**Kekeliruan yang perlu dihindari.** Jangan menyatakan jumlah dua komponen itu selalu sama dengan quoted nominal YTM untuk setiap obligasi dan horizon.

**Contoh hitung.** Current yield 8% dan capital gain yield 2% memberi return periode 10%.

```python
.08+.02
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-6"></a>
## 5-6 — Dekomposisi tingkat bunga

[PDF 249](../Financial_Management_Theory_and_Practice_15e.pdf#page=249)

$$
r_d=r^*+IP+MRP+DRP+LP
$$

**Variabel.** r*: real risk-free; IP: inflation premium; MRP: maturity risk premium; DRP: default; LP: liquidity.

**Penurunan dan logika.** Kerangka konseptual menjumlahkan kompensasi dasar dan premi risiko agar yield dapat diinterpretasikan.

**Syarat penggunaan.** Premi didefinisikan tanpa double counting; bukan bukti bahwa seluruh komponen dapat diobservasi secara terpisah dengan tepat.

**Kekeliruan yang perlu dihindari.** MRP di bab ini berarti maturity risk premium, berbeda dari market risk premium/RPM pada CAPM.

**Contoh hitung.** 2%+3%+1%+2%+0,5%=8,5%.

```python
.02+.03+.01+.02+.005
```
Hasil presisi mesin: `0.085`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-5-7"></a>
## 5-7 — Rata-rata inflation premium

[PDF 252](../Financial_Management_Theory_and_Practice_15e.pdf#page=252)

$$
IP_N=(\pi_1+\cdots+\pi_N)/N
$$

**Variabel.** πt: perkiraan inflasi tahun t, bukan return investasi.

**Penurunan dan logika.** Ambil rata-rata aritmetika ekspektasi inflasi sepanjang tenor sebagai pendekatan komponen inflasi yield.

**Syarat penggunaan.** Sumber menyebut approximated; untuk hubungan harga kumulatif exact gunakan produk faktor inflasi/geometric average.

**Kekeliruan yang perlu dihindari.** Rata-rata aritmetika ini tidak identik dengan inflasi majemuk tahunan pada jalur inflasi yang berubah.

**Contoh hitung.** Ekspektasi inflasi 2%,3%,4%: premium pendekatan 3%.

```python
(.02+.03+.04)/3
```
Hasil presisi mesin: `0.03`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-5-01"></a>
## U-5-01 — Fisher exact dan perkiraan

[PDF 250](../Financial_Management_Theory_and_Practice_15e.pdf#page=250) · [PDF 251](../Financial_Management_Theory_and_Practice_15e.pdf#page=251)

$$
1+r_n=(1+r_{real})(1+\pi),\quad r_n\approx r_{real}+\pi
$$

**Variabel.** rn: nominal return; pi: inflasi untuk periode sama.

**Penurunan dan logika.** Daya beli akhir=nilai nominal akhir dibagi indeks harga; rn=rreal+pi+rreal*pi.

**Syarat penggunaan.** Hubungan expected/realized inflation dibedakan; approximation mengabaikan perkalian.

**Kekeliruan yang perlu dihindari.** Tidak menambahkan premi default ke real rate ketika sedang mengisolasi Fisher dasar tanpa mengubah interpretasi.

**Contoh hitung.** Real 3%, inflasi 4%: nominal 7,12%, bukan tepat 7%.

```python
1.03*1.04-1
```
Hasil presisi mesin: `0.0712`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
