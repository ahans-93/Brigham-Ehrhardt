# Integrasi dua file kompilasi rumus v2

Pembaruan 4 November 2026. Kedua berkas **Kompilasi_Lengkap_Rumus_Financial_Management_Brigham_Ehrhardt_v2**, format Markdown dan Word, dibaca lengkap. Markdown memuat **197 entri**; Word dibaca sampai baris 1.101 dari 19 halaman. Kedua format menyajikan kompilasi yang sama secara substansi, dengan tata letak berbeda.

- [Kompilasi terintegrasi: seluruh 197 entri](KOMPILASI_TERINTEGRASI.md)
- [12 kelompok pelengkap: variabel, logika, asumsi, dan contoh](LENGKAPAN.md)
- [Pemetaan terstruktur tiap entri](pemetaan-197-rumus.json)
- [Hasil pemeriksaan integrasi](hasil-verifikasi.json)
- [Markdown masukan](sumber/Kompilasi_Lengkap_Rumus_Financial_Management_Brigham_Ehrhardt_v2.md)
- [Ekstraksi teks lengkap Word](sumber/DOCX_teks_lengkap.txt)
- [Metadata dan batas pengarsipan](sumber-manifest.json)
- [Kajian manual sebelumnya: 236 persamaan bernomor](../kajian-rumus/README.md)

## Keputusan penggabungan

Kompilasi terintegrasi menjadi pintu baca cepat tambahan, sedangkan kajian manual sebelumnya tetap menjadi rujukan derivasi dan asumsi. Ada **50 entri** yang diberi penjelasan atau koreksi khusus. Seluruh 197 entri memiliki tautan kajian; pemetaan tidak menambah 197 rumus unik di luar inventaris lama karena banyak yang sama atau varian penyajian.

Bid–ask spread, EBIT/EBITDA, penggunaan FCF, growing annuity, CV, return aktual saham, estimasi total-payout pasar, NI/EPS, IPO money left, kepemilikan stock merger, dan pemetaan opsi riil dilengkapi dalam 12 kelompok pendamping.

NCF tidak disamakan dengan CFO/FCF; inventory turnover pada HPP dibedakan dari varian sales; EAR dibedakan dari bunga riil; YTC dibedakan dari valuasi callable bond lengkap; konvensi tanda NAL direkonsiliasi. Asumsi timing utang/shield, harga sebelum pengumuman versus sebelum eksekusi buyback, dan penghitungan kas nonoperasi pada FCFE juga diperjelas.

## Cakupan yang dipertahankan

Kompilasi v2 tidak mempunyai bagian tersendiri untuk Bab 13, 23, dan 24. Dokumentasi ketiga bab itu tetap tersedia dalam kajian lama. PDF asli, 26 bab teks sumber, 236 kajian bernomor, dan materi latihan tidak dihapus. Klaim kelengkapan judul masukan tidak dijadikan bukti bahwa semua soal atau sel spreadsheet telah diperiksa.

## Bentuk berkas yang tersimpan — diperbarui 5 November 2026

[Kedua file asli sudah tersimpan](sumber/unggahan-2026-11-05/README.md): Word `.docx` 58.473 byte dan Markdown/LaTeX terbaru 77.008 byte. File asli disalin tanpa perubahan dari Downloads. Unduhan melalui koneksi berkas sempat gagal; kekurangan arsip Word pada pembaruan sebelumnya kini diselesaikan melalui salinan lokal yang ditemukan pada jendela Downloads.

Markdown cocok byte demi byte dengan pembacaan unggahan terbaru. Word diperiksa sebagai paket DOCX valid berisi 23 tabel dan 197 baris rumus; seluruh nama, formula teks, halaman, dan keterangan cocok dengan sumber kompilasi sebelumnya setelah normalisasi format/spasi. [Hasil verifikasi dan SHA-256](verifikasi-arsip-2026-11-05.json) disertakan. Ekstraksi teks lama dipertahankan sebagai jejak pembacaan awal.

Seluruh 197 kolom formula masukan terbaru sudah diperbarui ke LaTeX pada data pemetaan dan kompilasi terintegrasi. Nama rumus, bab, halaman, dan keterangan tidak berubah; 50 catatan penjelasan/koreksi tetap dipakai. Format LaTeX bukan bukti bahwa setiap rumus masukan sudah benar tanpa syarat.

## Pemeriksaan

Seluruh **197 entri terpetakan**, semua target dan anchor kajian tersedia, dan **30 pemeriksaan numerik tambahan lulus**. Pemeriksaan lama sebanyak 298 dan 42 juga tetap lulus; total 370 pemeriksaan. Angka ini adalah jumlah pemeriksaan, bukan jumlah rumus unik atau soal buku yang sudah diselesaikan.

Jalankan `python verify_v2_integration.py` dari root repository. Pemeriksaan memastikan 197 entri terpetakan, target dan anchor kajian tersedia, contoh tambahan dihitung ulang, dan identitas lintas cara (growing annuity, FCF uses, NAL, serta timing opsi) konsisten. Pemeriksaan lama dapat dijalankan dengan `python verify_formula_review.py` dan `python verify_calculations.py`.
