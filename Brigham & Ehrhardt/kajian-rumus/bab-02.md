# Bab 2: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../02-chapter.md)

## Navigasi

- [2-1: Net cash flow umum](#rumus-2-1)
- [2-2: Net cash flow pendekatan D&A](#rumus-2-2)
- [2-3: NOPAT](#rumus-2-3)
- [2-4: Net operating working capital](#rumus-2-4)
- [2-5: Total net operating capital](#rumus-2-5)
- [2-6: Total investor-supplied capital](#rumus-2-6)
- [2-7: Rekonsiliasi modal investor ke modal operasi](#rumus-2-7)
- [2-8: Free cash flow berbasis investasi neto](#rumus-2-8)
- [2-9: FCF berbasis investasi bruto](#rumus-2-9)
- [2-9a: Rekonsiliasi FCF investasi bruto dan neto](#rumus-2-9a)
- [2-9b: FCF setelah membatalkan depresiasi](#rumus-2-9b)
- [2-10: ROIC](#rumus-2-10)
- [2-11: Operating profitability ratio](#rumus-2-11)
- [2-11a: Substitusi operating profitability Micro Drive](#rumus-2-11a)
- [2-12: Capital requirement ratio](#rumus-2-12)
- [2-12a: Substitusi capital requirement Micro Drive](#rumus-2-12a)
- [2-13: MVA ekuitas](#rumus-2-13)
- [2-13a: MVA berbasis seluruh modal investor](#rumus-2-13a)
- [2-14: Economic value added](#rumus-2-14)
- [2-15: EVA dari spread ROIC](#rumus-2-15)

<a id="rumus-2-1"></a>
## 2-1 — Net cash flow umum

[PDF 107](../Financial_Management_Theory_and_Practice_15e.pdf#page=107)

$$
NCF=NI-NoncashRevenue+NoncashExpense
$$

**Variabel.** NI: laba tersedia bagi common shareholders; NCF: ukuran cash earnings buku; revenue/expense nonkas: unsur laba tanpa kas periode ini.

**Penurunan dan logika.** Mulai dari laba akrual; pendapatan tanpa kas dibalik dengan pengurangan, beban tanpa kas dibalik dengan penambahan. Ini rekonsiliasi unsur nonkas, bukan otomatis seluruh rekonsiliasi CFO.

**Syarat penggunaan.** Klasifikasi nonkas benar dan memakai periode yang sama. Perubahan piutang, persediaan, serta utang operasi masih perlu dianalisis untuk laporan arus kas.

**Kekeliruan yang perlu dihindari.** Jangan menyamakan NCF versi buku dengan kas bank, CFO, atau FCF.

**Contoh hitung.** NI 100, revenue nonkas 10, expense nonkas 30 menghasilkan NCF 120.

```python
100-10+30
```
Hasil presisi mesin: `120`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-2"></a>
## 2-2 — Net cash flow pendekatan D&A

[PDF 107](../Financial_Management_Theory_and_Practice_15e.pdf#page=107)

$$
NCF\approx NI+Depreciation+Amortization
$$

**Variabel.** D&A: penyusutan dan amortisasi yang masuk NI.

**Penurunan dan logika.** Bentuk khusus 2-1 saat neto unsur nonkas selain D&A diasumsikan nol. Tanda tambah mengembalikan beban nonkas yang sudah mengurangi laba.

**Syarat penggunaan.** Pendekatan penyederhanaan; bukan kesamaan universal jika ada pendapatan nonkas, provisi, atau impairment lain.

**Kekeliruan yang perlu dihindari.** Menambahkan D&A tanpa memeriksa unsur nonkas lain dapat melebihkan/merendahkan cash earnings.

**Contoh hitung.** NI 100 dan D&A 20, tanpa unsur nonkas lain: NCF 120.

```python
100+20
```
Hasil presisi mesin: `120`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-3"></a>
## 2-3 — NOPAT

[PDF 109](../Financial_Management_Theory_and_Practice_15e.pdf#page=109)

$$
NOPAT=EBIT(1-T)
$$

**Variabel.** EBIT: laba operasi sebelum bunga/pajak; T: tarif pajak operasi model.

**Penurunan dan logika.** Pajak operasi hipotetis adalah T×EBIT; sisanya EBIT−T×EBIT. Biaya pendanaan dikeluarkan agar operasi dapat dinilai terpisah dari leverage.

**Syarat penggunaan.** Tarif dan manfaat/rugi pajak yang relevan benar-benar tersedia dalam model; jika tidak, proyeksikan pajak kas secara eksplisit.

**Kekeliruan yang perlu dihindari.** NI tidak boleh dipakai sebagai pengganti EBIT pada rumus ini.

**Contoh hitung.** EBIT 100 dan T 25% memberi NOPAT 75.

```python
100*(1-.25)
```
Hasil presisi mesin: `75`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-4"></a>
## 2-4 — Net operating working capital

[PDF 110](../Financial_Management_Theory_and_Practice_15e.pdf#page=110)

$$
NOWC=OCA-OCL
$$

**Variabel.** OCA: aset lancar operasi; OCL: kewajiban lancar operasi tanpa bunga.

**Penurunan dan logika.** Aset operasi yang dibiayai pemasok dan accruals tidak memerlukan pendanaan investor; selisihnya adalah kebutuhan modal kerja operasi neto.

**Syarat penggunaan.** Pisahkan excess cash/investasi nonoperasi dan utang berbunga. Operating cash minimum dapat termasuk OCA sesuai model.

**Kekeliruan yang perlu dihindari.** Mengurangkan notes payable sebagai OCL akan mengurangi kebutuhan modal dua kali ketika pendanaan utang juga dimodelkan.

**Contoh hitung.** OCA 140 dikurangi OCL 40 menghasilkan NOWC 100.

```python
140-40
```
Hasil presisi mesin: `100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-5"></a>
## 2-5 — Total net operating capital

[PDF 110](../Financial_Management_Theory_and_Practice_15e.pdf#page=110)

$$
K_{op}=NOWC+NOLA
$$

**Variabel.** NOLA: net operating long-term assets; Kop: seluruh modal operasi neto.

**Penurunan dan logika.** Gabungkan modal kerja operasi dengan aset operasi jangka panjang neto. Ini mengelompokkan modal menurut penggunaan, bukan sumber pendanaan.

**Syarat penggunaan.** Aset nonoperasi tidak dimasukkan; depresiasi dan klasifikasi aset konsisten dengan NOPAT.

**Kekeliruan yang perlu dihindari.** Total assets tidak otomatis sama dengan modal operasi neto.

**Contoh hitung.** NOWC 100 dan aset operasi jangka panjang neto 200: Kop 300.

```python
100+200
```
Hasil presisi mesin: `300`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-6"></a>
## 2-6 — Total investor-supplied capital

[PDF 110](../Financial_Management_Theory_and_Practice_15e.pdf#page=110)

$$
K_{inv}=NP+LTD+PS+CE
$$

**Variabel.** NP: notes payable berbunga; LTD: utang jangka panjang; PS: saham preferen; CE: common equity.

**Penurunan dan logika.** Jumlahkan klaim modal yang disediakan investor/kreditor. Operating payables tidak termasuk pendanaan investor dalam definisi model ini.

**Syarat penggunaan.** Gunakan basis neraca yang sama; tidak mencampur nilai pasar salah satu klaim dengan nilai buku klaim lain.

**Kekeliruan yang perlu dihindari.** Kinv dapat membiayai aset nonoperasi sehingga tidak selalu sama dengan Kop.

**Contoh hitung.** NP 20, LTD 100, PS 10 dan CE 170: modal investor 300.

```python
20+100+10+170
```
Hasil presisi mesin: `300`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-7"></a>
## 2-7 — Rekonsiliasi modal investor ke modal operasi

[PDF 111](../Financial_Management_Theory_and_Practice_15e.pdf#page=111)

$$
K_{inv,op}=K_{inv}-STI_{nonop}
$$

**Variabel.** STI: short-term investments yang tidak diperlukan operasi.

**Penurunan dan logika.** Kurangi modal investor yang tertanam dalam investasi nonoperasi untuk memperoleh modal yang mendanai operasi. Contoh sumber: 2.530−40=2.490.

**Syarat penggunaan.** Pada model sederhana sumber, hanya STI yang perlu dikeluarkan; perusahaan lain dapat memiliki aset nonoperasi tambahan.

**Kekeliruan yang perlu dihindari.** Kotak tercetak pada PDF 111 memakai kata operating pada ruas kanan secara ambigu. Ruas kanan harus dibaca sebagai TOTAL modal investor sebelum pengurangan; jika dibaca sebagai modal operasi yang sama, persamaan menjadi self-reference.

**Contoh hitung.** Modal investor 300 dan STI nonoperasi 20 menghasilkan modal investor operasi 280.

```python
300-20
```
Hasil presisi mesin: `280`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-8"></a>
## 2-8 — Free cash flow berbasis investasi neto

[PDF 111](../Financial_Management_Theory_and_Practice_15e.pdf#page=111)

$$
FCF_t=NOPAT_t-(K_{op,t}-K_{op,t-1})
$$

**Variabel.** ΔKop: tambahan modal operasi neto selama t.

**Penurunan dan logika.** NOPAT merupakan hasil operasi setelah pajak. Bagian yang harus ditahan untuk menambah modal operasi tidak tersedia bagi investor; sisanya adalah FCF.

**Syarat penggunaan.** Definisi modal dan NOPAT konsisten; transaksi akuisisi/penjualan/revaluasi perlu direkonsiliasi bila perubahan neraca bukan seluruhnya investasi kas.

**Kekeliruan yang perlu dihindari.** Jangan menganggap pertumbuhan modal karena revaluasi sebagai pembayaran CAPEX kas tanpa rekonsiliasi.

**Contoh hitung.** NOPAT 30, Kop akhir 280 dan awal 260: FCF 10.

```python
30-(280-260)
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-9"></a>
## 2-9 — FCF berbasis investasi bruto

[PDF 112](../Financial_Management_Theory_and_Practice_15e.pdf#page=112)

$$
FCF=EBIT(1-T)+Dep-CAPEX-\Delta NOWC
$$

**Variabel.** Dep: penyusutan yang sudah mengurangi EBIT; CAPEX: investasi bruto aset tetap operasi.

**Penurunan dan logika.** Gunakan Δnet fixed assets = CAPEX−Dep dalam 2-8. Penyusutan muncul kembali sebagai penambahan karena investasi bruto digunakan.

**Syarat penggunaan.** Tidak ada perubahan aset nonkas lain yang belum direkonsiliasi; untuk amortisasi, gunakan D&A dan klasifikasi investasi yang konsisten.

**Kekeliruan yang perlu dihindari.** Memakai CAPEX neto sekaligus menambahkan seluruh Dep akan menggandakan penyesuaian.

**Contoh hitung.** NOPAT 30, Dep 10, CAPEX 20 dan ΔNOWC 10: FCF 10.

```python
30+10-20-10
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-9a"></a>
## 2-9a — Rekonsiliasi FCF investasi bruto dan neto

[PDF 112](../Financial_Management_Theory_and_Practice_15e.pdf#page=112)

$$
FCF=(NOPAT+Dep)-(NetFAInvestment+Dep)-\Delta NOWC
$$

**Variabel.** NetFAInvestment: perubahan aset tetap operasi neto yang berasal dari investasi.

**Penurunan dan logika.** Substitusi gross CAPEX=net FA investment+Dep ke 2-9 menunjukkan Dep ada sekali pada penambahan dan sekali pada pengurangan.

**Syarat penggunaan.** Tidak ada revaluasi, transaksi nonkas atau perubahan klasifikasi aset yang belum direkonsiliasi.

**Kekeliruan yang perlu dihindari.** Menambahkan Dep setelah memakai formula 2-9b akan double count.

**Contoh hitung.** Data sumber NOPAT 300, Dep 200, net FAinvestment 300,ΔNOWC 260 memberi−260.

```python
(300+200)-(300+200)-260
```
Hasil presisi mesin: `-260`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-9b"></a>
## 2-9b — FCF setelah membatalkan depresiasi

[PDF 112](../Financial_Management_Theory_and_Practice_15e.pdf#page=112)

$$
FCF=NOPAT-NetFAInvestment-\Delta NOWC
$$

**Variabel.** Dua investasi neto menjumlah net investment in operating capital.

**Penurunan dan logika.** Batalkan +Dep dan−Dep pada 2-9a; gabungan pengurangan menghasilkan 2-8.

**Syarat penggunaan.** Definisi modal operasi serta rekonsiliasi nonkas konsisten.

**Kekeliruan yang perlu dihindari.** Ini bukan bukti depresiasi tidak berpengaruh ekonomi; efek pajak Dep sudah berada dalam NOPAT.

**Contoh hitung.** NOPAT 300, net FA 300,ΔNOWC 260 memberi−260.

```python
300-300-260
```
Hasil presisi mesin: `-260`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-10"></a>
## 2-10 — ROIC

[PDF 116](../Financial_Management_Theory_and_Practice_15e.pdf#page=116)

$$
ROIC=NOPAT/K_{op}
$$

**Variabel.** NOPAT dan Kop memakai basis operasi yang sama.

**Penurunan dan logika.** Definisi return operasi per unit modal: bagi laba operasi setelah pajak dengan modal yang menghasilkan laba tersebut.

**Syarat penggunaan.** Buku memakai modal yang ditentukan soal. Untuk analisis nyata, saldo awal/rata-rata harus dinyatakan dan tidak diganti diam-diam.

**Kekeliruan yang perlu dihindari.** NI/assets adalah ROA, bukan ROIC; ROIC berbasis saldo berbeda tidak langsung dapat dibandingkan.

**Contoh hitung.** NOPAT 30 dan Kop 300: ROIC 10%.

```python
30/300
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-11"></a>
## 2-11 — Operating profitability ratio

[PDF 116](../Financial_Management_Theory_and_Practice_15e.pdf#page=116)

$$
OP=NOPAT/Sales
$$

**Variabel.** OP: margin operasi setelah pajak, bukan EBIT margin.

**Penurunan dan logika.** Bagi hasil operasi setelah pajak dengan penjualan. Rasio menunjukkan laba operasi setelah pajak per unit pendapatan.

**Syarat penggunaan.** Penjualan dan NOPAT periode sama; normalisasi unsur operasi sekali jalan untuk perbandingan.

**Kekeliruan yang perlu dihindari.** Jangan membandingkan OP dengan net margin tanpa mengakui dampak bunga dan nonoperasi.

**Contoh hitung.** NOPAT 30 dan penjualan 500: OP 6%.

```python
30/500
```
Hasil presisi mesin: `0.06`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-11a"></a>
## 2-11a — Substitusi operating profitability Micro Drive

[PDF 116](../Financial_Management_Theory_and_Practice_15e.pdf#page=116)

$$
OP=300/5000=6\%
$$

**Variabel.** NOPAT 300 dan sales 5000 memakai satuan jutaan yang sama.

**Penurunan dan logika.** Penerapan langsung 2-11; satuan uang saling hapus.

**Syarat penggunaan.** Numerator NOPAT, bukan NI 300 yang kebetulan bernilai sama.

**Kekeliruan yang perlu dihindari.** 6% adalah OP, bukan ROIC karena modal operasi belum menjadi denominator.

**Contoh hitung.** Angka sumber menghasilkan 0,06.

```python
300/5000
```
Hasil presisi mesin: `0.06`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-12"></a>
## 2-12 — Capital requirement ratio

[PDF 116](../Financial_Management_Theory_and_Practice_15e.pdf#page=116)

$$
CR=K_{op}/Sales
$$

**Variabel.** CR: modal operasi yang dibutuhkan per unit penjualan.

**Penurunan dan logika.** Bagi modal operasi dengan penjualan. Menggabungkannya dengan 2-11 memberi ROIC = OP/CR jika basis modal sama.

**Syarat penggunaan.** Satuan penjualan adalah per tahun, sehingga rasio secara dimensional dapat dibaca sebagai kebutuhan modal per penjualan tahunan.

**Kekeliruan yang perlu dihindari.** CR yang lebih rendah bisa mencerminkan efisiensi, tetapi juga underinvestment atau kapasitas yang belum cukup.

**Contoh hitung.** Kop 300 dan sales 500: CR 0,6.

```python
300/500
```
Hasil presisi mesin: `0.6`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-12a"></a>
## 2-12a — Substitusi capital requirement Micro Drive

[PDF 116](../Financial_Management_Theory_and_Practice_15e.pdf#page=116)

$$
CR=3050/5000=61\%
$$

**Variabel.** 3050: total net operating capital;5000: sales.

**Penurunan dan logika.** Penerapan 2-12. Kotak sumber mencetak label OP pada contoh, tetapi numerator/denominator serta konteks menunjukkan CR.

**Syarat penggunaan.** Ini koreksi label dengan mempertahankan angka dan logika model sumber.

**Kekeliruan yang perlu dihindari.** Jangan menafsirkan 61% sebagai margin NOPAT; OP dari 2-11a adalah 6%.

**Contoh hitung.** Data sumber memberi CR 0,61.

```python
3050/5000
```
Hasil presisi mesin: `0.61`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-13"></a>
## 2-13 — MVA ekuitas

[PDF 118](../Financial_Management_Theory_and_Practice_15e.pdf#page=118)

$$
MVA=nP-CE_{book}
$$

**Variabel.** n: jumlah saham common; P: harga per saham; CEbook: modal common tercatat.

**Penurunan dan logika.** Nilai ekuitas pasar adalah n×P. Kurangi modal ekuitas yang disediakan investor sesuai definisi buku untuk mengukur nilai pasar tambahan.

**Syarat penggunaan.** Definisi berbasis ekuitas; MVA total perusahaan menggunakan semua klaim dan basis modal berbeda.

**Kekeliruan yang perlu dihindari.** Jangan mengurangi debt dari nP lagi; nP sudah merupakan nilai ekuitas.

**Contoh hitung.** 100 saham bernilai 5 per saham dan CEbook 300: MVA 200.

```python
100*5-300
```
Hasil presisi mesin: `200`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-13a"></a>
## 2-13a — MVA berbasis seluruh modal investor

[PDF 118](../Financial_Management_Theory_and_Practice_15e.pdf#page=118)

$$
MVA=(MarketEquity+MarketDebt)-InvestorSuppliedCapital
$$

**Variabel.** Semua klaim yang masuk definisi total harus dihitung konsisten, termasuk preferred jika ada dalam model.

**Penurunan dan logika.** Perluas MVA ekuitas menjadi selisih total nilai pasar klaim dan modal investor yang disediakan.

**Syarat penggunaan.** Buku menulis equity+debt dalam contoh sederhana; jangan menghilangkan preferred pada perusahaan yang memilikinya.

**Kekeliruan yang perlu dihindari.** MVA ekuitas dan MVA total tidak identik bila nilai pasar debt berbeda dari basis modal debt.

**Contoh hitung.** Market equity 700, debt 300, modalinvestor 800 menghasilkan 200.

```python
700+300-800
```
Hasil presisi mesin: `200`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-14"></a>
## 2-14 — Economic value added

[PDF 119](../Financial_Management_Theory_and_Practice_15e.pdf#page=119)

$$
EVA=NOPAT-K_{op}WACC
$$

**Variabel.** Kop×WACC: biaya ekonomis modal setelah pajak yang dipakai operasi.

**Penurunan dan logika.** Laba operasi setelah pajak dikurangi imbal hasil minimum yang disyaratkan penyedia modal menghasilkan economic profit.

**Syarat penggunaan.** WACC dan ROIC menggunakan basis kapital serta risiko yang konsisten; EVA satu tahun bukan nilai perusahaan.

**Kekeliruan yang perlu dihindari.** Jangan mengurangkan bunga kas sekali lagi setelah biaya modal gabungan telah dibebankan.

**Contoh hitung.** NOPAT 30, modal 200, WACC 10%: EVA 10.

```python
30-200*.1
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-2-15"></a>
## 2-15 — EVA dari spread ROIC

[PDF 120](../Financial_Management_Theory_and_Practice_15e.pdf#page=120)

$$
EVA=K_{op}(ROIC-WACC)
$$

**Variabel.** ROIC−WACC: spread return operasi atas required return.

**Penurunan dan logika.** Substitusikan NOPAT=Kop×ROIC ke 2-14 dan faktorkan Kop. Bentuk ini menjelaskan hubungan volume modal dengan economic profit.

**Syarat penggunaan.** Kop yang dipakai menghitung ROIC harus sama dengan Kop pengali; tidak mencampur modal akhir dengan ROIC rata-rata.

**Kekeliruan yang perlu dihindari.** Pertumbuhan hanya menciptakan EVA tambahan bila return modal tambahan mengungguli cost of capital yang sesuai.

**Contoh hitung.** Modal 200, ROIC 15%, WACC 10%: EVA 10.

```python
200*(.15-.10)
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
