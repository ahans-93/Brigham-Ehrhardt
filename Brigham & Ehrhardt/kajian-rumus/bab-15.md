# Bab 15: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../15-chapter.md)

## Navigasi

- [15-1: Valuasi operasi dan struktur modal](#rumus-15-1)
- [15-2: WACC debt dan common equity](#rumus-15-2)
- [15-3: Operating break-even condition](#rumus-15-3)
- [15-4: Kuantitas break-even](#rumus-15-4)
- [15-5: MM proposition I tanpa pajak](#rumus-15-5)
- [15-6: MM cost equity tanpa pajak](#rumus-15-6)
- [15-7: Nilai levered sebagai nilai dasar plus efek samping](#rumus-15-7)
- [15-8: MM corporate tax value](#rumus-15-8)
- [15-9: MM cost equity dengan corporate tax](#rumus-15-9)
- [15-10: Miller corporate dan personal taxes](#rumus-15-10)
- [15-10a: Substitusi pajak pada Miller](#rumus-15-10a)
- [15-11: Hamada levered beta](#rumus-15-11)
- [15-11a: Hamada dalam bobot struktur modal](#rumus-15-11a)
- [15-12: Unlevering beta](#rumus-15-12)
- [15-13: Saham repurchase dari penerbitan utang](#rumus-15-13)
- [15-14: Saham setelah recapitalization](#rumus-15-14)
- [15-15: Equity pasca-repurchase dari target weight](#rumus-15-15)
- [15-16: Saham tersisa dari value bridge recap](#rumus-15-16)
- [15-17: Harga pasca-repurchase recap](#rumus-15-17)
- [15-18: Equity risky-debt sebagai call atas aset](#rumus-15-18)
- [15-19: d 1 dan d 2 untuk equity-as-option](#rumus-15-19)
- [15-20: Yield zero-coupon risky debt](#rumus-15-20)

<a id="rumus-15-1"></a>
## 15-1 — Valuasi operasi dan struktur modal

[PDF 645](../Financial_Management_Theory_and_Practice_15e.pdf#page=645)

$$
V_{op}=\sum_{t=1}^{\infty}FCF_t/(1+WACC)^t
$$

**Variabel.** FCF operasi dan WACC seperti 7-1.

**Penurunan dan logika.** Struktur modal dapat memengaruhi nilai melalui discount rate dan efek pendanaan; nilai tidak ditentukan oleh EPS saja.

**Syarat penggunaan.** Cash flow dan risk model harus konsisten ketika leverage diubah.

**Kekeliruan yang perlu dihindari.** Tidak boleh menurunkan WACC lewat bobot debt sambil mempertahankan cost of equity seolah leverage tidak meningkat.

**Contoh hitung.** FCF 100 konstan, WACC 10% memberi 1000.

```python
100/.1
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-2"></a>
## 15-2 — WACC debt dan common equity

[PDF 646](../Financial_Management_Theory_and_Practice_15e.pdf#page=646)

$$
WACC=w_Dr_D(1-T)+w_Er_E
$$

**Variabel.** wD+wE=1; model tidak memiliki preferred stock.

**Penurunan dan logika.** Bentuk dua komponen dari 9-2; cost of equity dapat naik akibat financial risk.

**Syarat penggunaan.** Bobot market/target dan manfaat pajak yang efektif sesuai asumsi.

**Kekeliruan yang perlu dihindari.** Perubahan WACC harus dihitung bersamaan dengan perubahan biaya tiap komponen.

**Contoh hitung.** wD 40%, rd 8%, T 25%, wE 60%, re 12% menghasilkan 9,6%.

```python
.4*.08*.75+.6*.12
```
Hasil presisi mesin: `0.096`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-3"></a>
## 15-3 — Operating break-even condition

[PDF 647](../Financial_Management_Theory_and_Practice_15e.pdf#page=647)

$$
EBIT=PQ-vQ-F=0
$$

**Variabel.** P: harga per unit; v: biaya variabel per unit; F: fixed operating costs.

**Penurunan dan logika.** Penjualan dikurangi biaya variabel dan fixed cost memberi EBIT. Break-even menetapkan EBIT nol.

**Syarat penggunaan.** Harga/unit cost tetap pada rentang relevan; model single product atau product mix stabil.

**Kekeliruan yang perlu dihindari.** Operating break-even bukan financial break-even setelah bunga dan pajak.

**Contoh hitung.** P 10, v 6, Q 25, F 100 menghasilkan EBIT 0.

```python
10*25-6*25-100
```
Hasil presisi mesin: `0`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-4"></a>
## 15-4 — Kuantitas break-even

[PDF 648](../Financial_Management_Theory_and_Practice_15e.pdf#page=648)

$$
Q_{BE}=F/(P-v)
$$

**Variabel.** P−v: contribution margin per unit.

**Penurunan dan logika.** Susun ulang (P−v)Q=F dari 15-3.

**Syarat penggunaan.** P>v dan fixed cost terukur; bila P≤v tidak ada finite positive break-even dengan Fpositif.

**Kekeliruan yang perlu dihindari.** Jangan membagi F dengan persentase margin jika yang dicari jumlah unit.

**Contoh hitung.** F 100, P 10, v 6 memberi 25 unit.

```python
100/(10-6)
```
Hasil presisi mesin: `25`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-5"></a>
## 15-5 — MM proposition I tanpa pajak

[PDF 652](../Financial_Management_Theory_and_Practice_15e.pdf#page=652)

$$
V_L=V_U=E_L+D
$$

**Variabel.** L/U: levered/unlevered; E: nilai ekuitas; D: nilai utang.

**Penurunan dan logika.** Replikasi/homemade leverage memberi payoff operasi yang sama dari kombinasi klaim; no-arbitrage menyamakan total nilai.

**Syarat penggunaan.** Pasar ideal tanpa pajak, biaya distress/transaksi, dan perbedaan akses pendanaan yang relevan.

**Kekeliruan yang perlu dihindari.** Irrelevance hasil model bukan bukti bahwa struktur modal nyata selalu tidak penting.

**Contoh hitung.** Equity 700+debt 300 merekonsiliasi value 1000.

```python
700+300
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-6"></a>
## 15-6 — MM cost equity tanpa pajak

[PDF 652](../Financial_Management_Theory_and_Practice_15e.pdf#page=652)

$$
r_{EL}=r_U+(r_U-r_D)D/E
$$

**Variabel.** rU: biaya modal/equity bisnis tanpa leverage.

**Penurunan dan logika.** Gunakan rU=(E/V)rEL+(D/V)rD dari WACC konstan dan selesaikan rEL.

**Syarat penggunaan.** Asumsi MM tanpa pajak; D/E memakai nilai pasar.

**Kekeliruan yang perlu dihindari.** Cost equity naik dengan leverage; bobot debt murah tidak membuat modal gabungan gratis.

**Contoh hitung.** rU 10%, rd 6%, D/E 0,5 memberi rEL 12%.

```python
.10+(.10-.06)*.5
```
Hasil presisi mesin: `0.12`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-7"></a>
## 15-7 — Nilai levered sebagai nilai dasar plus efek samping

[PDF 653](../Financial_Management_Theory_and_Practice_15e.pdf#page=653)

$$
V_L=V_U+PV(FinancingSideEffects)
$$

**Variabel.** Dalam model MM pajak sumber, side effect utama adalah interest tax shield.

**Penurunan dan logika.** Pisahkan operasi tanpa leverage dari nilai sekarang pengaruh pendanaan. Efek negatif dapat ditulis sebagai pengurang dalam APV yang lebih umum.

**Syarat penggunaan.** Masing-masing komponen memakai discount rate sesuai risikonya.

**Kekeliruan yang perlu dihindari.** Jangan menambahkan tax shield jika sudah sepenuhnya dicakup WACC pada nilai dasar levered yang dipakai.

**Contoh hitung.** VU 1000 dan PVtax shield 50 menghasilkan 1050.

```python
1000+50
```
Hasil presisi mesin: `1050`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-8"></a>
## 15-8 — MM corporate tax value

[PDF 653](../Financial_Management_Theory_and_Practice_15e.pdf#page=653)

$$
V_L=V_U+TD
$$

**Variabel.** T: corporate tax rate; D: utang permanen dalam model.

**Penurunan dan logika.** Tax shield tahunan TrDD didiskontokan pada rD sebagai perpetuitas, sehingga PV=TD.

**Syarat penggunaan.** Utang tetap permanen, manfaat pajak tersedia, risiko shield mengikuti asumsi sumber; tanpa distress/personal tax.

**Kekeliruan yang perlu dihindari.** Untuk utang berubah atau tax loss, TD tidak otomatis benar.

**Contoh hitung.** VU 1000, T 25%, D 200 menghasilkan 1050.

```python
1000+.25*200
```
Hasil presisi mesin: `1050`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-9"></a>
## 15-9 — MM cost equity dengan corporate tax

[PDF 654](../Financial_Management_Theory_and_Practice_15e.pdf#page=654)

$$
r_{EL}=r_U+(r_U-r_D)(1-T)D/E
$$

**Variabel.** rEL: cost of equity levered dalam model MM pajak.

**Penurunan dan logika.** Manfaat pajak mengurangi kenaikan financial risk premium pada hubungan model, menghasilkan faktor 1−T dibanding 15-6.

**Syarat penggunaan.** Asumsi kebijakan utang/risiko tax shield MM; jangan digabung sembarang dengan compressed APV.

**Kekeliruan yang perlu dihindari.** Hubungan tanpa faktor 1−T di Bab 21 memakai kerangka berbeda, bukan otomatis kontradiksi.

**Contoh hitung.** rU 10%, rd 6%, T 25%, D/E 0,5 memberi 11,5%.

```python
.10+(.10-.06)*.75*.5
```
Hasil presisi mesin: `0.115`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-10"></a>
## 15-10 — Miller corporate dan personal taxes

[PDF 654](../Financial_Management_Theory_and_Practice_15e.pdf#page=654)

$$
V_L=V_U+\left[1-\frac{(1-T_c)(1-T_s)}{1-T_d}\right]D
$$

**Variabel.** Tc: pajak perusahaan; Ts: pajak personal equityincome; Td: pajak personal debtincome.

**Penurunan dan logika.** Bandingkan nilai setelah pajak dari kas yang disalurkan lewat utang versus ekuitas; personal tax dapat mengurangi keuntungan corporate debt shield.

**Syarat penggunaan.** Kerangka Miller dengan tax rates marginal dan asumsi equilibrium model; 1−Td>0.

**Kekeliruan yang perlu dihindari.** Rate historis contoh bukan tarif Indonesia. Jika bracket tax advantage nol, debt tidak menambah nilai lewat kanal pajak ini.

**Contoh hitung.** VU 1000, Tc 30%, Ts 20%, Td 25%, D 100 memberi 1025,333333.

```python
1000+(1-(1-.3)*(1-.2)/(1-.25))*100
```
Hasil presisi mesin: `1025.33333333`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-10a"></a>
## 15-10a — Substitusi pajak pada Miller

[PDF 655](../Financial_Management_Theory_and_Practice_15e.pdf#page=655)

$$
V_L=V_U+\left[1-\frac{(1-.40)(1-.12)}{1-.30}\right]D
$$

**Variabel.** Tc 40%, Ts 12%, Td 30% adalah asumsi historis contoh sumber.

**Penurunan dan logika.** Masukkan angka ke 15-10. Koefisien exact adalah 0,2457142857; sumber membulatkannya menjadi sekitar 0,25.

**Syarat penggunaan.** Ini ilustrasi model, bukan tarif pajak berlaku sekarang.

**Kekeliruan yang perlu dihindari.** Jangan menyebut tambahan 0,25D sebagai exact untuk tiga tarif yang diberikan.

**Contoh hitung.** Koefisien tax advantage dari angka sumber adalah 24,571429%.

```python
1-(1-.4)*(1-.12)/(1-.3)
```
Hasil presisi mesin: `0.245714285714`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-11"></a>
## 15-11 — Hamada levered beta

[PDF 668](../Financial_Management_Theory_and_Practice_15e.pdf#page=668)

$$
\beta_L=\beta_U[1+(1-T)D/E]
$$

**Variabel.** βU: operating/business beta tanpa leverage; βL: beta ekuitas levered.

**Penurunan dan logika.** Hubungkan premium CAPM dengan hubungan MM corporate-tax dan anggap debt beta nol sesuai bentuk sederhana.

**Syarat penggunaan.** Asumsi Hamada, debt risk dan risiko shield sesuai; D/E market values.

**Kekeliruan yang perlu dihindari.** Menggunakan formula pada risky debt tanpa meninjau beta utang dapat salah.

**Contoh hitung.** βU 0,8, T 25%, D/E 0,5 menghasilkanβL 1,1.

```python
.8*(1+.75*.5)
```
Hasil presisi mesin: `1.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-11a"></a>
## 15-11a — Hamada dalam bobot struktur modal

[PDF 668](../Financial_Management_Theory_and_Practice_15e.pdf#page=668)

$$
\beta_L=\beta_U[1+(1-T)w_D/w_E]
$$

**Variabel.** wD/wE sama dengan D/E bila kedua bobot memakai total nilai yang sama.

**Penurunan dan logika.** Substitusikan D=wDV dan E=wEV ke 15-11 sehingga V saling hapus.

**Syarat penggunaan.** Asumsi 15-11; wE bukan nol.

**Kekeliruan yang perlu dihindari.** Nomor bersufiks a ini adalah bentuk tersendiri di PDF dan tidak boleh hilang dari inventaris.

**Contoh hitung.** βU 0,8, T 25%, wD 1/3, wE 2/3 menghasilkan 1,1.

```python
.8*(1+.75*((1/3)/(2/3)))
```
Hasil presisi mesin: `1.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-12"></a>
## 15-12 — Unlevering beta

[PDF 668](../Financial_Management_Theory_and_Practice_15e.pdf#page=668)

$$
\beta_U=\beta_L/[1+(1-T)D/E]
$$

**Variabel.** Bentuk sumber memakai wD/wE yang ekuivalen.

**Penurunan dan logika.** Bagi kedua sisi 15-11 dengan faktor leverage; diperoleh beta risiko bisnis tanpa financial leverage model.

**Syarat penggunaan.** Basis tax dan leverage harus sama dengan yang membentuk βL.

**Kekeliruan yang perlu dihindari.** Unlever lalu relever memakai struktur target berbeda harus dilakukan berurutan, bukan langsung menyamakan beta peer dengan beta proyek.

**Contoh hitung.** βL 1,1, T 25%, D/E 0,5 memberiβU 0,8.

```python
1.1/(1+.75*.5)
```
Hasil presisi mesin: `0.8`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-13"></a>
## 15-13 — Saham repurchase dari penerbitan utang

[PDF 673](../Financial_Management_Theory_and_Practice_15e.pdf#page=673)

$$
n_{rep}=(D_{new}-D_{old})/P_{rep}
$$

**Variabel.** Seluruh tambahan debt dipakai membeli saham dalam model recapitalization.

**Penurunan dan logika.** Kas hasil net debt issue dibagi harga pembelian per saham.

**Syarat penggunaan.** Tidak ada fee/penggunaan kas lain; harga sesaat sebelum pembelian sudah mencerminkan informasi perubahan nilai.

**Kekeliruan yang perlu dihindari.** Pprior pada sumber bukan harga lama sebelum pengumuman recap.

**Contoh hitung.** Debt naik 100ke 300, harga 20: repurchase 10 saham.

```python
(300-100)/20
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-14"></a>
## 15-14 — Saham setelah recapitalization

[PDF 673](../Financial_Management_Theory_and_Practice_15e.pdf#page=673)

$$
n_{post}=n_{prior}-(D_{new}-D_{old})/P_{rep}
$$

**Variabel.** nprior: jumlah saham sebelum transaksi repurchase.

**Penurunan dan logika.** Kurangi jumlah saham yang dibeli pada 15-13 dari jumlah awal.

**Syarat penggunaan.** Asumsi transaksi 15-13; tidak ada issue common bersamaan.

**Kekeliruan yang perlu dihindari.** Jangan hanya mengurangi equity value tanpa menyesuaikan share count.

**Contoh hitung.** nprior 100, tambahan debt 200, harga 20 menghasilkan 90 saham.

```python
100-(300-100)/20
```
Hasil presisi mesin: `90`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-15"></a>
## 15-15 — Equity pasca-repurchase dari target weight

[PDF 674](../Financial_Management_Theory_and_Practice_15e.pdf#page=674)

$$
E_{post}=V_{op,new}(1-w_D)
$$

**Variabel.** Model tanpa aset nonoperasi dan preferred stock setelah transaksi.

**Penurunan dan logika.** Debt mengambil porsi wD dari value operasi; sisanya merupakan common equity.

**Syarat penggunaan.** wD=Dnew/VopNew; seluruh kas recap telah dipakai.

**Kekeliruan yang perlu dihindari.** Jika masih ada excess cash atau preferred, bridge sederhana ini harus diperluas.

**Contoh hitung.** Vop 2100, wD 300/2100 menghasilkan equity 1800.

```python
2100*(1-300/2100)
```
Hasil presisi mesin: `1800`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-16"></a>
## 15-16 — Saham tersisa dari value bridge recap

[PDF 674](../Financial_Management_Theory_and_Practice_15e.pdf#page=674)

$$
n_{post}=n_{prior}\frac{V_{op,new}-D_{new}}{V_{op,new}-D_{old}}
$$

**Variabel.** VopNew: nilai operasi setelah efek struktur modal diakui.

**Penurunan dan logika.** Harga fair sebelum repurchase adalah (VopNew−Dold)/nprior; substitusi ke 15-14 menghasilkan rasio ini.

**Syarat penggunaan.** Tidak ada aset nonoperasi, klaim lain atau fee; repurchase fair.

**Kekeliruan yang perlu dihindari.** Menempatkan VopOld pada denominator mengabaikan perubahan nilai yang sudah diketahui saat repurchase.

**Contoh hitung.** n 100, Vnew 2100, Dnew 300, Dold 100 menghasilkan 90.

```python
100*(2100-300)/(2100-100)
```
Hasil presisi mesin: `90`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-17"></a>
## 15-17 — Harga pasca-repurchase recap

[PDF 674](../Financial_Management_Theory_and_Practice_15e.pdf#page=674)

$$
P_{post}=(V_{op,new}-D_{old})/n_{prior}
$$

**Variabel.** Dold, bukan Dnew, muncul karena nprior masih share count sebelum repurchase.

**Penurunan dan logika.** Bagi equitypost=VopNew−Dnew dengan npost 15-16; faktor VopNew−Dnew saling hapus.

**Syarat penggunaan.** Harga sebelum dan sesudah pelaksanaan sama dalam model fair setelah informasi nilai baru diakui.

**Kekeliruan yang perlu dihindari.** Ini tidak menyatakan harga tidak berubah pada tanggal pengumuman.

**Contoh hitung.** Vnew 2100, Dold 100, nprior 100 memberi harga 20.

```python
(2100-100)/100
```
Hasil presisi mesin: `20`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-18"></a>
## 15-18 — Equity risky-debt sebagai call atas aset

[PDF 677](../Financial_Management_Theory_and_Practice_15e.pdf#page=677)

$$
E=C(V_A,F,r_f,T,\sigma_A)
$$

**Variabel.** VA: nilai aset perusahaan; F: face debt tunggal pada maturity; σA: volatility aset.

**Penurunan dan logika.** Pada maturity, common equity menerima max(VA−F,0), sama dengan payoff call. Model opsi dapat menilai klaim residual tersebut.

**Syarat penggunaan.** Model Merton sederhana: zero-coupon debt tunggal, limited liability, struktur pembayaran/aset dan asumsi opsi konsisten.

**Kekeliruan yang perlu dihindari.** Volatilitas saham bukan otomatis volatilitas aset; debt value diperoleh VA−E.

**Contoh hitung.** VA=F 100, r 5%, T 1,σA 20% memberi equity 10,45058357.

```python
bs_call(100,100,.05,1,.2)
```
Hasil presisi mesin: `10.4505835722`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-19"></a>
## 15-19 — d 1 dan d 2 untuk equity-as-option

[PDF 677](../Financial_Management_Theory_and_Practice_15e.pdf#page=677)

$$
d_1=[\ln(V_A/F)+(r_f+\sigma_A^2/2)T]/(\sigma_A\sqrt T),\ d_2=d_1-\sigma_A\sqrt T
$$

**Variabel.** Input opsi sekarang adalah aset dan face debt, bukan harga common stock dan strike exchange option.

**Penurunan dan logika.** Substitusi VA, F,σA ke parameter Black–Scholes 8-10/8-11.

**Syarat penggunaan.** T>0,σA>0, VA, F>0; tidak mengganti model debt dengan risiko berbeda tanpa penyesuaian.

**Kekeliruan yang perlu dihindari.** Face debt F pada maturity berbeda dari market debt value hari ini.

**Contoh hitung.** VA=F 100, r 5%, T 1,σA 20%: d 1=0,35, d 2=0,15.

```python
(.05+.2**2/2)/.2-.2
```
Hasil presisi mesin: `0.15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-15-20"></a>
## 15-20 — Yield zero-coupon risky debt

[PDF 678](../Financial_Management_Theory_and_Practice_15e.pdf#page=678)

$$
y=(FaceDebt/MarketDebt)^{1/N}-1
$$

**Variabel.** N: tahun/periode sampai maturity; debt price hari ini sebagai PV.

**Penurunan dan logika.** Balik hubungan FV=PV(1+y)^N setelah market value debt ditentukan dari asset−equity.

**Syarat penggunaan.** Kontrak satu pembayaran akhir; ini promised yield, bukan expected realized return bila default mungkin.

**Kekeliruan yang perlu dihindari.** Yield tinggi sebagian mengkompensasi kehilangan kas saat default; bukan keuntungan pasti investor.

**Contoh hitung.** Face 100, market 80, N 2 memberi 11,803399%.

```python
(100/80)**(1/2)-1
```
Hasil presisi mesin: `0.11803398875`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
