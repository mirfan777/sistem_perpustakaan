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

cariBuku()