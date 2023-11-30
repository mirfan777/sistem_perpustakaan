import json

class AnggotaPerpustakaan:
    def __init__(self, id_anggota, nama, email, telepon, username):
        self.id_anggota = id_anggota
        self.nama = nama
        self.email = email
        self.telepon = telepon
        self.username = username

class Perpustakaan:
    def __init__(self, json_file="anggota.json"):
        self.json_file = json_file
        self.daftar_anggota = []
        self._load_from_json()

    def _load_from_json(self):
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                for item in data:
                    anggota = AnggotaPerpustakaan(item['id_anggota'], item['nama'], item['email'], item['telepon'], item['username'])
                    self.daftar_anggota.append(anggota)
        except FileNotFoundError:
            pass

    def _save_to_json(self):
        with open(self.json_file, 'w') as file:
            data = []
            for anggota in self.daftar_anggota:
                data.append({
                    'id_anggota': anggota.id_anggota,
                    'nama': anggota.nama,
                    'email': anggota.email,
                    'telepon': anggota.telepon,
                    'username': anggota.username
                })
            json.dump(data, file, indent=2)

    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
        self._save_to_json()
        print("Anggota ditambahkan!")

    def hapus_anggota(self, id_anggota):
        for anggota in self.daftar_anggota:
            if anggota.id_anggota == id_anggota:
                self.daftar_anggota.remove(anggota)
                self._save_to_json()
                print("Anggota dihapus!")
                return
        print("ID Anggota tidak ditemukan.")

    def edit_anggota(self, id_anggota, nama, email, telepon, username):
        for anggota in self.daftar_anggota:
            if anggota.id_anggota == id_anggota:
                anggota.nama = nama
                anggota.email = email
                anggota.telepon = telepon
                anggota.username = username
                self._save_to_json()
                print("Data anggota diubah!")
                return
        print("ID Anggota tidak ditemukan.")

    def tampilkan_anggota(self):
        print("\nDaftar Anggota Perpustakaan:")
        for anggota in self.daftar_anggota:
            print(f"ID: {anggota.id_anggota}, Nama: {anggota.nama}, email: {anggota.email}, Telepon: {anggota.telepon}, Username: {anggota.username}")
            

# Inisialisasi objek perpustakaan
perpustakaan = Perpustakaan()

while True:
    print("\nPilih Operasi:")
    print("1. Tambah Anggota")
    print("2. Hapus Anggota")
    print("3. Edit Data Anggota")
    print("4. Tampilkan Daftar Anggota")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan (0-4): ")

    if pilihan == "1":
        id_anggota = (input("Masukkan ID Anggota: "))
        nama = input("Masukkan Nama: ")
        email = input("Masukkan Email: ")
        telepon = input("Masukkan Nomor Telepon: ")
        username = input("Masukkan username pengguna :")
        anggota_baru = AnggotaPerpustakaan(id_anggota, nama, email, telepon, username)
        perpustakaan.tambah_anggota(anggota_baru)

    elif pilihan == "2":
        id_anggota = int(input("Masukkan ID Anggota yang akan dihapus: "))
        perpustakaan.hapus_anggota(id_anggota)

    elif pilihan == "3":
        id_anggota = (input("Masukkan ID Anggota yang akan diubah: "))
        nama = input("Masukkan Nama Baru: ")
        email = input("Masukkan email Baru: ")
        telepon = int(input("Masukkan Nomor Telepon Baru: "))
        username = input("Masukkan Username Baru: ")
        perpustakaan.edit_anggota(id_anggota, nama, email, telepon, username)
        
        if not email.endswith('@gmail.com'):
            print("Email harus diakhiri dengan '@gmail.com'. Perubahan dibatalkan.")
            continue

    elif pilihan == "4":
        perpustakaan.tampilkan_anggota()

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")