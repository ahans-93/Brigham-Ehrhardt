# Bab 1: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../01-chapter.md)

## Navigasi

- [1-1: Nilai operasi sebagai PV arus kas](#rumus-1-1)

<a id="rumus-1-1"></a>
## 1-1 — Nilai operasi sebagai PV arus kas

[PDF 47](../Financial_Management_Theory_and_Practice_15e.pdf#page=47)

$$
V_{op,0}=\sum_{t=1}^{\infty}\frac{FCF_t}{(1+WACC)^t}
$$

**Variabel.** FCFt: kas bebas operasi pada akhir t; WACC: required return gabungan penyedia modal per periode; Vop: nilai operasi hari ini.

**Penurunan dan logika.** Nilai sebuah klaim adalah penjumlahan nilai sekarang pembayaran yang mendasarinya. FCF ditentukan sebelum distribusi bunga/dividen, sehingga memakai biaya modal gabungan. Bila FCF konstan, deret geometri menjadi FCF/WACC.

**Syarat penggunaan.** WACC konstan, risiko dan kebijakan pendanaan sesuai, arus kas setelah pajak operasi; deret harus konvergen. Untuk risiko/leverage berubah, gunakan discount factor per periode atau APV.

**Kekeliruan yang perlu dihindari.** Nilai operasi bukan nilai ekuitas. Notasi FCF∞/(1+WACC)^∞ pada buku merupakan singkatan deret berlanjut, bukan satu kas yang ditambahkan pada waktu tak hingga.

**Contoh hitung.** Perpetuitas FCF 100 per tahun, WACC 10%: nilai operasi 1.000.

```python
100/0.10
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
