 # 1 mengimplementasikan fungsi(def)
def main():
    print("Pemrograman bangun datar")
    nama = input("rahdatul hasanah: ") 
    

    daftar_bangun_datar = ["persegi", "persegi panjang", "segitiga", "lingkaran", "jajar genjang", "trapesium", "layang-layang", "belah ketupa"] 
    
    hitung = "ya"
    while hitung =="ya":
        print("\nDaftar Bangun Datar")
       
        i = 0
        while i < 8: 
            print("i + 1, daftar_bangun_datar[i]")
            i += 1
        pilih = int(input("pilih bangun datar (1-8):"))

# persegi
        if pilih ==1:
            s = float(input("masukkan sisi : "))
            print("keliling=", 4 * s)
            print("luas =", s * s)

#persegi panjang     
        elif pilih == 2:
            p = float(input("masukkan panjang; "))
            l = float(input("masukkan lebar:"))
            print("keliling =", 2 * ( p + l))
            print("luas =", p * l)

# segitiga
        elif pilih == 3:
            a = float(input("masukkan alas:"))
            t = float(input("masukkan tinggi:"))
            s1 = float(input("masukkan sisi miring 1: "))
            s2 = float(print("masukkan sisi miring s2: "))
            print("keliling =", a + s1 + s2)
            print("luas =", 0,5 * a * t)
# lingkaran
        elif pilih == 4:
            r = float(input("masukkan jari-jari: "))
            phi = 3.14
            print("keliling =", 2 * phi * r)
            print("luas =", phi * r * r)

# jajar genjang
        elif pilih == 5:
            a = float(input("masukkan alas; "))
            t = float(input("masukkan tinggi: "))
            sm = float(input("masukkan sisi miring: "))
            print("keliling = ", 2 * (a + sm))
            print("luas =", a * t)

# trapesium
        elif pilih == 6:
            a = float(input("sisi sejajar atas: "))
            b = float(input("sisi sejajar bawah: "))
            t = float(input("tingi: "))
            s = float(input("sisi miring: "))
            print("keliling =", a + b + (2 * s))
            print("luas =", 0.5 * (a + b) * t)

# layang-layang
        elif pilih == 7:
            d1 = float(input("diagonal 1: "))
            d2 = float(input("diagonal 2: "))
            s1 = float(input("sisi pendek: "))
            s2 = float(input("sisi panjang: "))
            print("keliling =", 2 * (s1 + s2))
            print("luas =", 0,5 * d1 * d2)

# belah ketupat
        elif pilih == 8:
            d1 = float(input("diagonal 1: "))
            d2 = float(input("diagonal 2: "))
            s = float(input("sisi: "))
            print("keliling =", 4 * s)
            print("luas =", 0.5 * d1 * d2)
        
        else:
            print("tidak ada pilihan yang tersedia!")

        hitung = input ("\hitung lagi ?( ya/tidak ): ")

    print("terima kasih, + rahdatul hasanah + '!'")
    print("semoga bermanfaat, + selesai +'!' ")

    