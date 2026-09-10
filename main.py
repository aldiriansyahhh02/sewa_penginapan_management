# ===================================
# [Sewa Penginapan]
# ===================================
# Developed by. Muhammad Aldi Riansyah
# JCDSBSD - [34]


# /************************************/

# /===== Data Kamar =====/
data_kamar = [
    {"id": 1, "tipe": "standar", "harga": 450000, "kasur": "single", "status":"tersedia"},
    {"id": 2, "tipe": "standar", "harga": 450000, "kasur": "single", "status":"tersedia"},
    {"id": 3, "tipe": "standar", "harga": 450000, "kasur": "double", "status":"terisi"},
    {"id": 4, "tipe": "deluxe", "harga": 550000, "kasur": "double", "status":"terisi"},
    {"id": 5, "tipe": "vip", "harga": 750000, "kasur": "double", "status":"tersedia"}
]

id_terakhir = 5

# /===== Program =====/

def tambah_kamar():
    global id_terakhir
    print("--- Tambah Kamar Baru ---")
    tipe = input("Masukkan tipe kamar: ")
    harga = input("Masukkan harga kamar: ")

    while True:
        try:
            kasur = input("Masukkan Jenis Kasur (single/double): ")
            if kasur != "single" and kasur != "double":
                print("Kasur hanya terdiri dari ingle atau double")
                continue
            break
        except:
            print("Masukkan kasur yang valid")

    while True:
            try:
                status = input("Masukkan Status kamar (tersedia/disewa): ")
                if kasur != "tersedia" and kasur != "disewa":
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

def tampilkan_kamar():
    print("\n--- DAFTAR SEMUA KAMAR ---")
    if not data_kamar:
        print("Belum ada kamar yang terdaftar")
        return

    print(f"{"ID":<5} | {"Tipe Kamar":<30} | {"Harga":<20} | {"Kasur":<10} | {"Status":<10}")
    print("-"*70)
    for kamar in data_kamar:
            print(f"{kamar["id"]:<5} | {kamar["tipe"]:<30} | {kamar["harga"]:<20} | {kamar["kasur"]:<10} | {kamar["status"]:<10}")
    print("-"*70)

def ubah_kamar():
    pass


def hapus_kamar():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
while True:
    print("\n=============================")
    print(" SISTEM KELOLA KAMAR PENGINAPAN")
    print("\n=============================")
    print("1. Tambahkan Kamar")
    print("2. Tampilkan Semua Kamar")
    print("3. Ubah Data Kamar")
    print("4. Hapus Kamar")
    print("5. keluar")

    pilih_menu = int(input("Pilih Menu: "))

    if pilih_menu == 1:
        tambah_kamar()
    elif pilih_menu == 2:
        tampilkan_kamar()
    elif pilih_menu == 3:
        pass
    elif pilih_menu == 4:
        pass
    elif pilih_menu == 5:
        print("Terima kasih telah menggunakan program ini, Sampai jumpa!")
        break
    else:
        print("Input salah ! Masukkan input yang benar")