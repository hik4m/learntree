import os

bersih = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class Barang():
    def __init__(
        self,
        kodeBarang: str,
        namaBarang: str,
        stok: int,
        harga: int
    ):
        if stok < 0:
            raise ValueError("Stok tidak boleh kurang dari 0.")

        if harga < 0:
            raise ValueError("Harga tidak boleh kurang dari 0.")

        self.kodeBarang = kodeBarang
        self.namaBarang = namaBarang
        self.stok = stok
        self.harga = harga

    def hitungHarga(self, jumlah: int):
        if jumlah <= 0:
            print("Jumlah barang harus lebih dari 0.")
            return 0

        return self.harga * jumlah

    def kurangiStok(self, jumlah: int):
        if jumlah <= 0:
            print("Jumlah barang yang dibeli harus lebih dari 0.")
            return False

        if jumlah > self.stok:
            print(
                f"Stok dari barang {self.namaBarang} tidak cukup."
                f"\nStok saat ini : {self.stok} unit."
            )
            return False

        self.stok -= jumlah

        print(
            f"Stok dari barang {self.namaBarang} berhasil dikurangi "
            f"sebanyak {jumlah} unit."
            f"\nStok saat ini : {self.stok} unit."
        )

        return True

    def tambahStok(self, jumlah: int):
        if jumlah <= 0:
            print("Jumlah stok yang ditambahkan harus lebih dari 0.")
            return False

        self.stok += jumlah

        print(
            f"Stok dari barang {self.namaBarang} berhasil ditambahkan "
            f"sebanyak {jumlah} unit."
            f"\nStok saat ini : {self.stok} unit."
        )

        return True

    def info(self):
        print(f"Kode Barang  : {self.kodeBarang}")
        print(f"Nama Barang  : {self.namaBarang}")
        print(f"Harga Barang : Rp{self.harga}")
        print(f"Stok Barang  : {self.stok}")
        print("==================================")


def cariBarang(listBarang, keyword):
    keyword = keyword.strip().lower()

    def cari(index):
        if index >= len(listBarang):
            return None

        barang = listBarang[index]
        kode = barang.kodeBarang.lower()
        nama = barang.namaBarang.lower()

        if kode == keyword or nama == keyword:
            return barang

        if kode.startswith(keyword) or nama.startswith(keyword):
            return barang

        return cari(index + 1)

    if not keyword:
        return None

    hasil = cari(0)
    if hasil is not None:
        return hasil

    # Jika tidak ada awalan yang cocok, cari keyword di bagian mana pun.
    def cariSebagian(index):
        if index >= len(listBarang):
            return None

        barang = listBarang[index]
        if (keyword in barang.kodeBarang.lower() or
                keyword in barang.namaBarang.lower()):
            return barang

        return cariSebagian(index + 1)

    return cariSebagian(0)


def totalAset(listBarang):
    total = 0

    for barang in listBarang:
        total += barang.stok * barang.harga

    return total


def filterStok(listBarang):
    if len(listBarang) == 0:
        return None, None

    stokTerbanyak = listBarang[0]
    stokTerdikit = listBarang[0]

    for barang in listBarang:
        if barang.stok > stokTerbanyak.stok:
            stokTerbanyak = barang

        if barang.stok < stokTerdikit.stok:
            stokTerdikit = barang

    return stokTerbanyak, stokTerdikit


listBarang = [
    Barang("B001", "Buku Tulis", 100, 5000),
    Barang("B002", "Pensil", 200, 2000),
    Barang("B003", "Penghapus", 150, 3000),
]


while True:
    print("\n==========[MENU KASIR]==========")
    print("1. Tampilkan semua barang")
    print("2. Cari barang")
    print("3. Beli barang")
    print("4. Tambah stok")
    print("5. Total aset barang")
    print("6. Stok terbanyak dan terdikit")
    print("7. Keluar")
    print("================================")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        bersih()
        print("\n==========[DAFTAR BARANG]==========")

        if len(listBarang) == 0:
            print("Belum ada barang.")
        else:
            for barang in listBarang:
                barang.info()

    elif pilihan == "2":
        bersih()
        print("\n==========[CARI BARANG]==========")

        keyword = input("Masukkan kode/nama barang : ")

        barang = cariBarang(listBarang, keyword)

        if barang is None:
            print(f"Barang dengan kode {keyword} tidak ditemukan.")
        else:
            barang.info()

    elif pilihan == "3":
        bersih()
        print("\n==========[PEMBELIAN BARANG]==========")

        keyword = input("Masukkan kode/nama barang : ")
        barang = cariBarang(listBarang, keyword)

        if barang is None:
            print(f"Barang dengan kode {keyword} tidak ditemukan.")
            continue

        try:
            jumlahBeli = int(input("Jumlah yang dibeli : "))

            totalHarga = barang.hitungHarga(jumlahBeli)

            if totalHarga == 0:
                continue

            if barang.kurangiStok(jumlahBeli):
                print("\n==========[INFO PEMBELIAN]==========")
                print(f"Barang yang dibeli  : {barang.namaBarang}")
                print(f"Jumlah yang dibeli  : {jumlahBeli}")
                print(f"Total harga         : Rp{totalHarga}")
                print("====================================")

        except ValueError:
            print("Jumlah barang harus berupa angka.")

    elif pilihan == "4":
        bersih()
        print("\n==========[TAMBAH STOK]==========")

        keyword = input("Masukkan kode/nama barang : ")
        barang = cariBarang(listBarang, keyword)

        if barang is None:
            print(f"Barang dengan kode {keyword} tidak ditemukan.")
            continue

        try:
            jumlahStok = int(input("Jumlah stok yang ditambahkan : "))
            barang.tambahStok(jumlahStok)

        except ValueError:
            print("Jumlah stok harus berupa angka.")

    elif pilihan == "5":
        bersih()
        print("\n==========[TOTAL ASET]==========")

        total = totalAset(listBarang)

        print(f"Total aset seluruh barang : Rp{total}")
        print("================================")

    elif pilihan == "6":
        bersih()
        print("\n==========[FILTER STOK]==========")

        stokTerbanyak, stokTerdikit = filterStok(listBarang)

        if stokTerbanyak is None:
            print("Belum ada barang.")
        else:
            print(
                f"Stok terbanyak : "
                f"{stokTerbanyak.namaBarang} "
                f"({stokTerbanyak.stok} unit)"
            )

            print(
                f"Stok terdikit  : "
                f"{stokTerdikit.namaBarang} "
                f"({stokTerdikit.stok} unit)"
            )

        print("=================================")

    elif pilihan == "7":
        bersih()
        print("\n==========[PROGRAM SELESAI]==========")
        print("Terima kasih telah menggunakan aplikasi kasir.")
        print("======================================")
        break

    else:
        print("Pilihan menu tidak tersedia.")