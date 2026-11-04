# Bab 23: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../23-chapter.md)

Tidak ditemukan persamaan dengan nomor bab-persamaan pada isi bab ini. Keluarga/formalisasi tambahan di bawah menghubungkan pembahasan dengan perhitungannya.

## Navigasi

- [U-23-01: Forward/futures payoff dasar](#rumus-u-23-01)
- [U-23-02: Jumlah kontrak hedge dan basis](#rumus-u-23-02)
- [U-23-03: Interest-rate swap net settlement](#rumus-u-23-03)
- [U-23-04: Expected loss dan insurance retention](#rumus-u-23-04)

<a id="rumus-u-23-01"></a>
## U-23-01 — Forward/futures payoff dasar

[PDF 953](../Financial_Management_Theory_and_Practice_15e.pdf#page=953) · [PDF 954](../Financial_Management_Theory_and_Practice_15e.pdf#page=954) · [PDF 955](../Financial_Management_Theory_and_Practice_15e.pdf#page=955) · [PDF 956](../Financial_Management_Theory_and_Practice_15e.pdf#page=956) · [PDF 957](../Financial_Management_Theory_and_Practice_15e.pdf#page=957)

$$
Payoff_{long}=Q(S_T-K),\quad Payoff_{short}=Q(K-S_T)
$$

**Variabel.** Q: jumlah underlying; K: harga kontrak; ST: harga settlement.

**Penurunan dan logika.** Long membeli pada harga kontrak; keuntungan dibanding harga pasar adalah ST-K per unit. Short kebalikannya.

**Syarat penggunaan.** Payoff forward saat maturity; futures memiliki mark-to-market sehingga timing kas danreinvestment dapat berbeda.

**Kekeliruan yang perlu dihindari.** Margin bukan harga beli seluruh underlying danbukan batas maksimum kerugian.

**Contoh hitung.** Long 100 unit, K 50, ST 55: untung 500.

```python
100*(55-50)
```
Hasil presisi mesin: `500`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-23-02"></a>
## U-23-02 — Jumlah kontrak hedge dan basis

[PDF 957](../Financial_Management_Theory_and_Practice_15e.pdf#page=957) · [PDF 958](../Financial_Management_Theory_and_Practice_15e.pdf#page=958) · [PDF 959](../Financial_Management_Theory_and_Practice_15e.pdf#page=959) · [PDF 960](../Financial_Management_Theory_and_Practice_15e.pdf#page=960) · [PDF 961](../Financial_Management_Theory_and_Practice_15e.pdf#page=961)

$$
N=Q_{exposure}/q_{contract},\quad Basis=S-F
$$

**Variabel.** qcontract: jumlah unit per kontrak; basis: spot dikurangifutures menurutkonvensi ini.

**Penurunan dan logika.** Cocokkan volume yang akan dibeli/dijual denganunit kontrak; hedge dapat mengurangi perubahan spot tetapi menyisakan perubahan basis.

**Syarat penggunaan.** Ini hedge satu-banding-satu untuk underlying danperiode cocok; crosshedge memerlukan rasio risiko tambahan.

**Kekeliruan yang perlu dihindari.** Pembeli komoditas biasanya long hedge; penjual short hedge. Jangan membalik arah.

**Contoh hitung.** Eksposur 10.000 unit, kontrak 1.000: 10 kontrak.

```python
10000/1000
```
Hasil presisi mesin: `10`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-23-03"></a>
## U-23-03 — Interest-rate swap net settlement

[PDF 964](../Financial_Management_Theory_and_Practice_15e.pdf#page=964) · [PDF 965](../Financial_Management_Theory_and_Practice_15e.pdf#page=965) · [PDF 966](../Financial_Management_Theory_and_Practice_15e.pdf#page=966) · [PDF 967](../Financial_Management_Theory_and_Practice_15e.pdf#page=967) · [PDF 968](../Financial_Management_Theory_and_Practice_15e.pdf#page=968) · [PDF 969](../Financial_Management_Theory_and_Practice_15e.pdf#page=969)

$$
Net_{payfixed}=Notional\,(r_{float}-r_{fixed})\Delta t
$$

**Variabel.** Net positif: penerimaan bersih pihak bayarfixed/terima floating; notional umumnya tidak ditukar.

**Penurunan dan logika.** Kurangi pembayaran tetap dari penerimaanfloating pada periode yang sama.

**Syarat penggunaan.** Daycount, reset, danpayment dates mengikuti kontrak; ini settlement periode, bukan valuasi PV swap.

**Kekeliruan yang perlu dihindari.** Floatingrate dipatok pada reset date, tidak selalu rate spot pada payment date.

**Contoh hitung.** Notional 1 juta, floating 6%, fixed 5%, halfyear: menerima 5.000.

```python
1000000*(.06-.05)*.5
```
Hasil presisi mesin: `5000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-23-04"></a>
## U-23-04 — Expected loss dan insurance retention

[PDF 970](../Financial_Management_Theory_and_Practice_15e.pdf#page=970) · [PDF 971](../Financial_Management_Theory_and_Practice_15e.pdf#page=971) · [PDF 972](../Financial_Management_Theory_and_Practice_15e.pdf#page=972) · [PDF 973](../Financial_Management_Theory_and_Practice_15e.pdf#page=973)

$$
E[Loss]=\sum_s p_sL_s,\quad RetainedLoss=\min(L,Deductible)
$$

**Variabel.** L: kerugian; deductible: bagian ditanggung tertanggung pada kontrak sederhana.

**Penurunan dan logika.** Expectedloss adalah mean probabilitas; perusahaan membandingkan premi dengan transfer risiko dan friksi, bukan sekadar rata-rata.

**Syarat penggunaan.** Ini formalisasi pembahasan risk management; polis aktual mempunyai limit, exclusions, dan coinsurance.

**Kekeliruan yang perlu dihindari.** Premi wajar tidak harus samaexpected loss karena beban, modal, danrisiko insurer.

**Contoh hitung.** Peluang 2% rugi 100.000: expected loss 2.000.

```python
.02*100000
```
Hasil presisi mesin: `2000`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
