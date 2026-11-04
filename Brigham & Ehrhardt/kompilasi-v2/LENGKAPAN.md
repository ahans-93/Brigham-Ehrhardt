# Pelengkap kajian dari kompilasi v2

[Indeks integrasi](README.md) · [Pemetaan semua entri](KOMPILASI_TERINTEGRASI.md)

Dua belas kelompok di bawah melengkapi kajian sebelumnya. Ini bukan tambahan 12 persamaan bernomor dari buku; beberapa merupakan pengelompokan atau perluasan rumus tanpa nomor. Contoh numerik ditulis untuk menjelaskan mekanisme.

<a id="rumus-a01"></a>
## A01 — Bid–ask spread

Bab 1.

`Spread=Ask-Bid`

**Variabel.** Ask: harga jual yang ditawarkan dealer; bid: harga beli dealer, untuk kuotasi aset dan waktu yang sama.

**Penurunan/logika.** Investor membeli pada ask dan menjual pada bid. Tanpa perubahan harga, selisih keduanya adalah biaya round trip per unit sebelum komisi.

**Syarat.** Bid/ask harus untuk ukuran dan pasar yang sebanding; spread relatif memerlukan penyebut yang dinyatakan, misalnya midpoint.

**Kekeliruan penggunaan.** Spread bukan laba pasti dealer setelah biaya, risiko inventory, dan adverse selection.

**Contoh.** Bid99,ask101: spread2; relatif midpoint100 adalah2%.

```python
101-99
```

<a id="rumus-a02"></a>
## A02 — EBIT, EBITDA, dan investasi neto

Bab 2.

`EBIT=Sales-CashOperatingCosts-D&A; EBITDA=EBIT+D&A; NetInvestment=K_t-K_{t-1}`

**Variabel.** D&A: depresiasi dan amortisasi; K: modal operasi neto, dengan perimeter aset/liabilitas yang sama antarperiode.

**Penurunan/logika.** Pisahkan beban operasi kas dan nonkas dari penjualan. Selisih K akhir dan awal adalah tambahan investasi neto yang mengurangi NOPAT untuk memperoleh FCF.

**Syarat.** Beban nonkas lain, pajak, modal kerja, dan capex masih perlu rekonsiliasi terpisah. Untuk transaksi akuisisi, kurs, dan revaluasi, perubahan saldo bukan otomatis investasi kas.

**Kekeliruan penggunaan.** EBITDA bukan laba kotor dan bukan arus kas operasi yang persis. Laba kotor adalah sales minus HPP.

**Contoh.** Sales500,biaya kas350,D&A50: EBIT100,EBITDA150. K naik dari200 ke230: investasi30.

```python
(500-350-50)+50
```

<a id="rumus-a03"></a>
## A03 — Rekonsiliasi penggunaan FCF

Bab 2.

`FCF=I(1-T)+NetDebtRepayment+Dividends+NetStockRepurchase+NetNonopInvestment`

**Variabel.** Net debt repayment: pokok dibayar minus utang baru; repurchase neto: pembelian kembali minus emisi saham; investasi nonoperasi neto termasuk perubahan aset kas nonoperasi yang dipilih.

**Penurunan/logika.** Identitas sumber-penggunaan kas: kas operasi setelah seluruh reinvestasi harus dialokasikan ke kreditur, pemilik, atau aset nonoperasi. Emisi utang/saham baru memberi penggunaan neto negatif.

**Syarat.** Perimeter dan klasifikasi kas sama; preferred dividends dan klaim lain harus dimasukkan bila relevan. Semua perubahan yang dipakai harus berupa kas, bukan kenaikan saldo nonkas.

**Kekeliruan penggunaan.** Jangan memaksa rekonsiliasi dengan menghilangkan perubahan saldo kas; tentukan apakah kas tersebut operasi atau nonoperasi.

**Contoh.** Bunga setelah pajak15,pokok neto10,dividen20,buyback30,investasi nonoperasi25: FCF100.

```python
15+10+20+30+25
```

<a id="rumus-a04"></a>
## A04 — Growing annuity: PV, FV, dan batas r=g

Bab 4.

`PV=CF1[1-((1+g)/(1+r))^N]/(r-g); FV=CF1[(1+r)^N-(1+g)^N]/(r-g)`

**Variabel.** CF1: pembayaran pertama pada akhir tahun1; N: jumlah pembayaran; g: pertumbuhan kas per periode; r: tingkat diskonto per periode.

**Penurunan/logika.** Jumlahkan CF1(1+g)^(t-1)/(1+r)^t untuk t1..N sebagai deret geometri. Kalikan PV dengan (1+r)^N untuk FV. Bila r=g, setiap suku PV sama dengan CF1/(1+r), sehingga PV=N*CF1/(1+r), dan FV=N*CF1*(1+r)^(N-1).

**Syarat.** Rumus finite tidak mensyaratkan r>g; syarat itu berlaku untuk perpetuitas. Tetap perlukan 1+r>0 dan timing pembayaran yang konsisten.

**Kekeliruan penggunaan.** Menggunakan CF0 sebagai CF1 atau memakai rumus (r-g) ketika r=g menghasilkan salah tanggal atau pembagian nol.

**Contoh.** CF1=100,r10%,g5%,N3: PV260,518407; FV346,75.

```python
100*(1-(1.05/1.1)**3)/(.10-.05)
```

<a id="rumus-a05"></a>
## A05 — Coefficient of variation return

Bab 6.

`CV=sigma/E[R]`

**Variabel.** Sigma: SD return; E[R]: expected return dengan horizon dan satuan sama.

**Penurunan/logika.** CV menormalkan penyebaran terhadap mean. Ini rasio tanpa dimensi bila pembilang dan penyebut sama-sama berupa return desimal.

**Syarat.** Mean positif dan cukup jauh dari nol untuk perbandingan risiko-per-unit-mean yang masuk akal.

**Kekeliruan penggunaan.** Mean negatif tidak membuat investasi otomatis lebih aman karena CV menjadi negatif; mean nol membuat CV tidak terdefinisi.

**Contoh.** Sigma20%,mean10%: CV2.

```python
.20/.10
```

<a id="rumus-a06"></a>
## A06 — Return saham aktual dan expected yield

Bab 7.

`HPR=(D+P1-P0)/P0; ExpectedReturn=D1/P0+g`

**Variabel.** D: dividen selama horizon; P0,P1: harga awal/akhir ex-dividend sesuai pengukuran; g: capital gain yield pada model Gordon stabil.

**Penurunan/logika.** Return pemegang saham berasal dari distribusi tunai dan perubahan harga. Untuk Gordon konstan, harga tumbuh g sehingga capital-gain yield juga g.

**Syarat.** Satu pembayaran dividen di akhir periode pada bentuk sederhana. Banyak dividen/interim cash memerlukan metode pengukuran return serta reinvestasi yang ditentukan.

**Kekeliruan penggunaan.** Pertumbuhan dividen tidak berarti harga aktual pasti tumbuh g setiap tahun; g pada expected model berbeda dari realisasi.

**Contoh.** P0=100,P1=106,D4: HPR10%.

```python
(4+106-100)/100
```

<a id="rumus-a07"></a>
## A07 — Return pasar dengan repurchase

Bab 9.

`rM=(1+Rep/Div)*(D1/P0)+g`

**Variabel.** Rep/Div: perbandingan agregat buyback terhadap dividen pada basis dan periode yang konsisten; D1/P0: dividend yield pasar.

**Penurunan/logika.** Faktor 1+Rep/Div mengubah dividend yield menjadi total distribution yield. Bentuk yang tidak membagi dengan dividen adalah rM=(Div+Rep)/MarketValue+g pada basis agregat yang sesuai.

**Syarat.** Growth harus didefinisikan konsisten dengan model total payout. Jika g per saham sudah terdorong berkurangnya saham akibat buyback, menambahkan seluruh buyback yield dapat menghitung efek dua kali. Pilih model agregat atau per-saham secara sadar.

**Kekeliruan penggunaan.** Div0 membuat Rep/Div tidak terdefinisi; gunakan total payout langsung. Net issuance dapat memerlukan repurchase neto.

**Contoh.** Dividend yield3%,Rep/Div0,5,g4%: estimasi8,5%.

```python
(1+.5)*.03+.04
```

<a id="rumus-a08"></a>
## A08 — Mean, SD, dan CV NPV proyek

Bab 11.

`Mean=sum(p_s*NPV_s); Sigma=sqrt(sum(p_s*(NPV_s-Mean)^2)); CV=Sigma/Mean`

**Variabel.** p_s: probabilitas skenario; NPV_s: nilai proyek pada skenario; sigma mempunyai unit uang seperti mean.

**Penurunan/logika.** Hitung NPV tiap skenario dahulu, lalu jumlahkan berbobot peluang. Varians probabilitas tidak dibagi jumlah skenario minus satu; SD adalah akar varians.

**Syarat.** Probabilitas nonnegatif dan berjumlah1; CV memerlukan mean positif dan tidak mendekati nol.

**Kekeliruan penggunaan.** CV NPV berbeda dari CV nilai aset positif yang dipakai untuk mengestimasi volatilitas lognormal opsi riil.

**Contoh.** NPV−10,20,50 dengan peluang0,25/0,5/0,25: mean20,varians450,SD21,213203,CV1,060660.

```python
sqrt(.25*(-10-20)**2+.5*(20-20)**2+.25*(50-20)**2)/20
```

<a id="rumus-a09"></a>
## A09 — NI dan EPS sesudah leverage

Bab 15.

`NI=(EBIT-rd*D)(1-T); EPS=NI/n`

**Variabel.** D: utang yang menghasilkan bunga; n: saham common sesudah tindakan pendanaan; rd: bunga sesuai risiko utang.

**Penurunan/logika.** Bunga mengurangi EBIT sebelum pajak; laba common dibagi jumlah saham. Jika ada preferred dividend atau unsur nonoperasi, lakukan penyesuaian sebelum EPS.

**Syarat.** Model sederhana satu tarif pajak dan saldo utang; saham tertimbang waktu untuk EPS laporan dapat berbeda dari jumlah saham proforma pascarekap.

**Kekeliruan penggunaan.** Kenaikan EPS karena saham berkurang tidak membuktikan nilai perusahaan naik; risiko dan biaya ekuitas juga berubah.

**Contoh.** EBIT100,D200,rd6%,T25%,n20: NI66,EPS3,3.

```python
(100-.06*200)*.75/20
```

<a id="rumus-a10"></a>
## A10 — IPO money left on the table

Bab 18.

`MoneyLeft=(Pclose-Poffer)*n_sold`

**Variabel.** Pclose: harga penutupan hari pertama; Poffer: harga emisi; n_sold: jumlah saham yang definisinya dinyatakan, primer/sekunder.

**Penurunan/logika.** Kalikan selisih harga per saham dengan saham yang dialokasikan pada harga penawaran. Ini ukuran ex-post underpricing dalam dolar, berbeda dari spread underwriting.

**Syarat.** Harga penutupan tidak otomatis harga yang dapat diterapkan untuk seluruh emisi tanpa mempengaruhi demand; ini ukuran deskriptif.

**Kekeliruan penggunaan.** Jangan menjumlahkan ukuran ini sebagai biaya kas yang dibayarkan emiten. Saham sekunder memberi proceeds kepada penjual lama, bukan perusahaan.

**Contoh.** Poffer10,Pclose12,n1juta: money left2juta.

```python
(12-10)*1000000
```

<a id="rumus-a11"></a>
## A11 — Kepemilikan pemegang target pada stock merger

Bab 22.

`fTarget=nNew/(nNew+nOld)=ValueSharesToTarget/PostMergerEquity`

**Variabel.** nNew: saham entitas gabungan diserahkan kepada pemilik target; nOld: saham acquirer sebelum transaksi; kelas saham sama.

**Penurunan/logika.** Jumlah saham target claimant dibagi total klaim saham pascamerger. Dengan harga per saham sama, kalikan pembilang dan penyebut dengan harga untuk memperoleh rasio nilai.

**Syarat.** Satu kelas saham yang mempunyai hak setara; total post-merger equity sudah memperhitungkan sinergi, biaya, kas deal, dan pendanaan sesuai model.

**Kekeliruan penggunaan.** Rasio pertukaran saham tidak sama dengan persentase kepemilikan; dan nilai standalone target/total standalone bukan otomatis ownership hasil negosiasi.

**Contoh.** 40saham baru diserahkan ke target,100saham lama: target28,571429%.

```python
40/(100+40)
```

<a id="rumus-a12"></a>
## A12 — CV nilai proyek dan pemetaan opsi riil

Bab 26.

`CVvalue=SD(Vt)/E[Vt]; sigma2=ln(1+CVvalue^2)/t; S=PV(project cash flows),K=investment cost`

**Variabel.** Vt: nilai aset proyek positif pada waktu opsi exercise; t: waktu dalam tahun; sigma: volatilitas log return aset proyek, bukan SD uang.

**Penurunan/logika.** Untuk Vt lognormal, CVvalue^2=exp(sigma2*t)-1. Ambil log dan bagi waktu untuk annual variance, kemudian akar untuk sigma input opsi. S adalah nilai aset yang diterima setelah exercise; K adalah biaya exercise, sehingga jangan memasukkan biaya investasi yang sama ke S dan menguranginya lagi lewat K.

**Syarat.** Pemetaan Black–Scholes adalah pendekatan untuk proyek tidak diperdagangkan; risiko, opportunity cost penundaan, kompetisi, dan kemampuan exercise harus dianalisis. Gunakan probabilitas/diskonto konsisten.

**Kekeliruan penggunaan.** CV NPV yang dapat negatif bukan CV nilai aset lognormal. Varian tahunan0,20 berarti sigma sekitar44,7%, bukan volatilitas20%.

**Contoh.** CV0,47,t1: variance0,199588292,sigma44,675305%.

```python
sqrt(log(1+.47**2))
```
