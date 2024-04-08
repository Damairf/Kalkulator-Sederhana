print("KALKULATOR SEDERHANA - DAMAIRF")
print("(1) Bilangan Bulat\n(2) Bilangan Desimal")
while True:
    bilangan = int(input("Silahkan masukkan kode bilangan: "))
    if bilangan < 1 or bilangan > 2:
        print("Nomor tidak valid. Silahkan masukkan nomor antara 1 dan 2")
    else:
        break
    
if bilangan == 1:
        print()
        print("Anda memasuki kalkulator bilangan bulat")
        print("(1) Penjumlahan\n(2) Pengurangan\n(3) Perkalian\n(4) Pembagian")
        while True:
            menu = int(input("Silahkan pilih kode nomor kalkulator yang diinginkan: "))
            if menu < 1 or menu > 4:
                print("Nomor tidak valid. Silakan masukkan nomor antara 1 dan 4.")
            else:
                break
        if menu == 1:
            jumlahPertama = int(input("Masukkan angka penjumlahan pertama: "))
            jumlahKedua = int(input("Masukkan angka penjumlahan kedua: "))
            jumlahTotal = jumlahPertama + jumlahKedua
            print(jumlahPertama, "+", jumlahKedua, "=", jumlahTotal)
        elif menu == 2:
            kurangPertama = int(input("Masukkan angka pengurangan pertama: "))
            kurangKedua = int(input("Masukkan angka pengurangan kedua: "))
            kurangTotal =  kurangPertama - kurangKedua
            print(kurangPertama, "-", kurangKedua, "=", kurangTotal)
        elif menu == 3:
            kaliPertama = int(input("Masukkan angka perkalian pertama: "))
            kaliKedua = int(input("Masukkan angka perkalian kedua: "))
            kaliTotal = kaliPertama * kaliKedua
            print(kaliPertama, "x", kaliKedua, "=", kaliTotal)
        elif menu == 4:
            bagiPertama = int(input("Masukkan angka pembagian pertama: "))
            bagiKedua = int(input("Masukkan angka pembagian kedua: "))
            bagiTotal = bagiPertama / bagiKedua
            print(bagiPertama, ":", bagiKedua, "=", bagiTotal)
            
if bilangan == 2:    
        print()
        print("Anda memasuki kalkulator bilangan desimal")
        print("(1) Penjumlahan\n(2) Pengurangan\n(3) Perkalian\n(4) Pembagian")
        while True:
            menu = int(input("Silahkan pilih kode nomor kalkulator yang diinginkan: "))
            if menu < 1 or menu > 4:
                print("Nomor tidak valid. Silakan masukkan nomor antara 1 dan 4.")
            else:
                break
        if menu == 1:
            jumlahPertama = float(input("Masukkan angka penjumlahan pertama: "))
            jumlahKedua = float(input("Masukkan angka penjumlahan kedua: "))
            jumlahTotal = jumlahPertama + jumlahKedua
            print(jumlahPertama, "+", jumlahKedua, "=", jumlahTotal)
        elif menu == 2:
            kurangPertama = float(input("Masukkan angka pengurangan pertama: "))
            kurangKedua = float(input("Masukkan angka pengurangan kedua: "))
            kurangTotal =  kurangPertama - kurangKedua
            print(kurangPertama, "-", kurangKedua, "=", kurangTotal)
        elif menu == 3:
            kaliPertama = float(input("Masukkan angka perkalian pertama: "))
            kaliKedua = float(input("Masukkan angka perkalian kedua: "))
            kaliTotal = kaliPertama * kaliKedua
            print(kaliPertama, "x", kaliKedua, "=", kaliTotal)
        elif menu == 4:
            bagiPertama = float(input("Masukkan angka pembagian pertama: "))
            bagiKedua = float(input("Masukkan angka pembagian kedua: "))
            bagiTotal = bagiPertama / bagiKedua
            print(bagiPertama, ":", bagiKedua, "=", bagiTotal)