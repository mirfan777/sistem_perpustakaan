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
                lisear.append(f"{counter}. {i['judul']}\nID Buku : {i['id']}\nAuthor : {i['author']} genre : {'Tidak ada genre' if len(i['genre'])==0 else ','.join(i['genre'])}\n")
                counter +=1

        print("\nHasil :\n")
        if len(lisear)==0:
            print("Tidak ditemukan.")
        else:
            if len(lisear)<=10:
                for i in lisear:
                    print(i)
            else:
                awal = 0
                akhir = 10
                while True:
                    for i in lisear[awal:akhir]:
                        print(i)
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
                        print("Pilihan tidak valid.\n")
                    print(awal, akhir)
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
                            print("Pilihan tidak valid.\n")
                        print(awal, akhir)
                    if pagi == "e":
                        break

def sortBuku():
    with open("buku.json", "r") as sortBuku:
        file = json.load(sortBuku)

cariBuku()