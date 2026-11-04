# Bab 8: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../08-chapter.md)

## Navigasi

- [8-1: Exercise value call](#rumus-8-1)
- [8-2: Jumlah saham pada hedge binomial](#rumus-8-2)
- [8-3: Binomial risk-neutral value](#rumus-8-3)
- [8-4: State price naik yang sudah didiskontokan](#rumus-8-4)
- [8-5: State price turun yang sudah didiskontokan](#rumus-8-5)
- [8-6: Opsi dari state prices](#rumus-8-6)
- [8-7: Up factor CRR](#rumus-8-7)
- [8-8: Down factor CRR](#rumus-8-8)
- [8-9: Black–Scholes European call](#rumus-8-9)
- [8-10: Parameter d 1](#rumus-8-10)
- [8-11: Parameter d 2](#rumus-8-11)
- [8-12: Put–call parity](#rumus-8-12)
- [8-13: Black–Scholes European put](#rumus-8-13)
- [U-8-01: Put payoff dan put profit](#rumus-u-8-01)

<a id="rumus-8-1"></a>
## 8-1 — Exercise value call

[PDF 382](../Financial_Management_Theory_and_Practice_15e.pdf#page=382)

$$
Payoff_{call}=\max(S-K,0)
$$

**Variabel.** S: harga saham saat exercise; K: strike.

**Penurunan dan logika.** Hak membeli bernilai S−K bila positif; pemilik dapat tidak exercise bila negatif.

**Syarat penggunaan.** Payoff langsung/exercise value, bukan otomatis market value opsi sebelum jatuh tempo.

**Kekeliruan yang perlu dihindari.** Premi yang dibayar belum dikurangkan; payoff tidak sama dengan profit.

**Contoh hitung.** S 115, K 100 memberi payoff 15.

```python
max(115-100,0)
```
Hasil presisi mesin: `15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-2"></a>
## 8-2 — Jumlah saham pada hedge binomial

[PDF 387](../Financial_Management_Theory_and_Practice_15e.pdf#page=387)

$$
\Delta=(C_u-C_d)/(S_u-S_d)
$$

**Variabel.** Cu, Cd: payoff call; Su, Sd: harga saham pada dua state.

**Penurunan dan logika.** Samakan payoff ΔSu−Cu dengan ΔSd−Cd, kemudian selesaikan Δ. Portfolio long Δ saham dan short satu call menjadi riskless dalam model.

**Syarat penggunaan.** Dua state, Su≠Sd; delta opsi adalah pergerakan nilai opsi relatif saham.

**Kekeliruan yang perlu dihindari.** Delta bukan probabilitas dan dapat berubah pada tiap node multi-period.

**Contoh hitung.** Cu 20, Cd 0, Su 120, Sd 80 memberi Δ0,5.

```python
(20-0)/(120-80)
```
Hasil presisi mesin: `0.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-3"></a>
## 8-3 — Binomial risk-neutral value

[PDF 390](../Financial_Management_Theory_and_Practice_15e.pdf#page=390)

$$
C_0=[qC_u+(1-q)C_d]/R,\quad q=(R-d)/(u-d),\ R=e^{r\Delta t}
$$

**Variabel.** u, d: faktor perubahan saham; r: continuous risk-free; Δt=T/n.

**Penurunan dan logika.** No-arbitrage hedge 8-2 menentukan harga opsi yang sama dengan expected payoff risk-neutral didiskontokan pada risk-free.

**Syarat penggunaan.** d<R<u, tanpa dividen pada bentuk dasar, trading dan pendanaan dalam asumsi model.

**Kekeliruan yang perlu dihindari.** q bukan probabilitas aktual naik dan tidak boleh diganti expected return saham.

**Contoh hitung.** u 1,2, d 0,8, R 1,05, Cu 20, Cd 0: call 11,904762.

```python
((1.05-.8)/(1.2-.8)*20)/1.05
```
Hasil presisi mesin: `11.9047619048`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-4"></a>
## 8-4 — State price naik yang sudah didiskontokan

[PDF 391](../Financial_Management_Theory_and_Practice_15e.pdf#page=391)

$$
\pi_u=\frac{(R-d)/(u-d)}{R}=q/R
$$

**Variabel.** πu adalah discounted state price per unit payoff di state u.

**Penurunan dan logika.** Pisahkan koefisien Cu pada 8-3. Ia mengandung probabilitas risk-neutral DAN faktor diskonto.

**Syarat penggunaan.** Asumsi binomial 8-3 sama; πu+πd=1/R.

**Kekeliruan yang perlu dihindari.** πu bukan q; menormalisasi πu+πd menjadi 1 lalu tidak mendiskontokan lagi memberi harga keliru.

**Contoh hitung.** R 1,05, u 1,2, d 0,8 memberi πu 0,595238095.

```python
((1.05-.8)/(1.2-.8))/1.05
```
Hasil presisi mesin: `0.595238095238`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-5"></a>
## 8-5 — State price turun yang sudah didiskontokan

[PDF 391](../Financial_Management_Theory_and_Practice_15e.pdf#page=391)

$$
\pi_d=\frac{(u-R)/(u-d)}R=(1-q)/R
$$

**Variabel.** πd: nilai kini unit pembayaran yang hanya terjadi di state d.

**Penurunan dan logika.** Pisahkan koefisien Cd dari 8-3.

**Syarat penggunaan.** No-arbitrage dan discount factor konsisten dengan 8-4.

**Kekeliruan yang perlu dihindari.** Jumlah πu dan πd kurang dari 1 untuk r positif karena sudah berupa nilai sekarang.

**Contoh hitung.** R 1,05, u 1,2, d 0,8 memberi πd 0,357142857.

```python
((1.2-1.05)/(1.2-.8))/1.05
```
Hasil presisi mesin: `0.357142857143`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-6"></a>
## 8-6 — Opsi dari state prices

[PDF 391](../Financial_Management_Theory_and_Practice_15e.pdf#page=391)

$$
C_0=C_u\pi_u+C_d\pi_d
$$

**Variabel.** State prices 8-4 dan 8-5 sudah didiskontokan.

**Penurunan dan logika.** Tulis ulang 8-3 menggunakan dua koefisien yang sama untuk kontrak berbeda pada tree yang sama.

**Syarat penggunaan.** Cash flows pada tanggal/state yang sesuai; dapat dipakai node demi node.

**Kekeliruan yang perlu dihindari.** Jangan membagi dengan R lagi setelah memakai πu,πd.

**Contoh hitung.** Cu 20, Cd 0 danstate prices 8-4/8-5 memberi 11,904762.

```python
20*((1.05-.8)/(.4)/1.05)
```
Hasil presisi mesin: `11.9047619048`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-7"></a>
## 8-7 — Up factor CRR

[PDF 392](../Financial_Management_Theory_and_Practice_15e.pdf#page=392)

$$
u=e^{\sigma\sqrt{T/n}}
$$

**Variabel.** σ: annualized volatility return; T: tahun; n: jumlah langkah.

**Penurunan dan logika.** CRR memilih lompatan log-price ±σ√Δt sehingga variance per langkah berskala Δt; limit tree mendekati proses lognormal.

**Syarat penggunaan.** Δt=T/n; pengukuran σ konsisten dengan satuan T.

**Kekeliruan yang perlu dihindari.** σ 20% harus ditulis 0,20, bukan 20. Faktor u bukan return persentase itu sendiri.

**Contoh hitung.** σ 20%, T 1, n 1 memberi u 1,221402758.

```python
exp(.2)
```
Hasil presisi mesin: `1.22140275816`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-8"></a>
## 8-8 — Down factor CRR

[PDF 392](../Financial_Management_Theory_and_Practice_15e.pdf#page=392)

$$
d=1/u=e^{-\sigma\sqrt{T/n}}
$$

**Variabel.** d: faktor pengali harga pada langkah turun.

**Penurunan dan logika.** Pilih lompatan log-price simetris sehingga tree recombining dan u×d=1.

**Syarat penggunaan.** Khusus parameterisasi CRR; tree lain dapat memilih u, d berbeda.

**Kekeliruan yang perlu dihindari.** Menggunakan d=1−(u−1) tidak sama dengan 1/u.

**Contoh hitung.** u=e^0,2 memberi d 0,818730753.

```python
exp(-.2)
```
Hasil presisi mesin: `0.818730753078`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-9"></a>
## 8-9 — Black–Scholes European call

[PDF 395](../Financial_Management_Theory_and_Practice_15e.pdf#page=395)

$$
C=SN(d_1)-Ke^{-rT}N(d_2)
$$

**Variabel.** N(): standard-normal CDF; S: saham; K: strike; r: risk-free dengan compounding kontinu.

**Penurunan dan logika.** Limit model replikasi kontinu memberi posisiΔ=N(d 1) saham dan pendanaan nilai Kdiscount×N(d 2); hasilnya formula call.

**Syarat penggunaan.** European, tanpa dividen, σ dan r konstan pada bentuk dasar; T>0,σ>0. Untuk T 0/σ 0 gunakan batas yang benar.

**Kekeliruan yang perlu dihindari.** N(d 1) bukan sekadar probabilitas risk-neutral exercise; N(d 2) berkaitan dengan exercise probability dalam model.

**Contoh hitung.** S=K 100, r 5%, T 1,σ 20% memberi 10,45058357.

```python
bs_call(100,100,.05,1,.2)
```
Hasil presisi mesin: `10.4505835722`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-10"></a>
## 8-10 — Parameter d 1

[PDF 395](../Financial_Management_Theory_and_Practice_15e.pdf#page=395)

$$
d_1=[\ln(S/K)+(r+\sigma^2/2)T]/(\sigma\sqrt T)
$$

**Variabel.** ln adalah natural log; semua rate annualized dengan T dalamtahun.

**Penurunan dan logika.** Standardisasi log-moneyness dengan volatility horizon; term σ²/2 berasal dari hubungan lognormal dan replikasi.

**Syarat penggunaan.** S, K>0;σ, T>0. Dividen kontinu q akan mengubah drift menjadi r−q.

**Kekeliruan yang perlu dihindari.** Logbasis 10 atau menulisσ² sebagaiσ membuat hasil opsi salah.

**Contoh hitung.** S=K 100, r 5%,σ 20%, T 1 memberi d 1=0,35.

```python
(log(100/100)+(.05+.2**2/2)*1)/(.2*sqrt(1))
```
Hasil presisi mesin: `0.35`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-11"></a>
## 8-11 — Parameter d 2

[PDF 395](../Financial_Management_Theory_and_Practice_15e.pdf#page=395)

$$
d_2=d_1-\sigma\sqrt T
$$

**Variabel.** Volatility horizonσ√T menghubungkan dua normal variates.

**Penurunan dan logika.** Substitusi definisid 1 memberi ln(S/K)+(r−σ²/2)T di numerator.

**Syarat penggunaan.** Asumsi Black–Scholes 8-10.

**Kekeliruan yang perlu dihindari.** d 2 biasanya lebih kecil darid 1; N(d 2) harus dihitung ulang, bukan N(d 1)−σ√T.

**Contoh hitung.** d 10,35,σ 20%, T 1 memberi d 20,15.

```python
.35-.2*sqrt(1)
```
Hasil presisi mesin: `0.15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-12"></a>
## 8-12 — Put–call parity

[PDF 401](../Financial_Management_Theory_and_Practice_15e.pdf#page=401)

$$
P_{put}=C-S+Ke^{-rT}
$$

**Variabel.** Put dan call memiliki K, T yang sama.

**Penurunan dan logika.** Portfolio put+saham dan call+risk-free bond K memiliki payoff sama pada maturity, sehingga harganya sama pada no-arbitrage.

**Syarat penggunaan.** European tanpa dividen dan asumsi pendanaan/shortsale sesuai; opsi Amerika memiliki penyesuaian/batas.

**Kekeliruan yang perlu dihindari.** Menambahkan premi call tanpa mengurangi harga saham mencampur portfolio yang berbeda.

**Contoh hitung.** C 10,45058357, S 100, K 100, r 5%, T 1 memberi put 5,57352602.

```python
bs_call(100,100,.05,1,.2)-100+100*exp(-.05)
```
Hasil presisi mesin: `5.57352602226`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-8-13"></a>
## 8-13 — Black–Scholes European put

[PDF 401](../Financial_Management_Theory_and_Practice_15e.pdf#page=401)

$$
P_{put}=S[N(d_1)-1]-Ke^{-rT}[N(d_2)-1]
$$

**Variabel.** Bentuk ekuivalen adalah Ke^(-rT)N(−d 2)−SN(−d 1).

**Penurunan dan logika.** Substitusi call 8-9 ke parity 8-12 dan kelompokkan suku.

**Syarat penggunaan.** Asumsi sama dengan 8-9; parameterput memakai d 1, d 2 yang sama.

**Kekeliruan yang perlu dihindari.** Kedua kurung bertanda N(d)−1: mengganti hanya salah satunya dengan 1−N(d) membalik tanda.

**Contoh hitung.** S=K 100, r 5%, T 1,σ 20% memberi put 5,57352602.

```python
100*(cdf(.35)-1)-100*exp(-.05)*(cdf(.15)-1)
```
Hasil presisi mesin: `5.57352602226`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-8-01"></a>
## U-8-01 — Put payoff dan put profit

[PDF 383](../Financial_Management_Theory_and_Practice_15e.pdf#page=383) · [PDF 384](../Financial_Management_Theory_and_Practice_15e.pdf#page=384)

$$
Payoff_{put}=\max(K-S_T,0),\quad Profit=Payoff-Premium_{FV}
$$

**Variabel.** K: exercise price; ST: harga akhir; premium FV: biaya premium disesuaikan horizon jika diperlukan.

**Penurunan dan logika.** Hak menjual pada K bernilai selisih positif ketika pasar lebih rendah. Untung investasi mengurangi biaya hak tersebut.

**Syarat penggunaan.** Opsi Eropa dasar; laba bergantung konvensi pengukuran biaya premium.

**Kekeliruan yang perlu dihindari.** Payoff positif tidak selalu berarti laba positif setelah premium.

**Contoh hitung.** K 100, ST 80, premium 5 diabaikan bunga: payoff 20, profit 15.

```python
max(100-80,0)-5
```
Hasil presisi mesin: `15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
