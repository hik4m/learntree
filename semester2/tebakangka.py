# impor library random buat jawaban angka random
import random
# variabel untuk menyimpan angka benar secara random 1 sampai 100
angkaBenar = random.randint(1, 100)
# JUDUL PROGRAM
print("PROGRAM TEBAK ANGKA DARI 1 - 100")

# (PERULANGAN WHILE) While true akan berulang terus-menerus sampai ada pernyataan 'break'
while True:
    # input tebakan angka dan akan berulang terus sampai pada kondisi 'break'
    tebakan = int(input('TEBAK ANGKANYE BANG : '))
    # if-elif-else
    # jika input tebakan sama dengan angka yang benar maka akan mengeluarkan output dan menghentikan perulangan
    if tebakan == angkaBenar:
        print("KEREN, ANGKA BENAR JIR")
        break # perulangan dihentikan
    # jika angka tebakan lebih besar dari angka benar maka akan menampilkan petunjuk bawah
    elif tebakan > angkaBenar:
        print("Belum tepat, Petunjuk : Bawah")
    # jika angka tebakan lebih besar dari angka benar maka akan menampilkan petunjuk atas
    elif tebakan < angkaBenar:
        print("Belum tepat, Petunjuk : Atas")
