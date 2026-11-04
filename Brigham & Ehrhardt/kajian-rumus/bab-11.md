# Bab 11: kajian rumus

[Indeks kajian](README.md) · [Teks sumber](../11-chapter.md)

Tidak ditemukan persamaan dengan nomor bab-persamaan pada isi bab ini. Keluarga/formalisasi tambahan di bawah menghubungkan pembahasan dengan perhitungannya.

## Navigasi

- [U-11-01: Kas operasi inkremental](#rumus-u-11-01)
- [U-11-02: Kas awal proyek danreplacement](#rumus-u-11-02)
- [U-11-03: Salvage setelah pajak](#rumus-u-11-03)
- [U-11-04: Kas akhir proyek](#rumus-u-11-04)
- [U-11-05: Risiko skenario NPV](#rumus-u-11-05)
- [U-11-06: Inflasi dalam proyeksi proyek](#rumus-u-11-06)

<a id="rumus-u-11-01"></a>
## U-11-01 — Kas operasi inkremental

[PDF 491](../Financial_Management_Theory_and_Practice_15e.pdf#page=491) · [PDF 492](../Financial_Management_Theory_and_Practice_15e.pdf#page=492) · [PDF 497](../Financial_Management_Theory_and_Practice_15e.pdf#page=497) · [PDF 498](../Financial_Management_Theory_and_Practice_15e.pdf#page=498)

$$
OCF=(\Delta Sales-\Delta CashCosts)(1-T)+T\Delta Dep
$$

**Variabel.** Delta: perbedaan dengan dan tanpa proyek; Dep: depresiasi fiskal yang berpengaruh pada pajak.

**Penurunan dan logika.** Mulai dari EBIT=(sales-cashcosts-dep). OCF=EBIT(1-T)+Dep, sehingga Dep menyumbang tax shield TDep.

**Syarat penggunaan.** Pajak marginal dan manfaat rugi tersedia; abaikan bunga untuk FCF proyek.

**Kekeliruan yang perlu dihindari.** Sunk cost tidak inkremental; opportunity cost dan cannibalization yang nyata harus masuk.

**Contoh hitung.** Sales 100, cashcosts 60, Dep 10, T 25%: OCF 32,5.

```python
(100-60)*(1-.25)+.25*10
```
Hasil presisi mesin: `32.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-11-02"></a>
## U-11-02 — Kas awal proyek danreplacement

[PDF 491](../Financial_Management_Theory_and_Practice_15e.pdf#page=491) · [PDF 493](../Financial_Management_Theory_and_Practice_15e.pdf#page=493) · [PDF 494](../Financial_Management_Theory_and_Practice_15e.pdf#page=494) · [PDF 497](../Financial_Management_Theory_and_Practice_15e.pdf#page=497)

$$
CF_0=-InstalledCost-\Delta NOWC+AfterTaxSaleOld
$$

**Variabel.** Installed Cost: harga, pengiriman, dan instalasi yang relevan; NOWC: modal kerja operasi neto.

**Penurunan dan logika.** Kas keluar aset baru dan modal kerja ditambah penerimaan bersih menjual aset lama; bandingkan alternatif mempertahankan aset.

**Syarat penggunaan.** Seluruh komponen pada tanggal awal dan benar-benar inkremental.

**Kekeliruan yang perlu dihindari.** Nilai buku aset lama bukan kas keluar baru; hanya mempengaruhi pajak penjualan.

**Contoh hitung.** Biaya 120, delta NOWC 10, penjualan lama neto 30: CF 0−100.

```python
-120-10+30
```
Hasil presisi mesin: `-100`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-11-03"></a>
## U-11-03 — Salvage setelah pajak

[PDF 499](../Financial_Management_Theory_and_Practice_15e.pdf#page=499) · [PDF 500](../Financial_Management_Theory_and_Practice_15e.pdf#page=500)

$$
ATSV=SV-T(SV-BV)
$$

**Variabel.** SV: harga jual kas; BV: basis pajak tersisa; T: tarif efektif atas laba/rugi penjualan dalam model.

**Penurunan dan logika.** Laba kena pajak=SV-BV. Kurangi pajak laba atau tambahkan manfaat rugi jika benar-benar dapat digunakan.

**Syarat penggunaan.** Perlakuan recapture/capital gain disederhanakan; gunakan peraturan aktual jika menerapkan kasus nyata.

**Kekeliruan yang perlu dihindari.** Pajak bukan T*SV jika basis buku fiskal belum nol.

**Contoh hitung.** SV 50, BV 20, T 25%: ATSV 42,5.

```python
50-.25*(50-20)
```
Hasil presisi mesin: `42.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-11-04"></a>
## U-11-04 — Kas akhir proyek

[PDF 498](../Financial_Management_Theory_and_Practice_15e.pdf#page=498) · [PDF 499](../Financial_Management_Theory_and_Practice_15e.pdf#page=499)

$$
CF_N=OCF_N+ATSV+NOWC_{released}
$$

**Variabel.** NOWCreleased: kas yang benar-benar pulih dari modal kerja pada penghentian.

**Penurunan dan logika.** Kas operasi terakhir ditambah penjualan aset dan penutupan saldo persediaan/piutang/utang operasi.

**Syarat penggunaan.** Pemulihan tidak otomatis 100%; sesuaikan collectability dan kewajiban penutupan.

**Kekeliruan yang perlu dihindari.** Jangan menghitung pemulihan NOWC dua kali melalui delta NOWC negatif dan tambahan terminal terpisah.

**Contoh hitung.** OCF 30, ATSV 42,5, pemulihan 10: kas 82,5.

```python
30+42.5+10
```
Hasil presisi mesin: `82.5`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-11-05"></a>
## U-11-05 — Risiko skenario NPV

[PDF 508](../Financial_Management_Theory_and_Practice_15e.pdf#page=508) · [PDF 509](../Financial_Management_Theory_and_Practice_15e.pdf#page=509) · [PDF 510](../Financial_Management_Theory_and_Practice_15e.pdf#page=510)

$$
E[NPV]=\sum_s p_sNPV_s,\quad \sigma^2_{NPV}=\sum_s p_s(NPV_s-E[NPV])^2
$$

**Variabel.** ps: probabilitas skenario lengkap; jumlahps 1; NPV dinilai memakai arus kas skenario.

**Penurunan dan logika.** Aplikasikan definisi mean danvarians pada distribusi NPV, bukan pada return saham.

**Syarat penggunaan.** Skenario mutually exclusive dancollectively exhaustive; ini population variance berbobot probabilitas.

**Kekeliruan yang perlu dihindari.** Jangan membagi varians skenario dengan N-1; aturan itu untuk estimasi sampel historis.

**Contoh hitung.** NPV−10,20,50 dengan probabilitas 0,25/0,5/0,25: mean 20, varians 450.

```python
.25*(-10-20)**2+.5*(20-20)**2+.25*(50-20)**2
```
Hasil presisi mesin: `450`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).

<a id="rumus-u-11-06"></a>
## U-11-06 — Inflasi dalam proyeksi proyek

[PDF 501](../Financial_Management_Theory_and_Practice_15e.pdf#page=501) · [PDF 502](../Financial_Management_Theory_and_Practice_15e.pdf#page=502)

$$
CF_{nom,t}=CF_{real,t}(1+\pi)^t,\quad 1+r_{nom}=(1+r_{real})(1+\pi)
$$

**Variabel.** CFreal: kas pada daya beli tahun dasar; pi: inflasi seragam dalam contoh.

**Penurunan dan logika.** Deflator yang sama pada kas danfaktor diskonto saling menghapus, sehingga PV nominal danreal identik.

**Syarat penggunaan.** Depresiasi fiskal danharga relatif dapat tidak meningkat dengan inflasi yang sama.

**Kekeliruan yang perlu dihindari.** Mendiskontokan kas nominal pada tingkatreal membesarkan nilai.

**Contoh hitung.** Kasreal 100 pada tahun 2, inflasi 4%, rreal 6%: PV 88,999644.

```python
100*1.04**2/(1.06*1.04)**2
```
Hasil presisi mesin: `88.9996440014`. Toleransi dan nilai pembanding tersedia di [hasil verifikasi](verification-results.json).
