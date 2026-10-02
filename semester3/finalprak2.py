from abc import ABC, abstractmethod
from decimal import Decimal


class Kendaraan(ABC):
    def __init__(self, plat_nomor, tarif_dasar):
        if not isinstance(plat_nomor, str):
            raise TypeError("Plat nomor harus berupa string.")

        if not plat_nomor.strip():
            raise ValueError("Plat nomor tidak boleh kosong.")

        self.__plat_nomor = plat_nomor.strip()
        self.tarif_dasar = tarif_dasar

    @property
    def plat_nomor(self):
        return self.__plat_nomor

    @property
    def tarif_dasar(self):
        return self._tarif_dasar

    @tarif_dasar.setter
    def tarif_dasar(self, nilai):
        if not isinstance(nilai, Decimal):
            raise TypeError("Tarif dasar harus berupa Decimal.")

        if nilai < 0:
            raise ValueError("Tarif dasar tidak boleh negatif.")

        self._tarif_dasar = nilai

    @abstractmethod
    def hitung_biaya_sewa(self, lama_hari):
        raise NotImplementedError("Method harus dibuat di class turunan.")


class Motor(Kendaraan):

    def hitung_biaya_sewa(self, lama_hari):
        if not isinstance(lama_hari, int):
            raise TypeError("Lama hari harus berupa integer.")

        if lama_hari <= 0:
            raise ValueError("Lama hari harus lebih dari 0.")

        return self.tarif_dasar * lama_hari


class Mobil(Kendaraan):

    def hitung_biaya_sewa(self, lama_hari):
        if not isinstance(lama_hari, int):
            raise TypeError("Lama hari harus berupa integer.")

        if lama_hari <= 0:
            raise ValueError("Lama hari harus lebih dari 0.")

        asuransi = Decimal("50000")

        return (self.tarif_dasar * lama_hari) + asuransi


kendaraan = [
    Motor("AG3473ABC", Decimal("40000")),
    Mobil("AG4233DEF", Decimal("60000")),
    Motor("AG6958GHI", Decimal("45000")),
    Mobil("AG8754JKL", Decimal("70000"))
]

for k in kendaraan:
    jenis = k.__class__.__name__
    biaya_sewa = k.hitung_biaya_sewa(3)

    print(f"{k.plat_nomor} - {jenis} -> Rp. {biaya_sewa}")