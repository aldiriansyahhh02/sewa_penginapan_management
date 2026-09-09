# ===================================
# [Sewa Penginapan]
# ===================================
# Developed by. Muhammad Aldi Riansyah
# JCDSBSD - [34]


# /************************************/

# /===== Data Model =====/
# Create your data model here
data_kamar = [
    {"id": 1, "tipe": "standar", "harga": 450000, "kasur": "Single"},
    {"id": 2, "tipe": "standar", "harga": 450000, "kasur": "Single"},
    {"id": 3, "tipe": "standar", "harga": 450000, "kasur": "Double"},
    {"id": 4, "tipe": "deluxe", "harga": 550000, "kasur": "Double"},
    {"id": 5, "tipe": "vip", "harga": 750000, "kasur": "Double"}
] # Example data model

id_terakhir = 5

# /===== Feature Program =====/
# Create your feature program here

def tambah_kamar():
    global id_terakhir
    print("--- Tambah Kamar Baru ---")
    tipe = input("Masukkan tipe kamar: ")
    harga = input("Masukkan harga kamar: ")

    while True:
        try:
            kasur = input("Masukkan Jenis Kasur: ")
            if kasur != "Single" or kasur != "Double":
                break
            print("Kasur hanya terdiri dari Single atau Double")
        except:
            print("Masukkan angka yang valid")

    id_terakhir = id_terakhir + 1 
    kamar_baru = {
        "id": id_terakhir,
         "tipe": tipe,
         "harga": harga,
         "kasur": kasur
    }
    data_kamar.append(kamar_baru)
    print(f"Kamar {tipe} telah didaftarkan dengan ID {id_terakhir}")

def tampilkan_kamar():
    print("\n--- DAFTAR SEMUA KAMAR ---")
    if not data_kamar:
        print("Belum ada kamar yang terdaftar")
        return

    print(f"{"ID":<5} | {"Tipe Kamar":<30} | {"Harga":<20} | {"Kasur":<10}")
    print("-"*70)
    for kamar in data_kamar:
            print(f"{kamar["id"]:<5} | {kamar["tipe"]:<30} | {kamar["harga"]:<20} | {kamar["kasur"]:<10}")
    print("-"*70)

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

# /===== Main Program =====/
# Create your main program here
while True:
    print("\n=============================")
    print("       SISTEM KELOLA KAMAR")
    print("\n=============================")
    print("1. Tambahkan Kamar")
    print("2. Tampilkan Semua Kamar")
    print("3. Cari Kamar")
    print("4. Ubah Data Kamar")
    print("5. Hapus Kamar")
    print("6. keluar")

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
        pass
    elif pilih_menu == 6:
        print("Terima kasih telah menggunakan program ini, Sampai jumpa!")
        break
    else:
        print("Input salah !")