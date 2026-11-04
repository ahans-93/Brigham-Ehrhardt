# Bab 3: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../03-chapter.md)

## Navigasi

- [3-1: Equity multiplier](#rumus-3-1)
- [3-2: Extended DuPont](#rumus-3-2)
- [3-3: DuPont dua faktor](#rumus-3-3)
- [U-3-01: Current ratio](#rumus-u-3-01)
- [U-3-02: Quick ratio](#rumus-u-3-02)
- [U-3-03: Perputaran aset tetap](#rumus-u-3-03)
- [U-3-04: Total asset turnover](#rumus-u-3-04)
- [U-3-05: Inventory turnover](#rumus-u-3-05)
- [U-3-06: Debt-to-assets dan liabilities-to-assets](#rumus-u-3-06)
- [U-3-07: Debt/equity dan market debt ratio](#rumus-u-3-07)
- [U-3-08: Times-interest-earned](#rumus-u-3-08)
- [U-3-09: EBITDA coverage versi buku](#rumus-u-3-09)
- [U-3-10: Margin laba](#rumus-u-3-10)
- [U-3-11: BEP, ROA, ROE](#rumus-u-3-11)
- [U-3-12: EPS dan price/earnings](#rumus-u-3-12)
- [U-3-13: Price/cash-flow](#rumus-u-3-13)
- [U-3-14: Book value per share dan market/book](#rumus-u-3-14)

<a id="rumus-3-1"></a>
## 3-1 — Equity multiplier

[PDF 160](../Financial_Management_Theory_and_Practice_15e.pdf#page=160)

$$
EM=A/E
$$

**Variabel.** A: total assets; E: common equity pada basis yang sama.

**Penurunan dan logika.** Identitas leverage neraca membagi sumber daya perusahaan dengan modal common. Dengan A=L+E, EM=1+L/E bila tidak ada klaim lain yang dipisahkan.

**Syarat penggunaan.** E bukan nol; basis rata-rata/akhir konsisten dengan ROA dan ROE yang direkonsiliasi.

**Kekeliruan yang perlu dihindari.** E negatif membuat interpretasi leverage tradisional tidak dapat dipakai seperti perusahaan berekuitas positif.

**Contoh hitung.** Aset 300 dan common equity 100: EM 3.

```python
300/100
```
Hasil presisi mesin: `3`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-3-2"></a>
## 3-2 — Extended DuPont

[PDF 160](../Financial_Management_Theory_and_Practice_15e.pdf#page=160)

$$
ROE=(NI/Sales)(Sales/A)(A/E)
$$

**Variabel.** NI: laba common; Sales: penjualan; A: aset; E: common equity.

**Penurunan dan logika.** Mulai dari NI/E, kalikan Sales/Sales dan A/A. Faktor tengah saling hapus, menghasilkan margin×turnover×leverage.

**Syarat penggunaan.** Semua basis akuntansi, periode dan denominator harus konsisten; Sales, A, E tidak nol.

**Kekeliruan yang perlu dihindari.** Menaikkan EM tidak menjamin ROE naik karena bunga dapat menurunkan NI dan leverage meningkatkan risiko.

**Contoh hitung.** NI 30, Sales 600, A 300, E 100: ROE 30%.

```python
(30/600)*(600/300)*(300/100)
```
Hasil presisi mesin: `0.3`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-3-3"></a>
## 3-3 — DuPont dua faktor

[PDF 160](../Financial_Management_Theory_and_Practice_15e.pdf#page=160)

$$
ROE=ROA\times EM
$$

**Variabel.** ROA=NI/A; EM=A/E.

**Penurunan dan logika.** Kalikan NI/A dengan A/E; A saling hapus. Bentuk ini memisahkan profitabilitas aset dan leverage.

**Syarat penggunaan.** ROA harus berbasis NI yang sama dengan numerator ROE, bukan EBIT atau NOPAT.

**Kekeliruan yang perlu dihindari.** Menggunakan ROIC sebagai pengganti ROA membuat identitas ini tidak lagi berlaku tanpa penyesuaian pendanaan.

**Contoh hitung.** ROA 10% dan EM 3: ROE 30%.

```python
.10*3
```
Hasil presisi mesin: `0.3`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-01"></a>
## U-3-01 — Current ratio

[PDF 141](../Financial_Management_Theory_and_Practice_15e.pdf#page=141)

$$
CR_{liq}=CA/CL
$$

**Variabel.** CA: aset lancar; CL: liabilitas lancar, termasuk utang berbunga yang jatuh tempo.

**Penurunan dan logika.** Bandingkan aset yang diklasifikasikan lancar dengan kewajiban lancar dalam unit mata uang sama.

**Syarat penggunaan.** CL positif; klasifikasi periode konsisten.

**Kekeliruan yang perlu dihindari.** Rasio tinggi belum membuktikan persediaan mudah dijual atau piutang tertagih.

**Contoh hitung.** CA 200, CL 100: 2 kali.

```python
200/100
```
Hasil presisi mesin: `2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-02"></a>
## U-3-02 — Quick ratio

[PDF 142](../Financial_Management_Theory_and_Practice_15e.pdf#page=142)

$$
QR=(CA-Inventory)/CL
$$

**Variabel.** QR: proksi likuiditas yang mengeluarkan persediaan dari pembilang.

**Penurunan dan logika.** Kurangi komponen aset lancar yang biasanya perlu dijual sebelum menghasilkan kas.

**Syarat penggunaan.** Definisi sumber ini dipertahankan; pengeluaran prepaid dalam varian lain harus dinyatakan.

**Kekeliruan yang perlu dihindari.** Jangan menyamakan quick ratio dengan cash ratio.

**Contoh hitung.** CA 200, persediaan 80, CL 100: 1,2 kali.

```python
(200-80)/100
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-03"></a>
## U-3-03 — Perputaran aset tetap

[PDF 143](../Financial_Management_Theory_and_Practice_15e.pdf#page=143)

$$
FAT=Sales/NetFixedAssets
$$

**Variabel.** Sales: pendapatan periode; aset tetap neto sesudah depresiasi.

**Penurunan dan logika.** Ukur rupiah penjualan per rupiah nilai buku aset produktif.

**Syarat penggunaan.** Saldo rata-rata lebih informatif jika aset berubah material.

**Kekeliruan yang perlu dihindari.** Aset tua dengan nilai buku kecil bisa membuat rasio tinggi tanpa efisiensi ekonomi lebih baik.

**Contoh hitung.** Sales 500, NFA 250: 2 kali.

```python
500/250
```
Hasil presisi mesin: `2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-04"></a>
## U-3-04 — Total asset turnover

[PDF 143](../Financial_Management_Theory_and_Practice_15e.pdf#page=143)

$$
TAT=Sales/Assets
$$

**Variabel.** Assets: total aset pada basis saldo yang dinyatakan.

**Penurunan dan logika.** Membagi aliran penjualan dengan stok aset mengukur intensitas penggunaan aset.

**Syarat penggunaan.** Jangan mencampur saldo rata-rata pada satu perusahaan dengan saldo akhir pada pembanding.

**Kekeliruan yang perlu dihindari.** TAT bukan margin; penjualan tinggi belum tentu menghasilkan laba.

**Contoh hitung.** Sales 500, A 400: 1,25 kali.

```python
500/400
```
Hasil presisi mesin: `1.25`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-05"></a>
## U-3-05 — Inventory turnover

[PDF 145](../Financial_Management_Theory_and_Practice_15e.pdf#page=145)

$$
IT=COGS/Inventory
$$

**Variabel.** COGS: HPP termasuk depresiasi produksi; Inventory: persediaan pada biaya.

**Penurunan dan logika.** Stok biaya persediaan dibandingkan aliran biaya tahunan; periode hari=365/IT.

**Syarat penggunaan.** Saldo awal/akhir atau rata-rata mengikuti konteks; depresiasi produksi jangan dikeluarkan dua kali.

**Kekeliruan yang perlu dihindari.** Sumber membedakan COGS dari biaya operasi tanpa depresiasi; memakai sales mengubah rasio.

**Contoh hitung.** COGS 4000, Inventory 1000: 4 kali.

```python
4000/1000
```
Hasil presisi mesin: `4`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-06"></a>
## U-3-06 — Debt-to-assets dan liabilities-to-assets

[PDF 146](../Financial_Management_Theory_and_Practice_15e.pdf#page=146) · [PDF 147](../Financial_Management_Theory_and_Practice_15e.pdf#page=147)

$$
DA=D/A,\qquad LA=L/A
$$

**Variabel.** D: utang berbunga; L: seluruh liabilitas; A: total aset.

**Penurunan dan logika.** Pisahkan klaim pembiayaan berbunga dari kewajiban operasi. D biasanya lebih kecil dari L.

**Syarat penggunaan.** Definisi debt harus dinyatakan; gunakan basis buku untuk rasio neraca ini.

**Kekeliruan yang perlu dihindari.** Utang pemasok masuk liabilitas tetapi tidak otomatis masuk interest-bearing debt.

**Contoh hitung.** D 150, L 240, A 400: debt/assets 37,5%; liabilities/assets 60%.

```python
150/400
```
Hasil presisi mesin: `0.375`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-07"></a>
## U-3-07 — Debt/equity dan market debt ratio

[PDF 147](../Financial_Management_Theory_and_Practice_15e.pdf#page=147)

$$
DE=D/E,\qquad MDR=D/(D+E_{market})
$$

**Variabel.** E buku atau pasar harus ditentukan; MDR memakai nilai pasar ekuitas.

**Penurunan dan logika.** DE membandingkan dua klaim; MDR membagi utang dengan total modal investor pada basis yang dipilih.

**Syarat penggunaan.** Debt market value ideal untuk valuasi; sumber dapat memakai book debt sebagai proksi.

**Kekeliruan yang perlu dihindari.** Book equity dalam DE dan market equity dalam MDR tidak dapat dipertukarkan tanpa penjelasan.

**Contoh hitung.** D 150, Epasar 450: MDR 25%, market DE 1/3.

```python
150/(150+450)
```
Hasil presisi mesin: `0.25`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-08"></a>
## U-3-08 — Times-interest-earned

[PDF 148](../Financial_Management_Theory_and_Practice_15e.pdf#page=148)

$$
TIE=EBIT/I
$$

**Variabel.** I: beban bunga periode; EBIT sebelum bunga dan pajak.

**Penurunan dan logika.** Ukur berapa kali laba sebelum bunga dapat menutup biaya bunga.

**Syarat penggunaan.** Bunga positif; definisi EBIT konsisten.

**Kekeliruan yang perlu dihindari.** TIE tidak mencakup kebutuhan pembayaran pokok, capex, atau perubahan modal kerja.

**Contoh hitung.** EBIT 500, I 120: TIE 4,166667.

```python
500/120
```
Hasil presisi mesin: `4.16666666667`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-09"></a>
## U-3-09 — EBITDA coverage versi buku

[PDF 149](../Financial_Management_Theory_and_Practice_15e.pdf#page=149)

$$
Coverage=\frac{EBITDA+Lease}{I+Principal+Lease}
$$

**Variabel.** Lease: pembayaran sewa yang sudah mengurangi EBIT dalam contoh; Principal: pokok utang jatuh tempo.

**Penurunan dan logika.** Tambahkan kembali beban sewa ke kapasitas kas sebelum pembayaran, lalu bandingkan dengan seluruh pembayaran tetap yang dimasukkan model.

**Syarat penggunaan.** Definisi mengikuti akuntansi contoh historis sumber; rekonsiliasi jika penyajian sewa berbeda.

**Kekeliruan yang perlu dihindari.** Ini bukan DSCR universal dan EBITDA bukan kas tersedia persis setelah pajak/modal kerja.

**Contoh hitung.** EBITDA 700, lease 28, I 120, pokok 20: coverage 4,333333.

```python
(700+28)/(120+20+28)
```
Hasil presisi mesin: `4.33333333333`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-10"></a>
## U-3-10 — Margin laba

[PDF 150](../Financial_Management_Theory_and_Practice_15e.pdf#page=150) · [PDF 151](../Financial_Management_Theory_and_Practice_15e.pdf#page=151)

$$
GM=(Sales-COGS)/Sales,\quad OM=EBIT/Sales,\quad NM=NI_{common}/Sales
$$

**Variabel.** GM: margin kotor; OM: margin operasi sebelum pajak; NM: margin bersih common.

**Penurunan dan logika.** Tiga tingkat laba dibagi penjualan menunjukkan biaya yang diserap pada tiap lapisan laporan laba rugi.

**Syarat penggunaan.** Klasifikasi HPP, biaya operasi, dan hak preferen konsisten.

**Kekeliruan yang perlu dihindari.** OM=EBIT/Sales berbeda dari OP=NOPAT/Sales pada 2-11.

**Contoh hitung.** Sales 500, COGS 300, EBIT 100, NI 60: margin 40%,20%,12%.

```python
(500-300)/500
```
Hasil presisi mesin: `0.4`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-11"></a>
## U-3-11 — BEP, ROA, ROE

[PDF 151](../Financial_Management_Theory_and_Practice_15e.pdf#page=151) · [PDF 152](../Financial_Management_Theory_and_Practice_15e.pdf#page=152) · [PDF 153](../Financial_Management_Theory_and_Practice_15e.pdf#page=153)

$$
BEP=EBIT/A,\quad ROA=NI_{common}/A,\quad ROE=NI_{common}/E_{common}
$$

**Variabel.** BEP: basic earning power; ROA dan ROE memakai laba setelah bunga/pajak sesuai definisi common.

**Penurunan dan logika.** Ubah pembilang dan basis klaim agar masing-masing mengukur hasil aset sebelum pendanaan, aset sesudah pendanaan, dan ekuitas.

**Syarat penggunaan.** Gunakan basis saldo yang sama untuk pembandingan dan DuPont.

**Kekeliruan yang perlu dihindari.** ROA bukan ROIC: total aset dan total modal operasi neto adalah dua penyebut berbeda.

**Contoh hitung.** EBIT 100, NI 60, A 400, E 200: BEP 25%, ROA 15%, ROE 30%.

```python
60/200
```
Hasil presisi mesin: `0.3`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-12"></a>
## U-3-12 — EPS dan price/earnings

[PDF 154](../Financial_Management_Theory_and_Practice_15e.pdf#page=154)

$$
EPS=NI_{common}/n,\quad PE=P/EPS
$$

**Variabel.** n: saham rata-rata tertimbang untuk EPS; P: harga saham.

**Penurunan dan logika.** Alokasikan laba common per saham, kemudian bandingkan harga dengan laba per saham.

**Syarat penggunaan.** Basic/diluted serta trailing/forward EPS harus dipilih dan dilabeli.

**Kekeliruan yang perlu dihindari.** EPS nol/negatif membuat PE tidak bermakna untuk pengurutan biasa.

**Contoh hitung.** NI 220, n 50: EPS 4,4; P 27 memberi PE 6,136364.

```python
27/(220/50)
```
Hasil presisi mesin: `6.13636363636`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-13"></a>
## U-3-13 — Price/cash-flow

[PDF 154](../Financial_Management_Theory_and_Practice_15e.pdf#page=154) · [PDF 155](../Financial_Management_Theory_and_Practice_15e.pdf#page=155)

$$
CFPS=(NI+D\&A)/n,\quad PCF=P/CFPS
$$

**Variabel.** CFPS memakai definisi cash earnings sederhana sumber, bukan CFOper saham.

**Penurunan dan logika.** Tambahkan biaya nonkas utama ke laba lalu alokasikan per saham; bandingkan harga.

**Syarat penggunaan.** Komponen nonkas lain, modal kerja, dancapex belum direkonsiliasi.

**Kekeliruan yang perlu dihindari.** Rasio ini tidak sama denganprice/FCF.

**Contoh hitung.** NI 60, D&A 20, n 10, P 40: CFPS 8, PCF 5.

```python
40/((60+20)/10)
```
Hasil presisi mesin: `5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-3-14"></a>
## U-3-14 — Book value per share dan market/book

[PDF 155](../Financial_Management_Theory_and_Practice_15e.pdf#page=155)

$$
BVPS=E_{book}/n,\quad MB=P/BVPS
$$

**Variabel.** Ebook: common equity buku, bukan total termasuk preferred.

**Penurunan dan logika.** Bagi nilai buku common dengan saham, lalu bandingkan dengan harga pasar.

**Syarat penggunaan.** Jumlah saham pada tanggal neraca sesuai nilai buku; tangani treasury shares.

**Kekeliruan yang perlu dihindari.** Ekuitas negatif membuat M/B sulit diinterpretasikan sebagai multiple normal.

**Contoh hitung.** E 200, n 10, P 30: BVPS 20, M/B 1,5.

```python
30/(200/10)
```
Hasil presisi mesin: `1.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
