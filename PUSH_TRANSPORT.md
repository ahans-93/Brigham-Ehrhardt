# Publikasi melalui Git dan koneksi GitHub terautentikasi

Pada 4 November 2026, perintah native `git push origin main` dalam lingkungan terminal sesi ChatGPT gagal menghubungi github.com:443 sebelum autentikasi. Konfigurasi proxy Git tidak ditemukan sebagai penyebab. Login browser tidak otomatis memperbaiki jalur jaringan terminal.

Untuk publikasi sesi ini digunakan transport Git tambahan bernama `ghapp`, dengan remote lokal `connected`. Transport tersebut mengoordinasikan permintaan Git dengan koneksi GitHub yang sudah diotorisasi pengguna:

1. Blob, tree, dan commit disiapkan melalui GitHub API terautentikasi.
2. Isi tree dan SHA commit dibandingkan dengan objek Git lokal.
3. `git push connected main:main` memanggil remote-helper lokal.
4. Helper menerima permintaan push dan meminta pembaruan branch dengan guard SHA parent saat ini; force push dan penghapusan branch ditolak.
5. Coordinator memperbarui ref melalui koneksi GitHub dan membaca ulang ref tersebut.
6. Helper hanya menjawab sukses bila SHA remote hasil verifikasi tepat sama dengan SHA yang diminta Git.

Transport ini adalah adaptor sesi ChatGPT, **bukan perbaikan koneksi HTTPS langsung**, bukan akses jaringan baru untuk seluruh terminal, dan bukan autentikasi Git permanen di komputer. Tidak ada password atau token GitHub disimpan di repository. Adaptor dan receipt operasional berada di workspace sesi, bukan bagian materi buku.

Untuk penggunaan Git biasa di terminal pengguna yang memiliki koneksi GitHub dan autentikasi sendiri:

```powershell
git clone https://github.com/ahans-93/Brigham-Ehrhardt.git
Set-Location Brigham-Ehrhardt
# Edit atau tambahkan materi.
git add --all
git commit -m 'docs: update verified study material'
git push origin main
```

Jangan menjalankan force push untuk mengatasi perbedaan riwayat. Ambil perubahan remote terlebih dahulu dan selesaikan perbedaan isi secara sadar.
