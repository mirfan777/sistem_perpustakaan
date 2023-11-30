import csv
import os
import json

def affected_file(file):
    file_size_before = os.path.getsize(file)
    file_size_after = os.path.getsize(file)

    if file_size_before != file_size_after:
        return False
    else:
        return True
        
def buku():
    with open("buku.csv" , "r") as bukuFile:
        file = csv.reader(bukuFile)

        for row in file:
            print(row)
    

def tambahBuku(data):
    with open("buku.csv" , "a") as tambahBuku:
        file = csv.writer(tambahBuku)

        file.writerow(data)
    return

def hapusBuku():
    with open("buku.csv" , ) as deleteBuku:
        file = csv.writer(deleteBuku)

        file.writerow([231,231,231])
    return 

def editBuku():
    return

# def cariBuku():
#     with open("buku.json", "r") as cariBuku:
#         file = json.load(cariBuku)["data"]
#         lis = []
#         namaBuku = 0
#         idBuku = 1
#         authorBuku = 2
#         genreBuku = 3

#         print("Cari buku berdasarkan :\n1. Judul Buku\n2. ID Buku\n3. Author/Penulis\n")
#         filter = input("Pilihanmu : ")

#         buku = input("\nCari : ").lower()
#         for i in file:
#             lis.append(f"{i['judul']};{i['id']};{i['author']};{i['genre']}")
#         lis.sort()

#         pertama = 0
#         terakhir = len(file) - 1
#         ada = False
#         lisear = []

#         while pertama <= terakhir and not ada:
#             tengah = (pertama + terakhir) // 2
#             center = lis[tengah].split(";")[0].lower()
#             if buku in center:
#                 ada = True
#                 counter = 1
#                 for i in lis:
#                     if buku in i.lower():
#                         lisear.append(f"{counter}. {i.split(';')[namaBuku]}\nID Buku : {i.split(';')[idBuku]} \n")
#                         counter += 1
#             else:
#                 if buku < center:
#                     terakhir = tengah - 1
#                 else:
#                     pertama = tengah + 1

#         print("\nHasil :\n")
#         for i in lisear:
#             print(i)

def cariBuku():
    with open("buku.j son", "r") as cariBuku:
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
                lisear.append(f"{counter}. {i['judul']}\nID Buku : {i['id']}\nAuthor : {i['author']} genre : {'Tidak ada genre' if len(i['genre'])==0 else ','.join(i['genre'])}\n")
                counter +=1

        # if len(lisear)

        print("\nHasil :\n")
        if len(lisear)==0:
            print("Tidak ditemukan.")
        else:
            for i in lisear:
                print(i)

def sortBuku():
    with open("buku.json", "r") as sortBuku:
        file = json.load(sortBuku)

cariBuku()