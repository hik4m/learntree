class Buku: 

    def __init__(self, judul, stok, penulis):
         self.judul = judul 
         self.penulis = penulis 
         self.stok = stok 

    def pinjam(self): 
        if self.stok <= 0: 
            print(f"{self.judul} sedang habis stok") 
            self.stok -= 1 
            return True 

    def kembalikan(self): 
        self.stok += 1 
        return True 

class Peminjam: 

    def __init__(self, nama, idAnggota): 
        self.nama = nama 
        self.idAnggota = idAnggota 

class Peminjaman: 
    
    def __init__(self, buku, peminjam, tanggalPinjam): 
        self.buku = buku 
        self.peminjam = peminjam 
        self.tanggalPinjam = tanggalPinjam 
        self.tanggalKembali = None 
        self.denda = 0 
        self.status = "dipinjam" 

        if not self.buku.pinjam(): 
            print("Buku tidak tersedia untuk dipinjam") 

    def kembalikan(self, tanggalKembali): 
        if self.status != "dipinjam": 
            print("Buku ini sudah dikembalikan") 
            return 

        self.tanggalKembali = tanggalKembali 
        self.buku.kembalikan() 
        self.status = "dikembalikan" 

        selisihHari = (tanggalKembali - self.tanggalPinjam).days 
        if selisihHari > 7: 
            self.denda = (selisihHari - 7) * 2000 