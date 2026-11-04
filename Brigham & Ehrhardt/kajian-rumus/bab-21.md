# Bab 21: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../21-chapter.md)

## Navigasi

- [21-1: Adjusted present value umum](#rumus-21-1)
- [21-1a: APV dengan tax shield saja](#rumus-21-1a)
- [21-2: Nilai perusahaan tanpa utang](#rumus-21-2)
- [21-3: Pertumbuhan konstan unlevered](#rumus-21-3)
- [21-4: Penghematan pajak bunga per tahun](#rumus-21-4)
- [21-5: PV tax shield umum](#rumus-21-5)
- [21-6: Shield dengan utang tumbuh](#rumus-21-6)
- [21-7: Nilai levered dengan utang tumbuh](#rumus-21-7)
- [21-8: Biaya ekuitas levered umum](#rumus-21-8)
- [21-9: Beta levered umum](#rumus-21-9)
- [21-10: MM tanpa pajak: nilai](#rumus-21-10)
- [21-11: MM tanpa pajak: biaya ekuitas](#rumus-21-11)
- [21-12: MM pajak: nilai](#rumus-21-12)
- [21-13: MM pajak: biaya ekuitas](#rumus-21-13)
- [21-14: Hamada](#rumus-21-14)
- [21-15: Compressed APV: nilai](#rumus-21-15)
- [21-16: Compressed APV: biaya ekuitas](#rumus-21-16)
- [21-16a: Mencari biaya modal unlevered](#rumus-21-16a)
- [21-17: Compressed APV: beta](#rumus-21-17)
- [21-17a: Beta compressed APV dengan utang beta nol](#rumus-21-17a)
- [21-18: Horizon value FCF](#rumus-21-18)
- [21-19: Nilai FCF dengan horizon eksplisit](#rumus-21-19)
- [21-20: Free cash flow to equity](#rumus-21-20)
- [21-20a: FCFE dari laba bersih](#rumus-21-20a)
- [21-21: Nilai ekuitas dari FCFE](#rumus-21-21)
- [21-22: Horizon value FCFE](#rumus-21-22)
- [21-23: Nilai ekuitas dua tahap](#rumus-21-23)
- [21-24: Basis operasi APV](#rumus-21-24)
- [21-25: Horizon unlevered](#rumus-21-25)
- [21-26: Nilai unlevered dua tahap](#rumus-21-26)
- [21-27: PV shield selama forecast CAPV](#rumus-21-27)
- [21-28: Terminal tax shield](#rumus-21-28)
- [21-29: Seluruh PV shield CAPV](#rumus-21-29)

<a id="rumus-21-1"></a>
## 21-1 — Adjusted present value umum

[PDF 888](../Financial_Management_Theory_and_Practice_15e.pdf#page=888)

$$
V_L=V_U+PV(SideEffects)
$$

**Variabel.** VL: nilai dengan pendanaan; VU: nilai operasi tanpa leverage; efek samping: shield, subsidi, biaya emisi/distress yang dimodelkan.

**Penurunan dan logika.** Pisahkan nilai investasi operasi dari konsekuensi pendanaannya. Setiap komponen didiskontokan sesuai risiko sendiri.

**Syarat penggunaan.** Efek dihitung inkremental dan tanpa penghitungan ganda.

**Kekeliruan yang perlu dihindari.** APV tidak berarti semua manfaat pendanaan didiskontokan pada biaya utang.

**Contoh hitung.** VU 1.000, shield 80, biaya emisi 10: VL 1.070.

```python
1000+80-10
```
Hasil presisi mesin: `1070`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-1a"></a>
## 21-1a — APV dengan tax shield saja

[PDF 888](../Financial_Management_Theory_and_Practice_15e.pdf#page=888)

$$
V_L=V_U+V_{TS}
$$

**Variabel.** VTS: PV penghematan pajak bunga.

**Penurunan dan logika.** Kasus khusus 21-1 ketika hanya tax shield yang dimasukkan sebagai efek pendanaan.

**Syarat penggunaan.** Biaya distress dan efek lain diabaikan oleh model ini.

**Kekeliruan yang perlu dihindari.** Jika VU sudah dihitung memakai WACC setelah pajak, menambah shield lagi menghitung manfaat dua kali.

**Contoh hitung.** VU 1.000 dan VTS 80: VL 1.080.

```python
1000+80
```
Hasil presisi mesin: `1080`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-2"></a>
## 21-2 — Nilai perusahaan tanpa utang

[PDF 888](../Financial_Management_Theory_and_Practice_15e.pdf#page=888)

$$
V_U=\sum_{t=1}^{\infty}\frac{FCF_t}{(1+r_U)^t}
$$

**Variabel.** rU: biaya ekuitas tanpa leverage; FCF: kas operasi bebas setelah pajak operasi.

**Penurunan dan logika.** Tanpa utang, seluruh risiko operasi dan seluruh FCF ditanggung ekuitas; WACC=rU.

**Syarat penggunaan.** Risiko operasi stabil; penambahan shield dilakukan terpisah.

**Kekeliruan yang perlu dihindari.** Jangan mengganti FCF dengan laba bersih levered.

**Contoh hitung.** FCF 100 konstan, rU 10%: VU 1.000.

```python
100/.10
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-3"></a>
## 21-3 — Pertumbuhan konstan unlevered

[PDF 888](../Financial_Management_Theory_and_Practice_15e.pdf#page=888)

$$
V_U=\frac{FCF_1}{r_U-g_L}
$$

**Variabel.** gL: pertumbuhan jangka panjang; FCF 1: kas tahun depan.

**Penurunan dan logika.** Jumlahkan deret 21-2 dengan FCFt=FCF 1(1+gL)^(t-1).

**Syarat penggunaan.** rU>gL dan pertumbuhan konstan berkelanjutan.

**Kekeliruan yang perlu dihindari.** FCF 0 belum dikalikan 1+g tidak boleh langsung dipakai sebagai pembilang.

**Contoh hitung.** FCF 1=100, rU 10%, g 2%: VU 1.250.

```python
100/(.10-.02)
```
Hasil presisi mesin: `1250`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-4"></a>
## 21-4 — Penghematan pajak bunga per tahun

[PDF 888](../Financial_Management_Theory_and_Practice_15e.pdf#page=888)

$$
TS_t=r_dD_tT
$$

**Variabel.** Dt: saldo utang yang menghasilkan bunga tahun t; T: tarif pajak marginal efektif untuk bunga.

**Penurunan dan logika.** Bunga rdDt mengurangi laba kena pajak; pajak yang dihemat sama dengan bunga dikali T.

**Syarat penggunaan.** Pengurangan bunga benar-benar dapat digunakan dan tidak dibatasi; timing saldo mengikuti kontrak.

**Kekeliruan yang perlu dihindari.** Pajak rugi/tax limitation dapat menunda atau meniadakan shield; ini bukan tarif aktual universal.

**Contoh hitung.** D 200, rd 8%, T 25%: TS 4.

```python
.08*200*.25
```
Hasil presisi mesin: `4`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-5"></a>
## 21-5 — PV tax shield umum

[PDF 888](../Financial_Management_Theory_and_Practice_15e.pdf#page=888)

$$
V_{TS}=\sum_{t=1}^{\infty}\frac{TS_t}{(1+r_{TS})^t}
$$

**Variabel.** rTS: required return sesuai risiko tax shield.

**Penurunan dan logika.** Tax shield merupakan arus kas tersendiri sehingga nilainya adalah PV semua manfaat pajak.

**Syarat penggunaan.** rTS ditentukan oleh kebijakan utang dan risiko pemanfaatan pajak; tidak otomatis sama denganrd.

**Kekeliruan yang perlu dihindari.** Menggunakan rU pada shield tetap yang aman atau rd pada shield yang bergerak bersama operasi memerlukan alasan model.

**Contoh hitung.** Shield 4 konstan, rTS 8%: nilai 50.

```python
4/.08
```
Hasil presisi mesin: `50`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-6"></a>
## 21-6 — Shield dengan utang tumbuh

[PDF 889](../Financial_Management_Theory_and_Practice_15e.pdf#page=889)

$$
V_{TS}=\frac{r_dTD_0(1+g_L)}{r_{TS}-g_L}
$$

**Variabel.** D 0: basis utang pada waktu 0 dalam konvensi pertumbuhan sumber; D 1=D 0(1+gL).

**Penurunan dan logika.** Substitusi TSt=rdTD 0(1+gL)^t ke 21-5, lalu jumlahkan deret geometri.

**Syarat penggunaan.** rTS>gL; rd, T, g tetap; jumlah utang dan tahun bunga ditetapkan konsisten.

**Kekeliruan yang perlu dihindari.** Jika bunga tahun 1 dikenakan pada saldo D 0, pembilang pertama justru rdTD 0; jangan mencampur timing.

**Contoh hitung.** D 0=100, g 2%, rd 6%, T 25%, rTS 10%: shield 19,125.

```python
.06*.25*100*1.02/(.10-.02)
```
Hasil presisi mesin: `19.125`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-7"></a>
## 21-7 — Nilai levered dengan utang tumbuh

[PDF 889](../Financial_Management_Theory_and_Practice_15e.pdf#page=889)

$$
V_L=V_U+\frac{r_d}{r_{TS}-g_L}TD_0(1+g_L)
$$

**Variabel.** Variabel mengikuti 21-6.

**Penurunan dan logika.** Masukkan PV shield 21-6 ke 21-1a. Ini menjelaskan saluran pertumbuhan utang terhadap nilai manfaat pajak.

**Syarat penggunaan.** Hanya shield sebagai efek pendanaan; struktur pertumbuhan dan discount rate sama seperti 21-6.

**Kekeliruan yang perlu dihindari.** Pertumbuhan utang tidak menciptakan manfaat tanpa batas ketika g mendekati rTS; model menjadi sangat sensitif.

**Contoh hitung.** VU 1.000 ditambah shield 19,125: VL 1.019,125.

```python
1000+.06*.25*100*1.02/(.10-.02)
```
Hasil presisi mesin: `1019.125`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-8"></a>
## 21-8 — Biaya ekuitas levered umum

[PDF 889](../Financial_Management_Theory_and_Practice_15e.pdf#page=889) · [PDF 890](../Financial_Management_Theory_and_Practice_15e.pdf#page=890)

$$
r_L=r_U+(r_U-r_d)\frac{w_d}{w_s}-(r_U-r_{TS})\frac{r_dT}{r_{TS}-g_L}\frac{w_d}{w_s}
$$

**Variabel.** wd/ws: rasio nilai pasar utang terhadap ekuitas; rL: required return ekuitas levered.

**Penurunan dan logika.** Identitas risiko klaim memberi rL=rU+(rU-rd)D/E-(rU-rTS)VTS/E. Substitusi hubungan VTS/D yang diasumsikan menghasilkan bentuk sumber.

**Syarat penggunaan.** Definisikan D dan timing shield konsisten: bentuk sumber memakai VTS/D=rdT/(rTS-g). Dengan D 0 pada 21-6, rasio memuat faktor 1+g; jangan mencampur kedua konvensi tanpa rekonsiliasi.

**Kekeliruan yang perlu dihindari.** Hamada hanya kasus khusus; rumus umum ini memerlukan risiko shield, bukan hanya tarif pajak.

**Contoh hitung.** rU 10%, rd 6%, rTS 8%, T 25%, g 0, D/E 0,5: rL 11,8125%.

```python
.10+(.10-.06)*.5-(.10-.08)*(.06*.25/.08)*.5
```
Hasil presisi mesin: `0.118125`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-9"></a>
## 21-9 — Beta levered umum

[PDF 889](../Financial_Management_Theory_and_Practice_15e.pdf#page=889)

$$
\beta_L=\beta_U+(\beta_U-\beta_d)\frac{D}{E}-(\beta_U-\beta_{TS})\frac{r_dT}{r_{TS}-g_L}\frac{D}{E}
$$

**Variabel.** Beta U, betad, beta TS: sensitivitas pasar operasi, utang, dan shield.

**Penurunan dan logika.** Gunakan beta E E+betad D=beta U VU+beta TS VTS dan VU=E+D-VTS. Susun ulang lalu substitusi rasio shield.

**Syarat penggunaan.** Beta semua klaim terhadap pasar dan horizon sama; konvensi VTS/D mengikuti 21-8.

**Kekeliruan yang perlu dihindari.** Utang berisiko dapat mempunyai beta positif; menganggapnya nol dapat membesar-besarkan beta ekuitas.

**Contoh hitung.** beta U 1, betad 0,2, beta TS 0,5, D/E 0,5, rd 6%, T 25%, rTS 8%, g 0: beta L 1,353125.

```python
1+(1-.2)*.5-(1-.5)*(.06*.25/.08)*.5
```
Hasil presisi mesin: `1.353125`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-10"></a>
## 21-10 — MM tanpa pajak: nilai

[PDF 891](../Financial_Management_Theory_and_Practice_15e.pdf#page=891)

$$
V_L=V_U
$$

**Variabel.** VL, VU: nilai operasi dengan/tanpa utang.

**Penurunan dan logika.** Jika pendanaan hanya membagi arus kas yang sama dan investor dapat mereplikasi leverage, arbitrase menyamakan total nilai.

**Syarat penggunaan.** Model MM tanpa pajak, friksi, distress, atau efek informasi; sumber memakaig 0.

**Kekeliruan yang perlu dihindari.** Kesetaraan nilai tidak berarti saham levered sama risikonya dengan saham unlevered.

**Contoh hitung.** VU 1.000 tetap 1.000 setelah perubahan pendanaan dalam model.

```python
1000+0
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-11"></a>
## 21-11 — MM tanpa pajak: biaya ekuitas

[PDF 891](../Financial_Management_Theory_and_Practice_15e.pdf#page=891)

$$
r_L=r_U+(r_U-r_d)D/E
$$

**Variabel.** D/E: leverage nilai pasar.

**Penurunan dan logika.** T 0 menghilangkan shield pada 21-8; seluruh tambahan risiko operasi dialihkan ke ekuitas yang lebih kecil.

**Syarat penggunaan.** Asumsi MM tanpa pajak; required return utang sesuai risiko.

**Kekeliruan yang perlu dihindari.** Kenaikan biaya ekuitas mengimbangi penggunaan utang murah; WACC tidak otomatis turun.

**Contoh hitung.** rU 10%, rd 6%, D/E 0,5: rL 12%.

```python
.10+(.10-.06)*.5
```
Hasil presisi mesin: `0.12`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-12"></a>
## 21-12 — MM pajak: nilai

[PDF 891](../Financial_Management_Theory_and_Practice_15e.pdf#page=891)

$$
V_L=V_U+TD
$$

**Variabel.** T: pajak perusahaan; D: utang permanen tetap.

**Penurunan dan logika.** Dengan shield=rdDT dan diskonto rd, perpetuitas shield menjadi TD.

**Syarat penggunaan.** Utang tetap, pajak dapat digunakan, tanpa distress; bukan formula setiap kebijakan utang tumbuh.

**Kekeliruan yang perlu dihindari.** TD tidak dapat ditambahkan ke nilai yang telah memasukkan shield lewat WACC.

**Contoh hitung.** VU 1.000, T 25%, D 200: VL 1.050.

```python
1000+.25*200
```
Hasil presisi mesin: `1050`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-13"></a>
## 21-13 — MM pajak: biaya ekuitas

[PDF 891](../Financial_Management_Theory_and_Practice_15e.pdf#page=891)

$$
r_L=r_U+(r_U-r_d)(1-T)D/E
$$

**Variabel.** rU, rL: biaya ekuitas tanpa/dengan utang.

**Penurunan dan logika.** Masukkan g 0, rTS=rd ke 21-8; suku shield mengurangi leverage ekonomi sebesar T.

**Syarat penggunaan.** Asumsi utang permanen dan shield berisiko seperti utang.

**Kekeliruan yang perlu dihindari.** Faktor 1-T tidak boleh dipindahkan begitu saja ke compressed APV.

**Contoh hitung.** rU 10%, rd 6%, T 25%, D/E 0,5: rL 11,5%.

```python
.10+(.10-.06)*.75*.5
```
Hasil presisi mesin: `0.115`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-14"></a>
## 21-14 — Hamada

[PDF 891](../Financial_Management_Theory_and_Practice_15e.pdf#page=891)

$$
\beta_L=\beta_U[1+(1-T)D/E]
$$

**Variabel.** Beta U: beta aset operasi tanpa leverage; beta L: beta ekuitas.

**Penurunan dan logika.** Pada 21-9, tetapkan g 0, betad 0, beta TS 0, rTS=rd sehingga suku beta U TD/E dikurangkan.

**Syarat penggunaan.** Beta utang diabaikan dan asumsi MM pajak berlaku.

**Kekeliruan yang perlu dihindari.** Untuk peer comparison, unlever beta tiap peer dengan leverage masing-masing sebelum mengambil rata-rata.

**Contoh hitung.** Beta U 0,8, T 25%, D/E 0,5: beta L 1,1.

```python
.8*(1+.75*.5)
```
Hasil presisi mesin: `1.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-15"></a>
## 21-15 — Compressed APV: nilai

[PDF 892](../Financial_Management_Theory_and_Practice_15e.pdf#page=892)

$$
V_L=V_U+\frac{r_dTD_1}{r_U-g_L}
$$

**Variabel.** D 1: basis utang untuk shield tahun pertama; rU dipakai juga untuk risiko shield.

**Penurunan dan logika.** Asumsikan rTS=rU pada 21-6 dan D 1=D 0(1+g). Nilai shield terpisah dari nilai operasi.

**Syarat penggunaan.** Shield mengikuti risiko operasi; rU>gL; timing D 1 tegas.

**Kekeliruan yang perlu dihindari.** Memakai TD seperti MM bersamaan dengan asumsi compressed APV tidak konsisten.

**Contoh hitung.** VU 1.000, D 1=102, rd 6%, T 25%, rU 10%, g 2%: VL 1.019,125.

```python
1000+.06*.25*102/(.10-.02)
```
Hasil presisi mesin: `1019.125`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-16"></a>
## 21-16 — Compressed APV: biaya ekuitas

[PDF 892](../Financial_Management_Theory_and_Practice_15e.pdf#page=892) · [PDF 900](../Financial_Management_Theory_and_Practice_15e.pdf#page=900)

$$
r_L=r_U+(r_U-r_d)D/E
$$

**Variabel.** D/E: rasio nilai pasar; rU: required return operasi.

**Penurunan dan logika.** Dengan rTS=rU, suku terakhir 21-8 nol; bentuknya sama dengan MM tanpa pajak meskipun nilai shield tetap positif.

**Syarat penggunaan.** Model compressed APV; jangan menafsirkan tidak adanya T sebagai pajak tidak bermanfaat.

**Kekeliruan yang perlu dihindari.** Jangan memakai Hamada yang mengandung 1-T untuk melengkapi model ini secara otomatis.

**Contoh hitung.** rU 11%, rd 7%, D/E 0,5: rL 13%.

```python
.11+(.11-.07)*.5
```
Hasil presisi mesin: `0.13`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-16a"></a>
## 21-16a — Mencari biaya modal unlevered

[PDF 900](../Financial_Management_Theory_and_Practice_15e.pdf#page=900)

$$
r_U=w_s r_L+w_d r_d
$$

**Variabel.** ws+wd=1; bobot nilai pasar.

**Penurunan dan logika.** Kalikan 21-16 dengan E, kumpulkan rU(E+D), lalu bagi E+D.

**Syarat penggunaan.** Compressed APV; ini rata-rata sebelum efek pajak bunga, bukan WACC setelah pajak.

**Kekeliruan yang perlu dihindari.** Jangan memakai rd(1-T) di sini lalu menyebut hasilnyar U.

**Contoh hitung.** ws 0,7, wd 0,3, rL 13%, rd 9%: rU 11,8%.

```python
.7*.13+.3*.09
```
Hasil presisi mesin: `0.118`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-17"></a>
## 21-17 — Compressed APV: beta

[PDF 892](../Financial_Management_Theory_and_Practice_15e.pdf#page=892) · [PDF 900](../Financial_Management_Theory_and_Practice_15e.pdf#page=900)

$$
\beta_L=\beta_U+(\beta_U-\beta_d)D/E
$$

**Variabel.** Beta TS=beta U pada asumsi compressed APV.

**Penurunan dan logika.** Suku terakhir 21-9 hilang karena risiko shield sama dengan risiko operasi.

**Syarat penggunaan.** Nilai pasar utang/ekuitas dan beta utang sebanding.

**Kekeliruan yang perlu dihindari.** Menggunakan beta utang nol harus dinyatakan sebagai pendekatan.

**Contoh hitung.** Beta U 0,8, betad 0,2, D/E 0,5: beta L 1,1.

```python
.8+(.8-.2)*.5
```
Hasil presisi mesin: `1.1`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-17a"></a>
## 21-17a — Beta compressed APV dengan utang beta nol

[PDF 893](../Financial_Management_Theory_and_Practice_15e.pdf#page=893)

$$
\beta_L=\beta_U(1+D/E)
$$

**Variabel.** Beta utang diabaikan; D/E=wd/ws.

**Penurunan dan logika.** Tetapkan betad 0 dalam 21-17 dan faktorkan beta U.

**Syarat penggunaan.** Compressed APV, beta utang kecil; bukan Hamada.

**Kekeliruan yang perlu dihindari.** Faktor 1-T sengaja tidak muncul karena asumsi risiko shield berbeda.

**Contoh hitung.** Beta U 0,8, D/E 0,5: beta L 1,2.

```python
.8*(1+.5)
```
Hasil presisi mesin: `1.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-18"></a>
## 21-18 — Horizon value FCF

[PDF 893](../Financial_Management_Theory_and_Practice_15e.pdf#page=893)

$$
HV_{FCF,N}=\frac{FCF_N(1+g_L)}{WACC-g_L}
$$

**Variabel.** HV di akhir N; FCFN adalah kas terakhir periode eksplisit.

**Penurunan dan logika.** Terapkan deret perpetuitas tumbuh pada kas mulai N+1.

**Syarat penggunaan.** WACC dan pertumbuhan stabil sesudah N; WACC>gL.

**Kekeliruan yang perlu dihindari.** HV belum berada di waktu 0 dan harus didiskontokan N periode.

**Contoh hitung.** FCFN 100, g 2%, WACC 10%: HV 1.275.

```python
100*1.02/(.10-.02)
```
Hasil presisi mesin: `1275`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-19"></a>
## 21-19 — Nilai FCF dengan horizon eksplisit

[PDF 893](../Financial_Management_Theory_and_Practice_15e.pdf#page=893)

$$
V_{FCF}=\sum_{t=1}^{N}\frac{FCF_t}{(1+WACC)^t}+\frac{HV_{FCF,N}}{(1+WACC)^N}
$$

**Variabel.** N: akhir proyeksi; HV mencakup kas mulai N+1.

**Penurunan dan logika.** Pisahkan deret nilai ke interval 1..N dan sisanya, lalu diskontokan masing-masing.

**Syarat penggunaan.** Risiko dan leverage cukup stabil untuk WACC yang dipakai; jika berubah, gunakan faktor periode.

**Kekeliruan yang perlu dihindari.** Jangan masukkan FCFN lagi dalam terminal kas pertama.

**Contoh hitung.** N 2, kas 90 dan 100, HV 1.275, WACC 10%: nilai 1.218,181818.

```python
90/1.1+(100+1275)/1.1**2
```
Hasil presisi mesin: `1218.18181818`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-20"></a>
## 21-20 — Free cash flow to equity

[PDF 894](../Financial_Management_Theory_and_Practice_15e.pdf#page=894)

$$
FCFE=FCF-I(1-T)+NewDebt-PrincipalRepaid
$$

**Variabel.** FCF: kas bebas operasi; I: bunga; delta D=utang baru minus pokok dibayar.

**Penurunan dan logika.** Dari kas untuk semua penyedia modal, kurangi bunga setelah pajak dan pembayaran pokok; tambahkan pembiayaan utang baru.

**Syarat penggunaan.** Shield tersedia; pisahkan transaksi nonkas dan komponen pendanaan lain jika material.

**Kekeliruan yang perlu dihindari.** Kenaikan saldo utang akibat kurs atau akuisisi nonkas bukan penerimaan utang tunai.

**Contoh hitung.** FCF 100, I 20, T 25%, utang baru 30, pokok 10: FCFE 105.

```python
100-20*(1-.25)+30-10
```
Hasil presisi mesin: `105`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-20a"></a>
## 21-20a — FCFE dari laba bersih

[PDF 894](../Financial_Management_Theory_and_Practice_15e.pdf#page=894)

$$
FCFE=NI-\Delta NOWC-\Delta NetOperatingLongTermAssets+\Delta D
$$

**Variabel.** Delta modal operasi neto mencakup perubahan aset tetap neto sehingga depresiasi sudah direkonsiliasi.

**Penurunan dan logika.** FCF=NOPAT-delta K dan NI=NOPAT-I(1-T); masukkan ke 21-20.

**Syarat penggunaan.** NI dan modal operasi mencakup perimeter operasi sama; tidak ada preferred atau nonoperating income yang belum disesuaikan.

**Kekeliruan yang perlu dihindari.** Jika memakai gross capex, tambah kembali depresiasi; jangan menguranginya dua kali lewat perubahan aset neto.

**Contoh hitung.** NI 80, delta K 25, delta D 10: FCFE 65.

```python
80-25+10
```
Hasil presisi mesin: `65`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-21"></a>
## 21-21 — Nilai ekuitas dari FCFE

[PDF 894](../Financial_Management_Theory_and_Practice_15e.pdf#page=894)

$$
V_E=\sum_{t=1}^{\infty}\frac{FCFE_t}{(1+r_L)^t}
$$

**Variabel.** rL: required return pemegang saham dengan leverage yang sesuai.

**Penurunan dan logika.** FCFE milik ekuitas saja, sehingga didiskontokan pada biaya ekuitas.

**Syarat penggunaan.** Kebijakan utang dan cash flow forecast konsisten; jika rL berubah, gunakan discount factor per tahun.

**Kekeliruan yang perlu dihindari.** Jangan mendiskontokan FCFE dengan WACC atau mengurangi utang lagi dari hasil nilai ekuitas.

**Contoh hitung.** FCFE 60 konstan, rL 12%: VE 500.

```python
60/.12
```
Hasil presisi mesin: `500`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-22"></a>
## 21-22 — Horizon value FCFE

[PDF 894](../Financial_Management_Theory_and_Practice_15e.pdf#page=894)

$$
HV_{E,N}=\frac{FCFE_{N+1}}{r_L-g_L}=\frac{FCFE_N(1+g_L)}{r_L-g_L}
$$

**Variabel.** HV ekuitas pada akhir N; gL pertumbuhan stabil.

**Penurunan dan logika.** Jumlahkan FCFE mulai N+1 sebagai perpetuitas tumbuh.

**Syarat penggunaan.** rL>gL; kebutuhan reinvestasi dan kebijakan utang mendukung pertumbuhan.

**Kekeliruan yang perlu dihindari.** Jangan menggunakan FCF operasi dalam terminal ekuitas.

**Contoh hitung.** FCFEN 60, g 2%, rL 12%: HV 612.

```python
60*1.02/(.12-.02)
```
Hasil presisi mesin: `612`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-23"></a>
## 21-23 — Nilai ekuitas dua tahap

[PDF 895](../Financial_Management_Theory_and_Practice_15e.pdf#page=895)

$$
V_E=\sum_{t=1}^{N}\frac{FCFE_t}{(1+r_L)^t}+\frac{HV_{E,N}}{(1+r_L)^N}
$$

**Variabel.** Semua arus kas setelah pembayaran kepada kreditur.

**Penurunan dan logika.** Pisahkan PV FCFE eksplisit dan PV seluruh kas sesudah horizon.

**Syarat penggunaan.** Biaya ekuitas sesuai leverage; terminal tidak menghitung kas N dua kali.

**Kekeliruan yang perlu dihindari.** Menambahkan kas nonoperasi memerlukan pengecekan apakah sudah didistribusikan dalam FCFE.

**Contoh hitung.** N 2, FCFE 50,60, HV 612, rL 12%: VE 580,357143.

```python
50/1.12+(60+612)/1.12**2
```
Hasil presisi mesin: `580.357142857`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-24"></a>
## 21-24 — Basis operasi APV

[PDF 895](../Financial_Management_Theory_and_Practice_15e.pdf#page=895)

$$
V_U=\sum_{t=1}^{\infty}\frac{FCF_t}{(1+r_U)^t}
$$

**Variabel.** Persamaan identik 21-2, digunakan pada proyeksi APV multiperiode.

**Penurunan dan logika.** Nilai bisnis tanpa pendanaan dihitung terlebih dahulu; shield diproyeksikan terpisah.

**Syarat penggunaan.** FCF tidak mengandung bunga; rU sesuai risiko bisnis.

**Kekeliruan yang perlu dihindari.** Kesamaan nomor keluarga tidak berarti review ini melewatkan pengulangan sumber.

**Contoh hitung.** FCF 80 konstan, rU 10%: VU 800.

```python
80/.10
```
Hasil presisi mesin: `800`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-25"></a>
## 21-25 — Horizon unlevered

[PDF 895](../Financial_Management_Theory_and_Practice_15e.pdf#page=895)

$$
HV_{U,N}=\frac{FCF_N(1+g_L)}{r_U-g_L}
$$

**Variabel.** rU: biaya ekuitas tanpa leverage.

**Penurunan dan logika.** Nilai kas operasi mulai N+1 pada N dengan perpetuitas tumbuh.

**Syarat penggunaan.** rU>gL; risiko operasi stabil.

**Kekeliruan yang perlu dihindari.** Jangan memakai WACC setelah pajak dalam komponen VU lalu menambah shield.

**Contoh hitung.** FCFN 80, g 2%, rU 10%: HV 1.020.

```python
80*1.02/(.10-.02)
```
Hasil presisi mesin: `1020`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-26"></a>
## 21-26 — Nilai unlevered dua tahap

[PDF 896](../Financial_Management_Theory_and_Practice_15e.pdf#page=896)

$$
V_U=\sum_{t=1}^{N}\frac{FCF_t}{(1+r_U)^t}+\frac{HV_{U,N}}{(1+r_U)^N}
$$

**Variabel.** FCF eksplisit dan terminal tanpa efek bunga.

**Penurunan dan logika.** PV semua kas operasi menjadi basis APV.

**Syarat penggunaan.** Diskonto risiko operasi dan terminal konsisten.

**Kekeliruan yang perlu dihindari.** Hasil adalah nilai operasi tanpa leverage, bukan nilai saham levered.

**Contoh hitung.** N 2, FCF 70,80, HV 1.020, rU 10%: VU 972,727273.

```python
70/1.1+(80+1020)/1.1**2
```
Hasil presisi mesin: `972.727272727`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-27"></a>
## 21-27 — PV shield selama forecast CAPV

[PDF 896](../Financial_Management_Theory_and_Practice_15e.pdf#page=896)

$$
PV(TS_{1:N})=\sum_{t=1}^{N}\frac{TS_t}{(1+r_U)^t}
$$

**Variabel.** TSt: shield tahun t; rU dipakai dalam compressed APV.

**Penurunan dan logika.** Setiap shield eksplisit didiskontokan pada risiko operasi sesuai asumsi CAPV.

**Syarat penggunaan.** Formula tercetak berhenti pada N. Total shield yang berlanjut memerlukan terminal 21-28/29.

**Kekeliruan yang perlu dihindari.** Jangan menganggap jumlah finite ini seluruh nilai shield bila utang berlanjut sesudah N.

**Contoh hitung.** Shield 4 dan 5, rU 10%: PV 7,768595.

```python
4/1.1+5/1.1**2
```
Hasil presisi mesin: `7.76859504132`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-28"></a>
## 21-28 — Terminal tax shield

[PDF 896](../Financial_Management_Theory_and_Practice_15e.pdf#page=896)

$$
HV_{TS,N}=\frac{TS_N(1+g_L)}{r_U-g_L}
$$

**Variabel.** TSN: shield terakhir forecast; gL: pertumbuhan shield berikutnya.

**Penurunan dan logika.** Perpetuitas shield mulai N+1, berisiko seperti operasi pada CAPV.

**Syarat penggunaan.** rU>gL dan utang/shield tumbuh stabil.

**Kekeliruan yang perlu dihindari.** Pertumbuhan FCF tidak menjamin pertumbuhan shield jika kebijakan utang berubah.

**Contoh hitung.** TSN 5, g 2%, rU 10%: HV 63,75.

```python
5*1.02/(.10-.02)
```
Hasil presisi mesin: `63.75`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-21-29"></a>
## 21-29 — Seluruh PV shield CAPV

[PDF 896](../Financial_Management_Theory_and_Practice_15e.pdf#page=896)

$$
V_{TS}=\sum_{t=1}^{N}\frac{TS_t}{(1+r_U)^t}+\frac{HV_{TS,N}}{(1+r_U)^N}
$$

**Variabel.** VTS meliputi forecast dan seluruh shield setelah horizon.

**Penurunan dan logika.** Gabungkan 21-27 dan PV terminal 21-28; tambahkan keVU untuk mendapatkan VL.

**Syarat penggunaan.** Risk/timing shield konsisten dengan CAPV; tidak menambahkan manfaat pajak lain yang sama.

**Kekeliruan yang perlu dihindari.** Jangan langsung menjumlahkan HV pada N keVU pada 0.

**Contoh hitung.** N 2, TS 4,5, HV 63,75, rU 10%: VTS 60,454545.

```python
4/1.1+(5+63.75)/1.1**2
```
Hasil presisi mesin: `60.4545454545`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
