# Bab 9: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../09-chapter.md)

## Navigasi

- [9-1: Nilai operasi dan biaya modal](#rumus-9-1)
- [9-2: WACC empat sumber pendanaan](#rumus-9-2)
- [9-3: Biaya utang setelah pajak sederhana](#rumus-9-3)
- [9-4: After-tax debt cost dengan flotation](#rumus-9-4)
- [9-5: Cost of preferred dengan biaya emisi](#rumus-9-5)
- [9-6: Expected market return dari dividend growth](#rumus-9-6)
- [9-7: Cost of common equity via CAPM](#rumus-9-7)
- [9-8: Estimasi beta](#rumus-9-8)
- [9-9: Harga Gordon untuk cost equity](#rumus-9-9)
- [9-10: Cost equity dividend yield plus growth](#rumus-9-10)
- [9-11: Retention growth model](#rumus-9-11)
- [9-12: Cost of new common equity](#rumus-9-12)
- [9-13: Bond-yield plus judgmental equity premium](#rumus-9-13)

<a id="rumus-9-1"></a>
## 9-1 — Nilai operasi dan biaya modal

[PDF 413](../Financial_Management_Theory_and_Practice_15e.pdf#page=413)

$$
V_{op}=\sum_{t=1}^{\infty}FCF_t/(1+WACC)^t
$$

**Variabel.** WACC: marginal required cost yang konsisten risiko dan policy leverage.

**Penurunan dan logika.** Mengulang 7-1 untuk menegaskan bahwa biaya modal adalah input valuasi, bukan hanya beban bunga akuntansi.

**Syarat penggunaan.** Discount rate dan cash flow harus sesuai; opportunity cost modal dihitungforward.

**Kekeliruan yang perlu dihindari.** Memakai cost of debt saja untuk seluruh perusahaan mengabaikan klaim ekuitas.

**Contoh hitung.** FCF 100konstan, WACC 10% memberi 1000.

```python
100/.1
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-2"></a>
## 9-2 — WACC empat sumber pendanaan

[PDF 414](../Financial_Management_Theory_and_Practice_15e.pdf#page=414) · [PDF 430](../Financial_Management_Theory_and_Practice_15e.pdf#page=430)

$$
WACC=w_dr_d(1-T)+w_{std}r_{std}(1-T)+w_{ps}r_{ps}+w_sr_s
$$

**Variabel.** std: utang pendekberbunga; weights target market values menjumlah 1.

**Penurunan dan logika.** Required return gabungan adalah rata-rata tertimbang marginal cost tiap penyedia dana; debt cost disesuaikan manfaat pajak.

**Syarat penggunaan.** Operating payables sudah masuk NOWC; tax shield efektif dan leverage target sesuai.

**Kekeliruan yang perlu dihindari.** Bookweights/historical coupon tidak otomatis sama dengan bobotpasar/marginalyield.

**Contoh hitung.** Weights 30/10/10/50%, rates 8/6/9/12%, T 25% memberi 9,15%.

```python
.3*.08*.75+.1*.06*.75+.1*.09+.5*.12
```
Hasil presisi mesin: `0.0915`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-3"></a>
## 9-3 — Biaya utang setelah pajak sederhana

[PDF 418](../Financial_Management_Theory_and_Practice_15e.pdf#page=418)

$$
k_{d,after}=r_d(1-T)
$$

**Variabel.** rd: biaya utangmarginal sebelum pajak; T: marginal tax benefit.

**Penurunan dan logika.** Pembayaran bunga rd per unit utang dikurangi penghematan pajakrd T.

**Syarat penggunaan.** Deductibility dan kapasitas memanfaatkan pajak benar-benar tersedia; otherwise modelkan taxarus kas.

**Kekeliruan yang perlu dihindari.** Tidak otomatis berlaku pada seluruh leasing/preferred atau perusahaan yang tidak dapat memakai manfaat pajak.

**Contoh hitung.** rd 8%, T 25% menghasilkan 6%.

```python
.08*(1-.25)
```
Hasil presisi mesin: `0.06`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-4"></a>
## 9-4 — After-tax debt cost dengan flotation

[PDF 420](../Financial_Management_Theory_and_Practice_15e.pdf#page=420)

$$
M(1-F)=\sum_{t=1}^{N}\frac{INT(1-T)}{(1+y)^t}+\frac M{(1+y)^N}
$$

**Variabel.** F: pecahan flotation; y: after-tax financing yield yangdicari.

**Penurunan dan logika.** Bandingkan proceedsneto yangditerima dengan seluruh pembayaran kontraktual setelah manfaat pajak; cariy sebagai IRR pendanaan.

**Syarat penggunaan.** Sumber menulisy sebagai rd(1−T). Untuk flotation material, gunakan definisi yieldarus kasini, bukan sekadar kupon dikali 1−T.

**Kekeliruan yang perlu dihindari.** Jangan membebankan fee dua kali atau mengganti par M dengan proceeds pada pembayaranpokok.

**Contoh hitung.** Par 1000, F 5%, INT 80, T 25%, N 1: proceeds 950, kas 1060, y 11,578947%.

```python
ytm(950,60,1000,1)
```
Hasil presisi mesin: `0.115789473684`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-5"></a>
## 9-5 — Cost of preferred dengan biaya emisi

[PDF 421](../Financial_Management_Theory_and_Practice_15e.pdf#page=421)

$$
r_{ps}=D_{ps}/[P_{ps}(1-F)]
$$

**Variabel.** Dps: dividen tetap; Pps: hargaissuebruto; F: flotation fraction.

**Penurunan dan logika.** Perpetual financing yield adalah pembayaran per periodedibagi kasneto yangditerima perusahaan.

**Syarat penggunaan.** Preferenperpetualfixeddan F<1; preferenbertanggalmaturity memerlukan PVkaslengkap.

**Kekeliruan yang perlu dihindari.** Tidak mengalikan 1−T pada dividenpreferen dalam modelpajakbuku.

**Contoh hitung.** D 8, P 100, F 4% memberi 8,333333%.

```python
8/(100*.96)
```
Hasil presisi mesin: `0.0833333333333`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-6"></a>
## 9-6 — Expected market return dari dividend growth

[PDF 423](../Financial_Management_Theory_and_Practice_15e.pdf#page=423)

$$
\hat r_M=D_{1,M}/P_{0,M}+g_M
$$

**Variabel.** Input adalah dividen, harga, dan pertumbuhan agregatpasar.

**Penurunan dan logika.** Terapkan Gordonexpectedreturn pada aggregate marketportfolio, dengan asumsi distribusi seluruhnya dividen.

**Syarat penggunaan.** Pertumbuhanjangkapanjang konstan; repurchases memerlukan penyesuaian totalpayout dibahas Appendix C.

**Kekeliruan yang perlu dihindari.** Jangan memakai DPS satuperusahaan untuk marketriskpremium.

**Contoh hitung.** Marketdividend 4, harga 100, g 5% memberi 9%.

```python
4/100+.05
```
Hasil presisi mesin: `0.09`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-7"></a>
## 9-7 — Cost of common equity via CAPM

[PDF 425](../Financial_Management_Theory_and_Practice_15e.pdf#page=425)

$$
r_s=r_f+\beta_s RPM
$$

**Variabel.** r_s: opportunitycost retained earnings/common equity.

**Penurunan dan logika.** CAPM 6-15 dipakai sebagai costkomponenekuitas dalam WACC; laba ditahan tetap memiliki biayapeluang.

**Syarat penggunaan.** Beta dan premium sesuai bisnis, leverage, market, horizon.

**Kekeliruan yang perlu dihindari.** Retained earnings bukan modalgratis hanya karena tidak dibayar fee emisi.

**Contoh hitung.** rf 4%, beta 1,2, premium 5% memberi 10%.

```python
.04+1.2*.05
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-8"></a>
## 9-8 — Estimasi beta

[PDF 426](../Financial_Management_Theory_and_Practice_15e.pdf#page=426)

$$
\beta_i=(\sigma_i/\sigma_M)\rho_{iM}
$$

**Variabel.** SD/korelasi diestimasikan pada seri return yangdiselaraskan.

**Penurunan dan logika.** Bentuk 6-8 diulangi sebagai langkah estimasi input CAPM.

**Syarat penggunaan.** Datareturn termasuk pembagian/stocksplit yangdiperlukan; periksasamplingerror danperubahanleverage.

**Kekeliruan yang perlu dihindari.** Beta historis bukan parameter pasti permanen.

**Contoh hitung.** σi 30%,σM 20%,ρ0,8 memberi 1,2.

```python
(.3/.2)*.8
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-9"></a>
## 9-9 — Harga Gordon untuk cost equity

[PDF 427](../Financial_Management_Theory_and_Practice_15e.pdf#page=427)

$$
P_0=D_1/(r_s-g)
$$

**Variabel.** P 0: nilaiintrinsik/hargaequilibrium; D 1: dividenberikut.

**Penurunan dan logika.** Persamaanharga 7-17 dijadikan dasar inversi untuk memperoleh biaya ekuitas.

**Syarat penggunaan.** rs>g, dividen/pertumbuhan/payout stabil.

**Kekeliruan yang perlu dihindari.** Jika harga tidak berada diequilibrium, expected return darihargatersebut tidak otomatis samadenganrequired return.

**Contoh hitung.** D 1=4, rs 10%, g 5% memberi 80.

```python
4/(.10-.05)
```
Hasil presisi mesin: `80`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-10"></a>
## 9-10 — Cost equity dividend yield plus growth

[PDF 428](../Financial_Management_Theory_and_Practice_15e.pdf#page=428)

$$
r_s=D_1/P_0+g
$$

**Variabel.** Expected return disamakan dengan required return bagi marginal investor dalamequilibrium.

**Penurunan dan logika.** Balik 9-9 secaraaljabar.

**Syarat penggunaan.** Asumsi Gordon; g berasal dari basisdividen per saham yangsesuai.

**Kekeliruan yang perlu dihindari.** Menambahkan growthrate penjualan yangtidaksebanding ke dividendyield dapat merusakestimasi.

**Contoh hitung.** D 1=4, P 80, g 5% memberi 10%.

```python
4/80+.05
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-11"></a>
## 9-11 — Retention growth model

[PDF 429](../Financial_Management_Theory_and_Practice_15e.pdf#page=429)

$$
g=ROE\times b
$$

**Variabel.** b: retention ratio=1−payout; ROE: return atas ekuitas yangdireinvestasikan.

**Penurunan dan logika.** Laba yangditahan adalah b×NI; dengan ROE dan kebijakanstabil, tambahanekuitas menghasilkan pertumbuhan laba/dividen sesuaimodel.

**Syarat penggunaan.** Tidakada externalcommonissue, profitability/payout/leverage stabil dan timing ROE didefinisikan. Untuk ROE berbasisekuitasakhir, hubunganpertumbuhan exact dapat memerlukan bROE/(1−bROE).

**Kekeliruan yang perlu dihindari.** Ini modelpertumbuhanberkelanjutan, bukan identitas universalsetiappertumbuhanpenjualan.

**Contoh hitung.** ROE 15% dan retention 40% memberi modelg 6%.

```python
.15*.4
```
Hasil presisi mesin: `0.06`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-12"></a>
## 9-12 — Cost of new common equity

[PDF 433](../Financial_Management_Theory_and_Practice_15e.pdf#page=433)

$$
r_e=D_1/[P_0(1-F)]+g
$$

**Variabel.** F: issueflotationfraction; netproceeds P 0(1−F).

**Penurunan dan logika.** Sesuaikan dividendyield dengan proceedsneto, lalutambahkanpertumbuhandalammodel Gordon.

**Syarat penggunaan.** Fixed flotationfraction, constantgrowth; alternativemodelbiayaemisi sebagai outlay proyek harus diterapkan konsisten.

**Kekeliruan yang perlu dihindari.** Menggunakan reyangsudahdisesuaikanfee sekaligus menambahfee yang sama sebagaioutlay akan doublecount.

**Contoh hitung.** D 1=4, P 100, F 20%, g 5% memberi 10%.

```python
4/(100*.8)+.05
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-9-13"></a>
## 9-13 — Bond-yield plus judgmental equity premium

[PDF 434](../Financial_Management_Theory_and_Practice_15e.pdf#page=434)

$$
r_s=r_d+JRP
$$

**Variabel.** JRP: premiekuitassubjektif atas utangperusahaan itu sendiri.

**Penurunan dan logika.** Karena klaimcommon lebih residual daripada utang, analis menambahkan kompensasirisiko yangdinilai relevan.

**Syarat penggunaan.** Heuristik judgmental, bukan model CAPM yangmenggandakanbeta; JRP perlu justifikasi.

**Kekeliruan yang perlu dihindari.** Jangan menambahkan marketriskpremium secaraotomatis ke bondyield lalu menyebutnya CAPM.

**Contoh hitung.** Ownbondyield 6% danjudgmentalpremium 4% memberi 10%.

```python
.06+.04
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
