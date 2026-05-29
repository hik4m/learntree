RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"

def noAA():
    nilaiTes = int(input("Input Nilai Tes: "))
    if (nilaiTes>100 or nilaiTes<0):
        print("Tidak Diterima, Nilai Kamu:", nilaiTes)
    else:
        print("Diterima, Nilai Kamu:", nilaiTes)

def noBA():
    nilaiTes = int(input("Input Nomor Rumah Anda: "))
    reason = nilaiTes%13
    if (reason==0):
        print("Nomor Rumah Diterima\nNomor Rumah Anda:", nilaiTes)
    else:
        print("Nomor Rumah Tidak Diterima\nNomor Rumah Anda:", nilaiTes)

def noCA():
    tahun = int(input("Input Tahun: "))
    kabisat = tahun % 4
    if (kabisat==0):
        print("Tahun",tahun, "adalah tahun kabisat")
    else:
        print("Tahun", tahun, "adalah tahun biasa")

def noDA():
    striker = int(input("Input Jumlah Striker: "))
    playmaker = int(input("Input Jumlah Playmaker: "))
    gelandang = int(input("Input Jumlah Gelandang: "))
    bek = int(input("Input Jumlah Bek: "))
    jumlah = striker+playmaker+gelandang+bek
    if(jumlah==10):
        print("Valid\nSemua pemain berjumlah", jumlah)
    else:
        print("Tidak Valid\nSemua pemain berjumlah", jumlah)

def noEA():
    jam = int(input("Input Jam: "))
    menit = int(input("Input Menit: "))
    detik = int(input("Input Detik: "))
    if(jam>24 or menit>60 or detik>60):
        print("Tidak Valid\n",str(jam).zfill(2),":",str(menit).zfill(2),":",str(detik))
    else: 
        print("Valid\n",str(jam).zfill(2),":",str(menit).zfill(2),":",str(detik))
        
def noFA():
    r = int(input("Piksel Red   : "))
    g = int(input("Piksel Green : "))
    b = int(input("Piksel Blue  : "))

    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        print("Valid")
    else:
        print("Tidak")


def noAB():
    n = int(input("Nomor hari: "))

    if n == 1: print("Senin")
    elif n == 2: print("Selasa")
    elif n == 3: print("Rabu")
    elif n == 4: print("Kamis")
    elif n == 5: print("Jumat")
    elif n == 6: print("Sabtu")
    elif n == 7: print("Minggu")
    else: print("Tidak Valid")

def noBB():
    b = int(input("Nomor Bulan: "))

    if b == 1: print("Januari")
    elif b == 2: print("Februari")
    elif b == 3: print("Maret")
    elif b == 4: print("April")
    elif b == 5: print("Mei")
    elif b == 6: print("Juni")
    elif b == 7: print("Juli")
    elif b == 8: print("Agustus")
    elif b == 9: print("September")
    elif b == 10: print("Oktober")
    elif b == 11: print("November")
    elif b == 12: print("Desember")
    else: print("Tidak Valid")

def noCB():
    n = int(input("Nomor hari: "))
    b = int(input("Nomor Bulan: "))

    if b == 1: isBulan = "Januari"
    elif b == 2: isBulan = "Februari"
    elif b == 3: isBulan = "Maret"
    elif b == 4: isBulan = "April"
    elif b == 5: isBulan = "Mei"
    elif b == 6: isBulan = "Juni"
    elif b == 7: isBulan = "Juli"
    elif b == 8: isBulan = "Agustus"
    elif b == 9: isBulan = "September"
    elif b == 10: isBulan = "Oktober"
    elif b == 11: isBulan = "November"
    elif b == 12: isBulan = "Desember"
    else: isBulan = "Tidak Valid"
    print(n, isBulan)

def noDB():
    dd = int(input("Input Hari: "))
    mm = int(input("Input Bulan: "))
    yy = int(input("Input Tahun: "))

    isKabisat = (yy % 400 == 0) or (yy % 4 == 0 and yy % 100 != 0)
    if (dd>31 or mm>12): result = "TIDAK VALID\nTanggal Tidak boleh lebih dari 31 dan Bulan Tidak boleh lebih dari 12"
    elif (not isKabisat) and mm == 2 and dd >= 29: result = "TIDAK VALID\nBukan Tahun Kabisat: Februari hanya sampai tanggal 28\n"
    elif isKabisat and mm == 2 and dd >= 30: result = "TIDAK VALID\nTahun Kabisat: Februari hanya sampai tanggal 29\n"
    else: result = "VALID\n"
    
    if(mm==1):
        isBulan = "Januari"
    elif(mm==2):
        isBulan = "Februari"
    elif(mm==3):
        isBulan = "Maret"
    elif(mm==4):
        isBulan = "April"
    elif(mm==5):
        isBulan = "Mei"
    elif(mm==6):
        isBulan = "Juni"
    elif(mm==7):
        isBulan = "Juli"
    elif(mm==8):
        isBulan = "Agustus"
    elif(mm==9):
        isBulan = "September"
    elif(mm==10):
        isBulan = "Oktober"
    elif(mm==11):
        isBulan = "November"
    elif(mm==12):
        isBulan = "Desember"
    print(result, dd, isBulan, yy)

def noEB():
    print("Program Belum Tersedia")

def noFB():
    karbo = float(input("Input Gram Karbo; "))
    protein = float(input("Input Gram Protein; "))
    lemak = float(input("Input Gram Lemak; "))
    vit = float(input("Input Gram Vitamin; "))

    total = karbo+protein+lemak+vit

    pKarbo = karbo / total * 100
    pProtein = protein / total * 100
    pLemak = lemak / total * 100
    pVitMin = vit / total * 100

    if (55 <= pKarbo <= 60 and
        10 <= pProtein <= 20 and
        7  <= pLemak <= 10 and
        10 <= pVitMin <= 15):
        print("="*30,GREEN+ "\nSEHAT"+RESET, "Berikut Rincian Gizi Harian Anda:\n","="*30,"\nKarbohidrat:", round(pKarbo,2),"%\nProtein:", round(pProtein,2),"%\nLemak:", round(pLemak,2),"%\nVitamin & Mineral:", round(pVitMin,2),"%")
    else:
        print("="*30,RED+ "\nTIDAK SEHAT," + RESET, "Berikut Rincian Gizi Harian Anda:\n","="*30,"\nKarbohidrat:", round(pKarbo,2),"%\nProtein:", round(pProtein,2),"%\nLemak:", round(pLemak,2),"%\nVitamin & Mineral:", round(pVitMin,2),"%")


def kuis():
    nama = str(input("Input Nama Pegawai; "))
    bagian = str(input("Input Bagian: "))
    jHari = int(input("Input Jumlah Hari Anda: "))
    lembur = int(input("Input Jam Lembur: "))
    if(bagian=="Produksi"):
        print('OTWWW, SEKKKKKKK')
 
        
print(GREEN +"Penjelasan :\n(Soal)(Soal Bagian) : AA == Soal A Bagian A\n","="*30, "\nSelamat Datang di Program Latihan\n", "="*30 + RESET)
pilihan = str(input("Input Pilihan Program(AA/BA/CA/DA/EA/FA/KUIS/AB/BB/CB/DB/EB/FB): "))

match pilihan:
    case "AA" | "aa":
        print(RED + "="*30,"\nPROGRAM NILAI TES 0-100\n", "="*30 + RESET)
        noAA()
    case "BA" | "ba":
        print(RED + "\nPROGRAM NOMOR RUMAH KELIPATAN 13\n ","="*30 + RESET)
        noBA()
    case "CA" | "ca":
        print(RED + "="*30,"\nPROGRAM TAHUN KABISAT\n", "="*30 + RESET)
        noCA()
    case "DA" | "da":
        print(RED + "="*30,"\nPROGRAM PEMAIN BOLA\n", "="*30 + RESET)
        noDA()
    case "EA" | "ea":
        print(RED + "="*30,"\nPROGRAM FORMAT JAM\n", "="*30 + RESET)
        noEA()
    case "FA" | "fa":
        print(RED + "="*30,"\nPROGRAM KEBUTUHAN GIZI HARIAN\n", "="*30 + RESET)
        noFA()
    case "AB" | "ab":
        print(RED + "="*30,"\nPROGRAM NAMA HARI DARI NOMOR\n", "="*30 + RESET)
        noAB()
    case "BB" | "bb":
        print(RED + "="*30,"\nPROGRAM NAMA BULAN DARI NOMOR\n", "="*30 + RESET)
        noBB()
    case "CB" | "cb":
        print(RED + "="*30, "\nPROGRAM NAMA BULAN DAN HARI DARI NOMOR\n", "="*30 + RESET)
        noCB()     
    case "DB" | "db":
        print(RED + "="*30, "\nPROGRAM FORMAT DD/MM/YY\n", "="*30 + RESET)
        noDB()
    case "EB" | "eb":
        print(RED + "="*30, "\nPROGRAM FORMAT WAKTU\n", "="*30 + RESET)
        noEB()
    case "FB" | "fb":
        print(RED + "="*30, "\nPROGRAM KEBUTUHAN GIZI HARIAN\n", "="*30 + RESET)
        noFB()  
    case "Kuis" | "KUIS" | "kuis":
        print(RED + "="*30,"\nPROGRAM FORMAT MENGHITUNG GAJI KARYAWAN\n", "="*30 + RESET)
        kuis()
    case _: 
        print(RED + "Opsi", pilihan, "tidak terdata di program" + RESET)

