# ===================================
# [Sewa Penginapan]
# ===================================
# Developed by. Muhammad Aldi Riansyah
# JCDSBSD - [34]
import sys


# /************************************/

# /===== Data Kamar =====/
data_kamar = [
    {"id": 1, 
     "tipe": "standar", 
     "harga": 450000, 
     "kasur": "single", 
     "status":"tersedia"},

    {"id": 2, 
     "tipe": "standar", 
     "harga": 450000, 
     "kasur": "single", 
     "status":"tersedia"},

    {"id": 3, 
     "tipe": "standar", 
     "harga": 450000, 
     "kasur": "double", 
     "status":"terisi"},

    {"id": 4, "tipe": 
     "deluxe", 
     "harga": 550000, 
     "kasur": "double", 
     "status":"terisi"},

    {"id": 5, 
     "tipe": "vip", 
     "harga": 750000, 
     "kasur": "double", 
     "status":"tersedia"}
]

id_terakhir = 5

# /===== Program =====/
# Fungsi menambahkan kamar
def tambah_kamar():
    global id_terakhir
    print("--- Tambah Kamar Baru ---")
    tipe = input("Masukkan tipe kamar: ")
    while True:
        try:
            harga = int(input("Masukkan harga kamar: "))
            break
        except ValueError:
            print("Input hanya boleh berupa angka! Silakan coba lagi.")

    while True:
        try:
            kasur = input("Masukkan Jenis Kasur (single/double): ")
            if kasur != "single" and kasur != "double":
                print("Kasur hanya terdiri dari single atau double")
                continue
            break
        except:
            print("Masukkan kasur yang valid")

    while True:
            try:
                status = input("Masukkan Status kamar (tersedia/disewa): ")
                if status != "tersedia" and status != "disewa":
                    print("Status kamar hanya terdiri dari tersedia atau disewa")
                    continue
                break
            except:
                print("Masukkan kasur yang valid")

    id_terakhir = id_terakhir + 1 
    kamar_baru = {
        "id": id_terakhir,
         "tipe": tipe,
         "harga": harga,
         "kasur": kasur,
         "status":status
    }
    data_kamar.append(kamar_baru)
    print(f"Kamar {tipe} telah didaftarkan dengan ID {id_terakhir}")

# Fungsi menampilkan kamar
def tampilkan_kamar():
    print("\n=== MENU TAMPILKAN KAMAR ===")
    print("1. Tampilkan Semua Kamar")
    print("2. Cari Kamar (Berdasarkan Tipe/Status/Kasur)")
    print("3. Kembali ke Menu Utama")
    
    pilihan = int(input("Masukkan tindakan yang diinginkan: "))
    
    if pilihan == 3:
        return
    elif pilihan != 1 and pilihan != 2:
        print(" Pilihan tidak valid! Kembali ke menu utama.")
        return
    
    if not data_kamar:
        print("\n Belum ada kamar yang terdaftar.")
        return

    kata_kunci = ""
    if pilihan == 2:
        kata_kunci = input("\nMasukkan kata kunci pencarian (contoh: deluxe/tersedia/single): ").lower().strip()
        print(f"\n--- Hasil pencarian untuk: '{kata_kunci}' ---")
    else:
        print("\n--- Daftar semua Kamar ---")

    print(f"{'ID':<5} | {'Tipe Kamar':<30} | {'Harga':<20} | {'Kasur':<10} | {'Status':<10}")
    print("-" * 85)
    
    kamar_ditemukan = 0
    
    for kamar in data_kamar:
        if (pilihan == 1 or 
            kata_kunci in str(kamar["tipe"]).lower() or 
            kata_kunci in str(kamar["status"]).lower() or 
            kata_kunci in str(kamar["kasur"]).lower()):
            
            print(f"{kamar['id']:<5} | {kamar['tipe']:<30} | {kamar['harga']:<20} | {kamar['kasur']:<10} | {kamar['status']:<10}")
            kamar_ditemukan += 1
            
    print("-" * 85)

    
    if pilihan == 2 and kamar_ditemukan == 0:
        print(f" Tidak ada kamar yang cocok dengan kata kunci '{kata_kunci}'.")
    elif pilihan == 2:
        print(f" Ditemukan {kamar_ditemukan} kamar yang cocok.")

# Fungsi mengubah kamar
def ubah_kamar():
    if not data_kamar: 
        print("Belum ada kamar yang terdaftar")
        return
    
    try:
        id_kamar = int(input("\nMasukkan ID Kamar yang ingin diubah: "))
    except ValueError:
        print("ID Kamar harus berupa angka!")
        return
    
    for f in data_kamar:
        if f["id"] == id_kamar:
            print(f"\nMengubah kamar: {f['tipe']}")
            f["tipe"] = input("Masukkan tipe kamar baru: ")

            while True:
                try:
                    f["harga"] = int(input("Masukkan harga kamar Baru: "))
                    break
                except ValueError:
                    print("Pesan: Input hanya boleh berupa angka! Silakan coba lagi.")

            while True:
                try:
                    f["kasur"] = input("Masukkan tipe kasur kamar baru (single/double): ")
                    if f["kasur"] != "single" and f["kasur"] != "double":
                        print("Kasur hanya terdiri dari single atau double")
                        continue
                    break
                except ValueError:
                    print("Masukkan kasur yang valid")

            while True:
                try:
                    f["status"] = input("Masukkan status kamar saat ini (tersedia/disewa): ")
                    if f["status"] != "tersedia" and f["status"] != "disewa":
                        print("Status hanya terdiri dari tersedia atau disewa")
                        continue
                    break
                except ValueError:
                    print("Masukkan status yang valid")
            
                print(f"\n🔄 Data kamar ID {id_kamar} berhasil diperbarui!")
                return
            
    print(f"\nKamar dengan ID {id_kamar} tidak ditemukan!")
    print("Kembali ke menu utama")

# Fungsi menghapus kamar
def hapus_kamar():            
    print("\n--- Daftar Kamar Saat ini ---")
    for f in data_kamar:
        print(f"ID: {f['id']} | {f['tipe']}")
            
    id_kamar = int(input("\nMasukkan ID kamar yang ingin dihapus: "))
        
    ditemukan = False
    for f in data_kamar:
        if f["id"] == id_kamar:
            data_kamar.remove(f)
            print(f"\n Film dengan ID {id_kamar} berhasil dihapus!")
            ditemukan = True
            break
                
    if not ditemukan:
        print(f"\n Kamar dengan ID {id_kamar} tidak ditemukan!")

# /===== Main Program =====/
# Program Utama
while True:
    print("\n================================")
    print(" SISTEM KELOLA KAMAR PENGINAPAN")
    print("\n================================")
    print("1. Tambahkan Kamar")
    print("2. Tampilkan Semua Kamar")
    print("3. Ubah Data Kamar")
    print("4. Hapus Kamar")
    print("5. Keluar")

    pilih_menu = int(input("Pilih Menu: "))

    if pilih_menu == 1:
        print("==== Menu tambah kamar ====")
        print("1. Lanjut ke tambah kamar ")
        print("2. Kembali ke menu utama")
        
        while True:
            sub_menu1 = int(input("Apakah anda ingin melanjutkan? (input 1 atau 2): "))
            if sub_menu1 == 1:
                tambah_kamar()
                break
            elif sub_menu1 == 2:
                print("\nKembali ke menu utama...\n")
                break
            else:
                print("Masukkan input yang sesuai")
    elif pilih_menu == 2:
        print("==== Menu tampilkan kamar ====")
        print("1. Lanjut ke tampilkan kamar ")
        print("2. Kembali ke menu utama")

        while True:
            sub_menu2 = int(input("Apakah anda ingin melanjutkan? (input 1 atau 2): "))
            if sub_menu2 == 1:
                tampilkan_kamar()
                break
            elif sub_menu2 == 2:
                print("\nKembali ke menu utama...\n")
                break
            else:
                print("Masukkan input yang sesuai")
    elif pilih_menu == 3:
        print("==== Menu ubah kamar ====")
        print("1. Lanjut ke ubah data kamar ")
        print("2. Kembali ke menu utama")
                
        while True:
            sub_menu3 = int(input("Apakah anda ingin melanjutkan? (input 1 atau 2): "))
            if sub_menu3 == 1:
                ubah_kamar()
                break
            elif sub_menu3 == 2:
                print("\nKembali ke menu utama...\n")
                break
            else:
                print("Masukkan input yang sesuai")
    elif pilih_menu == 4:
        print("\n=== MENU HAPUS KAMAR ===")
        print("1. Lanjutkan Proses Hapus Kamar")
        print("2. Kembali ke Menu Utama")

        while True:
            sub_menu4 = int(input("Apakah anda ingin melanjutkan? (input 1 atau 2): "))
            if sub_menu4 == 1:
                hapus_kamar()
                break
            elif sub_menu4 == 2:
                print("\nKembali ke menu utama...\n")
                break
            else:
                print("Masukkan input yang sesuai")
    elif pilih_menu == 5:
        print("==== Menu konfirmasi keluar Program ====")
        print("1. Keluar dari Program")
        print("2. Kembali ke menu utama")
        while True:
            sub_menu5 = int(input("Apakah anda yakin ingin keluar dari program? (1 atau 2): "))
            if sub_menu5 == 2:
                print("\nKembali ke menu utama...\n")
                break
            elif sub_menu5 == 1:
                print("Terima kasih telah menggunakan program ini, Sampai jumpa!")
                sys.exit()
            elif sub_menu5 != 1 and sub_menu5 !=2:
                print("Input Salah! Silahkan coba lagi")
        
    else:
        print("Input salah! Masukkan input yang benar")