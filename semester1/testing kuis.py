import math 


def hitung_volume_bola(r):
    
    volume = (4/3) * math.pi * (r ** 3)
    return volume


def hitung_limas_segiempat():
    
    print("\n--- LIMAS SEGI EMPAT ---")
    
    try:
        s = float(input("Masukkan panjang sisi alas (s): "))
        t = float(input("Masukkan tinggi limas (t): "))
        t_s = float(input("Masukkan tinggi sisi tegak (t_s): "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    
    luas_alas = s * s 
    volume = (1/3) * luas_alas * t

    
    luas_sisi_tegak = 0.5 * s * t_s 
    luas_permukaan = luas_alas + (4 * luas_sisi_tegak)

    # Tampilkan hasil hitung dengan jelas
    print(f"\n✅ Hasil Perhitungan Limas Segi Empat:")
    print(f"   Volume Limas Segi Empat: {volume:,.2f}")
    print(f"   Luas Permukaan Limas Segi Empat: {luas_permukaan:,.2f}")



print("--- KUIS LOGIKA DAN ALGORITMA (SOAL B) ---")


jari_jari_bola = float(input("Masukkan jari-jari bola (r): "))
volume_bola_hasil = hitung_volume_bola(jari_jari_bola)
print(f"\n✅ Hasil Perhitungan Bola:")
print(f"   Jari-jari (r): {jari_jari_bola}")
print(f"   Volume Bola: {volume_bola_hasil:,.2f}") 


hitung_limas_segiempat()