# Bab 19: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../19-chapter.md)

## Navigasi

- [19-1: Keuntungan bersih leasing](#rumus-19-1)
- [U-19-01: Kas lease setelah pajak dan ownership](#rumus-u-19-01)

<a id="rumus-19-1"></a>
## 19-1 — Keuntungan bersih leasing

[PDF 838](../Financial_Management_Theory_and_Practice_15e.pdf#page=838)

$$
NAL=PV(CF_{lease})-PV(CF_{own})
$$

**Variabel.** CFlease, CFown: arus kas bertanda dari perspektif lessee; NAL: net advantage to leasing.

**Penurunan dan logika.** Bandingkan alternatif yang memberi jasa aset sama. NAL positif berarti biaya kas neto leasing lebih kecil dalam PV.

**Syarat penggunaan.** Arus kas setelah pajak, waktu sewa dibayar di muka/akhir sesuai kontrak; tingkat diskonto menyesuaikan risiko tiap komponen.

**Kekeliruan yang perlu dihindari.** Buku memakai PV biaya negatif. Jika memakai biaya positif, urutannya harus PVcostown-PVcostlease.

**Contoh hitung.** PVlease−60,50 dan PVown−63,33: NAL+2,83.

```python
-60.50-(-63.33)
```
Hasil presisi mesin: `2.83`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-19-01"></a>
## U-19-01 — Kas lease setelah pajak dan ownership

[PDF 834](../Financial_Management_Theory_and_Practice_15e.pdf#page=834) · [PDF 835](../Financial_Management_Theory_and_Practice_15e.pdf#page=835) · [PDF 836](../Financial_Management_Theory_and_Practice_15e.pdf#page=836) · [PDF 837](../Financial_Management_Theory_and_Practice_15e.pdf#page=837) · [PDF 838](../Financial_Management_Theory_and_Practice_15e.pdf#page=838)

$$
CF_{lease,t}=-L_t(1-T),\quad CF_{own,t}=-Maint_t(1-T)+TDep_t
$$

**Variabel.** Lt: sewa yang deductible; Dep: depresiasi pajak; Maint: pemeliharaan incremental.

**Penurunan dan logika.** Lessee mendapat shield atas sewa bila deductible. Pemilik mendapat shield depresiasi danmenanggung pemeliharaan; tambahkan harga beli awal danresidu sesuai timeline.

**Syarat penggunaan.** Contoh pajak/lease sumber historis; kontrak aktual danperpajakan menentukan deductible.

**Kekeliruan yang perlu dihindari.** Jika lessor menanggung pemeliharaan, jangan membebankannya pada alternatif lease lagi.

**Contoh hitung.** Sewa 20, T 25%: kas setelah pajak−15.

```python
-20*(1-.25)
```
Hasil presisi mesin: `-15`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
