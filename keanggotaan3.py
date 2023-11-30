import json
import time

class AnggotaPerpustakaan:
    def __init__(self, id_anggota, nama, email, telepon, username):
        self.id_anggota = id_anggota
        self.nama = nama
        self.email = email
        self.telepon = telepon
        self.username = username

class Perpustakaan:
    def __init__(self, file="anggota.json"):
        self.file = file
        self.daftarAnggota = []
        self.loadJson()

    def loadJson(self):
        try:
            with open(self.file, 'r') as file:
                data = json.load(file)
                for item in data:
                    anggota = AnggotaPerpustakaan(item['id_anggota'], item['nama'], item['email'], item['telepon'], item['username'])
                    self.daftarAnggota.append(anggota)
        except FileNotFoundError:
            pass

    def simpan(self):
        with open(self.file, 'w') as file:
            data = []
            for anggota in self.daftarAnggota:
                data.append({
                    'id_anggota': anggota.id_anggota,
                    'nama': anggota.nama,
                    'email': anggota.email,
                    'telepon': anggota.telepon,
                    'username': anggota.username
                })
            json.dump(data, file, indent=2)

    def tambah_anggota(self, anggota):
        self.daftarAnggota.append(anggota)
        self.simpan()
        print("\nAnggota ditambahkan!")

    def hapus_anggota(self, id_anggota):
        for anggota in self.daftarAnggota:
            if anggota.id_anggota == id_anggota:
                self.daftarAnggota.remove(anggota)
                self.simpan()
                print("\nAnggota dihapus!")
                return
        print("\nID Anggota tidak ditemukan.")

    def edit_anggota(self, id_anggota, nama, email, telepon, username):
        for anggota in self.daftarAnggota:
            if anggota.id_anggota == id_anggota:
                anggota.nama = nama
                anggota.email = email
                anggota.telepon = telepon
                anggota.username = username
                self.simpan()
                print("\nData anggota diubah!")
                return
        print("\nID Anggota tidak ditemukan.")

    def tampilkan_anggota(self):
        print("\nDaftar Anggota Perpustakaan:")
        for anggota in self.daftarAnggota:
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
        id_anggota = str(time.time())
        nama = input("Masukkan Nama: ")
        while True:
            email = input("Masukkan Email: ")
            if not email.endswith('@gmail.com'):
                print("Email harus diakhiri dengan '@gmail.com'. Perubahan dibatalkan.")
            else:
                break
        telepon = input("Masukkan Nomor Telepon: ")
        username = input("Masukkan username pengguna :")
        anggota_baru = AnggotaPerpustakaan(id_anggota, nama, email, telepon, username)
        perpustakaan.tambah_anggota(anggota_baru)

    elif pilihan == "2":
        id_anggota = int(input("Masukkan ID Anggota yang akan dihapus (Berupa angka): "))
        perpustakaan.hapus_anggota(id_anggota)

    elif pilihan == "3":
        id_anggota = (input("Masukkan ID Anggota yang akan diubah: "))
        nama = input("Masukkan Nama Baru: ")
        while True:
            email = input("Masukkan email Baru: ")
            if not email.endswith('@gmail.com'):
                print("Email harus diakhiri dengan '@gmail.com'. Perubahan dibatalkan.")
            else:
                break
        telepon = input("Masukkan Nomor Telepon Baru (Angka): ")
        username = input("Masukkan Username Baru: ")
        perpustakaan.edit_anggota(id_anggota, nama, email, telepon, username)

    elif pilihan == "4":
        perpustakaan.tampilkan_anggota()

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")