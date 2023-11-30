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
            "genre" : genreList,
            "status" : 0
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

def cariBuku():
    with open("buku.json", "r") as cariBuku:
        file = json.load(cariBuku)["data"]
        counter = 1
        lisear = []

        print("\nCari buku berdasarkan :\n1. Judul Buku\n2. ID Buku\n3. Author/Penulis\n")
        while True:
            filter = input("Pilihanmu : ")
            if not (filter=="1" or filter=="2" or filter=="3"):
                print("Pilihan Tidak Valid, Silahkan Coba Lagi.\n")
                continue
            else:
                filtering = "judul" if filter=="1" else ("id" if filter=="2" else ("author"))
                break

        urutan = sorted(file, key=lambda dict:dict[filtering])
        buku = input("\nCari : ").lower()

        for i in urutan:
            if buku in str(i[filtering]).lower():
                lisear.append([f"{counter}. {i['judul']}\nID Buku : {i['id']}\nAuthor : {i['author']}\nstatus : {'Tersedia' if i['status']==0 else 'Dipinjam'}\ngenre : {'Tidak ada genre' if len(i['genre'])==0 else ','.join(i['genre'])}\n", i["id"]])
                counter +=1

        print("\nHasil :\n")
        if len(lisear)==0:
            print("Tidak ditemukan.")
        else:
            if len(lisear)<=10:
                for i in lisear:
                    print(i[0])
            else:
                awal = 0
                akhir = 10
                buka = False
                while True:
                    for i in lisear[awal:akhir]:
                        print(i[0])
                    print("\nN untuk Next, B untuk Back, E untuk exit\n")
                    pagi = input("Pilihanmu : ").lower()
                    salah = False
                    if pagi == "n":
                        if len(lisear)-akhir <= 0:
                            print("Sudah Page Akhir\n")
                            salah = True
                        else:
                            awal += 10
                            akhir += 10
                    elif pagi == "b" :
                        if awal == 0:
                            print("Sudah Page Awal\n")
                            salah = True
                        else:
                            awal -= 10
                            akhir -= 10
                    elif pagi == "e":
                        break
                    else:
                        for i in lisear:
                            if pagi == i[0][len(pagi)-1]:
                                bukaBuku(i[1])
                                buka = True
                                break
                        if buka:
                            break
                        print("Pilihan tidak valid.\n")

                    while salah :
                        pagi = input("Pilihanmu : ")
                        if pagi == "n":
                            if len(lisear)-akhir <= 0:
                                print("Sudah Page Akhir\n")
                            else:
                                awal += 10
                                akhir += 10
                                salah = False
                        elif pagi == "b" :
                            if awal == 0:
                                print("Sudah Page Awal\n")
                            else:
                                awal -= 10
                                akhir -= 10
                                salah = False
                        elif pagi == "e":
                            break
                        else:
                            for i in lisear:
                                if pagi == i[0][len(pagi)-1]:
                                    bukaBuku(i[1])
                                    buka = True
                                    break
                            if buka:
                                break
                            print("Pilihan tidak valid.\n")
                            
                    if pagi == "e":
                        break
                    # print(i[0][len(pagi)-1])

def sortBuku():
    with open("buku.json", "r") as sortBuku:
        file = json.load(sortBuku)

def bukaBuku(id):
    with open("buku.json" , "r") as bukaBuku:
        file = json.load(bukaBuku)["data"]
        for i in file:
            if id == i["id"]:
                print(f"\nJudul Buku : {i['judul']}\nID Buku : {i['id']}\nAuthor : {i['author']}\nstatus : {'Tersedia' if i['status']==0 else 'Dipinjam'}\ngenre : {'Tidak ada genre' if len(i['genre'])==0 else ','.join(i['genre'])}\n\n(P untuk pinjam, E untuk exit)\n")
                while True:
                    pinjam = input("Pilihanmu : ").lower()
                    if pinjam == "p":
                        if i['status'] == 1:
                            print("Buku sedang dipinjam orang lain")
                        else:
                            print("Buku Berhasil Dipinjam!!\nTenggat waktu adalah 7 hari dari sekarang!\n")
                            break
                    elif pinjam == "e":
                        break
                    else:
                        "Pilihan Tidak Valid"

