# Bab 7: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../07-chapter.md)

## Navigasi

- [7-1: Model nilai operasi FCF](#rumus-7-1)
- [7-2: Nilai operasi zero growth](#rumus-7-2)
- [7-2a: Substitusi perpetuitas B&B](#rumus-7-2a)
- [7-3: Total intrinsic entity value](#rumus-7-3)
- [7-4: Bridge entity ke ekuitas common](#rumus-7-4)
- [7-5: Nilai intrinsik per saham](#rumus-7-5)
- [7-6: Pertumbuhan FCF rekursif](#rumus-7-6)
- [7-7: Pertumbuhan FCF dari FCF 1](#rumus-7-7)
- [7-8: Deret FCF constant growth](#rumus-7-8)
- [7-9: Closed form constant-growth FCF](#rumus-7-9)
- [7-10: Constant growth dari FCF 0](#rumus-7-10)
- [7-11: Horizon value operasi](#rumus-7-11)
- [7-12: Multistage operating valuation](#rumus-7-12)
- [7-13: Value drivers OP dan CR](#rumus-7-13)
- [7-14: ROIC sebagai OP dibagi CR](#rumus-7-14)
- [7-15: Value drivers berbasis ROIC](#rumus-7-15)
- [7-16: Dividend discount model umum](#rumus-7-16)
- [7-17: Gordon growth saham](#rumus-7-17)
- [7-18: Expected equity return Gordon](#rumus-7-18)
- [7-19: Horizon value saham](#rumus-7-19)
- [7-20: Multistage DDM](#rumus-7-20)
- [7-21: Nilai saham preferen perpetuitas](#rumus-7-21)
- [7-22: Expected yield preferen](#rumus-7-22)

<a id="rumus-7-1"></a>
## 7-1 — Model nilai operasi FCF

[PDF 335](../Financial_Management_Theory_and_Practice_15e.pdf#page=335)

$$
V_{op}=\sum_{t=1}^{\infty}FCF_t/(1+WACC)^t
$$

**Variabel.** FCF sebelum distribusi pendanaan; WACC sesuai risiko operasi dan kebijakan leverage.

**Penurunan dan logika.** Sama dengan 1-1, kini diterapkan sebagai entity valuation. Diskontokan semua kas operasi yang tersedia bagi investor, bukan hanya dividen.

**Syarat penggunaan.** Nilai nonoperasi dan klaim pendanaan direkonsiliasi terpisah.

**Kekeliruan yang perlu dihindari.** Bunga tidak dikurangkan lagi dari FCF ketika WACC sudah memasukkan biaya pendanaan.

**Contoh hitung.** FCF 100 konstan dan WACC 10% memberi Vop 1000.

```python
100/.1
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-2"></a>
## 7-2 — Nilai operasi zero growth

[PDF 335](../Financial_Management_Theory_and_Practice_15e.pdf#page=335)

$$
V_{op}=FCF/WACC
$$

**Variabel.** FCF tahunan konstan mulai akhir periode pertama.

**Penurunan dan logika.** Bentuk perpetuitas 4-4 diterapkan pada free cash flow operasi.

**Syarat penggunaan.** WACC>0 dan FCF dapat dipertahankan; maintenance CAPEX harus sudah diperhitungkan.

**Kekeliruan yang perlu dihindari.** Zero growth tidak berarti seluruh CAPEX nol; aset masih dapat memerlukan investasi pengganti.

**Contoh hitung.** FCF 100 dan WACC 10% memberi 1000.

```python
100/.1
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-2a"></a>
## 7-2a — Substitusi perpetuitas B&B

[PDF 336](../Financial_Management_Theory_and_Practice_15e.pdf#page=336)

$$
V_{op}=10/.10=100
$$

**Variabel.** FCF 10 dan value 100 dalam juta dolar pada contoh buku.

**Penurunan dan logika.** Penerapan langsung 7-2 pada FCF konstan.

**Syarat penggunaan.** Kebutuhan investasi pemeliharaan sudah tercermin dalam FCF 10.

**Kekeliruan yang perlu dihindari.** Nilai 100 adalah operasi; investasi nonoperasi dan debt/preferred ditangani pada 7-3/7-4.

**Contoh hitung.** 10 pada cost 10% memberi 100.

```python
10/.10
```
Hasil presisi mesin: `100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-3"></a>
## 7-3 — Total intrinsic entity value

[PDF 336](../Financial_Management_Theory_and_Practice_15e.pdf#page=336)

$$
V_{entity}=V_{op}+V_{nonop}
$$

**Variabel.** Dalam model sumber Vnonop adalah short-term investments.

**Penurunan dan logika.** Jumlahkan nilai operasi dan aset yang tidak menghasilkan FCF operasi di model. Ini aditivitas aset tanpa penghitungan ganda.

**Syarat penggunaan.** Perusahaan lain dapat memiliki aset nonoperasi selain STI; gunakan nilai yang sesuai.

**Kekeliruan yang perlu dihindari.** Kas operasi minimum yang sudah menjadi NOWC tidak ditambahkan kembali sebagai excess cash.

**Contoh hitung.** Vop 1000 dan STI 50 memberi entity 1050.

```python
1000+50
```
Hasil presisi mesin: `1050`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-4"></a>
## 7-4 — Bridge entity ke ekuitas common

[PDF 337](../Financial_Management_Theory_and_Practice_15e.pdf#page=337)

$$
E=V_{entity}-D-PS
$$

**Variabel.** D: seluruh utang berbunga yang relevan; PS: nilai klaim preferen.

**Penurunan dan logika.** Common stock adalah residual setelah klaim kreditor dan preferen dikurangkan dari nilai aset total.

**Syarat penggunaan.** Gunakan nilai klaim sesuai tanggal valuasi; tambahkan klaim lain jika model memerlukannya.

**Kekeliruan yang perlu dihindari.** Accounts payable yang sudah mengurangi NOWC tidak otomatis dikurangi lagi sebagai debt dalam bridge ini.

**Contoh hitung.** Entity 1050, debt 300, preferred 50: common equity 700.

```python
1050-300-50
```
Hasil presisi mesin: `700`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-5"></a>
## 7-5 — Nilai intrinsik per saham

[PDF 337](../Financial_Management_Theory_and_Practice_15e.pdf#page=337)

$$
P_0=E/n
$$

**Variabel.** n: saham common yang berhak atas nilai ekuitas dalam model.

**Penurunan dan logika.** Bagi total common equity value dengan jumlah unit klaim common yang konsisten.

**Syarat penggunaan.** Periksa dilution, opsi, treasury shares, dan tanggal share count.

**Kekeliruan yang perlu dihindari.** Nilai operasi dibagi saham tanpa mengurangkan debt akan menilai klaim common terlalu tinggi.

**Contoh hitung.** Equity 700 dan 100 saham memberi nilai 7 per saham.

```python
700/100
```
Hasil presisi mesin: `7`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-6"></a>
## 7-6 — Pertumbuhan FCF rekursif

[PDF 339](../Financial_Management_Theory_and_Practice_15e.pdf#page=339)

$$
FCF_t=FCF_{t-1}(1+g)
$$

**Variabel.** g: pertumbuhan konstan antarperiode yang berurutan.

**Penurunan dan logika.** Tambahkan kenaikan g×FCF sebelumnya ke FCF sebelumnya.

**Syarat penggunaan.** FCF dengan tanda negatif memerlukan interpretasi; persentase pertumbuhan tidak selalu berarti perbaikan ekonomi.

**Kekeliruan yang perlu dihindari.** Jangan menerapkan g tanpa reinvestasi yang konsisten dengan proyeksi operasi.

**Contoh hitung.** FCF sebelumnya 100 dan g 5% menghasilkan 105.

```python
100*1.05
```
Hasil presisi mesin: `105`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-7"></a>
## 7-7 — Pertumbuhan FCF dari FCF 1

[PDF 339](../Financial_Management_Theory_and_Practice_15e.pdf#page=339)

$$
FCF_t=FCF_1(1+g)^{t-1}
$$

**Variabel.** FCF 1 adalah kas satu periode dari sekarang; eksponen t−1.

**Penurunan dan logika.** Iterasikan 7-6 sebanyak t−1 langkah mulai dari tahun 1.

**Syarat penggunaan.** g konstan selama interval yang diproyeksikan.

**Kekeliruan yang perlu dihindari.** Eksponen t akan membuat FCF tumbuh satu periode terlalu banyak.

**Contoh hitung.** FCF 1=100, g 10%, t 3 menghasilkan 121.

```python
100*1.1**2
```
Hasil presisi mesin: `121`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-8"></a>
## 7-8 — Deret FCF constant growth

[PDF 339](../Financial_Management_Theory_and_Practice_15e.pdf#page=339)

$$
V_{op}=\sum_{t=1}^{\infty}\frac{FCF_1(1+g)^{t-1}}{(1+WACC)^t}
$$

**Variabel.** FCF 1: kas pertama yang belum diterima.

**Penurunan dan logika.** Substitusi 7-7 ke 7-1. Rasio suku deret q=(1+g)/(1+WACC).

**Syarat penggunaan.** Model standar memakai g>−1, WACC>g agar |q|<1.

**Kekeliruan yang perlu dihindari.** Bentuk deret berguna untuk memeriksa closed form; g≥WACC tidak menghasilkan nilai finite.

**Contoh hitung.** FCF 1=105, g 5%, WACC 10%: PV mendekati 2100.

```python
growing_pv_sum(105,.05,.10,1000)
```
Hasil presisi mesin: `2100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-9"></a>
## 7-9 — Closed form constant-growth FCF

[PDF 340](../Financial_Management_Theory_and_Practice_15e.pdf#page=340)

$$
V_{op}=FCF_1/(WACC-g)
$$

**Variabel.** WACC−g adalah selisih rate, bukan WACC dibagi g.

**Penurunan dan logika.** Gunakan jumlah deret geometri dari 7-8: [FCF 1/(1+WACC)]/[1−q]. Penyederhanaannya memberi denominator WACC−g.

**Syarat penggunaan.** Konvergensi 7-8 dan cash flow setelah reinvestasi yang memadai.

**Kekeliruan yang perlu dihindari.** Selisih kecil WACC−g membuat nilai sangat sensitif terhadap input.

**Contoh hitung.** 105/(10%−5%)=2100.

```python
105/(.10-.05)
```
Hasil presisi mesin: `2100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-10"></a>
## 7-10 — Constant growth dari FCF 0

[PDF 341](../Financial_Management_Theory_and_Practice_15e.pdf#page=341)

$$
V_{op}=FCF_0(1+g)/(WACC-g)
$$

**Variabel.** FCF 0: kas periode yang baru selesai, bukan pembayaran masa depan pertama.

**Penurunan dan logika.** Majukan FCF 0 satu periode dengan g untuk memperoleh FCF 1, lalu gunakan 7-9.

**Syarat penggunaan.** Pertumbuhan stabil dimulai segera setelah tanggal 0.

**Kekeliruan yang perlu dihindari.** Memakai FCF 0 langsung sebagai numerator menurunkan nilai sebesar faktor 1+g.

**Contoh hitung.** FCF 0=100, g 5%, WACC 10% memberi 2100.

```python
100*1.05/(.10-.05)
```
Hasil presisi mesin: `2100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-11"></a>
## 7-11 — Horizon value operasi

[PDF 343](../Financial_Management_Theory_and_Practice_15e.pdf#page=343)

$$
HV_T=FCF_T(1+g)/(WACC-g)
$$

**Variabel.** HVT: nilai pada akhir T atas FCF setelah T.

**Penurunan dan logika.** Pada tanggal T, FCF berikutnya adalah FCF(T+1). Terapkan 7-9 pada tanggal baru itu.

**Syarat penggunaan.** Parameter stabil mulai T+1; tidak memasukkan FCF(T) lagi dalam horizon.

**Kekeliruan yang perlu dihindari.** Horizon value bukan PVhariini; masih harus didiskontokan T periode.

**Contoh hitung.** FCFT 100, g 5%, WACC 10% memberi HVT 2100.

```python
100*1.05/(.10-.05)
```
Hasil presisi mesin: `2100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-12"></a>
## 7-12 — Multistage operating valuation

[PDF 345](../Financial_Management_Theory_and_Practice_15e.pdf#page=345)

$$
V_{op,0}=\sum_{t=1}^{T}\frac{FCF_t}{(1+WACC)^t}+\frac{HV_T}{(1+WACC)^T}
$$

**Variabel.** Forecast eksplisit sampai T; horizon memuat kas mulai T+1.

**Penurunan dan logika.** Pisahkan deret seluruh kas menjadi dua bagian yang tidak tumpang tindih; diskontokan keduanya ke 0.

**Syarat penggunaan.** Rate tunggal sesuai risiko; untuk rate berubah gunakan produk discount factors.

**Kekeliruan yang perlu dihindari.** Jangan memasukkan kas T+1 dalam forecast eksplisit sekaligus seluruh terminal value yang sudah mencakup kas tersebut.

**Contoh hitung.** FCF 1=100, HV 1=1000, WACC 10% memberi nilai 1000.

```python
(100+1000)/1.1
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-13"></a>
## 7-13 — Value drivers OP dan CR

[PDF 355](../Financial_Management_Theory_and_Practice_15e.pdf#page=355)

$$
V_{op,T}=K_T\left[1+\frac{(1+g)(OP_T/CR_T)-WACC}{WACC-g}\right]
$$

**Variabel.** K: modal operasi; OP=NOPAT/Sales; CR=K/Sales pada T.

**Penurunan dan logika.** Dengan rasio stabil, NOPAT(T+1)=(1+g)OP×Sales T dan ΔK=gKT. Substitusi FCF(T+1)=(1+g)NOPATT−gKT ke horizon model memberi bentuk ini.

**Syarat penggunaan.** OP, CR, g stabil pada horizon; WACC>g; timing modal mengikuti model sumber.

**Kekeliruan yang perlu dihindari.** Jangan mengganti CR dengan asset turnover tanpa membalik pecahan atau mengubah basis operasi.

**Contoh hitung.** K 100, OP 6%, CR 0,4, g 5%, WACC 10% memberi 215.

```python
100*(1+((1.05)*(.06/.4)-.10)/(.10-.05))
```
Hasil presisi mesin: `215`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-14"></a>
## 7-14 — ROIC sebagai OP dibagi CR

[PDF 355](../Financial_Management_Theory_and_Practice_15e.pdf#page=355)

$$
OP/CR=(NOPAT/Sales)/(K/Sales)=NOPAT/K=ROIC
$$

**Variabel.** OP, CR, K menggunakan tanggal dan penjualan yang sama.

**Penurunan dan logika.** Sales saling hapus dari dua pecahan; hasilnya definisi ROIC.

**Syarat penggunaan.** Sales dan modal bukan nol; basis kapital sama.

**Kekeliruan yang perlu dihindari.** Ini bukan ROE; common equity tidak menjadi denominator.

**Contoh hitung.** OP 6% dan CR 0,4 memberi ROIC 15%.

```python
.06/.4
```
Hasil presisi mesin: `0.15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-15"></a>
## 7-15 — Value drivers berbasis ROIC

[PDF 355](../Financial_Management_Theory_and_Practice_15e.pdf#page=355)

$$
V_{op,T}=K_T\left[1+\frac{(1+g)ROIC_T-WACC}{WACC-g}\right]
$$

**Variabel.** ROICT berbasis modal T sesuai 7-14.

**Penurunan dan logika.** Ganti OP/CR di 7-13 dengan ROIC. Bentuk ekuivalen adalah K[(1+g)ROIC−g]/(WACC−g).

**Syarat penggunaan.** Asumsi horizon 7-13 tetap diperlukan; ROIC average/awal berbeda tidak dapat ditukar begitu saja.

**Kekeliruan yang perlu dihindari.** Pertumbuhan tidak boleh dinaikkan secara terpisah tanpa proyeksi tambahan modal operasi.

**Contoh hitung.** K 100, ROIC 15%, g 5%, WACC 10% memberi 215.

```python
100*(1+(1.05*.15-.10)/(.10-.05))
```
Hasil presisi mesin: `215`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-16"></a>
## 7-16 — Dividend discount model umum

[PDF 358](../Financial_Management_Theory_and_Practice_15e.pdf#page=358)

$$
P_0=\sum_{t=1}^{\infty}D_t/(1+r_s)^t
$$

**Variabel.** Dt: dividen common per saham; rs: required equity return.

**Penurunan dan logika.** Nilai saham adalah PV distribusi kas kepada pemiliknya; penjualan saham di masa depan mewakili PV dividen setelah tanggal penjualan.

**Syarat penggunaan.** Model distribusi konsisten dan deret konvergen; perubahan repurchase/sharecount harus dipertimbangkan dalam dividen per saham.

**Kekeliruan yang perlu dihindari.** Gunakan cost of equity, bukan WACC, untuk kas khusus pemegang saham.

**Contoh hitung.** Dividen 10 konstan mulai tahun 1 dan rs 10% memberi harga 100.

```python
10/.1
```
Hasil presisi mesin: `100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-17"></a>
## 7-17 — Gordon growth saham

[PDF 359](../Financial_Management_Theory_and_Practice_15e.pdf#page=359)

$$
P_0=D_0(1+g)/(r_s-g)=D_1/(r_s-g)
$$

**Variabel.** D 0: dividen baru dibayar; D 1: dividen berikutnya.

**Penurunan dan logika.** Substitusi pertumbuhan dividen konstan ke 7-16 dan jumlahkan geometric series.

**Syarat penggunaan.** rs>g, pertumbuhan berkelanjutan dan kebijakan distribusi koheren.

**Kekeliruan yang perlu dihindari.** Harga sangat sensitif terhadap g mendekati rs; dividen nol sementara bukan alasan nilai perusahaan harus nol.

**Contoh hitung.** D 0=4, g 5%, rs 10% memberi P 084.

```python
4*1.05/(.10-.05)
```
Hasil presisi mesin: `84`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-18"></a>
## 7-18 — Expected equity return Gordon

[PDF 360](../Financial_Management_Theory_and_Practice_15e.pdf#page=360)

$$
\hat r_s=D_1/P_0+g
$$

**Variabel.** D 1/P 0: expected dividend yield; g: expected capital gains yield pada model stabil.

**Penurunan dan logika.** Susun ulang 7-17: P 0(rs−g)=D 1. Dalam equilibrium expected return sama dengan required return, tetapi konsepnya tetap berbeda.

**Syarat penggunaan.** Harga mencerminkan model constant growth dan parameter tepat.

**Kekeliruan yang perlu dihindari.** g tidak sama dengan realized capital gain untuk satu tahun yang kebetulan diamati.

**Contoh hitung.** D 1=4,2, P 0=84, g 5% memberi expected 10%.

```python
4.2/84+.05
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-19"></a>
## 7-19 — Horizon value saham

[PDF 362](../Financial_Management_Theory_and_Practice_15e.pdf#page=362)

$$
P_T=D_{T+1}/(r_s-g)=D_T(1+g)/(r_s-g)
$$

**Variabel.** Nilai saham tepat setelah dividen T dibayar.

**Penurunan dan logika.** Terapkan Gordon pada tanggal T atas pembayaran sesudah T.

**Syarat penggunaan.** Stabil mulai T+1; rs>g.

**Kekeliruan yang perlu dihindari.** Jika valuasi cum-dividend sebelum dividen T, pembayaran T perlu perlakuan tersendiri.

**Contoh hitung.** DT 4, g 5%, rs 10% memberi PT 84.

```python
4*1.05/(.10-.05)
```
Hasil presisi mesin: `84`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-20"></a>
## 7-20 — Multistage DDM

[PDF 363](../Financial_Management_Theory_and_Practice_15e.pdf#page=363)

$$
P_0=\sum_{t=1}^{T}D_t/(1+r_s)^t+P_T/(1+r_s)^T
$$

**Variabel.** PT: terminal equity price, bukan nilai operasi.

**Penurunan dan logika.** Aditivitas PV dividen fase nonconstant dan seluruh dividen masa stabil yang diringkas diPT.

**Syarat penggunaan.** Periode dan share count konsisten; terminal dividend berasal dari T+1.

**Kekeliruan yang perlu dihindari.** Jangan mengurangkan debt lagi dari hasil DDM; model ini sudah khusus ekuitas.

**Contoh hitung.** D 1=4, PTpadatahun 1=84, rs 10% memberi P 080.

```python
(4+84)/1.1
```
Hasil presisi mesin: `80`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-21"></a>
## 7-21 — Nilai saham preferen perpetuitas

[PDF 367](../Financial_Management_Theory_and_Practice_15e.pdf#page=367)

$$
V_{ps}=D_{ps}/r_{ps}
$$

**Variabel.** Dps: dividen preferen tetap per periode.

**Penurunan dan logika.** Perpetuitas 4-4 diterapkan pada fixed preferred dividend.

**Syarat penggunaan.** Preferen tidak memiliki maturity, call atau redemption yang mengubah arus kas dalam bentuk dasar ini.

**Kekeliruan yang perlu dihindari.** Preferen callable/floating-rate tidak otomatis bernilai menurut perpetuitas fixed sederhana.

**Contoh hitung.** Dps 8 dan required 8% memberi 100.

```python
8/.08
```
Hasil presisi mesin: `100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-7-22"></a>
## 7-22 — Expected yield preferen

[PDF 367](../Financial_Management_Theory_and_Practice_15e.pdf#page=367)

$$
\hat r_{ps}=D_{ps}/V_{ps}
$$

**Variabel.** Yield preferen perpetual dengan distribusi konstan.

**Penurunan dan logika.** Susun ulang 7-21 untuk mencari required/expected yield dalam equilibrium.

**Syarat penggunaan.** Dividen dibayar sebagaimana model; perubahan harga dan default/omission dapat mengubah realized return.

**Kekeliruan yang perlu dihindari.** Yield dividen bukan jaminan total return terealisasi.

**Contoh hitung.** Dividen 8 dan harga 100 memberi 8%.

```python
8/100
```
Hasil presisi mesin: `0.08`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
