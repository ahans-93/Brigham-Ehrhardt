# Bab 13: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../13-chapter.md)

Tidak ditemukan persamaan dengan nomor bab-persamaan pada isi bab ini. Keluarga/formalisasi tambahan di bawah menghubungkan pembahasan dengan perhitungannya.

## Navigasi

- [U-13-01: Nilai insentif saham danopsi](#rumus-u-13-01)

<a id="rumus-u-13-01"></a>
## U-13-01 — Nilai insentif saham danopsi

[PDF 588](../Financial_Management_Theory_and_Practice_15e.pdf#page=588) · [PDF 589](../Financial_Management_Theory_and_Practice_15e.pdf#page=589) · [PDF 590](../Financial_Management_Theory_and_Practice_15e.pdf#page=590) · [PDF 591](../Financial_Management_Theory_and_Practice_15e.pdf#page=591) · [PDF 592](../Financial_Management_Theory_and_Practice_15e.pdf#page=592) · [PDF 593](../Financial_Management_Theory_and_Practice_15e.pdf#page=593)

$$
V_{stock}=nS,\quad Payoff_{options}=n\max(S_T-K,0)
$$

**Variabel.** n: unit kompensasi; S: harga saham; K: strike; ST: harga tanggalexercise.

**Penurunan dan logika.** Saham memberi eksposur linear; opsi memberi payoff konveks sehingga sensitivitas risiko/manajerial berbeda.

**Syarat penggunaan.** Ini representasi matematis atas pembahasan kompensasi, bukan persamaan bernomor baru dari buku; vesting danforfeiture perlu dimodelkan.

**Kekeliruan yang perlu dihindari.** Payoff akhir opsi bukan nilai wajar opsi saat hibah; jangan menyamakannya dengan biaya kompensasi akuntansi.

**Contoh hitung.** 100 opsi, K 20, ST 30: payoff 1.000.

```python
100*max(30-20,0)
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
