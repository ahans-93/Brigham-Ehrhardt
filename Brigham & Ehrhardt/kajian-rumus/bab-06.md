# Bab 6: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../06-chapter.md)

## Navigasi

- [6-1: Expected return distribusi](#rumus-6-1)
- [6-2: Varians probabilitas](#rumus-6-2)
- [6-3: Standar deviasi distribusi](#rumus-6-3)
- [6-4: Mean historis aritmetika](#rumus-6-4)
- [6-5: Sample standard deviation](#rumus-6-5)
- [6-6: Realized portfolio return](#rumus-6-6)
- [6-7: Korelasi sampel](#rumus-6-7)
- [6-8: Beta dari korelasi dan volatilitas](#rumus-6-8)
- [6-9: Beta portofolio](#rumus-6-9)
- [6-10: Varians portofolio terdiversifikasi](#rumus-6-10)
- [6-11: SD portofolio terdiversifikasi](#rumus-6-11)
- [6-12: Kontribusi beta aset ke SD sistematis portofolio](#rumus-6-12)
- [6-13: Covariance dari korelasi](#rumus-6-13)
- [6-14: Beta dari covariance](#rumus-6-14)
- [6-15: CAPM required return](#rumus-6-15)
- [6-16: Premi risiko saham](#rumus-6-16)
- [6-17: Expected portfolio return](#rumus-6-17)
- [6-18: Required portfolio return dari aset](#rumus-6-18)
- [6-19: CAPM portofolio](#rumus-6-19)
- [6-20: Regresi tiga faktor Fama–French](#rumus-6-20)
- [U-6-01: Interpretasi regresi Fama–French (pendamping 6-20)](#rumus-u-6-01)

<a id="rumus-6-1"></a>
## 6-1 — Expected return distribusi

[PDF 282](../Financial_Management_Theory_and_Practice_15e.pdf#page=282)

$$
\mu=\sum_i p_iR_i
$$

**Variabel.** pi: probabilitas skenario; Ri: return skenario; jumlah pi=1.

**Penurunan dan logika.** Definisi ekspektasi adalah rata-rata tertimbang probabilitas seluruh kemungkinan yang saling eksklusif dan mencakup distribusi.

**Syarat penggunaan.** Probabilitas bukan bobot investasi; distribusi dan periode harus jelas.

**Kekeliruan yang perlu dihindari.** Expected return bukan janji return terealisasi.

**Contoh hitung.** Dua skenario berpeluang 50% dengan return 0% dan 20%: ekspektasi 10%.

```python
.5*0+.5*.2
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-2"></a>
## 6-2 — Varians probabilitas

[PDF 283](../Financial_Management_Theory_and_Practice_15e.pdf#page=283)

$$
\sigma^2=\sum_i p_i(R_i-\mu)^2
$$

**Variabel.** μ dari 6-1; σ²: rata-rata kuadrat deviasi.

**Penurunan dan logika.** Kuadrat deviasi menghindari saling hapus deviasi positif-negatif; bobotnya adalah probabilitas.

**Syarat penggunaan.** Distribusi lengkap memakai pi, tidak menggunakan koreksi sampel N−1.

**Kekeliruan yang perlu dihindari.** Varians bersatuan return kuadrat; 0,01 variance bukan otomatis volatilitas 1%.

**Contoh hitung.** Return 0 dan 20%, μ10%, peluangsama: variance 0,01.

```python
.5*(0-.1)**2+.5*(.2-.1)**2
```
Hasil presisi mesin: `0.01`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-3"></a>
## 6-3 — Standar deviasi distribusi

[PDF 283](../Financial_Management_Theory_and_Practice_15e.pdf#page=283)

$$
\sigma=\sqrt{\sum_i p_i(R_i-\mu)^2}
$$

**Variabel.** σ: akar varians, kembali ke satuan return.

**Penurunan dan logika.** Ambil akar 6-2; akar nonnegatif dipilih karena ukuran sebaran tidak bertanda.

**Syarat penggunaan.** Semua input return konsisten sebagai desimal atau persen; hasil mengikuti satuannya.

**Kekeliruan yang perlu dihindari.** Volatilitas simetris tidak sendirinya mengukur semua tail risk atau risiko gagal bayar.

**Contoh hitung.** Variance 0,01 memberi SD 10%.

```python
sqrt(.01)
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-4"></a>
## 6-4 — Mean historis aritmetika

[PDF 286](../Financial_Management_Theory_and_Practice_15e.pdf#page=286)

$$
\bar R=\frac1T\sum_{t=1}^{T}R_t
$$

**Variabel.** T: banyak observasi return dengan horizon sama.

**Penurunan dan logika.** Tiap observasi diberi bobot 1/T. Ini rata-rata return satu periode, berbeda dari compound growth selama T periode.

**Syarat penggunaan.** Sample frequency sama dan tidak ada missing observation yang diperlakukan sebagai nol.

**Kekeliruan yang perlu dihindari.** Untuk return multi-periode yang dikompaun gunakan geometric mean, bukan otomatis mean aritmetika.

**Contoh hitung.** Observasi 0%,20% memiliki mean 10%.

```python
(0+.2)/2
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-5"></a>
## 6-5 — Sample standard deviation

[PDF 286](../Financial_Management_Theory_and_Practice_15e.pdf#page=286)

$$
s=\sqrt{\frac{\sum_{t=1}^{T}(R_t-\bar R)^2}{T-1}}
$$

**Variabel.** s: estimasi SD dari sampel; T>1.

**Penurunan dan logika.** Estimasi mean dari sampel menghabiskan satu degree of freedom. Pembagi T−1 memberi sample variance tak bias pada asumsi sampling standar; akarnya tidak persis tak bias.

**Syarat penggunaan.** Observasi sebanding; annualization dengan akar waktu memerlukan asumsi tambahan tentang dependensi.

**Kekeliruan yang perlu dihindari.** Jangan memakai T−1 untuk distribusi probabilitas lengkap pada 6-2.

**Contoh hitung.** Sampel 0%,20% menghasilkan s 14,142136%.

```python
sqrt(((0-.1)**2+(.2-.1)**2)/(2-1))
```
Hasil presisi mesin: `0.141421356237`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-6"></a>
## 6-6 — Realized portfolio return

[PDF 290](../Financial_Management_Theory_and_Practice_15e.pdf#page=290)

$$
R_{p,t}=\sum_iw_{i,t-1}R_{i,t}
$$

**Variabel.** w: proporsi nilai awal periode; Ri: total return masing-masing aset.

**Penurunan dan logika.** Jumlah nilai akhir tiap aset dibanding total nilai awal menghasilkan rata-rata tertimbang return.

**Syarat penggunaan.** Bobot awal menjumlah satu, return termasuk dividen bila relevan; arus kas eksternal perlu penyesuaian.

**Kekeliruan yang perlu dihindari.** Bobot akhir periode tidak boleh langsung dipakai sebagai bobot realized return periode yang sama.

**Contoh hitung.** Bobot 50/50, realized 8% dan 12%: portfolio 10%.

```python
.5*.08+.5*.12
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-7"></a>
## 6-7 — Korelasi sampel

[PDF 291](../Financial_Management_Theory_and_Practice_15e.pdf#page=291)

$$
\hat\rho_{ij}=\frac{\sum_t(R_{it}-\bar R_i)(R_{jt}-\bar R_j)}{\sqrt{\sum_t(R_{it}-\bar R_i)^2\sum_t(R_{jt}-\bar R_j)^2}}
$$

**Variabel.** Kedua seri harus sejajar tanggal dan memiliki varians positif.

**Penurunan dan logika.** Bagi sample covariance dengan dua sample SD; faktor T−1 pada numerator dan denominator saling hapus.

**Syarat penggunaan.** Titik pengamatan berpasangan; korelasi berada dalam−1 sampai 1 tetapi tidak menunjukkan sebab-akibat.

**Kekeliruan yang perlu dihindari.** Data asynchronous atau harga stale dapat menurunkan korelasi yang terukur secara semu.

**Contoh hitung.** Seri 1,2,3 dan 2,4,6 memiliki korelasi 1.

```python
corr([1,2,3],[2,4,6])
```
Hasil presisi mesin: `1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-8"></a>
## 6-8 — Beta dari korelasi dan volatilitas

[PDF 294](../Financial_Management_Theory_and_Practice_15e.pdf#page=294)

$$
\beta_i=\rho_{iM}\sigma_i/\sigma_M
$$

**Variabel.** M: portofolio pasar; σM>0.

**Penurunan dan logika.** Gunakan beta sebagai covariance/market variance dan covariance=ρσiσM; satu σM saling hapus.

**Syarat penggunaan.** Periode dan benchmark sama; beta adalah sensitivitas sistematis, bukan total risiko.

**Kekeliruan yang perlu dihindari.** Aset sangat volatil dapat memiliki beta kecil bila korelasinya rendah.

**Contoh hitung.** σi 30%,σM 20%,ρ0,8 memberi beta 1,2.

```python
.8*.3/.2
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-9"></a>
## 6-9 — Beta portofolio

[PDF 294](../Financial_Management_Theory_and_Practice_15e.pdf#page=294)

$$
\beta_p=\sum_iw_i\beta_i
$$

**Variabel.** wi: bobot; βi: beta setiap aset terhadap benchmark sama.

**Penurunan dan logika.** Covariance linear terhadap penjumlahan return portofolio, sehingga beta juga linear terhadap bobot.

**Syarat penggunaan.** Bobot didefinisikan pada tanggal yang sama; leverage/short position tercermin dalam bobot.

**Kekeliruan yang perlu dihindari.** Tidak benar bahwa SD portofolio selalu rata-rata SD aset; linearitas ini khusus beta/mean.

**Contoh hitung.** 50% beta 1 dan 50% beta 1,4: beta 1,2.

```python
.5*1+.5*1.4
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-10"></a>
## 6-10 — Varians portofolio terdiversifikasi

[PDF 295](../Financial_Management_Theory_and_Practice_15e.pdf#page=295)

$$
\sigma_p^2\approx\beta_p^2\sigma_M^2
$$

**Variabel.** Portofolio cukup terdiversifikasi sehingga residual risk kecil.

**Penurunan dan logika.** Model single-index memberi variance=beta²×market variance+residual variance. Buang komponen residual hanya sebagai pendekatan diversifikasi.

**Syarat penggunaan.** Residual saling tidak berkorelasi/terdiversifikasi; tidak berlaku otomatis untuk portofolio terkonsentrasi.

**Kekeliruan yang perlu dihindari.** Tanda aproksimasi tidak boleh diubah menjadi identitas untuk setiap aset.

**Contoh hitung.** Beta 1,2 dan σM 20%: systematic variance 0,0576.

```python
1.2**2*.2**2
```
Hasil presisi mesin: `0.0576`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-11"></a>
## 6-11 — SD portofolio terdiversifikasi

[PDF 295](../Financial_Management_Theory_and_Practice_15e.pdf#page=295)

$$
\sigma_p\approx|\beta_p|\sigma_M
$$

**Variabel.** Buku menulis βpσM untuk beta portofolio positif.

**Penurunan dan logika.** Ambil akar 6-10. Akar beta kuadrat adalah nilai absolut beta; syarat beta positif menjelaskan bentuk sumber.

**Syarat penggunaan.** Asumsi diversifikasi 6-10 tetap berlaku.

**Kekeliruan yang perlu dihindari.** Beta negatif tidak berarti standar deviasi negatif.

**Contoh hitung.** Beta 1,2 dan σM 20% memberi SD 24%.

```python
abs(1.2)*.2
```
Hasil presisi mesin: `0.24`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-12"></a>
## 6-12 — Kontribusi beta aset ke SD sistematis portofolio

[PDF 295](../Financial_Management_Theory_and_Practice_15e.pdf#page=295)

$$
\sigma_p\approx\left|\sum_iw_i\beta_i\right|\sigma_M
$$

**Variabel.** Bobot dan beta seperti 6-9; interpretasi sumber untuk beta gabungan positif.

**Penurunan dan logika.** Substitusi 6-9 ke 6-11. Bentuk ini menunjukkan risiko sistematis berubah ketika aset berbobot/beta tertentu diganti.

**Syarat penggunaan.** Bukan formula lengkap variance portofolio tanpa syarat diversifikasi.

**Kekeliruan yang perlu dihindari.** Tidak menjumlah nilai absolut beta per aset; netting beta terjadi sebelum mengambil absolut portofolio.

**Contoh hitung.** Bobot 50/50 beta 1 dan 1,4, σM 20%: SDsistematis 24%.

```python
abs(.5*1+.5*1.4)*.2
```
Hasil presisi mesin: `0.24`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-13"></a>
## 6-13 — Covariance dari korelasi

[PDF 297](../Financial_Management_Theory_and_Practice_15e.pdf#page=297)

$$
Cov(R_i,R_M)=\rho_{iM}\sigma_i\sigma_M
$$

**Variabel.** Covariance bersatuan return kuadrat.

**Penurunan dan logika.** Susun ulang definisi korelasi, yaitu covariance dibagi produk SD.

**Syarat penggunaan.** Parameter dihitung pada periode yang sama.

**Kekeliruan yang perlu dihindari.** Covariance negatif sah; covariance tidak dibatasi−1 sampai 1 seperti korelasi.

**Contoh hitung.** ρ0,8,σi 30%,σM 20%: covariance 0,048.

```python
.8*.3*.2
```
Hasil presisi mesin: `0.048`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-14"></a>
## 6-14 — Beta dari covariance

[PDF 298](../Financial_Management_Theory_and_Practice_15e.pdf#page=298)

$$
\beta_i=Cov(R_i,R_M)/Var(R_M)
$$

**Variabel.** Var(RM)=σM², bukan σM.

**Penurunan dan logika.** Koefisien slope regresi Ri terhadap RM adalah covariance dibagi variance independent variable.

**Syarat penggunaan.** Market variance positif; hasil estimasi memiliki error dan dapat berubah.

**Kekeliruan yang perlu dihindari.** Membagi dengan SD pasar saja mengubah satuan dan memberi beta salah.

**Contoh hitung.** Covariance 0,048 dan variancepasar 0,04: beta 1,2.

```python
.048/.04
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-15"></a>
## 6-15 — CAPM required return

[PDF 301](../Financial_Management_Theory_and_Practice_15e.pdf#page=301)

$$
r_i=r_f+\beta_i RPM
$$

**Variabel.** RPM=E(RM)−rf; semua return untuk horizon yang sama.

**Penurunan dan logika.** CAPM menilai hanya exposure pasar yang tidak dapat dihilangkan melalui diversifikasi; premium aset adalah beta kali premium pasar.

**Syarat penggunaan.** Hubungan equilibrium dalam asumsi CAPM; estimasi rf, RPM, beta mengandung ketidakpastian.

**Kekeliruan yang perlu dihindari.** Required return bukan realized return; gunakan premium pasar, bukan return pasar total, sebagai pengali beta.

**Contoh hitung.** rf 4%, beta 1,2, RPM 5% memberi 10%.

```python
.04+1.2*.05
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-16"></a>
## 6-16 — Premi risiko saham

[PDF 302](../Financial_Management_Theory_and_Practice_15e.pdf#page=302)

$$
RP_i=\beta_i RPM
$$

**Variabel.** RPi merupakan bagian required return di atas risk-free.

**Penurunan dan logika.** Kurangi rf dari kedua sisi 6-15.

**Syarat penggunaan.** Asumsi CAPM dan definisi benchmark tetap sama.

**Kekeliruan yang perlu dihindari.** Angka 6% pada contoh adalah premium, bukan total required return.

**Contoh hitung.** Beta 1,2 dan RPM 5% memberi premium 6%.

```python
1.2*.05
```
Hasil presisi mesin: `0.06`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-17"></a>
## 6-17 — Expected portfolio return

[PDF 306](../Financial_Management_Theory_and_Practice_15e.pdf#page=306)

$$
E(R_p)=\sum_iw_iE(R_i)
$$

**Variabel.** Mean setiap aset, bukan realized return tertentu.

**Penurunan dan logika.** Ekspektasi linear: E(sumw Ri)=sumw E(Ri) untuk bobot yang ditentukan.

**Syarat penggunaan.** Bobot known; strategi bobot state-dependent perlu menilai E(wRi), tidak otomatis E(w)E(Ri).

**Kekeliruan yang perlu dihindari.** Jangan mencampur mean historis satu aset dengan forward expected return aset lain tanpa dasar.

**Contoh hitung.** 50/50 expected 8%,12% memberi 10%.

```python
.5*.08+.5*.12
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-18"></a>
## 6-18 — Required portfolio return dari aset

[PDF 306](../Financial_Management_Theory_and_Practice_15e.pdf#page=306)

$$
r_p=\sum_iw_ir_i
$$

**Variabel.** ri: required return aset yang konsisten model pricing.

**Penurunan dan logika.** Dalam CAPM, jumlahkan rf+βiRPM dengan bobot berjumlah satu; hasilnya rf+βpRPM.

**Syarat penggunaan.** Bobot dan model required return sama.

**Kekeliruan yang perlu dihindari.** Expected dan required return tidak selalu sama di luar equilibrium.

**Contoh hitung.** 50/50 required 8%,12% menghasilkan 10%.

```python
.5*.08+.5*.12
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-19"></a>
## 6-19 — CAPM portofolio

[PDF 306](../Financial_Management_Theory_and_Practice_15e.pdf#page=306)

$$
r_p=r_f+\beta_pRPM
$$

**Variabel.** βp: beta agregat dari 6-9.

**Penurunan dan logika.** Substitusikan beta tertimbang ke hasil 6-18; risk-free tidak dikalikan jumlah aset karena bobot menjumlah satu.

**Syarat penggunaan.** Portofolio boleh memiliki risiko spesifik, tetapi model required return hanya memberi kompensasi untuk beta.

**Kekeliruan yang perlu dihindari.** Rumus tidak mengatakan bahwa dua portofolio dengan beta sama pasti memiliki distribusi return identik.

**Contoh hitung.** rf 4%,βp 1,2, RPM 5% memberi 10%.

```python
.04+1.2*.05
```
Hasil presisi mesin: `0.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-6-20"></a>
## 6-20 — Regresi tiga faktor Fama–French

[PDF 314](../Financial_Management_Theory_and_Practice_15e.pdf#page=314) · [PDF 315](../Financial_Management_Theory_and_Practice_15e.pdf#page=315)

$$
R_{it}-r_{ft}=\alpha_i+b_i(R_{Mt}-r_{ft})+s_iSMB_t+h_iHML_t+\epsilon_{it}
$$

**Variabel.** SMB/HML: return factor-mimicking; α: intercept; b, s, h: loadings; ε: residual.

**Penurunan dan logika.** Perluas regresi pasar dengan dua faktor size/value; predicted excess return menetapkan residual ekspektasian nol, actual tetap dapat berbeda.

**Syarat penggunaan.** Ini persamaan regresi realized excess return. Expected pricing relation perlu asumsi tambahan terhadap alpha dan expected factor premiums.

**Kekeliruan yang perlu dihindari.** Jangan menambahkan rf dua kali atau menyebut semua faktor sebagai bukti kausal.

**Contoh hitung.** α0,1%, b 1,2, market excess 5%, s 0,2, SMB 1%, h 0,3, HML−2%,ε0 memberi excess 5,7%.

```python
.001+1.2*.05+.2*.01+.3*(-.02)
```
Hasil presisi mesin: `0.057`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-6-01"></a>
## U-6-01 — Interpretasi regresi Fama–French (pendamping 6-20)

[PDF 314](../Financial_Management_Theory_and_Practice_15e.pdf#page=314) · [PDF 315](../Financial_Management_Theory_and_Practice_15e.pdf#page=315)

$$
r_i-r_f=\alpha_i+\beta_i(r_M-r_f)+s_iSMB+h_iHML+e_i
$$

**Variabel.** SMB: return small-minus-big; HML: return high-minus-low book/market; si, hi: loading.

**Penurunan dan logika.** Tambahkan portofolio faktor size dan value pada excess-return market model; masing-masing loading mengukur eksposur, bukan bobot investasi langsung.

**Syarat penggunaan.** Definisi dataset, frekuensi, dan benchmark konsisten; ini model empiris, bukan jaminan premi positif setiap periode.

**Kekeliruan yang perlu dihindari.** Jangan mengurangi rf dari SMB/HML lagi jika keduanya sudah long-short self-financing returns.

**Contoh hitung.** Alpha 0, beta 1,2, excess M 5%, s 0,3, SMB 2%, h 0,4, HML−1%: excess 6,2%.

```python
1.2*.05+.3*.02+.4*(-.01)
```
Hasil presisi mesin: `0.062`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
