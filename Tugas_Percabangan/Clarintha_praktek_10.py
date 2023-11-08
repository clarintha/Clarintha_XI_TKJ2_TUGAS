#nama: Clarintha Chelsy N
#Kelas: XI TKJ 2
#Absen: 07
#Soal: Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman.

durasi_peminjaman = int(input("Masukkan durasi peminjaman dalam hari: "))

if durasi_peminjaman <= 7:
    jenis_pinjaman = "Peminjaman Pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_pinjaman = "Peminjaman Menengah"
else:
    jenis_pinjaman = "Peminjaman Panjang"

print("Jenis Pinjaman:", jenis_pinjaman)