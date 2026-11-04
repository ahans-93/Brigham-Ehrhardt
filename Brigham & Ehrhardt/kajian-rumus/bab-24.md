# Bab 24: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../24-chapter.md)

Tidak ditemukan persamaan dengan nomor bab-persamaan pada isi bab ini. Keluarga/formalisasi tambahan di bawah menghubungkan pembahasan dengan perhitungannya.

## Navigasi

- [U-24-01: Distribusi sederhana liquidation waterfall](#rumus-u-24-01)
- [U-24-02: Recovery rate dan reorganisasi](#rumus-u-24-02)

<a id="rumus-u-24-01"></a>
## U-24-01 — Distribusi sederhana liquidation waterfall

[PDF 997](../Financial_Management_Theory_and_Practice_15e.pdf#page=997) · [PDF 998](../Financial_Management_Theory_and_Practice_15e.pdf#page=998) · [PDF 999](../Financial_Management_Theory_and_Practice_15e.pdf#page=999) · [PDF 1000](../Financial_Management_Theory_and_Practice_15e.pdf#page=1000) · [PDF 1001](../Financial_Management_Theory_and_Practice_15e.pdf#page=1001)

$$
Payment_j=\min(Claim_j,\max(RemainingBefore_j,0))
$$

**Variabel.** Claimj: tagihan kelas j; urutan dimulai dari prioritas tertinggi sesuai asumsi contoh.

**Penurunan dan logika.** Bayar klaim senior terlebih dahulu, kurangi aset tersedia, lalu lanjutkan kelas berikutnya; equity menerima residu.

**Syarat penggunaan.** Ini aritmetika contoh terstruktur, bukan pernyataan hukum prioritas aktual. Collateral, biaya, danurutan resmi sumber harus diterapkan tersendiri.

**Kekeliruan yang perlu dihindari.** Jangan membagi aset prorata ke semua kreditur jika tingkat prioritas berbeda.

**Contoh hitung.** Aset 80, klaim senior 60, junior 40: senior 60, junior 20, equity 0.

```python
min(40,max(80-60,0))
```
Hasil presisi mesin: `20`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-24-02"></a>
## U-24-02 — Recovery rate dan reorganisasi

[PDF 990](../Financial_Management_Theory_and_Practice_15e.pdf#page=990) · [PDF 991](../Financial_Management_Theory_and_Practice_15e.pdf#page=991) · [PDF 992](../Financial_Management_Theory_and_Practice_15e.pdf#page=992) · [PDF 993](../Financial_Management_Theory_and_Practice_15e.pdf#page=993) · [PDF 994](../Financial_Management_Theory_and_Practice_15e.pdf#page=994) · [PDF 995](../Financial_Management_Theory_and_Practice_15e.pdf#page=995) · [PDF 999](../Financial_Management_Theory_and_Practice_15e.pdf#page=999) · [PDF 1000](../Financial_Management_Theory_and_Practice_15e.pdf#page=1000)

$$
Recovery=Payment/Claim,\quad GoingConcernValue=PV(FCF)
$$

**Variabel.** Payment: nilai distribusi ke kelas klaim; nilai saham/utang baru dinilai pasar/PV, bukan sematan nominal.

**Penurunan dan logika.** Bandingkan nilai going concern bersih dengan liquidation bersih. Recovery mengukur proporsi klaim yang dipulihkan.

**Syarat penggunaan.** Tanggal nilai dan biaya reorganisasi konsisten; prioritas dan persetujuan hukum di luar aritmetika ini.

**Kekeliruan yang perlu dihindari.** Mengganti utang 100 dengan saham nominal 100 tidak membuktikan recovery 100%.

**Contoh hitung.** Klaim 40, menerima nilai 20: recovery 50%.

```python
20/40
```
Hasil presisi mesin: `0.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
