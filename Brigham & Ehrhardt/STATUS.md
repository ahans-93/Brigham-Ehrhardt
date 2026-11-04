# Status pekerjaan dan batas hasil

Tanggal: 4 November 2026.

| Komponen | Status |
|---|---|
| Identitas sumber | 15e, Cengage 2017, ISBN 978-1-305-63229-5 |
| Ukuran PDF sumber | 18.123.922 byte; 1.221 halaman |
| Teks sumber | 80.851 baris hasil pembacaan; 4.214.743 karakter sesudah penggabungan |
| Cakupan penanda halaman | 1–1.221, tepat satu kali, tanpa rentang terlewat |
| Bab utama | 26 file Markdown dengan rujukan halaman PDF |
| Bagian tambahan | Bagian awal, Appendix A–D, glosarium, indeks |
| Navigasi | README.md dan SUMMARY.md |
| Panduan belajar | Sintesis pengantar seluruh 26 bab, formula standar, delapan kelompok contoh baru |
| Register rumus | Seluruh 13 halaman Selected Equations Appendix C telah diperiksa secara visual; register, asumsi, transformasi, dan derivasi inti tersedia; pemetaan semua persamaan isi utama belum selesai |
| Pembahasan ulang soal sumber | Sembilan kelompok soal sumber; 42 pemeriksaan hitung lulus termasuk contoh panduan |
| Inventaris | 397 kandidat nomor, 283 lokasi halaman dengan penanda self-test, 104 penanda bagian soal/pertanyaan; hasil deteksi, bukan jumlah soal final |
| Pemeriksaan seluruh rumus/tabel terhadap gambar PDF | Belum selesai |
| Pembahasan manual setiap contoh dan soal | Belum selesai |
| PDF biner asli di repository | Tersedia: Financial_Management_Theory_and_Practice_15e.pdf, 18.123.922 byte, 1.221 halaman; salinan lokal ditemukan di Downloads dan diunggah melalui browser |
| GitBook/Jekyll live | Belum diterbitkan; yang disediakan adalah sumber Markdown |
| Metode penyimpanan GitHub | Git remote-helper ghapp memakai koneksi GitHub terautentikasi, dengan verifikasi SHA; lihat PUSH_TRANSPORT.md di root |
| git push | Menggunakan remote connected melalui adaptor sesi; HTTPS native origin tetap gagal ke github.com:443 |

## Keterbatasan sumber

Ekstraksi mempertahankan teks yang bisa dibaca dari PDF. Cakupan penanda halaman bukan bukti bahwa seluruh konten visual ikut terambil. Sebagian operator persamaan, huruf Yunani, superscript/subscript, dan struktur tabel rusak atau hilang. Watermark dan pemberitahuan hak cipta berulang dipertahankan di teks sumber. Blok teks sumber bukan salinan tata letak PDF.

Bab 27–30 tercantum sebagai Web Chapters pada daftar isi. PDF yang tersedia tidak memuat teks bab-bab web tersebut. File Web Extensions dan Excel Tool Kits juga belum disertakan sebagai materi mandiri. Penyebutannya dalam teks tidak berarti file eksternalnya sudah diarsipkan.

## Pemeriksaan yang sudah dilakukan

Rentang pembacaan teks dirangkai berurutan dari baris 1 sampai 80.851. Seluruh penanda halaman 1 sampai 1.221 diperiksa secara programatis. Pembagian bab menggunakan halaman cetak daftar isi dengan offset PDF +37; judul pada halaman awal bab dicocokkan. Navigasi lokal dan contoh hitung panduan diperiksa. Pemeriksaan ini tidak menggantikan pembacaan rinci dan pembuktian setiap persamaan.

## Yang masih diperlukan agar permintaan awal tuntas

1. PDF biner asli sudah ditambahkan; SHA-256: 1638b312422c14a3b870c27fd16f4498ba5ed3de8cb63ea278ad1ab4862ce56c.
2. Untuk Git biasa di luar adaptor sesi ini, koneksi HTTPS dan autentikasi terminal harus tersedia. Publikasi melalui adaptor dijelaskan di PUSH_TRANSPORT.md.
3. Menyelesaikan kajian mendalam per subbab, derivasi rumus, pembahasan contoh, serta penyelesaian soal secara manual.
4. Membandingkan seluruh tabel, grafik, dan rumus dengan halaman PDF untuk memperbaiki konversi.
5. Menyediakan Web Chapters/Extensions/Tool Kits jika pemilik mempunyai file materinya.

## Mengirim perubahan berikutnya dengan Git

Sesudah Git dan autentikasi tersedia pada komputer, clone repository privat berikut, tambahkan file PDF atau perbaikan dokumentasi, lalu commit dan push:

```powershell
git clone https://github.com/ahans-93/Brigham-Ehrhardt.git
Set-Location Brigham-Ehrhardt
# Tambahkan PDF dan perubahan dokumentasi ke folder Brigham & Ehrhardt.
git add -- 'Brigham & Ehrhardt'
git commit -m 'docs: add source PDF and verified study notes'
git push origin main
```

Login browser tidak otomatis menyediakan autentikasi untuk Git di terminal. Jangan meletakkan password atau token di file dokumentasi maupun URL remote.
