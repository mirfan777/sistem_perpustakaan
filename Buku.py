import json
import time
import copy
        
def daftarBuku():
    with open("buku.json" , "r") as bukuFile:
        data = json.load(bukuFile)


        return data
    

def tambah(judul,author,genre):
    with open("buku.json" , "r+") as tambahBuku:
        # validasi data input genre agar tidak terjadi data ganda
        setData = set(genre.split(','))
        genreList = list(setData)
        
        data = json.load(tambahBuku)
        
        # membuat variable untuk notifikasi data berhasil di input
        before = copy.deepcopy(data)

        # input data dengan unique id
        data["data"].append({
            "id" : int(time.time()),
            "judul" : judul,
            "author" : author,
            "genre" : genreList
            })
        
        with open("buku.json" , "w") as file:
            json.dump(data, file , indent=4)

        # notifikasi data
        if(data != before):
            print("data berhasil diubah")
        else:
            print("data gagal diubah")
    
def hapus(id):

    with open('buku.json', 'r') as file:
        data = json.load(file)
        # membuat variable untuk notifikasi data berhasil di input
        before = copy.deepcopy(data)

        # menghapus data buku
        data['data'] = [buku for buku in data['data'] if buku['id'] != id]

    with open('buku.json', 'w') as file:
        json.dump(data, file , indent=4)

        # notifikasi data
        if(data != before):
            print("data berhasil diubah")
        else:
            print("id tidak ditemukan")

def edit(id,judul,author,genre):
    with open('buku.json', 'r') as file:
    # validasi data input genre agar tidak terjadi data ganda
        setData = set(genre.split(','))
        genreList = list(setData)

        data = json.load(file)

    # membuat variable untuk notifikasi data berhasil di input
        before = copy.deepcopy(data)


    # mencari id buku dan edit data
    for book in data['data']:
        if book['id'] == id:
            book.update({
            "judul" : book["judul"] if judul == "" else judul,
            "author" : book["author"] if author == "" else author,
            "genre" : book["genre"] if genreList == [""] else genreList
            })
            break

    with open('buku.json', 'w') as file:

        json.dump(data, file ,indent=4)

    # notifikasi data
        if(data != before):
            print("data berhasil diubah")
        else:
            print("data gagal diubah")

# def buatLisBuku():
#     print("\nCari buku berdasarkan:\n1. Judul\n2. Author\n3. Nomor Buku\n")
#     jenis = input("Pilihanmu : ")

    # with open("buku.csv", "r") as cariBuku:
    #     file = csv.reader(cariBuku)
    #     lis = []
    #     buku = 1
    #     idbuku = 0

    #     for row in file:
    #         lis.append(f"{row[buku].lower()};{row[idbuku]}")

    #     return lis


def cariBuku():
    with open("buku.json", "r") as cariBuku:
        file = json.load(cariBuku)["data"]
        lis = []
        namaBuku = 0
        idBuku = 1
        buku = input("\nCari : ").lower()
        for i in file:
            lis.append(f"{i['judul']};{i['id']}")
        lis.sort()

        pertama = 0
        terakhir = len(file) - 1
        ada = False
        lisear = []

        while pertama <= terakhir and not ada:
            tengah = (pertama + terakhir) // 2
            center = lis[tengah].lower()
            if buku in center:
                ada = True
                counter = 1
                for i in lis:
                    if buku in i.lower():
                        lisear.append(f"{counter}. {i.split(';')[namaBuku]}\nID Buku : {i.split(';')[idBuku]} \n")
                        counter += 1
            else:
                if buku < center:
                    terakhir = tengah - 1
                else:
                    pertama = tengah + 1

        print("\nHasil :\n")
        for i in lisear:
            print(i)

