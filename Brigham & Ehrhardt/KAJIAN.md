# Panduan Belajar Financial Management — 15e

[Daftar isi sumber](SUMMARY.md) · [Status pekerjaan](STATUS.md)

Panduan ini merupakan sintesis pengantar lintas 26 bab, bukan ulasan tuntas setiap halaman. File bab menyimpan teks ekstraksi sumber secara lebih lengkap. Contoh numerik di bawah dibuat untuk panduan ini; bukan salinan soal atau kunci jawaban buku. Rujukan bab dan halaman ada di SUMMARY.md.

## Benang merah buku

Pengantar buku menempatkan nilai intrinsik perusahaan sebagai penghubung seluruh materi. Laporan keuangan membantu mengenali arus kas dan kebutuhan modal. Nilai waktu uang mengubah arus kas masa depan menjadi nilai sekarang. Risiko memengaruhi tingkat imbal hasil yang diminta. Keputusan investasi, pendanaan, distribusi kas, dan pengelolaan operasi kemudian dinilai dari pengaruhnya terhadap nilai perusahaan.

Hubungan dasar:

$$V_{op,0}=\sum_{t=1}^{\infty}\frac{FCF_t}{(1+WACC)^t}$$

Persamaan ini mengasumsikan tingkat diskonto yang sesuai dan konstan. Jika struktur modal atau risiko berubah, tingkat diskonto dan pendekatan valuasinya perlu disesuaikan. Nilai operasi bukan otomatis nilai ekuitas: perlu rekonsiliasi aset nonoperasi, utang, dan klaim lain.

## 1. Lingkungan dan tujuan manajemen keuangan

[Teks Bab 1](01-chapter.md)

Pelajari siklus hidup perusahaan, bentuk organisasi, hubungan pemegang saham dan manajemen, lembaga keuangan, pasar uang dan pasar modal, serta pasar primer dan sekunder. Pembiayaan memindahkan dana dari pihak yang memiliki surplus kepada pihak yang membutuhkan dana melalui klaim atas arus kas.

Tujuan meningkatkan nilai intrinsik harus dilihat bersama horizon jangka panjang, risiko, tata kelola, serta kewajiban perusahaan. Laba per saham yang meningkat belum membuktikan penciptaan nilai: peningkatan itu dapat disertai investasi modal yang terlalu mahal atau risiko berlebihan. Bedakan harga pasar saat ini, nilai buku, dan estimasi nilai intrinsik.

Pertanyaan belajar: bagaimana keputusan operasional mengubah FCF, dan bagaimana risiko serta kondisi pasar mengubah biaya modal?

## 2. Laporan keuangan, arus kas, dan pajak

[Teks Bab 2](02-chapter.md)

Neraca adalah posisi pada tanggal tertentu; laba rugi dan arus kas mencakup suatu periode. Laporan perubahan ekuitas menjembatani modal awal, laba, distribusi, dan perubahan lain. Akuntansi akrual membuat laba berbeda dari kas. Penyusutan mengurangi laba tetapi bukan pembayaran kas pada periode penyusutannya.

Untuk model operasi sederhana:

$$NOPAT=EBIT(1-T)$$
$$FCF=NOPAT+D\&A-CAPEX-\Delta NOWC$$

NOWC menghubungkan aset lancar operasi dengan kewajiban lancar operasi tanpa bunga. Jangan memasukkan utang berbunga sebagai pengurang modal kerja operasi lalu menghitung biaya pendanaan itu kembali. FCF dapat negatif ketika perusahaan berinvestasi untuk tumbuh; kesimpulannya bergantung pada pengembalian investasi tersebut.

$$ROIC=NOPAT/InvestedCapital$$
$$EVA=NOPAT-WACC\times InvestedCapital$$

Definisi dan basis modal harus konsisten, termasuk penggunaan saldo awal atau rata-rata. Materi pajak dalam buku adalah konteks historis Amerika Serikat, bukan rujukan ketentuan Indonesia saat ini.

## 3. Analisis laporan keuangan

[Teks Bab 3](03-chapter.md)

Kelompok utama rasio meliputi likuiditas, pengelolaan aset, utang, profitabilitas, dan nilai pasar. Gunakan tren beberapa periode, common-size, serta pembanding dengan karakter bisnis dan kebijakan akuntansi yang sebanding. Rasio tunggal tidak menjelaskan penyebab.

$$CurrentRatio=CurrentAssets/CurrentLiabilities$$
$$ROE=\frac{NI}{Sales}\times\frac{Sales}{Assets}\times\frac{Assets}{Equity}$$

DuPont menjelaskan hubungan margin, perputaran aset, dan leverage. ROE dapat naik karena utang bertambah walaupun produktivitas operasi tidak membaik. Untuk DSO, tetapkan apakah penjualan kredit atau total penjualan digunakan; untuk rasio perputaran, saldo rata-rata sering lebih sesuai dengan arus satu periode. Musiman, transaksi sekali jalan, dan window dressing membatasi interpretasi.

## 4. Nilai waktu uang

[Teks Bab 4](04-chapter.md)

Mulai dari garis waktu: tanggal arus kas, tanda masuk/keluar, satuan periode, serta waktu pembayaran. Samakan tingkat bunga dengan frekuensi arus kas.

$$FV=PV(1+r)^n,\qquad PV=FV/(1+r)^n$$
$$PV_{annuity}=PMT\frac{1-(1+r)^{-n}}{r}$$
$$EAR=(1+APR/m)^m-1$$

Anuitas biasa dibayar pada akhir periode; anuitas jatuh tempo dibayar pada awal periode sehingga nilainya sama dengan anuitas biasa dikali $(1+r)$ pada tanggal penilaian yang sama. Perpetuitas konstan bernilai $CF_1/r$. Untuk arus kas tumbuh konstan, nilai $CF_1/(r-g)$ mensyaratkan $r>g$. Jangan memasukkan bunga tahunan ke jadwal bulanan tanpa konversi.

## 5. Obligasi dan tingkat bunga

[Teks Bab 5](05-chapter.md)

Nilai obligasi adalah jumlah PV kupon dan pelunasan pokok:

$$P=\sum_{t=1}^{n}\frac{C}{(1+y)^t}+\frac{F}{(1+y)^n}$$

Untuk kupon semesteran, sesuaikan kupon, jumlah periode, dan yield periodik. Kupon adalah ketentuan kontrak; current yield adalah kupon tahunan dibagi harga; YTM adalah tingkat diskonto yang menyamakan harga dengan arus kas kontraktual. YTM bukan jaminan return terealisasi karena default, penjualan sebelum jatuh tempo, dan reinvestasi dapat berbeda.

Harga bergerak berlawanan dengan yield. Risiko suku bunga harga berbeda dari risiko reinvestasi. Telaah call provision, sinking fund, default, likuiditas, dan term structure. Durasi membantu mengukur sensitivitas harga, tetapi pendekatan linear menjadi kurang tepat untuk perubahan yield besar.

## 6. Risiko dan return

[Teks Bab 6](06-chapter.md)

Expected return adalah rata-rata tertimbang probabilitas, bukan hasil yang pasti. Standar deviasi mengukur sebaran return; beta mengukur sensitivitas terhadap pasar. Diversifikasi mengurangi risiko spesifik perusahaan, tetapi tidak menghilangkan semua risiko pasar.

$$E(R)=\sum_i p_iR_i$$
$$\beta_i=Cov(R_i,R_M)/Var(R_M)$$
$$r_i=r_f+\beta_i[E(R_M)-r_f]$$

CAPM menghubungkan expected required return dengan risiko sistematis dalam kerangka asumsi model. Jangan mengganti beta dengan volatilitas total. Estimasi beta berubah menurut periode data dan komposisi usaha. Bab ini juga mengenalkan efisiensi pasar, faktor Fama–French, serta bias perilaku; harga yang berfluktuasi tidak otomatis membuktikan pasar selalu tidak rasional.

## 7. Valuasi perusahaan dan saham

[Teks Bab 7](07-chapter.md)

Bedakan model FCF untuk operasi, dividend discount model untuk ekuitas, dan pembanding multiple. Dalam model FCF, diskontokan arus kas bagi seluruh penyedia modal dengan WACC. Dalam model dividen, diskontokan dividen kepada pemegang saham dengan biaya ekuitas.

$$TV_N=FCF_{N+1}/(WACC-g)$$
$$EquityValue=V_{op}+NonoperatingAssets-Debt-OtherClaims$$
$$P_0=D_1/(r_s-g)$$

Terminal value dihitung pada akhir tahun N lalu didiskontokan ke tanggal valuasi. Jangan memakai FCF tahun N ketika pembilang harus tahun N+1. Pertumbuhan memerlukan reinvestasi: menaikkan pertumbuhan tanpa menaikkan kebutuhan modal dapat menghasilkan nilai yang terlalu tinggi. Multiple harus menggunakan definisi pembilang dan penyebut yang sesuai.

## 8. Opsi keuangan

[Teks Bab 8](08-chapter.md)

Call memberi hak membeli dan put memberi hak menjual. Payoff pada jatuh tempo berbeda dari keuntungan setelah premi. Nilai intrinsik call adalah $max(S-K,0)$; put adalah $max(K-S,0)$. Nilai waktu dapat membuat harga opsi melebihi nilai intrinsiknya.

Model binomial memakai portofolio replikasi atau probabilitas risk-neutral. Black–Scholes untuk call Eropa tanpa dividen dalam bentuk dasarnya:

$$C=SN(d_1)-Ke^{-rT}N(d_2)$$
$$d_1=\frac{\ln(S/K)+(r+\sigma^2/2)T}{\sigma\sqrt T},\quad d_2=d_1-\sigma\sqrt T$$

Asumsi model mencakup volatilitas dan parameter tertentu yang tetap serta karakter perdagangan yang ideal. Opsi karyawan dan opsi aset riil dapat memiliki kendala berbeda. Jangan memperlakukan probabilitas risk-neutral sebagai ramalan probabilitas aktual.

## 9. Biaya modal

[Teks Bab 9](09-chapter.md)

$$WACC=w_dr_d(1-T)+w_{ps}r_{ps}+w_sr_s$$

Gunakan biaya marginal dan bobot nilai pasar/target yang sesuai. Bunga utang memperoleh penyesuaian pajak hanya sejauh manfaat pajaknya relevan. Biaya ekuitas dapat diestimasi dengan CAPM atau dividend growth model, tetapi hasilnya sensitif pada input.

WACC perusahaan sesuai untuk proyek dengan risiko dan kebijakan pendanaan yang sebanding. Memakai satu WACC bagi proyek berisiko sangat berbeda dapat menerima proyek terlalu berisiko dan menolak proyek lebih aman. Biaya modal bukan rata-rata biaya historis. Perlakukan flotation costs secara konsisten agar tidak dihitung dua kali.

## 10. Capital budgeting

[Teks Bab 10](10-chapter.md)

$$NPV=CF_0+\sum_{t=1}^{N}\frac{CF_t}{(1+r)^t}$$

NPV menunjukkan tambahan nilai pada tanggal penilaian. IRR membuat NPV nol. MIRR menggunakan tingkat pembiayaan dan reinvestasi yang ditetapkan. Payback membantu menilai kecepatan pengembalian tetapi mengabaikan sebagian informasi; discounted payback memperbaiki aspek nilai waktu, bukan seluruh kelemahannya.

Untuk proyek independen dengan arus kas konvensional, aturan NPV dan IRR biasanya sejalan. Untuk proyek mutually exclusive, perbedaan skala dan waktu dapat membalik peringkat. Arus kas dengan perubahan tanda berulang dapat memiliki beberapa IRR. Jangan otomatis memilih persentase IRR tertinggi ketika pertanyaannya adalah tambahan nilai terbesar dengan kendala yang relevan.

## 11. Estimasi arus kas dan analisis risiko

[Teks Bab 11](11-chapter.md)

Gunakan arus kas incremental setelah pajak: bandingkan keadaan dengan proyek dan tanpa proyek. Keluarkan sunk cost yang tidak berubah, tetapi masukkan opportunity cost, kanibalisasi, perubahan modal kerja, belanja modal, serta hasil penjualan aset setelah pajak. Penyusutan memengaruhi pajak, bukan arus kas langsung.

$$OCF=(Revenue-CashOperatingCosts)(1-T)+Depreciation\times T$$

Ini adalah bentuk sederhana dengan asumsi pajak terkait dapat dimanfaatkan. Biaya bunga tidak dikurangkan lagi dalam FCF proyek ketika biaya pendanaan sudah tercermin melalui WACC. Bedakan sensitivity analysis satu variabel, scenario analysis beberapa variabel konsisten, dan simulasi distribusi banyak kemungkinan. Korelasi input memengaruhi hasil simulasi; skenario ekstrem tidak otomatis memiliki probabilitas yang sama.

## 12. Perencanaan dan valuasi

[Teks Bab 12](12-chapter.md)

Forecast penjualan harus diterjemahkan ke margin, aset operasi, kewajiban operasi, investasi, dan kebutuhan pembiayaan. Pertumbuhan penjualan dapat memperbesar kebutuhan dana walaupun laba meningkat. Pendekatan persentase penjualan adalah titik awal, dengan keterbatasan ketika kapasitas, margin, atau efisiensi modal berubah.

Model proyeksi perlu menghubungkan neraca, laba rugi, dan arus kas. Tentukan sumber pendanaan tambahan serta implikasinya terhadap bunga, laba, laba ditahan, dan saldo kas. Hubungan ini dapat menimbulkan circularity yang harus diselesaikan secara eksplisit. Uji kesamaan aset dengan liabilitas plus ekuitas, rekonsiliasi kas, dan konsistensi asumsi terminal.

## 13. Tata kelola perusahaan

[Teks Bab 13](13-chapter.md)

Agency conflict muncul ketika pihak yang mengelola sumber daya memiliki insentif berbeda dari pemilik atau kreditor. Mekanisme pengendalian meliputi dewan, monitoring, kepemilikan, kontrak kompensasi, keterbukaan, dan disiplin pasar.

Kompensasi berbasis saham dapat menyelaraskan kepentingan sekaligus mendorong pengambilan risiko atau fokus harga jangka pendek jika desainnya keliru. Tinjau horizon, target kinerja, potensi manipulasi, dan pengawasan. Corporate governance terhubung dengan valuasi melalui penggunaan kas, kualitas keputusan, serta risiko. Bagian peraturan Amerika Serikat dalam buku merupakan konteks edisi tersebut.

## 14. Dividen dan pembelian kembali saham

[Teks Bab 14](14-chapter.md)

Perusahaan menyeimbangkan kebutuhan investasi bernilai positif dengan distribusi kas. Model residual memperkirakan distribusi setelah kebutuhan ekuitas untuk anggaran investasi dan struktur modal target terpenuhi. Praktik kebijakan dividen juga mempertimbangkan stabilitas, sinyal, clientele, dan fleksibilitas.

Dividen mengurangi kas dan memberi pembayaran langsung. Repurchase mengurangi kas serta jumlah saham. EPS dapat naik sesudah repurchase tanpa peningkatan nilai operasi; harga pembelian kembali penting bagi pemegang saham yang tetap bertahan. Stock split dan stock dividend mengubah unit saham, bukan otomatis kekayaan ekonomi. Analisis nilai memerlukan melihat jumlah kas, harga, pajak, dan peluang investasi secara bersama.

## 15. Struktur modal

[Teks Bab 15](15-chapter.md)

Leverage menambah risiko finansial di atas risiko bisnis. Utang dapat memberi manfaat pajak namun membawa biaya distress, konflik kepentingan, dan berkurangnya fleksibilitas. Model Modigliani–Miller membantu memisahkan pengaruh asumsi pasar sempurna, pajak, dan friksi lainnya.

Dalam model MM dengan pajak perusahaan dan utang permanen yang memenuhi asumsi:

$$V_L=V_U+TD$$

Persamaan tersebut bukan aturan universal bahwa lebih banyak utang selalu lebih baik. Trade-off theory, signaling, pecking order, dan kapasitas berutang menambahkan konteks. Evaluasi recapitalization lewat perubahan nilai operasi, biaya modal, kas untuk repurchase, nilai utang, serta saham tersisa; bukan hanya EPS.

## 16. Rantai pasok dan modal kerja

[Teks Bab 16](16-chapter.md)

$$CCC=DIO+DSO-DPO$$

Cash conversion cycle menggambarkan waktu antara pembayaran input dan penerimaan kas pelanggan. Persediaan terlalu rendah dapat menghambat penjualan; kredit pelanggan terlalu longgar meningkatkan risiko gagal tagih; menunda pemasok terlalu lama dapat merusak pasokan atau menghilangkan diskon.

Hubungkan kebijakan persediaan, piutang, utang usaha, saldo kas, serta pembiayaan jangka pendek dengan ramalan arus kas. Neraca modal kerja tidak menggantikan cash budget menurut tanggal aktual. Bedakan pembiayaan aset permanen dan kebutuhan musiman serta risiko refinancing. Untuk proyek konstruksi, progres pekerjaan, termin, retensi, dan pembayaran pemasok perlu ditelusuri ke jadwal kas tersendiri; ini adalah penerapan tambahan, bukan contoh khusus dari buku.

## 17. Manajemen keuangan multinasional

[Teks Bab 17](17-chapter.md)

Tetapkan arah kuotasi kurs sebelum menghitung: mata uang domestik per unit asing atau kebalikannya. Konsistensi ini menentukan interpretasi apresiasi, depresiasi, dan forward premium. Bedakan exposure transaksi, translasi, dan ekonomi.

Untuk kuotasi domestik per asing dengan periode bunga yang sama, covered interest parity secara sederhana ditulis:

$$F/S=(1+r_{dom})/(1+r_{for})$$

Model tersebut mengandalkan asumsi pasar dan transaksi yang sesuai. Capital budgeting lintas negara menuntut konsistensi mata uang arus kas dengan discount rate, inflasi, pajak, pembatasan transfer, dan risiko negara. Jangan mendiskontokan arus kas mata uang asing menggunakan tingkat diskonto mata uang domestik tanpa penyesuaian yang benar.

## 18. Pendanaan publik dan privat

[Teks Bab 18](18-chapter.md)

Pelajari peran angel investor, venture capital, IPO, seasoned offering, private placement, dan investment bank. Dana bruto yang dihimpun berbeda dari dana bersih sesudah biaya. Nilai pre-money, post-money, harga saham, jumlah saham baru, dan dilusi perlu direkonsiliasi.

IPO menambah akses modal dan likuiditas sekaligus membawa biaya dan kewajiban keterbukaan. Analisis refunding membandingkan PV penghematan pendanaan setelah pajak dengan biaya transaksi dan pelunasan, bukan sekadar selisih kupon. Penjelasan proses SEC dan pasar Amerika dalam sumber adalah materi historis buku, bukan panduan prosedur Indonesia.

## 19. Lease financing

[Teks Bab 19](19-chapter.md)

Analisis ekonomi leasing membandingkan arus kas menyewa dengan memiliki yang dibiayai utang secara konsisten. Bandingkan pembayaran, penghematan pajak yang relevan, pemeliharaan, nilai residu, serta risiko yang dialihkan.

$$NAL=PV(CostOfOwning)-PV(CostOfLeasing)$$

Dengan konvensi biaya positif ini, NAL positif mendukung leasing. Penilaian lessee dan lessor dapat berbeda karena pajak, biaya modal, skala, dan risiko residu. Pembahasan pengakuan akuntansi leasing dalam edisi 2017 tidak boleh langsung diperlakukan sebagai standar pelaporan Indonesia saat ini. Pisahkan keputusan pendanaan ekonomis dari perlakuan akuntansinya.

## 20. Saham preferen, warrant, dan convertible

[Teks Bab 20](20-chapter.md)

Instrumen hibrida menggabungkan karakter klaim tetap dengan karakter ekuitas. Saham preferen memiliki hak pembayaran tertentu; warrant memberi hak membeli saham baru; convertible memungkinkan konversi klaim menjadi saham sesuai ketentuan.

$$ConversionRatio=ParValue/ConversionPrice$$
$$ConversionValue=ConversionRatio\times SharePrice$$

Pelaksanaan warrant umumnya memasukkan kas baru ke perusahaan sementara obligasi terlampir dapat tetap beredar. Konversi obligasi menukar klaim utang menjadi ekuitas dan biasanya tidak menghasilkan kas baru saat konversi. Telaah dilusi, call provision, straight-debt value, dan nilai opsi. Kupon yang lebih rendah bukan berarti seluruh biaya pendanaan otomatis lebih rendah.

## 21. Struktur modal dinamis dan valuasi

[Teks Bab 21](21-chapter.md)

Jika leverage berubah selama forecast, penggunaan WACC konstan dapat tidak sesuai. APV memisahkan nilai operasi tanpa leverage dari nilai efek pendanaan. Model FCFE menilai arus kas pemegang saham dengan biaya ekuitas, sedangkan FCF/WACC menilai operasi.

$$APV=V_{unlevered}+PV(FinancingEffects)$$
$$FCFE=FCF-Interest(1-T)+NetBorrowing$$

Bentuk FCFE di atas memakai kerangka sederhana tanpa klaim preferen. Risiko tax shield menentukan discount rate yang relevan; jangan selalu menganggap sama dengan tingkat utang atau biaya ekuitas. Pastikan jadwal utang, bunga, pajak, dan terminal leverage konsisten. Hasil beberapa pendekatan seharusnya dapat direkonsiliasi ketika asumsi ekonominya sama.

## 22. Merger dan pengendalian perusahaan

[Teks Bab 22](22-chapter.md)

Bedakan nilai standalone target, nilai sinergi, biaya integrasi, dan harga penawaran. Sinergi memerlukan sumber operasional atau finansial yang dapat dijelaskan, bukan sekadar pertumbuhan ukuran. Diversifikasi perusahaan tidak otomatis memberi nilai tambahan kepada investor yang dapat melakukan diversifikasi sendiri.

$$Synergy=V_{combined}-(V_A+V_B)$$

Nilai bersih untuk pengakuisisi dipengaruhi premium serta biaya transaksi/integrasi yang belum masuk estimasi sinergi. Jangan menghitung biaya yang sama dua kali. Telaah merger horizontal, vertikal, congeneric, conglomerate, friendly/hostile, divestiture, serta dampak perubahan struktur modal. EPS accretion tidak cukup membuktikan merger menciptakan nilai.

## 23. Enterprise risk management

[Teks Bab 23](23-chapter.md)

ERM menghubungkan identifikasi exposure, pengukuran, respons, kontrol, dan monitoring di tingkat perusahaan. Risiko kurs, komoditas, bunga, kredit, serta keselamatan memiliki saluran dampak yang berbeda terhadap arus kas, kebutuhan pembiayaan, dan kelangsungan operasi.

Forward/futures, opsi, dan swap mengubah profil risiko; masing-masing membawa biaya, basis risk, counterparty risk, serta kebutuhan likuiditas. Nilai hedge dilihat bersama posisi dasarnya. Kerugian instrumen hedge secara terpisah tidak otomatis berarti lindung nilai gagal. VaR menunjukkan batas kuantil kerugian dengan definisi tertentu; conditional VaR/expected shortfall memperhatikan rata-rata ekor kerugian. Keduanya bergantung pada model dan data.

## 24. Distress, reorganisasi, dan likuidasi

[Teks Bab 24](24-chapter.md)

Bedakan kekurangan kas temporer, ketidakmampuan memenuhi kewajiban, dan nilai ekonomi aset yang berada di bawah klaim. Pertanyaan keuangan utama adalah apakah nilai going concern lebih besar daripada nilai likuidasi setelah biaya dan risiko.

Workout, penjadwalan ulang, pengurangan klaim, reorganisasi formal, dan likuidasi memberi alternatif hasil bagi pemegang klaim. Pembagian recovery memerlukan nilai aset, biaya proses, jaminan, subordinasi, dan prioritas yang benar. Uraian Chapter 7 dan Chapter 11 di buku membahas sistem hukum Amerika pada konteks sumber; itu bukan prosedur kepailitan Indonesia.

## 25. Teori portofolio dan asset pricing

[Teks Bab 25](25-chapter.md)

$$E(R_p)=\sum_iw_iE(R_i)$$
$$\sigma_p^2=\sum_i\sum_jw_iw_jCov(R_i,R_j)$$

Korelasi membuat risiko portofolio berbeda dari rata-rata sederhana volatilitas aset. Efficient frontier memuat kombinasi yang tidak didominasi menurut expected return dan risiko dalam batas model. Capital Market Line menggunakan total risiko portofolio efisien; Security Market Line menggunakan beta untuk expected required return suatu aset.

Estimasi beta dengan regresi mengandung sampling error. Periode pengamatan, frekuensi return, benchmark, dan perubahan usaha memengaruhi hasil. Model multifaktor dan APT memberi kerangka tambahan, tetapi tidak menjadikan semua faktor statistik otomatis penjelasan kausal atau return masa depan yang pasti.

## 26. Real options

[Teks Bab 26](26-chapter.md)

Manajemen dapat menunda investasi, memperluas, mengubah kapasitas, atau meninggalkan proyek setelah informasi baru muncul. Fleksibilitas tersebut adalah hak mengambil tindakan, bukan kewajiban. NPV statis dengan satu jalur operasi dapat melewatkan nilai keputusan bersyarat.

Analisis dapat memakai pembahasan kualitatif, decision tree, model opsi, atau teknik financial engineering. Identifikasi aset dasar, biaya pelaksanaan, masa hak, ketidakpastian, serta siapa yang mengendalikan pilihan. Hindari menambahkan premi opsi jika fleksibilitas yang sama sudah tercermin dalam proyeksi arus kas. Volatilitas yang meningkatkan nilai opsi tidak berarti semua risiko operasional menguntungkan perusahaan.

## Contoh numerik dan interpretasi

### A. FCF dan EVA

Asumsi ilustratif: EBIT 500, tarif model 25%, D&A 80, CAPEX 140, kenaikan NOWC 60, modal operasi 2.000, WACC 10%. Seluruh nilai uang menggunakan satuan yang sama.

1. NOPAT = 500 × 75% = 375.
2. FCF = 375 + 80 − 140 − 60 = 255.
3. ROIC = 375 / 2.000 = 18,75%.
4. EVA = 375 − 10% × 2.000 = 175.

FCF 255 mengukur kas setelah reinvestasi operasi; EVA 175 mengukur surplus laba operasi setelah beban ekonomis modal. Keduanya bukan ukuran yang sama.

### B. Nilai waktu uang

PV 100, bunga 10% per tahun, tiga tahun: FV = 100 × 1,1³ = 133,10. Tiga penerimaan akhir tahun masing-masing 50 pada tingkat 10% bernilai sekarang sekitar 124,34. Penerimaan awal tahun pada jadwal setara bernilai sekitar 136,78.

### C. Obligasi

Nilai nominal 1.000, kupon tahunan 8%, sisa lima tahun, YTM tahunan 10%. PV kupon = 80 × [1 − 1,1⁻⁵] / 0,1 ≈ 303,26. PV pokok ≈ 620,92. Harga ≈ 924,18. Harga di bawah par sesuai dengan kupon yang lebih rendah daripada yield yang diminta.

### D. Biaya modal

Asumsi model: risk-free 4%, premium pasar 6%, beta 1,2. Biaya ekuitas = 4% + 1,2 × 6% = 11,2%. Bobot utang 40%, ekuitas 60%, biaya utang 7%, tarif pajak ilustratif 25%. WACC = 40% × 7% × 75% + 60% × 11,2% = 8,82%. Angka ini input latihan, bukan data pasar atau tarif pajak yang direkomendasikan.

### E. NPV

Investasi awal 100; kas akhir tahun 40 selama tiga tahun; tingkat diskonto 10%. PV penerimaan = 40/1,1 + 40/1,1² + 40/1,1³ ≈ 99,47. NPV ≈ −0,53. Proyek tidak menambah nilai menurut asumsi tersebut walaupun total kas masuk nominal 120 melebihi investasi awal.

### F. Terminal value

FCF tahun 5 = 100, pertumbuhan mulai tahun 6 = 3%, WACC = 10%. TV pada akhir tahun 5 = 103 / 7% ≈ 1.471,43. PV terminal hari ini = 1.471,43 / 1,1⁵ ≈ 913,64. Tambahkan PV FCF tahun 1–5 untuk nilai operasi; jangan menyamakan PV terminal dengan keseluruhan nilai perusahaan.

### G. Modal kerja

DIO 60 hari, DSO 45, DPO 30: CCC = 75 hari. Penurunan DSO menjadi 35 menurunkan CCC menjadi 65 hari jika faktor lain tetap. Dampak rupiahnya membutuhkan tingkat penjualan dan komponen kas yang sesuai; penurunan hari tidak dapat langsung dinyatakan sebagai kenaikan laba.

### H. Convertible dan opsi

Obligasi convertible bernilai nominal 1.000 dengan conversion price 25 mempunyai conversion ratio 40 saham. Pada harga saham 30, conversion value = 1.200. Ini belum menentukan harga pasar instrumen atau keputusan konversi optimal, karena nilai straight debt, opsi, bunga yang tersisa, serta call terms juga relevan.

Call dengan strike 100 dan harga saham saat jatuh tempo 115 memiliki payoff 15. Jika premi awal 8, keuntungan nominal sebelum biaya dan penyesuaian nilai waktu = 7. Payoff 15 tidak sama dengan keuntungan 15.

## Cara menggunakan arsip ini untuk belajar mendalam

Untuk setiap bab, baca teks utama, definisikan simbol dan asumsi, buat garis waktu bila ada arus kas, lalu kerjakan self-test sebelum membaca Appendix A. Gunakan Appendix B untuk memeriksa jawaban akhir terpilih, bukan menganggapnya pembahasan langkah demi langkah seluruh soal. Appendix C adalah indeks persamaan sumber; simbol hasil ekstraksinya perlu diperiksa pada PDF.

Catat per soal: halaman sumber, input, satuan, rumus, hasil antara tanpa pembulatan, hasil akhir, interpretasi, dan hal yang belum jelas. Daftar pekerjaan verifikasi itu belum diisi untuk seluruh soal dalam sesi ini. Web Extensions dan Web Chapters 27–30 disebut dalam daftar isi tetapi file materi terpisahnya tidak tersedia dalam PDF ini.
