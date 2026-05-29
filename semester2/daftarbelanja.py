# Inisialisasi dictionary buat menyimpan daftar belanja
daftar_belanja = {}

# 1. Procedure: Menambahkan item dengan iniisilasia harga Rp0
def tambah_item(nama_barang, harga=0):
    daftar_belanja[nama_barang] = harga
    print(f"✅ '{nama_barang}' (Rp{harga}) berhasil dimasukkan ke keranjang.")

# 2. Procedure: Menampilkan daftar 
def lihat_daftar():
    print("\n=====[ DAFTAR BELANJA ]=====")
    if not daftar_belanja:
        print("Keranjang belanja masih kosong.") # Kalo daftar belanja kosong
    else:
      # Looping buat output nanti
        for barang, harga in daftar_belanja.items():
            print(f"- {barang} : Rp{harga}")
    print("=======================")

# 3. Fungsi Return Value: Menghitung total dari value dictionary fungsi daftar belanja
def hitung_total():
    return sum(daftar_belanja.values())

# ==========================================
# PROGRAM UTAMA
# ==========================================
print("=======================")
print("Selamat Datang di Program Daftar Belanja!")
print("=======================")

# Pake looping while karna kondisi stop nya udah tau pake kondisi, kalo pake for saya tidam bisa
while True:
    print("\n=====[ MENU ]=====")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Selesai Belanja & Hitung Total")
    
    pilihan = input("Pilih menu (1/2/3): ")
    print("=======================")
    
    if pilihan == '1':
        nama_input = input("Masukkan nama barang: ")
        harga_input = input("Masukkan harga barang (tekan Enter/kosongkan jika gratis): ")
        print("=======================")
        
        # Cek apakah input harga kosong
        if harga_input == "":
            tambah_item(nama_input)
        else:
            # Pastikan harga yang diinput adalah angka pake try except
            try:
                harga_angka = int(harga_input)
                tambah_item(nama_input, harga_angka)
            except ValueError:
                print("❌ Error: Harga harus berupa angka! Silakan coba lagi.")
        print("=======================")

    elif pilihan == '2':
        lihat_daftar() # Kalo pilihan 2 = fungsi lihat daftar berjalan
        print("=======================")

    elif pilihan == '3':
        lihat_daftar()
        print("=======================")
        total_belanja = hitung_total()
        print(f"\n=====[ TOTAL BELANJA ]=====")
        print(f"Total yang harus dibayar: Rp{total_belanja}")
        print("Terima kasih telah berbelanja!")
        print("=======================")
        break # Menghentikan perulangan

    else:
        print("❌ Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        print("=======================")