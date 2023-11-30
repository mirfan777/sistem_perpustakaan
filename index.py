import Buku
import Keanggotaan

session = int 
anggota = Keanggotaan.Perpustakaan()

def login():
    print("-SISTEM PERPUSTAKAAN-")
    print("---------------------")
    username = input("masukan username : ")
    password = input("masukan password : ")

def main_Menu():
    print("-----Menu Utama-----")
    print("--------------------")
    print("1.daftar buku")
    print("2.pinjam buku")
    print("4.keluar")
    pilihan = int(input("masukan pilihan anda : "))
    if(pilihan == 1):
        daftarBuku()
    elif(pilihan == 2):
        pinjamBuku()
    elif(pilihan == 3):
        session = 0
        login()

def admin_main_Menu():
    print("--Menu Utama Admin--")
    print("--------------------")
    print("1.cari buku")
    print("2.tambah buku")
    print("3.edit buku")
    print("4.delete buku")
    print("5.daftar anggota")
    print("6.tambah anggota")
    print("7.hapus anggota")
    print("8.keluar")
    pilihan = int(input("masukan pilihan anda : "))

    if(pilihan == 1):
        search()
    elif(pilihan == 2):
        tambahBuku()
    elif(pilihan == 3):
        editBuku()
    elif(pilihan == 4):
        hapusBuku()
    elif(pilihan == 5):
        daftarAnggota()
    elif(pilihan == 6):
        tambahAnggot()
    elif(pilihan == 7):
        hapusAnggota()
    elif(pilihan == 8): 
        session = 0
        login()
    else:
        print("invalid input")
        admin_main_Menu()


def search():
    Buku.cariBuku()

# admin section
def tambahBuku():
    judul = input("masukan nama judul = ")
    author = input("masukan nama author = ")
    genre = input("masukan genre = ")

    Buku.tambah(judul,author,genre)

    pilihan = input("apakah anda ingin menambah buku lagi? (y) = ")

    if(pilihan.lower() == "y"):
        tambahBuku()
    else:
        admin_main_Menu()


def hapusBuku():
    try:
        id = int(input("masukan id buku yang ingin anda hapus : "))
        yakin = input("apakah anda yang ingin menghapus data terserbut? (y) :")
        
        if(yakin.lower() == "y"):
            Buku.hapus(id)
            admin_main_Menu()
        else:
            admin_main_Menu()
    except:
        print("input harus berisikan angka")
        hapusBuku()

def editBuku():
    try:
        id = int(input("masukan data id yang ingin anda edit : "))
        judul = input("masukan judul = ")
        author = input("masukan author = ")
        genre = input("masukan genre = ")
        yakin = input("apakah anda yang ingin menghapus data terserbut? (y) :")
        
        if(yakin.lower() == "y"):
            Buku.edit(id,judul=judul,author=author,genre=genre)
            admin_main_Menu()
        else:
            admin_main_Menu()
    except Exception as error:
        admin_main_Menu()

def daftarKeanggotaan():
    anggota.tampilkan_anggota()

def tambahKeanggotaan():
    nama = input("Masukkan Nama: ")
    email = input("Masukkan Email: ")
    telepon = input("Masukkan Nomor Telepon: ")
    username = input("Masukkan username pengguna :")
    anggota_baru = AnggotaPerpustakaan(id_anggota, nama, email, telepon, username)
    perpustakaan.tambah_anggota(anggota_baru)
    
    anggota.tambah_anggota()