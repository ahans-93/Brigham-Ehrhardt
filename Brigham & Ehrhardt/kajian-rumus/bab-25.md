# Bab 25: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../25-chapter.md)

## Navigasi

- [25-1: Return portofolio dua aset](#rumus-25-1)
- [25-1a: Return kombinasi risk-free dan pasar](#rumus-25-1a)
- [25-2: Simpangan baku portofolio dua aset](#rumus-25-2)
- [25-2a: Varians sebelum menyederhanakan aset bebas risiko](#rumus-25-2a)
- [25-2b: Risiko campuran risk-free dan pasar](#rumus-25-2b)
- [25-3: Bobot portofolio varians minimum](#rumus-25-3)
- [25-4: Expected return N aset](#rumus-25-4)
- [25-5: Varians N aset](#rumus-25-5)
- [25-5a: Varians dipisah diagonal dan kovarians](#rumus-25-5a)
- [25-6: Capital market line](#rumus-25-6)
- [25-7: Required return dan kovarians pasar](#rumus-25-7)
- [25-8: Beta dari kovarians](#rumus-25-8)
- [25-9: Security market line](#rumus-25-9)
- [25-10: Market model pada raw return](#rumus-25-10)
- [25-11: CAPM untuk return realisasi](#rumus-25-11)
- [25-12: Regresi excess return dan alpha](#rumus-25-12)
- [25-13: Sharpe ratio](#rumus-25-13)
- [25-14: Treynor ratio](#rumus-25-14)
- [25-15: Dekomposisi varians market model](#rumus-25-15)
- [25-16: Adjusted beta: koefisien tercetak perlu kehati-hatian](#rumus-25-16)
- [25-17: Return aktual: harapan dan kejutan pasar](#rumus-25-17)
- [25-18: Return aktual multifaktor](#rumus-25-18)
- [25-19: APT required return](#rumus-25-19)

<a id="rumus-25-1"></a>
## 25-1 — Return portofolio dua aset

[PDF 1020](../Financial_Management_Theory_and_Practice_15e.pdf#page=1020)

$$
E[r_p]=w_AE[r_A]+(1-w_A)E[r_B]
$$

**Variabel.** wA: bobot nilai aset A; sisanya B.

**Penurunan dan logika.** Kas hasil investasi adalah jumlah kas tiap aset; bagi dengan total nilai awal untuk memperoleh rata-rata tertimbang return.

**Syarat penggunaan.** Bobot awal periode; tidak ada kas eksternal intraperiode yang belum disesuaikan.

**Kekeliruan yang perlu dihindari.** Rata-rata return tidak ditimbang dengan volatilitas.

**Contoh hitung.** Bobot A 40%, return A 12%, B 8%: return 9,6%.

```python
.4*.12+.6*.08
```
Hasil presisi mesin: `0.096`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-1a"></a>
## 25-1a — Return kombinasi risk-free dan pasar

[PDF 1029](../Financial_Management_Theory_and_Practice_15e.pdf#page=1029)

$$
E[r_p]=w_{RF}r_{RF}+(1-w_{RF})E[r_M]
$$

**Variabel.** wRF: bobot aset bebas risiko; M: portofolio pasar.

**Penurunan dan logika.** Substitusi aset bebas risiko dan pasar ke 25-1.

**Syarat penggunaan.** Bunga pinjaman sama dengan bunga investasi bila bobot RF negatif dalam model CML.

**Kekeliruan yang perlu dihindari.** Bobot negatif adalah pinjaman/short, bukan otomatis mustahil; perlu izin dan biaya nyata.

**Contoh hitung.** wRF 25%, rf 4%, rM 10%: return 8,5%.

```python
.25*.04+.75*.10
```
Hasil presisi mesin: `0.085`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-2"></a>
## 25-2 — Simpangan baku portofolio dua aset

[PDF 1020](../Financial_Management_Theory_and_Practice_15e.pdf#page=1020)

$$
\sigma_p=\sqrt{w_A^2\sigma_A^2+(1-w_A)^2\sigma_B^2+2w_A(1-w_A)\rho_{AB}\sigma_A\sigma_B}
$$

**Variabel.** rho: korelasi; sigma: simpangan baku return dengan horizon sama.

**Penurunan dan logika.** Var(wArA+wBrB)=wA²VarA+wB²VarB+2wAwBCovAB; ambil akar untuk SD.

**Syarat penggunaan.** Kovarians tersedia, bobot tetap selama periode; matriks risiko harus valid.

**Kekeliruan yang perlu dihindari.** Jangan menjumlahkan SD tertimbang kecuali korelasi+1 dan bobot nonnegatif.

**Contoh hitung.** Bobot 50/50, SD 20% dan 10%, rho 0: SD 11,18034%.

```python
sqrt(.5**2*.2**2+.5**2*.1**2)
```
Hasil presisi mesin: `0.111803398875`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-2a"></a>
## 25-2a — Varians sebelum menyederhanakan aset bebas risiko

[PDF 1029](../Financial_Management_Theory_and_Practice_15e.pdf#page=1029)

$$
\sigma_p=\sqrt{w_{RF}^2\sigma_{RF}^2+(1-w_{RF})^2\sigma_M^2+2w_{RF}(1-w_{RF})\rho_{RF,M}\sigma_{RF}\sigma_M}
$$

**Variabel.** Sigma RF=0 untuk aset yang benar-benar bebas risiko pada horizon pengukuran.

**Penurunan dan logika.** Ganti A dengan RF dan B dengan M pada 25-2; seluruh suku yang mengandung sigma RF menjadi nol.

**Syarat penggunaan.** Korelasi dengan variabel konstan secara statistik tidak terdefinisi; secara aljabar suku kovarians nol, tidak perlu mengestimasi rho.

**Kekeliruan yang perlu dihindari.** Obligasi pemerintah jangka panjang tidak bebas risiko harga pada horizon pendek.

**Contoh hitung.** wRF 25%, sigma M 20%, sigma RF 0: SD 15%.

```python
sqrt(.25**2*0+.75**2*.2**2)
```
Hasil presisi mesin: `0.15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-2b"></a>
## 25-2b — Risiko campuran risk-free dan pasar

[PDF 1029](../Financial_Management_Theory_and_Practice_15e.pdf#page=1029)

$$
\sigma_p=|1-w_{RF}|\sigma_M
$$

**Variabel.** Sumber menulis(1-wRF)sigma M pada wilayah bobot pasar nonnegatif.

**Penurunan dan logika.** Akar kuadrat(1-wRF)² adalah nilai absolut. Hilangkan tanda absolut hanya jika 1-wRF>=0.

**Syarat penggunaan.** Risk-free benar-benar mempunyai varians nol; return pasar risiko tunggal.

**Kekeliruan yang perlu dihindari.** SD tidak pernah negatif; untuk short pasar, bentuk tanpa absolut tidak berlaku.

**Contoh hitung.** wRF 25%, sigma M 20%: SD 15%.

```python
abs(1-.25)*.20
```
Hasil presisi mesin: `0.15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-3"></a>
## 25-3 — Bobot portofolio varians minimum

[PDF 1022](../Financial_Management_Theory_and_Practice_15e.pdf#page=1022)

$$
w_A^*=\frac{\sigma_B^2-\rho_{AB}\sigma_A\sigma_B}{\sigma_A^2+\sigma_B^2-2\rho_{AB}\sigma_A\sigma_B}
$$

**Variabel.** wA*: solusi unconstrained dua aset.

**Penurunan dan logika.** Turunkan varians 25-2 terhadapw A. Set turunan 2wA(sigma A²+sigma B²-2cov)+2cov-2sigma B²=0 lalu selesaikan.

**Syarat penggunaan.** Penyebut positif; jika long-only, batasi solusi ke[0,1]. Matriks singular perlu ditangani terpisah.

**Kekeliruan yang perlu dihindari.** Minimum varians tidak sama dengan portofolio maksimum Sharpe atau return maksimum.

**Contoh hitung.** Sigma A 20%, sigma B 10%, rho 0: wA 20%.

```python
.1**2/(.2**2+.1**2)
```
Hasil presisi mesin: `0.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-4"></a>
## 25-4 — Expected return N aset

[PDF 1023](../Financial_Management_Theory_and_Practice_15e.pdf#page=1023)

$$
E[r_p]=\sum_{i=1}^{N}w_iE[r_i]
$$

**Variabel.** wi: bobot nilai awal; total bobot 1.

**Penurunan dan logika.** Linearitas ekspektasi berlaku walaupun return aset berkorelasi.

**Syarat penggunaan.** Return horizon sama; biaya dan arus kas eksternal ditangani konsisten.

**Kekeliruan yang perlu dihindari.** Tidak perlu asumsi independensi untuk formula expected return ini.

**Contoh hitung.** Bobot 20/30/50%, return 4/8/12%: return 9,2%.

```python
.2*.04+.3*.08+.5*.12
```
Hasil presisi mesin: `0.092`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-5"></a>
## 25-5 — Varians N aset

[PDF 1023](../Financial_Management_Theory_and_Practice_15e.pdf#page=1023)

$$
\sigma_p^2=\sum_{i=1}^{N}\sum_{j=1}^{N}w_iw_j\sigma_i\sigma_j\rho_{ij}=w^T\Sigma w
$$

**Variabel.** Sigma: matriks kovarians; rhoii=1.

**Penurunan dan logika.** Kembangkan ekspektasi kuadrat penyimpangan jumlah return tertimbang; semua pasangan i, j muncul.

**Syarat penggunaan.** Matriks kovarians simetris positive semidefinite; bobot dan satuan konsisten.

**Kekeliruan yang perlu dihindari.** Suku off-diagonal terhitung dua kali karena(i, j) dan(j, i); ini memang diperlukan.

**Contoh hitung.** Dua aset 50/50, SD 20/10%, rho 0,5: varians 0,0175.

```python
.5**2*.2**2+.5**2*.1**2+2*.5*.5*.5*.2*.1
```
Hasil presisi mesin: `0.0175`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-5a"></a>
## 25-5a — Varians dipisah diagonal dan kovarians

[PDF 1023](../Financial_Management_Theory_and_Practice_15e.pdf#page=1023)

$$
\sigma_p^2=\sum_iw_i^2\sigma_i^2+\sum_i\sum_{j\ne i}w_iw_j\sigma_i\sigma_j\rho_{ij}
$$

**Variabel.** Jumlah kedua tetap meliputi kedua urutan pasangan.

**Penurunan dan logika.** Pisahkan suku i=j dari jumlah ganda 25-5. Alternatif jumlah i<j harus dikali 2.

**Syarat penggunaan.** Semua asumsi matriks risiko 25-5 berlaku.

**Kekeliruan yang perlu dihindari.** Jangan mengalikan jumlah j≠i dengan 2 lagi karena pasangan sudah ganda.

**Contoh hitung.** Contoh 25-5 tetap memberi varians 0,0175.

```python
.01+.0025+.005
```
Hasil presisi mesin: `0.0175`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-6"></a>
## 25-6 — Capital market line

[PDF 1030](../Financial_Management_Theory_and_Practice_15e.pdf#page=1030)

$$
E[r_p]=r_{RF}+\frac{E[r_M]-r_{RF}}{\sigma_M}\sigma_p
$$

**Variabel.** Slope: Sharpe ratio pasar; sigmap: risiko total portofolio efisien.

**Penurunan dan logika.** Dari 25-2b untuk bobot pasar nonnegatif, wM=sigmap/sigma M. Substitusi ke 25-1a.

**Syarat penggunaan.** Portofolio efisien merupakan kombinasi pasar danrisk-free; model pinjaman/investasi sama.

**Kekeliruan yang perlu dihindari.** CML tidak menilai setiap saham individual berdasarkan sigma saham.

**Contoh hitung.** rf 4%, rM 10%, sigma M 20%, sigmap 15%: return 8,5%.

```python
.04+(.10-.04)/.20*.15
```
Hasil presisi mesin: `0.085`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-7"></a>
## 25-7 — Required return dan kovarians pasar

[PDF 1031](../Financial_Management_Theory_and_Practice_15e.pdf#page=1031)

$$
r_i=r_{RF}+(r_M-r_{RF})\frac{Cov(r_i,r_M)}{\sigma_M^2}
$$

**Variabel.** Cov: kovarians saham dengan pasar; sigma M²: varians pasar.

**Penurunan dan logika.** Pada optimum mean-variance, premi expected return per kontribusi marginal risiko harus sama untuk semua aset; normalisasi dengan aset pasar menghasilkan rasio kovarians ini.

**Syarat penggunaan.** Asumsi CAPM dan pasar sebagai portofolio mean-variance efisien; sigma M² positif.

**Kekeliruan yang perlu dihindari.** Risiko yang dihargai adalah kontribusi ke risiko pasar, bukan varians idiosinkratik.

**Contoh hitung.** rf 4%, premi 6%, cov 0,048, var M 0,04: ri 11,2%.

```python
.04+.06*.048/.04
```
Hasil presisi mesin: `0.112`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-8"></a>
## 25-8 — Beta dari kovarians

[PDF 1031](../Financial_Management_Theory_and_Practice_15e.pdf#page=1031)

$$
\beta_i=\frac{Cov(r_i,r_M)}{\sigma_M^2}=\rho_{iM}\frac{\sigma_i}{\sigma_M}
$$

**Variabel.** Beta: sensitivitas return aset terhadap return pasar.

**Penurunan dan logika.** Gunakan Cov=rho sigmai sigma M lalu bagi sigma M²; ini juga slope regresi OLS dengan intersep.

**Syarat penggunaan.** Horizon, benchmark, dan sampel konsisten; varians pasar tidak nol.

**Kekeliruan yang perlu dihindari.** Korelasi tinggi belum tentu beta tinggi jika volatilitas aset kecil.

**Contoh hitung.** rho 0,8, sigmai 30%, sigma M 20%: beta 1,2.

```python
.8*.30/.20
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-9"></a>
## 25-9 — Security market line

[PDF 1032](../Financial_Management_Theory_and_Practice_15e.pdf#page=1032)

$$
r_i=r_{RF}+\beta_i(r_M-r_{RF})
$$

**Variabel.** Premi pasar adalah required return pasar dikurangi risk-free.

**Penurunan dan logika.** Substitusi definisi beta 25-8 ke 25-7.

**Syarat penggunaan.** Hubungan expected/required return dalam keseimbangan CAPM, bukan return realisasi pasti.

**Kekeliruan yang perlu dihindari.** Beta negatif dapat memberi required return di bawahrf; bukan kesalahan tanda otomatis.

**Contoh hitung.** rf 4%, beta 1,2, premi 6%: required 11,2%.

```python
.04+1.2*.06
```
Hasil presisi mesin: `0.112`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-10"></a>
## 25-10 — Market model pada raw return

[PDF 1035](../Financial_Management_Theory_and_Practice_15e.pdf#page=1035)

$$
r_{i,t}=a_i+\beta_i r_{M,t}+e_{i,t}
$$

**Variabel.** ai: intersep regresi raw return; eit: residual.

**Penurunan dan logika.** Proyeksi linear OLS memisahkan komponen terkait pasar dan residual ortogonal terhadap regressor dalam sampel.

**Syarat penggunaan.** Hubungan statistik; tidak otomatis menyatakan CAPM benar atau salah.

**Kekeliruan yang perlu dihindari.** Intersep raw return ai bukan Jensen alpha; denganrf konstan, CAPM memprediksi ai=rf(1-beta).

**Contoh hitung.** a 1%, beta 1,2, return pasar 5%, residual−2%: saham 5%.

```python
.01+1.2*.05-.02
```
Hasil presisi mesin: `0.05`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-11"></a>
## 25-11 — CAPM untuk return realisasi

[PDF 1036](../Financial_Management_Theory_and_Practice_15e.pdf#page=1036)

$$
r_{i,t}=r_{RF,t}+\beta_i(r_{M,t}-r_{RF,t})+e_{i,t}
$$

**Variabel.** eit: kejutan khusus aset; rf, t: realizedrisk-free pada periode.

**Penurunan dan logika.** Expected SML dikombinasikan dengan kejutan pasar dan residual; return aktual dapat menyimpang dari harapan.

**Syarat penggunaan.** Beta stabil dan model faktor pasar memadai.

**Kekeliruan yang perlu dihindari.** Jangan menghapus residual lalu menganggap CAPM memprediksi return aktual tanpa error.

**Contoh hitung.** rf 1%, beta 1,2, rM 5%, e−2%: return 3,8%.

```python
.01+1.2*(.05-.01)-.02
```
Hasil presisi mesin: `0.038`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-12"></a>
## 25-12 — Regresi excess return dan alpha

[PDF 1036](../Financial_Management_Theory_and_Practice_15e.pdf#page=1036)

$$
r_{i,t}-r_{RF,t}=\alpha_i+\beta_i(r_{M,t}-r_{RF,t})+e_{i,t}
$$

**Variabel.** Alpha: intersep excess-return regression, berbeda dari ai raw-return.

**Penurunan dan logika.** Kurangkanrf pada 25-11, lalu tambahkan intersep untuk menguji deviasi empiris dari CAPM. Prediksi CAPM: alpha 0.

**Syarat penggunaan.** Benchmark danrf sesuai frekuensi; uji statistik serta biaya relevan sebelum menilai skill.

**Kekeliruan yang perlu dihindari.** Alpha positif satu sampel tidak membuktikan kinerja abnormal berkelanjutan.

**Contoh hitung.** Alpha 0,5%, beta 1,2, excesspasar 4%, e−2%: excess 3,3%.

```python
.005+1.2*.04-.02
```
Hasil presisi mesin: `0.033`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-13"></a>
## 25-13 — Sharpe ratio

[PDF 1037](../Financial_Management_Theory_and_Practice_15e.pdf#page=1037)

$$
S=\frac{\overline{r_p-r_{RF}}}{s(r_p-r_{RF})}
$$

**Variabel.** Pembilang: rata-rata excess return; penyebut: SD deret excess return per periode.

**Penurunan dan logika.** Normalisasi premi hasil dengan risiko total yang ditanggung; bila rf konstan, SD excess sama dengan SD portofolio.

**Syarat penggunaan.** Horizon sama; annualisasi akar waktu memerlukan asumsi serial independence yang sesuai.

**Kekeliruan yang perlu dihindari.** Notasi rata-rata sumber bukan perintah menghitung SD dari satu nilai rata-rata saja; diperlukan deret observasi.

**Contoh hitung.** Rata-rata return 10%, rf 4%, SD excess 15%: Sharpe 0,4.

```python
(.10-.04)/.15
```
Hasil presisi mesin: `0.4`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-14"></a>
## 25-14 — Treynor ratio

[PDF 1038](../Financial_Management_Theory_and_Practice_15e.pdf#page=1038)

$$
T=\frac{\overline{r_p}-\overline{r_{RF}}}{\beta_p}
$$

**Variabel.** Betap: sensitivitas pasar portofolio.

**Penurunan dan logika.** Premi return dibagi risiko sistematis, cocok ketika portofolio dievaluasi sebagai bagian investasi terdiversifikasi.

**Syarat penggunaan.** Beta benchmark tepat dan cukup stabil.

**Kekeliruan yang perlu dihindari.** Beta nol membuat rasio tidak terdefinisi; beta negatif memerlukan interpretasi khusus, bukan urutkan mekanis.

**Contoh hitung.** Premi 6%, beta 1,2: Treynor 5% per unit beta.

```python
.06/1.2
```
Hasil presisi mesin: `0.05`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-15"></a>
## 25-15 — Dekomposisi varians market model

[PDF 1038](../Financial_Management_Theory_and_Practice_15e.pdf#page=1038)

$$
\sigma_i^2=\beta_i^2\sigma_M^2+\sigma_{e_i}^2
$$

**Variabel.** Sigmae²: varians residual; Cov(rM, e)=0.

**Penurunan dan logika.** Ambil varians 25-10; suku silang hilang karena residual ortogonal terhadap pasar.

**Syarat penggunaan.** Single-index linear model dan residual uncorrelated dengan pasar; tidak memerlukan residual antarsemua saham independen untuk satu aset.

**Kekeliruan yang perlu dihindari.** Yang dijumlahkan adalah varians, bukan SD; risiko pasar beta²sigma M².

**Contoh hitung.** Beta 1,2, sigma M 20%, sigmae 10%: varians 0,0676 dan SD 26%.

```python
1.2**2*.20**2+.10**2
```
Hasil presisi mesin: `0.0676`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-16"></a>
## 25-16 — Adjusted beta: koefisien tercetak perlu kehati-hatian

[PDF 1039](../Financial_Management_Theory_and_Practice_15e.pdf#page=1039)

$$
\beta_{adj,printed}=0.67\beta_{hist}+0.35(1.0)
$$

**Variabel.** PDFhal 1039/cetak 1002 benar-benar menampilkan 0,67 dan 0,35.

**Penurunan dan logika.** Ini shrinkage beta historis ke sekitar 1. Namun koefisien tercetak berjumlah 1,02: beta historis 1 menjadi 1,02, sehingga tidak memiliki titik tetap 1. Bentuk konveks menuju 1 dengan bobot 0,67 adalah 0,67beta+0,33.

**Syarat penggunaan.** Pisahkan reproduksi cetakan dari rekomendasi implementasi; tidak mengklaim errata resmi penerbit. Pilihan estimator harus dinyatakan.

**Kekeliruan yang perlu dihindari.** Jangan diam-diam menyebut rumus cetak 0,35 identik dengan versi 0,33 atau menganggap beta tersesuaikan pasti lebih akurat.

**Contoh hitung.** Beta historis 1,5: cetakan memberi 1,355; versi bobot berjumlah 1 memberi 1,335.

```python
.67*1.5+.35
```
Hasil presisi mesin: `1.355`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-17"></a>
## 25-17 — Return aktual: harapan dan kejutan pasar

[PDF 1044](../Financial_Management_Theory_and_Practice_15e.pdf#page=1044)

$$
r_i=E[r_i]+\beta_i(r_M-E[r_M])+e_i
$$

**Variabel.** rM-E[rM]: kejutan return pasar; ei: kejutan khusus saham.

**Penurunan dan logika.** Kurangi dan tambah beta E[rM] pada market model; definisikan expected return saat residual berharapan nol.

**Syarat penggunaan.** Ekspektasi dan realisasi horizon sama; model linear satu faktor.

**Kekeliruan yang perlu dihindari.** Jangan menambahkan expected market return penuh lagi ke expected stock return; hanya kejutan pasar.

**Contoh hitung.** Expected saham 10%, beta 1,2, pasar aktual 8%, expected pasar 6%, e−1%: aktual 11,4%.

```python
.10+1.2*(.08-.06)-.01
```
Hasil presisi mesin: `0.114`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-18"></a>
## 25-18 — Return aktual multifaktor

[PDF 1044](../Financial_Management_Theory_and_Practice_15e.pdf#page=1044)

$$
r_i=E[r_i]+\sum_{j=1}^{J}\beta_{ij}(F_j-E[F_j])+e_i
$$

**Variabel.** Fj: realisasi faktor; betaij: sensitivitas; ei: residual aset.

**Penurunan dan logika.** Perluas kejutan pasar 25-17 ke beberapa sumber risiko sistematis.

**Syarat penggunaan.** Faktor dan sensitivitas didefinisikan; skala faktor, persentase atau level, harus sepadan denganbeta.

**Kekeliruan yang perlu dihindari.** Jangan menyamakan shock inflasi dengan return portofolio faktor tanpa definisi satuan.

**Contoh hitung.** Expected 10%, eksposur 1,2 dan 0,5, shock+2% dan−1%, e 0: return 11,9%.

```python
.10+1.2*.02+.5*(-.01)
```
Hasil presisi mesin: `0.119`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-25-19"></a>
## 25-19 — APT required return

[PDF 1045](../Financial_Management_Theory_and_Practice_15e.pdf#page=1045)

$$
r_i=r_{RF}+\sum_{j=1}^{J}\beta_{ij}(r_j-r_{RF})
$$

**Variabel.** rj: expected return portofolio faktor yang dinormalisasi; premi faktor rj-rf.

**Penurunan dan logika.** Tanpa arbitrase pada portofolio terdiversifikasi, expected excess return linear terhadap eksposur faktor. Umumnya ditulisri=rf+sum betaij lambdaj.

**Syarat penggunaan.** Faktor risiko terukur dan risiko residual dapat didiversifikasi; tidak semua faktor makro memiliki return mentahrj yang langsung dapat digunakan.

**Kekeliruan yang perlu dihindari.** Beta faktor dan premi harus memakai normalisasi sama; premi faktor tidak otomatis premi pasar CAPM.

**Contoh hitung.** rf 4%, beta 1,2 dan 0,5, premi 5% dan 2%: required 11%.

```python
.04+1.2*.05+.5*.02
```
Hasil presisi mesin: `0.11`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
