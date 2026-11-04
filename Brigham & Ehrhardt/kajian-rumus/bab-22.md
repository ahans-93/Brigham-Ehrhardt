# Bab 22: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../22-chapter.md)

## Navigasi

- [22-1: Biaya ekuitas merger CAPV](#rumus-22-1)
- [22-1a: Unlever biaya ekuitas merger](#rumus-22-1a)
- [22-2: Unlever/relever beta target](#rumus-22-2)
- [U-22-01: Sinergi dan NPV akuisisi](#rumus-u-22-01)

<a id="rumus-22-1"></a>
## 22-1 — Biaya ekuitas merger CAPV

[PDF 921](../Financial_Management_Theory_and_Practice_15e.pdf#page=921)

$$
r_L=r_U+(r_U-r_d)w_d/w_s
$$

**Variabel.** Model mengulang 21-16 dalam penilaian merger; leverage target harus dinyatakan.

**Penurunan dan logika.** Arus kas merger dipisahkan dari pendanaan; relasi risiko CAPV membantu mengestimasi rU.

**Syarat penggunaan.** Risiko bisnis target dan sinergi sesuai tingkat diskonto; bobot nilai pasar.

**Kekeliruan yang perlu dihindari.** Biaya ekuitas acquirer tidak otomatis tepat untuk seluruh target.

**Contoh hitung.** rU 11,8%, rd 9%, D/E 0,3/0,7: rL 13%.

```python
.118+(.118-.09)*.3/.7
```
Hasil presisi mesin: `0.13`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-22-1a"></a>
## 22-1a — Unlever biaya ekuitas merger

[PDF 921](../Financial_Management_Theory_and_Practice_15e.pdf#page=921)

$$
r_U=w_s r_L+w_d r_d
$$

**Variabel.** ws, wd: proporsi nilai pasar target.

**Penurunan dan logika.** Susun ulang 22-1 seperti 21-16a untuk mencari biaya risiko bisnis tanpa leverage.

**Syarat penggunaan.** CAPV; bobot berjumlah 1.

**Kekeliruan yang perlu dihindari.** Ini bukan WACC setelah pajak; substitusi rd(1-T) mengubah model.

**Contoh hitung.** ws 0,6983, wd 0,3017, rL 13%, rd 9%: rU 11,7932%.

```python
.6983*.13+.3017*.09
```
Hasil presisi mesin: `0.117932`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-22-2"></a>
## 22-2 — Unlever/relever beta target

[PDF 921](../Financial_Management_Theory_and_Practice_15e.pdf#page=921)

$$
\beta_L=\beta_U+(\beta_U-\beta_d)w_d/w_s
$$

**Variabel.** Beta target meliputi risiko operasi dan pembiayaan.

**Penurunan dan logika.** Relasi 21-17 diterapkan pada merger. Bentuk inverse: beta U=ws beta L+wd betad.

**Syarat penggunaan.** CAPV; beta utang nol hanya pendekatan.

**Kekeliruan yang perlu dihindari.** Sinergi dapat mempunyai risiko berbeda dari operasi target; jangan menyamakan beta tanpa analisis.

**Contoh hitung.** Beta L 1,2, betad 0,2, ws 0,7, wd 0,3: beta U 0,9.

```python
.7*1.2+.3*.2
```
Hasil presisi mesin: `0.9`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-22-01"></a>
## U-22-01 — Sinergi dan NPV akuisisi

[PDF 914](../Financial_Management_Theory_and_Practice_15e.pdf#page=914) · [PDF 915](../Financial_Management_Theory_and_Practice_15e.pdf#page=915) · [PDF 916](../Financial_Management_Theory_and_Practice_15e.pdf#page=916) · [PDF 917](../Financial_Management_Theory_and_Practice_15e.pdf#page=917)

$$
Synergy=V_{AB}-V_A-V_B,\quad NPV_A=Synergy-Premium-Costs
$$

**Variabel.** VA, VB: nilai standalone; premium: pembayaran di atas nilai standalone target.

**Penurunan dan logika.** Gabungan menciptakan nilai hanya jika PV kas inkremental melebihi transferpremium dan biaya integrasi/emisi.

**Syarat penggunaan.** Semua nilai tanggal sama, basis enterprise/equity konsisten; untukstockdeal masukkan kepemilikan pascamerger.

**Kekeliruan yang perlu dihindari.** Kenaikan EPS bukan bukti NPV positif.

**Contoh hitung.** Sinergi 50, premium 30, biaya 5: NPV 15.

```python
50-30-5
```
Hasil presisi mesin: `15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
