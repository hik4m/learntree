from abc import ABC, abstractmethod

class Kendaraan(ABC):
  def __init__(self, plat_nomor, tarif_dasar):
    self.__plat_nomor = plat_nomor
    self.tarif_dasar = tarif_dasar

  @property
  def tarif_dasar(self):
    return self._tarif_dasar

  @tarif_dasar.setter
  def tarif_dasar(self, nilai):
    if nilai < 0:
      raise ValueError("Gaoleh Negatif")
    self._tarif_dasar = nilai
    
  @abstractmethod
  def hitung_biaya_sewa(self, lama_hari):
    raise NotImplementedError("Harus dibuat  di class turunan") 

class Motor(Kendaraan):
  
  def hitung_biaya_sewa(self, lama_hari):
    return self.tarif_dasar * lama_hari

class Mobil(Kendaraan):
  
  def hitung_biaya_sewa(self, lama_hari):
    asuransi = 50000
    return (self.tarif_dasar * lama_hari) + asuransi


kendaraan = [
  Motor("placeholder", 40000),
  Mobil("njajal", 60000),
  Motor("test", 45000),
  Mobil("coba", 70000)
]

kendaraan[0].plat_nomor = "AG3473ABC"
kendaraan[1].plat_nomor = "AG4233DEF"
kendaraan[2].plat_nomor = "AG6958GHI"
kendaraan[3].plat_nomor = "AG8754JKL"

for k in kendaraan:
  jenis = k.__class__.__name__
  print(f"{k.plat_nomor} - {jenis} -> Rp. {k.hitung_biaya_sewa(3)}")
  