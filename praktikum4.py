# ==========================================
# 1. PROGRAM DAFTAR BELANJA
# ==========================================
def programBelanja():
    daftar = []
    while True:
        print("\n=====[ MENU DAFTAR BELANJA ]=====")
        print("1. Tambah Item\n2. Hapus Item\n3. Tampilkan Semua\n4. Total Item\n0. Kembali")
        pilihan = input("Pilih aksi (0-4): ")
        print("=======================")
        
        if pilihan == '1':
            item = input("Masukkan nama item: ")
            daftar.append(item) # Method List
            print(f"'{item} berhasil ditambahkan.")
            print("=======================")
        elif pilihan == '2':
            item = input("Masukkan nama item yang akan dihapus: ")
            if item in daftar:
                daftar.remove(item) # Method List
                print(f"'{item}' berhasil dihapus.")
            else:
                print("Item tidak ditemukan!")
            print("=======================")
        elif pilihan == '3':
            if daftar:
                print("Daftar saat ini:")
                for item in daftar:
                    print(f"  - {item}")
            else:
                print("Daftar kosong.")
            print("=======================")
        elif pilihan == '4':
            print(f"\nTotal item di keranjang: {len(daftar)}") # Method List
            print("=======================")
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.")

# ==========================================
# 2. PROGRAM KONVERSI SUHU
# ==========================================
def programSuhu():
    print("\n=====[ KONVERSI SUHU ]=====")
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    print("=======================")
    
    # Tuple berisi anonymous function (lambda)
    rumusKonversi = (lambda c: (c * 9/5) + 32, lambda c: c + 273.15)
    
    # Tuple unpacking
    rumusF, rumusK = rumusKonversi
    
    print(f"\n=====[ HASIL KONVERSI ]=====")
    print(f"{celsius}°C = {rumusF(celsius)}°F")
    print(f"{celsius}°C = {rumusK(celsius)} K")
    print("=======================")

# ==========================================
# 3. PROGRAM PERPUSTAKAAN SEDERHANA
# ==========================================
def programPerpus():
    perpus = []
    while True:
        print("\n=====[ MENU PERPUSTAKAAN ]=====")
        print("1. Tambah Buku | 2. Hapus Buku | 3. Cari Judul | 4. Buku Terbitan > 2020 | 0. Kembali")
        pilihan = input("Pilih aksi (0-4): ")
        print("=======================")
        
        if pilihan == '1':
            judul = input("Judul: ")
            penulis = input("Penulis: ")
            tahun = int(input("Tahun: "))
            perpus.append((judul, penulis, tahun)) # Simpan sebagai List of Tuples
            print("Buku ditambahkan.")
            print("=======================")
        elif pilihan == '2':
            judul = input("Judul yang akan dihapus: ")
            for buku in perpus:
                if buku[0] == judul:
                    perpus.remove(buku)
                    print("Buku dihapus.")
                    break
            print("=======================")
        elif pilihan == '3':
            judulCari = input("Masukkan judul yang dicari: ")
            # List Comprehension
            hasil = [buku for buku in perpus if buku[0] == judulCari]
            print(f"Hasil pencarian: {hasil}")
            print("=======================")
        elif pilihan == '4':
            # List Comprehension + Tuple Unpacking
            bukuBaru = [(j, p, t) for j, p, t in perpus if t > 2020]
            print(f"Buku terbitan setelah 2020: {bukuBaru}")
            print("=======================")
        elif pilihan == '0':
            break

# ==========================================
# 4. PROGRAM STATISTIK NILAI KELAS
# ==========================================
def programStatistik():
    print("\n=====[ STATISTIK NILAI KELAS ]=====")
    inputNilai = input("Masukkan nilai siswa, pisahkan dengan spasi (cth: 80 90 65 50): ")
    print("=======================")
    
    # Mengubah string input menjadi list of integers
    if not inputNilai:
        print("Tidak ada nilai yang dimasukkan.")
        return
        
    nilai = [int(x) for x in inputNilai.split()]
    # Menggunakan fungsi built-in untuk menghitung rata-rata, tertinggi(max), terendah(min), dan ranking(sorted)
    rataRata = sum(nilai) / len(nilai)
    tertinggi = max(nilai)
    terendah = min(nilai)
    ranking3 = sorted(nilai, reverse=True)[:3] #Menggunakan reverse untuk mendapatkan ranking tertinggi dan slicing untuk mengambil 3 teratas
    
    # List comprehension menghitung yang lulus
    jumlahLulus = len([n for n in nilai if n >= 60])
    
    print("\n=====[ STATISTIK KELAS ]=====")
    print(f"Rata-rata kelas  : {rataRata:.2f}")
    print(f"Nilai tertinggi  : {tertinggi}")
    print(f"Nilai terendah   : {terendah}")
    print(f"Ranking 3 teratas: {ranking3}")
    print(f"Jumlah lulus     : {jumlahLulus} siswa")
    print("=======================")

# ==========================================
# MENU UTAMA (MAIN LOOP)
# ==========================================
def main():
    while True:
        print("\n" + "="*35)
        print("=====[ MENU LATIHAN PYTHON ]=====")
        print("="*35)
        print("1. Program Daftar Belanja")
        print("2. Program Konversi Suhu")
        print("3. Program Perpustakaan Sederhana")
        print("4. Program Statistik Nilai Kelas")
        print("0. Keluar Aplikasi")
        print("="*35)
        
        pilihanUtama = input("Pilih program yang ingin dijalankan (0-4): ")
        print("=======================")
        
        if pilihanUtama == '1':
            programBelanja()
        elif pilihanUtama == '2':
            programSuhu()
        elif pilihanUtama == '3':
            programPerpus()
        elif pilihanUtama == '4':
            programStatistik()
        elif pilihanUtama == '0':
            print("\n=====[ TERIMA KASIH ]=====")
            print("Program selesai.")
            print("=======================")
            break
        else:
            print("Pilihan tidak ada. Silakan coba lagi.")
            print("=======================")

# Eksekusi Program
if __name__ == "__main__":
    main()