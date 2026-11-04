# Catatan kritis, derivasi penghubung, dan konvensi

[Indeks kajian](README.md). Sumber tetap PDF edisi 15e yang diarsipkan di repository. Catatan di bawah membedakan bentuk cetak, interpretasi ekonomi, dan perubahan bentuk aljabar. Penandaan potensi masalah cetak adalah hasil pemeriksaan penyusun, bukan errata resmi penerbit.

## 1. Net cash flow, CFO, FCF, dan FCFE

Persamaan 2-1 membalik pendapatan/beban nonkas dari laba. Persamaan 2-2 memakai pendekatan NI + depresiasi + amortisasi. Hasil ini tidak otomatis sama dengan arus kas operasi pada laporan arus kas: perubahan piutang, persediaan, utang operasi, dan komponen lain belum tentu sudah masuk.

Untuk kas bebas operasi, jalurnya adalah:

$$FCF=EBIT(1-T)+Dep-CAPEX-\Delta NOWC.$$

Karena perubahan aset operasi jangka panjang neto adalah CAPEX − Dep, rumus ini juga menjadi:

$$FCF=NOPAT-\Delta K_{op}.$$

Kemudian kas yang tersedia bagi common equity, pada model tanpa preferred dan komponen nonoperasi tambahan, adalah:

$$FCFE=FCF-I(1-T)+\Delta D_{cash}.$$

Perubahan utang di sini harus mewakili kas utang baru dikurangi pembayaran pokok; perubahan saldo akibat kurs atau transaksi nonkas tidak otomatis boleh dimasukkan. FCF didiskontokan dengan WACC yang sesuai; FCFE dengan biaya ekuitas. Nilai hasil FCFE sudah merupakan nilai ekuitas, sehingga utang tidak dikurangkan lagi.

## 2. Label modal pada 2-7 dan rasio pada 2-12a

- **2-7, PDF 111:** rekonsiliasi yang masuk akal adalah modal investor yang digunakan dalam operasi = total modal investor − investasi jangka pendek nonoperasi. Pembacaan literal salah satu label cetak dapat tampak mengurangkan investasi dari modal operasi yang sama di kedua sisi. Contoh 2.530 − 40 = 2.490 menjelaskan maksud rekonsiliasinya. Kajian memakai notasi yang tidak berputar: $K_{inv,op}=K_{inv}-STI_{nonop}$.
- **2-12a, PDF 116:** substitusi 3.050/5.000 = 61% adalah **capital requirement ratio (CR)**. Cetakan menampilkan label OP pada substitusi tersebut, sedangkan OP pada 2-11a adalah 300/5.000 = 6%. Kajian mempertahankan angka sumber dan menjelaskan pembetulan labelnya.

## 3. Periode bunga, tanda kas, dan batas formula

Untuk kupon semester: kupon tahunan dibagi dua, nominal yield dibagi dua, dan jumlah tahun dikali dua. EAR tidak boleh dibagi dua untuk memperoleh bunga semester; bunga efektif semester adalah $(1+EAR)^{1/2}-1$.

Persamaan kalkulator memakai kas masuk dan keluar bertanda berlawanan. Dalam perhitungan PI, biaya awal pada penyebut adalah besaran positif, yaitu $-CF_0$ bila kas awal ditulis negatif. Dalam NAL, sumber memakai PV biaya sebagai kas negatif: −60,50 − (−63,33) = +2,83, sehingga leasing lebih menguntungkan sebesar 2,83 dalam asumsi contoh.

Pada bunga nol, faktor anuitas bernilai N, bukan pembagian 0/0. Pada growing annuity dengan r = g, gunakan batas $N\,CF_1/(1+r)$. Perpetuitas tumbuh memerlukan r > g pada model biasa. Nilai terminal berada pada akhir forecast N dan dimulai dari kas N+1.

## 4. State prices bukan probabilitas biasa — 8-4/8-5

Untuk satu langkah binomial, dengan faktor kenaikan u, penurunan d, dan akumulasi bebas risiko R:

$$q=\frac{R-d}{u-d},\qquad \pi_u=\frac qR,\qquad \pi_d=\frac{1-q}R.$$

q adalah probabilitas risk-neutral; $\pi_u,\pi_d$ adalah harga sekarang satu unit kas yang hanya dibayar dalam masing-masing keadaan. Karena itu:

$$q+(1-q)=1,\qquad \pi_u+\pi_d=1/R.$$

Opsi dapat dihitung dengan $[qC_u+(1-q)C_d]/R$ atau $C_u\pi_u+C_d\pi_d$. Menggunakan state prices lalu membaginya dengan R lagi mendiskontokan dua kali. Untuk u = 1,2, d = 0,8, R = 1,05, Cu = 20, Cd = 0, kedua cara memberi 11,9047619. Portofolio replikasi dengan delta 0,5 dan pinjaman PV sebesar 40/1,05 menghasilkan nilai yang sama.

## 5. ROIC, pertumbuhan, dan nilai operasi — 7-13/7-15

Dengan modal operasi akhir T sebesar K dan ROIC yang diukur atas modal periode T seperti dalam model sumber, laba operasi tahun berikutnya adalah $(1+g)ROIC\,K$. Tambahan modal yang diperlukan adalah gK. Maka:

$$FCF_{T+1}=[(1+g)ROIC-g]K,$$

$$V_T=K\frac{(1+g)ROIC-g}{WACC-g}
=K\left[1+\frac{(1+g)ROIC-WACC}{WACC-g}\right].$$

Jika ROIC dihitung dengan modal awal tahun, hubungan FCF dengan reinvestasi memiliki timing berbeda. Jangan mengganti definisi ROIC di tengah derivasi. Identitas OP/CR = ROIC memerlukan basis modal yang sama pada kedua rasio.

## 6. Hamada, APV, dan compressed APV

Identitas risiko umum untuk klaim ekuitas dan utang adalah:

$$r_EE+r_DD=r_UV_U+r_{TS}V_{TS},\qquad V_U=E+D-V_{TS}.$$

Dengan menyusun ulang:

$$r_E=r_U+(r_U-r_D)D/E-(r_U-r_{TS})V_{TS}/E.$$

Identitas beta mempunyai bentuk analog:

$$\beta_E=\beta_U+(\beta_U-\beta_D)D/E-(\beta_U-\beta_{TS})V_{TS}/E.$$

Tiga kasus harus dipisahkan:

| Asumsi | Nilai shield/relasi | Implikasi |
|---|---|---|
| MM tanpa pajak | VTS = 0 | Tambahan risiko ekuitas tidak dikurangi shield |
| MM pajak, utang tetap permanen | rTS = rd, VTS = TD | Biaya ekuitas memuat faktor (1−T); Hamada juga memerlukan beta utang diabaikan |
| Compressed APV | rTS = rU dan betaTS = betaU | Suku terakhir identitas risiko hilang; biaya ekuitas dan beta relever tidak memuat faktor (1−T), meskipun VTS positif |

**Timing 21-6 sampai 21-8 perlu dinyatakan.** Pada 21-6/7, sumber menuliskan D0(1+g) untuk basis shield tahun pertama. Pada 21-8, koefisien shield/leverage ditulis rdT/(rTS−g) tanpa faktor 1+g. Implementasi yang memakai D0 dari 21-6 sebagai D dalam rasio D/E harus merekonsiliasi faktor tersebut. Gunakan identitas umum dengan VTS/E yang dihitung eksplisit untuk menghindari pencampuran timing. Untuk g = 0, masalah faktor timing hilang.

Pada 21-27, jumlah yang berhenti pada N hanya mencakup shield selama forecast. Bila shield berlanjut, tambahkan PV terminal melalui 21-28/29. Jangan menyebut jumlah forecast saja sebagai nilai seluruh shield.

## 7. Risiko total, risiko pasar, dan nilai absolut

$$\sigma_i^2=\beta_i^2\sigma_M^2+\sigma_e^2.$$

Untuk portofolio yang cukup terdiversifikasi, residual dapat mendekati nol sehingga $\sigma_p\approx|\beta_p|\sigma_M$. Bentuk tanpa nilai absolut hanya cocok ketika beta portofolio nonnegatif. Pada 25-2b, akar $(1-w_{RF})^2$ juga menghasilkan nilai absolut. SD negatif tidak mempunyai arti.

Bobot minimum varians pada 25-3 adalah solusi tanpa pembatasan short selling. Jika hanya bobot 0–1 diizinkan, periksa batasnya. CML memakai SD total untuk kombinasi efisien pasar dan aset bebas risiko; SML memakai beta untuk aset atau portofolio dalam CAPM. Keduanya tidak dapat ditukar.

## 8. Koefisien adjusted beta tercetak — 25-16

Pada PDF 1039 (cetak 1002), persamaan menampilkan:

$$\beta_{adj,printed}=0.67\beta_{historical}+0.35(1.0).$$

Koefisiennya berjumlah 1,02. Jika beta historis = 1, hasilnya 1,02, sehingga formula itu tidak memiliki titik tetap 1. Bahkan titik tetap iterasinya adalah $0.35/(1-0.67)=1.060606\ldots$.

Jika yang dimaksud adalah kombinasi konveks dengan bobot historis 0,67 menuju beta 1, koefisien kedua semestinya 0,33. Versi berbobot jumlah satu memberi 1,335 untuk beta historis 1,5; bentuk cetak memberi 1,355. Kajian dan uji hitung **menyimpan bentuk cetak sebagai bentuk cetak**, serta menunjukkan alternatif berbobot jumlah satu sebagai interpretasi matematis. Keduanya tidak disamakan, dan catatan ini tidak menyatakan penerbit telah mengeluarkan koreksi resmi.

## 9. Volatilitas opsi riil — 26-1/26-1a

Jika nilai proyek V pada horizon t diasumsikan lognormal, maka:

$$CV^2=Var(V)/E[V]^2=e^{\sigma^2t}-1.$$

Mengambil log menghasilkan $\sigma^2=\ln(1+CV^2)/t$. Untuk CV = 0,47 dan t = 1, varians sekitar 0,19958829; volatilitas adalah akarnya, sekitar 0,44675305 atau 44,6753% per akar tahun. Angka 0,20 pada sumber adalah pembulatan **varians**, bukan volatilitas 20%. Volatilitas aset proyek tidak boleh disamakan begitu saja dengan volatilitas saham perusahaan levered.

## 10. Arti verifikasi

298 pemeriksaan mencakup 280 contoh (236 bernomor dan 44 catatan pendamping), serta 18 identitas atau pemeriksaan lintas metode. Cakupan nomor diperiksa terpisah: 236 unik, 244 lokasi cetak, tanpa nomor kajian yang hilang, berlebih, atau ganda. Uji contoh mempunyai toleransi relatif 1e−7 dan absolut 1e−8; angka pada uraian dapat dibulatkan.

Catatan pendamping mengelompokkan rasio, perhitungan tabel, dan formalisasi konsep. Ini tidak berarti setiap substitusi angka di seluruh soal dan setiap sel Excel telah dikaji sebagai rumus baru. Daftar soal yang sudah dikerjakan tetap ditampilkan tersendiri pada PEMBAHASAN_SOAL.md.
