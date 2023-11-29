import Buku 
import Keanggotaan

def authMenu():
    print("-SISTEM PERPUSTAKAAN-")
    print("---------------------")
    print("1.LOGIN")
    print("2.DAFTAR")
    pilihan = int(input("masukan pilihan anda : "))

    if(pilihan == 1):
        Keanggotaan.login()
    elif(pilihan == 2):
        Keanggotaan.register()
    else:
        authMenu()

def mainMenu():
    print("-----Menu Utama-----")
    print("--------------------")
    print("1.daftar buku")
    print("2.pinjam buku")
    print("3.keanggotaan")
    print("4.keluar")
    pilihan = int(input("masukan pilihan anda : "))
    if(pilihan == 1):
        login()
    elif(pilihan == 2):
        register()
    elif(pilihan == 3):
        loginMenu()

def admin_main_Menu():
    print("--Menu Utama Admin--")
    print("--------------------")
    print("1.daftar buku")
    print("2.pinjam buku")
    print("3.tambah buku")
    print("4.edit buku")
    print("5.delete buku")
    print("6.keanggotaan")
    print("7.keluar")
    pilihan = int(input("masukan pilihan anda : "))

    if(pilihan == 1):
        login()
    elif(pilihan == 2):
        register()
    elif(pilihan == 3):
        loginMenu()

def daftarBuku():
    Buku.daftarBuku()

def tambahBuku():
    judul = input("masukan nama judul = ")
    author = input("masukan nama author = ")
    genre = input("masukan genre = ")

    Buku.tambahBuku(judul,author,genre)

    pilihan = input("apakah anda ingin menambah buku lagi? (y) = ")

    if(pilihan.lower() == "y"):
        tambahBuku()
    else:
        admin_main_Menu()


tambahBuku()