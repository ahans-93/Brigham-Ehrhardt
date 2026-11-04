# Register rumus dan derivasi

**Pembaruan 4 November 2026:** [kajian manual per persamaan](kajian-rumus/README.md) mencakup 236 persamaan bernomor unik dan 44 catatan pendamping, dengan rujukan PDF, variabel, penurunan, syarat, contoh, dan verifikasi hitung. Gunakan [catatan kritis](kajian-rumus/CATATAN_KRITIS.md) untuk ambiguitas atau potensi masalah cetak. Dokumen di bawah tetap menjadi ringkasan lintas topik.

[Daftar isi](SUMMARY.md) · [Teks Appendix C](29-appendix-c.md) · [Pembahasan soal](PEMBAHASAN_SOAL.md)

Register ini menuliskan kembali kelompok rumus utama dalam notasi yang terbaca, dengan penjelasan asumsi. Acuannya adalah Appendix C, PDF 1122–1134 (halaman cetak 1085–1097), serta bab terkait. Seluruh 13 halaman persamaan Appendix C sudah diperiksa secara visual terhadap PDF asli. Appendix C sendiri berjudul **Selected Equations**, sehingga daftar ini tidak dinyatakan sebagai semua persamaan buku. Rumus di bawah merupakan penulisan ulang konseptual dengan tambahan konteks; simbol yang rusak pada ekstraksi sumber tetap dapat dilihat di file sumber.

## Notasi dan disiplin perhitungan

Gunakan r sebagai tingkat diskonto per periode, n sebagai jumlah periode, t sebagai indeks waktu, T sebagai tarif pajak model, g sebagai pertumbuhan, S sebagai harga saham bila membahas opsi, dan E sebagai nilai ekuitas bila membahas struktur modal. Huruf yang sama dalam buku kadang memiliki arti berbeda antarbab. Semua satuan uang, mata uang, dan periode harus diseragamkan sebelum substitusi.

CF positif berarti penerimaan bagi pihak yang sedang dianalisis; CF negatif berarti pembayaran. PMT pada rumus faktor anuitas di bawah adalah besaran pembayaran positif. Dalam program spreadsheet, tanda PV dan PMT harus mengikuti sudut pandang masuk/keluar kas. Jangan membulatkan hasil antara sebelum perhitungan selesai.

## Bab 1–2: operasi dan penciptaan nilai

| Ukuran | Rumus yang ditulis ulang | Interpretasi/asumsi |
|---|---|---|
| EBIT | Revenue − operating costs, termasuk depresiasi/amortisasi yang relevan | Sebelum bunga dan pajak |
| EBITDA | EBIT + depreciation + amortization | Bukan pengganti FCF |
| Net cash flow sederhana | NI + D&A | Hanya penyesuaian nonkas yang disebut dalam model sederhana |
| NOWC | Operating current assets − operating current liabilities | Keluarkan pendanaan berbunga dan aset investasi nonoperasi |
| Total net operating capital | NOWC + net operating long-term assets | Basis modal konsisten dengan NOPAT |
| NOPAT | EBIT(1 − T) | Model pajak operasi sederhana |
| Net investment in operating capital | Operating capital akhir − operating capital awal | Termasuk perubahan modal kerja operasi dan aset operasi neto |
| FCF | NOPAT − net investment in operating capital | Arus kas bagi penyedia modal sebelum distribusi pendanaan |
| FCF alternatif | NOPAT + D&A − CAPEX − ΔNOWC | Ekuivalen jika perubahan aset operasi sesuai dengan CAPEX dan D&A |
| ROIC | NOPAT / invested operating capital | Tetapkan basis saldo sesuai model buku/soal |
| Operating profitability | NOPAT / sales | Margin operasi setelah pajak |
| Capital requirement ratio | Operating capital / sales | Modal yang terikat per unit penjualan |
| EVA | NOPAT − WACC × operating capital | Surplus laba operasi atas biaya modal |
| EVA alternatif | (ROIC − WACC) × operating capital | Menggunakan basis modal yang sama |
| MVA ekuitas | Market equity − book common equity | Definisi berbasis ekuitas |
| MVA total | Market value of investor claims − investor-supplied capital | Jangan campur definisi total dengan definisi ekuitas |

## Bab 3: rasio dan DuPont

| Rasio | Rumus | Hal yang perlu diperiksa |
|---|---|---|
| Current | CA / CL | Likuiditas kualitas aset tetap perlu dianalisis |
| Quick | (CA − inventory) / CL | Definisi sumber; penyesuaian prepaid dapat berbeda dalam praktik |
| Inventory turnover | COGS / inventory | Saldo rata-rata vs akhir harus konsisten |
| DSO | AR / (sales / 365) | Penjualan kredit lebih tepat bila tersedia dan sesuai soal |
| Fixed asset turnover | Sales / net fixed assets | Pengaruh usia aset dan depresiasi |
| Total asset turnover | Sales / total assets | Tetapkan saldo rata-rata/akhir |
| Debt/assets | Interest-bearing debt / assets | Debt bukan seluruh liabilities |
| Liabilities/assets | Total liabilities / assets | Rasio berbeda dari debt/assets |
| Market debt ratio | Debt / (debt + market equity) | Gunakan basis penilaian utang sesuai model |
| Debt/equity | Debt / common equity | Nilai buku atau pasar harus disebut |
| Equity multiplier | Assets / common equity | Menghubungkan ROA dan ROE |
| TIE | EBIT / interest | Tidak menangkap jadwal pelunasan pokok |
| EBITDA coverage versi sumber | (EBITDA + lease payments) / (interest + principal payments + lease payments) | Definisi arus pembayaran harus mengikuti soal; bukan DSCR universal |
| Net margin | NI available to common / sales | Konsisten dengan klaim preferen |
| Operating margin | EBIT / sales | Sebelum pajak dan pendanaan |
| Gross margin | (Sales − COGS) / sales | Kebijakan klasifikasi biaya memengaruhi perbandingan |
| ROA | NI available to common / assets | Bukan ROIC |
| BEP | EBIT / assets | Tidak memasukkan pajak dan bunga |
| ROE | NI available to common / common equity | Dapat terdorong leverage |
| P/E | Price per share / EPS | EPS negatif membatasi interpretasi |
| P/CF | Price per share / CF per share | Definisikan CF terlebih dahulu |
| BVPS | Common equity / shares outstanding | Bedakan diluted dan basic shares |
| M/B | Market price / BVPS | Nilai buku dapat kecil atau negatif |

### Derivasi DuPont

Mulai dari $ROE=NI/E$. Kalikan dengan $Sales/Sales$ dan $Assets/Assets$, yang masing-masing bernilai satu:

$$ROE=\frac{NI}{Sales}\frac{Sales}{Assets}\frac{Assets}{E}$$

Faktor pertama adalah margin, kedua perputaran aset, ketiga leverage. Kesamaan aljabar ini tidak membuktikan bahwa menaikkan leverage selalu memperbaiki kesejahteraan pemegang saham: bunga dan risiko dapat mengubah NI serta required return.

## Bab 4: nilai waktu uang

| Konsep | Rumus |
|---|---|
| Future value satu kas | $FV_n=PV(1+r)^n$ |
| Present value satu kas | $PV=FV_n/(1+r)^n$ |
| Mencari tingkat bunga | $r=(FV/PV)^{1/n}-1$ |
| Mencari waktu | $n=\ln(FV/PV)/\ln(1+r)$ |
| Perpetuitas konstan | $PV=PMT/r$ |
| FV anuitas biasa | $FV=PMT[(1+r)^n-1]/r$ |
| PV anuitas biasa | $PV=PMT[1-(1+r)^{-n}]/r$ |
| Anuitas due | Nilai anuitas biasa pada tanggal yang sama × $(1+r)$ |
| PV kas tidak seragam | $\sum_{t=1}^n CF_t/(1+r)^t$ |
| FV kas tidak seragam pada n | $\sum_{t=1}^n CF_t(1+r)^{n-t}$ |
| Bunga periodik dari APR | $r_{per}=APR/m$ |
| Jumlah periode | $n=m\times years$ |
| Effective annual rate | $EAR=(1+APR/m)^m-1$ |
| APR dari EAR | $APR=m[(1+EAR)^{1/m}-1]$ |
| Angsuran utang amortisasi | $PMT=PV\,r/[1-(1+r)^{-n}]$ |
| Bunga angsuran t | Saldo awal periode × r |
| Pokok angsuran t | PMT − bunga periode t |
| Bunga sederhana pecahan tahun | Principal × annual rate × day fraction |
| Fisher exact | $(1+r_{nominal})=(1+r_{real})(1+inflation)$ |
| PV growing annuity | $CF_1[1-((1+g)/(1+r))^n]/(r-g)$, untuk r ≠ g |

Pada r = 0, gunakan batas: PV/FV anuitas = n × PMT. Pada r = g dalam growing annuity, PV = n × CF1/(1+r). Jadwal pembayaran pertama tetap harus benar.

### Derivasi faktor anuitas

Untuk pembayaran akhir periode, $A=PMT[(1+r)^{-1}+...+(1+r)^{-n}]$. Kalikan dengan $(1+r)$ kemudian kurangkan A. Suku-suku tengah saling hapus, sehingga $rA=PMT[1-(1+r)^{-n}]$. Bagi r untuk memperoleh faktor PV. Mengalikan PV dengan $(1+r)^n$ memberi faktor FV. Memindahkan seluruh pembayaran satu periode lebih awal mengalikan nilai pada tanggal yang sama dengan $(1+r)$.

## Bab 5: obligasi

| Konsep | Rumus/ketentuan |
|---|---|
| Harga obligasi | $P=C[1-(1+y)^{-n}]/y+F(1+y)^{-n}$ |
| Kupon semester | C tahunan / 2; n = 2 × tahun; y = quoted YTM / 2 |
| Zero coupon | $P=F/(1+y)^n$ |
| YTM | Selesaikan harga = PV arus kas kontraktual hingga maturity |
| YTC | Selesaikan harga = PV kupon sampai call + PV call price |
| Current yield | Annual coupon / current price |
| Required debt return | Real risk-free + inflation premium + maturity premium + default premium + liquidity premium, sebagai dekomposisi model |
| Yield holding-period satu tahun | $[Coupon+P_1-P_0]/P_0$ |

YTM tidak sama dengan return terealisasi tanpa asumsi tambahan mengenai pembayaran, horizon, dan reinvestasi. Penjumlahan current yield dan capital gains yield harus menggunakan periode serta definisi return yang konsisten.

## Bab 6 dan 25: risiko, portofolio, dan asset pricing

| Ukuran | Rumus |
|---|---|
| Expected return | $\mu=\sum_i p_iR_i$ |
| Varians probabilitas | $\sigma^2=\sum_i p_i(R_i-\mu)^2$ |
| Sample variance historis | $s^2=\sum_t(R_t-\bar R)^2/(N-1)$ |
| Standard deviation | Akar varians |
| Coefficient of variation | $CV=\sigma/\mu$, interpretasi terbatas bila μ nol/negatif |
| Covariance | $Cov_{ij}=\rho_{ij}\sigma_i\sigma_j$ |
| Beta | $\beta_i=Cov(R_i,R_M)/\sigma_M^2$ |
| Beta portofolio | $\beta_p=\sum_iw_i\beta_i$ |
| CAPM/SML | $r_i=r_f+\beta_i[E(R_M)-r_f]$ |
| Return portofolio | $E(R_p)=\sum_iw_iE(R_i)$ |
| Varians portofolio | $\sigma_p^2=\sum_i\sum_jw_iw_jCov_{ij}$ |
| Dua aset | $w^2\sigma_A^2+(1-w)^2\sigma_B^2+2w(1-w)\rho\sigma_A\sigma_B$ |
| Bobot minimum variance A | $(\sigma_B^2-\rho\sigma_A\sigma_B)/(\sigma_A^2+\sigma_B^2-2\rho\sigma_A\sigma_B)$ |
| CML | $E(R_p)=r_f+[E(R_M)-r_f]\sigma_p/\sigma_M$, untuk portofolio efisien terkait |
| Sharpe | Average excess return / SD excess return |
| Treynor | Average excess return / portfolio beta |
| Single-index variance | $\sigma_i^2=\beta_i^2\sigma_M^2+\sigma_{e_i}^2$, jika residual tidak berkorelasi dengan pasar |
| APT | $E(R_i)=r_f+\sum_k\beta_{ik}\lambda_k$ |
| Fama–French regresi | $R_i-r_f=\alpha_i+\beta_i(R_M-r_f)+s_iSMB+h_iHML+\epsilon_i$ |

Bobot minimum variance di atas adalah solusi tanpa kendala short selling. Jika hanya bobot 0–1 diperbolehkan, evaluasi kendala tersebut. CML memakai total volatilitas untuk portofolio efisien; SML memakai beta untuk aset/portofolio dalam CAPM.

### Derivasi manfaat diversifikasi

Return dua aset adalah $R_p=wR_A+(1-w)R_B$. Varians jumlah variabel mencakup dua varians tertimbang dan dua kali covariance. Bila korelasi kurang dari satu, covariance lebih kecil daripada hasil kali volatilitas, sehingga risiko gabungan dapat lebih rendah dibanding penjumlahan tertimbang volatilitas. Korelasi nol bukan berarti seluruh risiko portofolio hilang.

## Bab 7: valuasi

| Model | Rumus |
|---|---|
| Nilai operasi umum | $V_{op}=\sum_{t=1}^{\infty}FCF_t/(1+WACC)^t$ |
| Terminal value FCF | $TV_N=FCF_{N+1}/(WACC-g)$ |
| Multistage FCF | PV FCF eksplisit + PV terminal value |
| Entity value | Value of operations + nonoperating assets |
| Equity value | Entity value − debt − preferred stock − klaim lain yang relevan |
| Value/share | Common equity value / appropriate shares outstanding |
| DDM umum | $P_0=\sum_{t=1}^{\infty}D_t/(1+r_s)^t$ |
| Gordon growth | $P_0=D_1/(r_s-g)$ |
| Expected equity return Gordon | $r_s=D_1/P_0+g$ |
| Zero-growth dividend | $P_0=D/r_s$ |
| Preferred value | $V_{ps}=D_{ps}/r_{ps}$ untuk perpetuitas konstan |

### Derivasi Gordon dan terminal value

Mulai dengan deret PV dividen yang tumbuh g. Rasio suku berikutnya adalah $(1+g)/(1+r_s)$. Jumlah deret tak hingga konvergen bila rasio absolut kurang dari satu; dalam model pertumbuhan biasa mensyaratkan $r_s>g$. Hasilnya $P_0=D_1/(r_s-g)$. Pada akhir forecast N, pembayaran pertama yang belum masuk forecast adalah D(N+1) atau FCF(N+1), sehingga itulah pembilang terminal value. Nilai terminal masih berada pada tanggal N.

## Bab 8: opsi

| Konsep | Rumus |
|---|---|
| Call payoff | $max(S_T-K,0)$ |
| Put payoff | $max(K-S_T,0)$ |
| Binomial delta | $(C_u-C_d)/(S_u-S_d)$ |
| Risk-neutral probability satu periode | $q=(R-d)/(u-d)$, R faktor pertumbuhan risk-free per periode |
| Binomial option value | $[qC_u+(1-q)C_d]/R$ |
| Black–Scholes call | $C=SN(d_1)-Ke^{-rT}N(d_2)$ |
| d1 | $[\ln(S/K)+(r+\sigma^2/2)T]/(\sigma\sqrt T)$ |
| d2 | $d_1-\sigma\sqrt T$ |
| Put–call parity | $P=C-S+Ke^{-rT}$ |

Bentuk Black–Scholes/parity di sini untuk opsi Eropa pada saham tanpa dividen dalam kerangka dasar. r memakai continuous compounding. Untuk binomial tanpa arbitrase diperlukan d < R < u. Probabilitas risk-neutral bukan perkiraan probabilitas nyata.

## Bab 9: cost of capital

| Komponen | Rumus/penjelasan |
|---|---|
| After-tax debt cost sederhana | $r_d(1-T)$ |
| Preferred cost dengan flotation | $D_{ps}/[P_{ps}(1-F)]$ |
| Equity via CAPM | $r_s=r_f+\beta RPM$ |
| Equity via DDM | $r_s=D_1/P_0+g$ |
| Equity via bond-yield-plus-risk | Own bond yield + judgmental equity risk premium |
| Growth via retention | $g=RetentionRatio\times ROE$, dengan asumsi kebijakan/return stabil |
| New common equity model | $r_e=D_1/[P_0(1-F)]+g$ |
| WACC | $\sum debtweights\,r_d(1-T)+w_{ps}r_{ps}+w_sr_s$ |

Utang jangka pendek berbunga dapat dimasukkan jika merupakan bagian pendanaan modal yang relevan; operating payables sudah dipertimbangkan dalam modal kerja operasi. Jangan menghitung flotation sebagai pengurang proceeds sekaligus biaya tambahan lain untuk efek yang sama.

## Bab 10–12: proyek dan perencanaan

| Konsep | Rumus |
|---|---|
| NPV | $\sum_{t=0}^{n}CF_t/(1+r)^t$ |
| IRR | Tingkat i yang membuat $\sum CF_t/(1+i)^t=0$ |
| MIRR | $(FV_{positive\ CF}/PV_{negative\ CF})^{1/n}-1$, dengan finance/reinvestment rates ditentukan |
| Profitability index, model investasi awal tunggal | PV kas masuk sesudah t0 / investasi awal |
| Payback linear intraperiode | Tahun penuh sebelum pulih + saldo belum pulih / kas periode pemulihan |
| Project CF | Investment outlay + operating CF + working-capital CF + salvage CF, dengan tanda masing-masing |
| After-tax salvage sederhana | $SalePrice-T(SalePrice-TaxBookValue)$ |
| Operating CF | $(Revenue-CashCosts)(1-T)+D\&A\times T$ |
| Expected NPV | $\sum_i p_iNPV_i$ |
| SD NPV | $\sqrt{\sum_i p_i(NPV_i-E[NPV])^2}$ |
| CV NPV | SD NPV / expected NPV; hati-hati denominator kecil/negatif |
| AFN | $(A^*/S_0)\Delta S-(L^*/S_0)\Delta S-M S_1(1-payout)$ |
| Full-capacity sales | Actual sales / capacity utilization |
| Required fixed assets | Projected sales × fixed assets / full-capacity sales |

AFN mengasumsikan rasio tertentu stabil, A* aset yang perlu naik mengikuti penjualan, L* kewajiban spontan, dan M margin bersih. AFN bukan saldo kas: ia menunjukkan tambahan dana eksternal menurut model. Analisis OCF dan salvage memerlukan ketentuan pajak serta pemanfaatan rugi yang sesuai asumsi soal.

### Derivasi konsistensi FCF dan WACC

NOPAT menghitung operasi seolah-olah tanpa biaya bunga. FCF diperoleh sesudah reinvestasi operasi, sehingga tersedia untuk pemegang utang dan ekuitas. WACC menggabungkan return yang diminta kelompok penyedia modal tersebut. Jika bunga dikurangkan dari FCF lalu kas itu didiskontokan menggunakan WACC, biaya pendanaan dapat dihitung ganda. Sebaliknya, FCFE sudah setelah pembayaran pendanaan utang dan dinilai menggunakan biaya ekuitas yang sesuai.

## Bab 14–15: distribusi dan leverage

| Konsep | Rumus/ketentuan |
|---|---|
| Residual distribution model | NI − target equity fraction × total capital budget |
| Shares repurchased | Repurchase cash / actual repurchase price |
| Shares remaining | Original shares − repurchased shares |
| EBIT break-even | $EBIT=(P-v)Q-FixedCost$ |
| Break-even units | $Q_{BE}=FixedCost/(P-v)$, untuk P > v |
| MM tanpa pajak | $V_L=V_U$ dalam asumsi model |
| MM dengan pajak perusahaan | $V_L=V_U+TD$ untuk utang permanen dan asumsi terkait |
| Miller tax adjustment | $V_L=V_U+[1-(1-T_c)(1-T_s)/(1-T_d)]D$ dalam model tersebut |
| Hamada | $\beta_L=\beta_U[1+(1-T)D/E]$, dengan asumsi beta utang nol dan kerangka terkait |
| Unlevering Hamada | $\beta_U=\beta_L/[1+(1-T)D/E]$ |
| NI model sederhana | $(EBIT-r_dD)(1-T)$ |
| EPS | NI available to common / shares |

Residual distribution negatif berarti kebutuhan ekuitas belum tercukupi dari laba dalam model; bukan instruksi membayar dividen negatif. Recapitalization harus menilai perubahan nilai operasi serta pendanaan sebelum menghitung harga dan saham yang dibeli kembali.

## Bab 16–20: operasi dan instrumen pendanaan

| Konsep | Rumus/ketentuan |
|---|---|
| DIO | Inventory / (COGS / 365) |
| DSO | Receivables / daily credit sales |
| DPO versi sederhana sumber | Payables / (COGS / 365); purchases digunakan bila tersedia dan relevan |
| CCC | DIO + DSO − DPO |
| AR target | Daily credit sales × DSO |
| Trade credit nominal annual cost | $d/(1-d)\times365/(N-n)$ |
| Trade credit effective annual cost | $(1+d/(1-d))^{365/(N-n)}-1$ |
| Covered interest parity | $F/S=(1+r_{dom})/(1+r_{for})$ untuk domestik per asing |
| PPP absolute | $S=P_{dom}/P_{for}$ untuk barang/keranjang yang sesuai dalam model |
| IPO money left on table | (First closing price − offer price) × new shares |
| New investor ownership | New shares / (new + existing shares) |
| Post-money sesudah biaya | Pre-money + offer price × new shares × (1 − flotation fraction) |
| Net advantage to leasing | PV cost owning − PV cost leasing |
| Bond plus warrants | Straight-debt value + value of attached warrants |
| Conversion ratio | Par / conversion price |
| Conversion value | Conversion ratio × common share price |

Dalam biaya trade credit, d adalah pecahan diskon, n batas hari diskon, dan N batas pembayaran penuh. Bandingkan kesempatan diskon dengan waktu tambahan kredit, bukan dengan seluruh tenor N. Pada model IPO, nilai ekonomis penggunaan proceeds dan definisi pre/post-money harus konsisten; jangan mengasumsikan seluruh biaya emisi menciptakan aset.

## Bab 21–22: leverage dinamis dan merger

| Konsep | Rumus |
|---|---|
| APV | Unlevered operating value + PV financing effects |
| Tax shield periodik sederhana | Interest × T |
| Growing tax-shield perpetuity | $TS_1/(r_{TS}-g)$ jika rTS > g dan proses risiko/pertumbuhan konsisten |
| Compressed APV | Diskontokan FCF dan tax shields sesuai asumsi rTS = unlevered cost of equity dalam model tersebut |
| Levered cost, MM no tax | $r_{sL}=r_{sU}+(r_{sU}-r_d)D/E$ |
| Levered cost, MM corporate tax | $r_{sL}=r_{sU}+(r_{sU}-r_d)(1-T)D/E$ |
| FCFE | FCF − interest × (1 − T) + net borrowing |
| FCFE value | PV FCFE eksplisit + PV terminal FCFE menggunakan biaya ekuitas sesuai periode |
| Target stockholder fraction | Value of shares received by target owners / total post-merger equity |
| Merger synergy | Combined value − standalone value A − standalone value B |

Jangan mencampurkan formula MM corporate-tax dengan compressed APV tanpa menyamakan asumsi risiko tax shield dan kebijakan utang. Pada merger, kurangi premium serta biaya integrasi yang belum diperhitungkan ketika menghitung keuntungan pembeli, tanpa menggandakan pengurangan yang sudah tercakup dalam combined value.

## Bab 23–24 dan 26

Bab ERM dan distress memerlukan analisis exposure, skenario, likuiditas, recovery, dan pilihan tindakan. Ketiadaan daftar formula tersendiri untuk dua bab itu di Appendix C tidak berarti bab tersebut tidak memiliki hitungan.

Untuk real options, sumber menghubungkan ketidakpastian PV proyek dengan volatilitas return menggunakan $\sigma^2=\ln(1+CV^2)/t$ dalam asumsi pemodelan terkait. Hubungan ini bukan prosedur universal mengubah semua risiko proyek menjadi volatilitas opsi. Definisikan aset dasar, tanggal keputusan, biaya exercise, hak eksklusif, dan pengaruh kompetisi sebelum memakai model opsi keuangan untuk aset riil.

## Pelengkap setelah pemeriksaan visual Appendix C

Bagian ini melengkapi bentuk dan transformasi yang tidak dirinci dalam tabel awal. Lokasi halaman membuat notasi sumber dan penulisan ulang dapat dibandingkan.

| PDF | Persamaan tambahan/transformasi | Penjelasan |
|---|---|---|
| 1122 | $FCF=OperatingCashFlow-GrossInvestmentInOperatingCapital$ | Dalam model operasi ini OCF = NOPAT + D&A; gross investment mencakup CAPEX dan perubahan NOWC. Jangan menyamakan OCF definisi model dengan semua klasifikasi laporan arus kas tanpa rekonsiliasi. |
| 1125 | $IP_N=(I_1+...+I_N)/N$ | Pendekatan rata-rata ekspektasi inflasi per tahun dalam dekomposisi yield buku. |
| 1125 | $\bar R=\sum_{t=1}^N R_t/N$ | Jumlah observasi pada penjumlahan dan denominator harus sama; huruf n dan T pada sumber perlu dibaca dalam konteks ini. |
| 1126 | $\hat\rho_{ij}=\sum_t(R_{it}-\bar R_i)(R_{jt}-\bar R_j)/\sqrt{\sum_t(R_{it}-\bar R_i)^2\sum_t(R_{jt}-\bar R_j)^2}$ | Korelasi sampel; faktor N−1 saling hapus. |
| 1126 | $RP_i=\beta_i RPM$ | Premi risiko sistematis menurut CAPM. |
| 1127 | Expected dividend yield = $D_1/P_0$; expected capital gain yield = $(\hat P_1-P_0)/P_0$ | Total expected equity return adalah penjumlahannya untuk periode sama; di Gordon growth, capital gain yield = g. |
| 1127 | $P_{put}=S[N(d_1)-1]-Ke^{-rT}[N(d_2)-1]$ | Bentuk put pada sumber; aljabarnya sama dengan put–call parity untuk opsi Eropa tanpa dividen. |
| 1127 | $NetProceeds=\sum_{t=1}^n C(1-T)/(1+y)^t+F/(1+y)^n$ | Untuk flotation utang, cari after-tax yield y dari proceeds neto dan arus kontraktual setelah pajak. Jika biaya/pengaruh pajak kompleks, jadwal harus disesuaikan. |
| 1128 | $r_M=(1+Rep/Div)D_1/P_0+g$ | Pendekatan payout yield pasar termasuk repurchases; D1, P0, dan g merujuk agregat pasar menurut sumber, bukan otomatis satu perusahaan. |
| 1130 | $V_{op}=FCF/WACC=NOPAT/WACC$ jika g = 0 dan net investment = 0 | NOPAT sama dengan FCF hanya di bawah asumsi reinvestasi neto nol ini. |
| 1130 | $V_L=E_L+D$; total corporate value = Vop + nonoperating short-term investments | Perhatikan apakah VL yang dimaksud mencakup aset nonoperasi pada suatu model. |
| 1130 | $D=w_dV_{op}$ dan $E=(1-w_d)V_{op}$ | Model sederhana tanpa preferen/aset nonoperasi. |
| 1130 | Dana recapitalization = $D_{new}-D_{old}$ | Untuk penerbitan utang yang seluruhnya dipakai membeli kembali saham, dengan asumsi model sumber. |
| 1130 | $P_{rep}=(V_{op,new}-D_{old})/n_{old}$ | Harga setelah informasi perubahan nilai diketahui, sebelum kas repurchase meninggalkan perusahaan, pada recapitalization adil tanpa friksi dalam model. |
| 1130 | $n_{new}=n_{old}-(D_{new}-D_{old})/P_{rep}$ | Karena saham yang dibeli kembali = kas repurchase / harga pembelian. |
| 1130 | $n_{new}=n_{old}(V_{op,new}-D_{new})/(V_{op,new}-D_{old})$ | Substitusi harga repurchase ke jumlah saham tersisa. |
| 1130 | $P_{post}=P_{rep}$ | Harga sebelum dan setelah pelaksanaan repurchase sama dalam model transaksi adil ini, setelah efek perubahan nilai terlebih dahulu diakui. Tidak menyatakan harga tidak pernah berubah saat pengumuman. |
| 1131 | $F_t=S[(1+r_{dom})/(1+r_{for})]^t$ | Bentuk multi-tahun dengan rates konstan dan kuotasi domestik per asing. Forward terikat parity bukan otomatis expected future spot. |
| 1131 | $n_{new}=q n_{old}/(1-q)$ | Turunan q = nNew/(nNew+nOld); 0 < q < 1. |
| 1132 | $P_{offer}=V_{pre}/(n_{old}+F n_{new})$ | Formula fair-price dengan flotation fraction F dalam model IPO buku; bukan proses bookbuilding universal. |
| 1132 | $q=I/[V_{pre}+(1-F)I]$ | I adalah dana bruto dari investor baru. Periksa model feasible dengan q < 1. |
| 1133 | $\beta_L=\beta_U+(\beta_U-\beta_D)D/E$ | Bentuk pada compressed APV dengan asumsi risiko tax shield terkait; jangan disamakan dengan Hamada bertarif (1−T). |
| 1133 | $r_{sU}=w_Er_{sL}+w_Dr_D$ | Hubungan pada kerangka compressed APV yang digunakan sumber. |
| 1133 | $HV_{U,N}=FCF_{N+1}/(r_{sU}-g)$ | Horizon value operasi tanpa leverage, dengan rsU > g. |
| 1133 | $HV_{TS,N}=TS_{N+1}/(r_{sU}-g)$ | Berlaku untuk asumsi rTS = rsU; gunakan risiko tax shield yang sesuai untuk model lain. |
| 1133 | $V_U=\sum_{t=1}^N FCF_t/(1+r_{sU})^t+HV_{U,N}/(1+r_{sU})^N$ | PV operasi tanpa leverage. |
| 1133 | $V_{TS}=\sum_{t=1}^N TS_t/(1+r_{sU})^t+HV_{TS,N}/(1+r_{sU})^N$ | Komponen terpisah tax shield pada compressed APV. |
| 1133 | $FCFE=NI-NetInvestmentInOperatingCapital+NetBorrowing$ | Dalam model sederhana dengan definisi NI, bunga, dan operasi konsisten. |
| 1133 | $HV_{FCFE,N}=FCFE_{N+1}/(r_{sL}-g)$ | Horizon stabil; jika leverage berubah, biaya ekuitas selama forecast dapat berbeda per periode. |
| 1133 | $E=V_{FCFE}+NonoperatingAssets$ | Tambahkan aset nonoperasi yang belum tercakup dalam FCFE. |
| 1133 | $q_{target}=n_{issued}/(n_{old}+n_{issued})$ | qtarget adalah bagian ekuitas gabungan yang diberikan kepada pemegang saham target. |
| 1134 | $\sigma_p=|1-w_{RF}|\sigma_M$ | Campuran aset risk-free dan portofolio pasar. Bentuk sumber tanpa absolut mengasumsikan bobot pasar tidak negatif. |
| 1134 | $CV=SD(PV\ future\ CF)/E(PV\ future\ CF)$ | CV khusus aset dasar model real option; berbeda dari CV NPV bila denominator/objek berbeda. |

### Derivasi recapitalization

Sebelum repurchase, setelah informasi recapitalization tercermin dalam nilai operasi, nilai yang tersedia untuk pemegang saham lama adalah $V_{op,new}-D_{old}$. Dengan nOld saham, harga adil pembelian kembali adalah nilai tersebut dibagi nOld. Perusahaan menerbitkan tambahan utang DNew−DOld dan membeli sejumlah kas/harga saham. Substitusi menghasilkan formula rasio nNew di tabel. Setelah kas keluar, ekuitas = VopNew−DNew; dibagi nNew, harga kembali sama dengan harga repurchase. Hasil ini bergantung pada transaksi adil dan asumsi sumber; jangan menerapkannya pada pembelian kembali di harga sembarang.

### Derivasi harga IPO dengan flotation

Nilai setelah pendanaan adalah $V_{post}=V_{pre}+(1-F)P_{offer}n_{new}$. Jika harga fair yang sama berlaku bagi semua saham setelah penawaran, $P_{offer}(n_{old}+n_{new})=V_{post}$. Pindahkan suku proceeds ke kiri sehingga $P_{offer}(n_{old}+Fn_{new})=V_{pre}$. Dari sini diperoleh formula harga pada tabel. Biaya emisi mengurangi proceeds yang menjadi aset perusahaan sehingga nilai bersih yang ditambahkan berbeda dari dana bruto investor.

## Yang belum diverifikasi

Seluruh 13 halaman Selected Equations telah dilihat secara visual dan kelompok formula serta transformasinya dirangkum di atas. Nomor seluruh persamaan pada isi utama belum dipetakan satu per satu ke register, dan pembuktian setiap formula spesifik belum seluruhnya dilakukan. Seluruh nomor kandidat persamaan yang terdeteksi disediakan di INVENTARIS_SUMBER.md; status kandidat tidak sama dengan validasi rumus atau pembahasan lengkap seluruh buku.
