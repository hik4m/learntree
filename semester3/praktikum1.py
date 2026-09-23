class Barang():
    def __init__(self, 
    kodeBarang: str, 
    namaBarang: str, 
    stok: int, 
    harga: int):
        self.kode = kodeBarang
        self.nama = namaBarang
        self.stok = stok
        self.harga = harga

    def hitungHarga (self, jumlah: int): 
        return self.harga * jumlah

    def kurangiStok(self, jumlah: int):
        if jumlah > self.stok:
            print(f"Stok dari barang {self.nama} tidak cukup \nStok saat ini : {self.stok} unit.")
            return False
        elif jumlah <= 0:
            print("Jumlah barang yang dibeli harus lebih dari 0 bang.")
            return False
        else:
            self.stok -= jumlah
            print(f"Stok dari barang {self.nama} berhasil dikurangi sebanyak {jumlah} unit. \nStok saat ini : {self.stok} unit.")
            return True

    def info(self):
        print("==========[INFO BARANG]==========")
        print(f"Kode Barang  : {self.kode}")
        print(f"Nama Barang  : {self.nama}")
        print(f"Harga Barang : {self.harga}") 
        print(f"Stok Barang  : {self.stok}")
        print("==================================")


listBarang = [ 
    Barang("B001", "Buku Tulis", 100, 5000),
    Barang("B002", "Pensil", 200, 2000),
    Barang("B003", "Penghapus", 150, 3000),
]

for barang in listBarang:
    barang.info()

dibeli = listBarang[0]
jumlahBeli = 10

print("==========[INFO PEMBELIAN]==========")
print(f"Barang yang dibeli  : {dibeli.nama}")
print(f"Jumlah yang dibeli  : {jumlahBeli}")
print(f"Total harga         : {dibeli.hitungHarga(jumlahBeli)}\n")

dibeli.kurangiStok(jumlahBeli)

dibeli.info()

listBarang[1].kurangiStok(50)