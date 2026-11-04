# Bab 12: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../12-chapter.md)

## Navigasi

- [12-1: Additional funds needed](#rumus-12-1)
- [12-2: Self-supporting growth rate](#rumus-12-2)
- [12-3: Penjualan pada kapasitas penuh](#rumus-12-3)
- [12-4: Target fixed-assets-to-sales](#rumus-12-4)
- [12-5: Kebutuhan aset tetap proyeksi](#rumus-12-5)

<a id="rumus-12-1"></a>
## 12-1 — Additional funds needed

[PDF 561](../Financial_Management_Theory_and_Practice_15e.pdf#page=561)

$$
AFN=(A_0^*/S_0)\Delta S-(L_0^*/S_0)\Delta S-M S_1(1-POR)
$$

**Variabel.** A*: aset yang bertambah bersama sales; L*: kewajiban spontan; M: net margin; POR: payout ratio.

**Penurunan dan logika.** Dana untuk tambahan aset dikurangi pembiayaan spontan dan tambahan retained earnings menghasilkan kebutuhan dana eksternal.

**Syarat penggunaan.** Rasio aset/sales, liability/sales, margin dan payout stabil; kapasitas serta biaya pendanaan belum menimbulkan perubahan yang diabaikan.

**Kekeliruan yang perlu dihindari.** AFN negatif adalah surplus dana model, bukan kebutuhan pinjaman negatif yang wajib dilaksanakan.

**Contoh hitung.** A*/S 0,6, L*/S 0,1,ΔS 100, S 1=1100, M 10%, POR 40% memberi AFN−16.

```python
.6*100-.1*100-.1*1100*(1-.4)
```
Hasil presisi mesin: `-16`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-12-2"></a>
## 12-2 — Self-supporting growth rate

[PDF 563](../Financial_Management_Theory_and_Practice_15e.pdf#page=563)

$$
g=\frac{M(1-POR)S_0}{A_0^*-L_0^*-M(1-POR)S_0}
$$

**Variabel.** g: pertumbuhan maksimum model tanpa tambahan modal eksternal; spontaneous liabilities tetap dapat naik.

**Penurunan dan logika.** Set AFN=0 pada 12-1, ganti ΔS=gS 0 dan S 1=(1+g)S 0, lalu kumpulkan suku g pada satu sisi.

**Syarat penggunaan.** Asumsi AFN berlaku dan denominator positif untuk solusi pertumbuhan positif yang finite.

**Kekeliruan yang perlu dihindari.** Ini berbeda dari sustainable growth berbasis leverage target dengan akses tambahan utang.

**Contoh hitung.** M 10%, retention 60%, S 01000, A*600, L*100 memberi g 13,636364%.

```python
(.1*.6*1000)/(600-100-.1*.6*1000)
```
Hasil presisi mesin: `0.136363636364`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-12-3"></a>
## 12-3 — Penjualan pada kapasitas penuh

[PDF 565](../Financial_Management_Theory_and_Practice_15e.pdf#page=565)

$$
Sales_{full}=Sales_{actual}/Utilization
$$

**Variabel.** Utilization: pecahan kapasitas yang sedang dipakai, misalnya 80%=0,8.

**Penurunan dan logika.** Jika actual sales=u×capacity sales, balik hubungan linear itu untuk mengestimasi sales pada kapasitas penuh.

**Syarat penggunaan.** Sales dan kapasitas diukur sebanding; 0<u≤1 dalam interpretasi dasar.

**Kekeliruan yang perlu dihindari.** Kapasitas produksi tidak selalu identik dengan kapasitas penjualan jika harga dan product mix berubah.

**Contoh hitung.** Sales 800 pada 80% kapasitas menghasilkan full-capacity sales 1000.

```python
800/.8
```
Hasil presisi mesin: `1000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-12-4"></a>
## 12-4 — Target fixed-assets-to-sales

[PDF 566](../Financial_Management_Theory_and_Practice_15e.pdf#page=566)

$$
(FA/Sales)_{target}=FA_{actual}/Sales_{full}
$$

**Variabel.** FA: aset tetap sesuai basis buku model.

**Penurunan dan logika.** Gunakan sales kapasitas penuh sebagai denominator agar kapasitas menganggur tidak dianggap kebutuhan aset tambahan permanen.

**Syarat penggunaan.** Teknologi dan intensitas aset tetap tidak berubah dalam proyeksi sederhana.

**Kekeliruan yang perlu dihindari.** Rasio FA/actual sales saat kapasitas belum penuh akan melebihkan kebutuhan aset target.

**Contoh hitung.** FA 200 dan full sales 1000 memberi target ratio 0,2.

```python
200/1000
```
Hasil presisi mesin: `0.2`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-12-5"></a>
## 12-5 — Kebutuhan aset tetap proyeksi

[PDF 566](../Financial_Management_Theory_and_Practice_15e.pdf#page=566)

$$
FA_{required}=(FA/Sales)_{target}\times Sales_{projected}
$$

**Variabel.** FArequired adalah stok aset yang dibutuhkan, bukan langsung CAPEX kas.

**Penurunan dan logika.** Kalikan intensitas aset target dengan tingkat sales yang direncanakan.

**Syarat penggunaan.** Periksa kapasitas yang sudah ada dan sifat investasi lumpy sebelum membeli aset.

**Kekeliruan yang perlu dihindari.** CAPEX tidak sama dengan required FA; kurangi stok aset tersedia dan rekonsiliasi depresiasi/disposal.

**Contoh hitung.** Target 0,2 dan projected sales 1200 memerlukan FA 240.

```python
.2*1200
```
Hasil presisi mesin: `240`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
