from datetime import date

class Buku:
    def __init__(self, idBuku, judul, penulis, stok):
        if not isinstance(idBuku, str) or not idBuku.strip():
            raise ValueError("ID buku harus diisi dengan benar")
        if not isinstance(judul, str) or not judul.strip():
            raise ValueError("Judul buku harus diisi")
        if not isinstance(penulis, str) or not penulis.strip():
            raise ValueError("Penulis buku harus diisi")
        if not isinstance(stok, int) or stok < 0:
            raise ValueError("Stok harus bilangan bulat non-negatif")

        self.idBuku = idBuku
        self.judul = judul
        self.penulis = penulis
        self._stok = stok

    @property
    def stok(self):
        return self._stok

    def pinjam(self):
        if self._stok <= 0:
            raise ValueError(f"{self.judul} sedang habis stok")
        self._stok -= 1
        return True

    def kembalikan(self):
        self._stok += 1
        return True

    def __str__(self):
        return f"{self.judul} (stok: {self._stok})"


class Peminjam:
    def __init__(self, idAnggota, nama):
        if not isinstance(idAnggota, str) or not idAnggota.strip():
            raise ValueError("ID anggota harus diisi")
        if not isinstance(nama, str) or not nama.strip():
            raise ValueError("Nama peminjam harus diisi")

        self.idAnggota = idAnggota
        self.nama = nama

    def __str__(self):
        return f"{self.nama} ({self.idAnggota})"


class Peminjaman:
    BATAS_HARI_PINJAM = 7
    DENDA_PER_HARI = 5000

    def __init__(self, idPeminjaman, buku, peminjam, tanggalPinjam):
        if not isinstance(buku, Buku):
            raise TypeError("buku harus objek dari class Buku")
        if not isinstance(peminjam, Peminjam):
            raise TypeError("peminjam harus objek dari class Peminjam")
        if not isinstance(tanggalPinjam, date):
            raise TypeError("tanggalPinjam harus berupa objek date")

        self.idPeminjaman = idPeminjaman
        self.buku = buku
        self.peminjam = peminjam
        self.tanggalPinjam = tanggalPinjam
        self.tanggalKembali = None
        self.denda = 0
        self.status = "dipinjam"

        self.buku.pinjam()

    def kembalikan(self, tanggalKembali):
        if self.status != "dipinjam":
            raise ValueError("Buku ini sudah dikembalikan")
        if not isinstance(tanggalKembali, date):
            raise TypeError("tanggalKembali harus berupa objek date")
        if tanggalKembali < self.tanggalPinjam:
            raise ValueError("Tanggal kembali tidak boleh sebelum tanggal pinjam")

        self.tanggalKembali = tanggalKembali
        selisihHari = (tanggalKembali - self.tanggalPinjam).days

        if selisihHari > self.BATAS_HARI_PINJAM:
            terlambat = selisihHari - self.BATAS_HARI_PINJAM
            self.denda = terlambat * self.DENDA_PER_HARI

        self.buku.kembalikan()
        self.status = "dikembalikan"
        return self.denda

    def __str__(self):
        return f"{self.peminjam.nama} meminjam {self.buku.judul}"


class Perpustakaan:
    def __init__(self):
        self.daftarBuku = {}
        self.daftarPeminjam = {}
        self.daftarPeminjaman = {}
        self.nomorPeminjaman = 0

    def tambahBuku(self, buku):
        if not isinstance(buku, Buku):
            raise TypeError("buku harus objek dari class Buku")
        if buku.idBuku in self.daftarBuku:
            raise ValueError(f"Buku dengan ID {buku.idBuku} sudah terdaftar")
        self.daftarBuku[buku.idBuku] = buku

    def tambahPeminjam(self, peminjam):
        if not isinstance(peminjam, Peminjam):
            raise TypeError("peminjam harus objek dari class Peminjam")
        if peminjam.idAnggota in self.daftarPeminjam:
            raise ValueError(f"Peminjam dengan ID {peminjam.idAnggota} sudah terdaftar")
        self.daftarPeminjam[peminjam.idAnggota] = peminjam

    def pinjamBuku(self, idBuku, idAnggota, tanggalPinjam):
        if idBuku not in self.daftarBuku:
            raise ValueError("Buku tidak ditemukan")
        if idAnggota not in self.daftarPeminjam:
            raise ValueError("Peminjam tidak ditemukan")

        buku = self.daftarBuku[idBuku]
        peminjam = self.daftarPeminjam[idAnggota]

        self.nomorPeminjaman += 1
        idPeminjaman = f"P{self.nomorPeminjaman:04d}"
        peminjaman = Peminjaman(idPeminjaman, buku, peminjam, tanggalPinjam)
        self.daftarPeminjaman[idPeminjaman] = peminjaman
        return peminjaman

    def kembalikanBuku(self, idPeminjaman, tanggalKembali):
        if idPeminjaman not in self.daftarPeminjaman:
            raise ValueError("Peminjaman tidak ditemukan")

        peminjaman = self.daftarPeminjaman[idPeminjaman]
        return peminjaman.kembalikan(tanggalKembali)


if __name__ == "__main__":
    perpus = Perpustakaan()

    buku1 = Buku("B001", "Python Dasar", "Andi", 1)
    buku2 = Buku("B002", "Struktur Data", "Budi", 3)
    peminjam1 = Peminjam("A001", "Hikam")

    perpus.tambahBuku(buku1)
    perpus.tambahBuku(buku2)
    perpus.tambahPeminjam(peminjam1)

    transaksi = perpus.pinjamBuku("B001", "A001", date(2026, 9, 20))
    print(transaksi)
    print(f"Stok setelah pinjam: {buku1.stok}")

    denda = perpus.kembalikanBuku(transaksi.idPeminjaman, date(2026, 9, 30))
    print(f"Denda: Rp{denda}")
    print(f"Stok setelah dikembalikan: {buku1.stok}")