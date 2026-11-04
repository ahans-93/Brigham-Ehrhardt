# Bab 26: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../26-chapter.md)

## Navigasi

- [26-1: Mengubah CV nilai proyek menjadi varians log return](#rumus-26-1)
- [26-1a: Substitusi CV contoh proyek](#rumus-26-1a)
- [U-26-01: Nilai opsi riil incremental](#rumus-u-26-01)

<a id="rumus-26-1"></a>
## 26-1 — Mengubah CV nilai proyek menjadi varians log return

[PDF 1062](../Financial_Management_Theory_and_Practice_15e.pdf#page=1062)

$$
\sigma^2=\frac{\ln(1+CV^2)}{t}
$$

**Variabel.** CV: SD nilai proyek pada tanggal opsi dibagi expected value; t: tahun sampai exercise; sigma²: varians log return per tahun.

**Penurunan dan logika.** Untuk Vt lognormal, Var(Vt)/E[Vt]²=exp(sigma²t)-1. Ambil ln dan bagi t.

**Syarat penggunaan.** Nilai positif, distribusi lognormal/GBM sebagai pendekatan, t>0, dan CV berasal dari distribusi pada tanggal yang sama.

**Kekeliruan yang perlu dihindari.** Sigma nilai rupiah bukan volatilitas return; jangan memasukkan SD proyek dalam mata uang langsung ke Black-Scholes.

**Contoh hitung.** CV 0,47, t 1: sigma²0,19958829 dan sigma 44,6753%.

```python
log(1+.47**2)
```
Hasil presisi mesin: `0.199588291693`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-26-1a"></a>
## 26-1a — Substitusi CV contoh proyek

[PDF 1062](../Financial_Management_Theory_and_Practice_15e.pdf#page=1062)

$$
\sigma^2=\ln(1+0.47^2)/1\approx0.20
$$

**Variabel.** CV 47% dan horizon 1 tahun adalah data contoh, bukan parameter universal real option.

**Penurunan dan logika.** Gunakan 26-1; pembulatan dua desimal menjelaskan 0,20 pada sumber.

**Syarat penggunaan.** Nilai dibulatkan hanya setelah transformasi; sigma=sqrt(varians).

**Kekeliruan yang perlu dihindari.** Angka 0,20 adalah varians tahunan; volatilitas sekitar 0,447, bukan 20%.

**Contoh hitung.** Dengan CV 0,47, simpangan baku logreturn 44,6753%.

```python
sqrt(log(1+.47**2))
```
Hasil presisi mesin: `0.446753054486`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-26-01"></a>
## U-26-01 — Nilai opsi riil incremental

[PDF 1054](../Financial_Management_Theory_and_Practice_15e.pdf#page=1054) · [PDF 1055](../Financial_Management_Theory_and_Practice_15e.pdf#page=1055) · [PDF 1056](../Financial_Management_Theory_and_Practice_15e.pdf#page=1056) · [PDF 1057](../Financial_Management_Theory_and_Practice_15e.pdf#page=1057) · [PDF 1063](../Financial_Management_Theory_and_Practice_15e.pdf#page=1063) · [PDF 1064](../Financial_Management_Theory_and_Practice_15e.pdf#page=1064)

$$
ExpandedNPV=StaticNPV+ValueOfFlexibility
$$

**Variabel.** Flexibility: hak menunda, meluaskan, menghentikan, atau mengganti operasi yang belum masuk static NPV.

**Penurunan dan logika.** Hak memilih aksi setelah informasi baru dapat membuang cabang negatif. Dalam decision tree, nilai tiap node=max(nilai aksi yang tersedia), lalu backward induction.

**Syarat penggunaan.** Probabilitas/diskonto harus konsisten; BS untuk proyek nyata adalahpendekatan, bukan replikasi sempurna ketika aset tidak diperdagangkan.

**Kekeliruan yang perlu dihindari.** Jangan menambahkan option value jika flexible actions sudah dimasukkan ke skenario FCF awal.

**Contoh hitung.** Static NPV−5, value flexibility 12: expanded NPV 7.

```python
-5+12
```
Hasil presisi mesin: `7`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
