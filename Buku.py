import csv
import os

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

def buatLisBuku():
    print("\nCari buku berdasarkan:\n1. Judul\n2. Author\n3. Nomor Buku\n")
    jenis = input("Pilihanmu : ")

    with open("buku.csv", "r") as cariBuku:
        file = csv.reader(cariBuku)
        lis = []

        for row in file:
            lis.append([row[0], row[1]])

        return(lis)

def cariBuku():
    lis = buatLisBuku()
    buku = input("\nCari : ")
    lisbuku = []
    for i in lis:
        lisbuku.append(f"{i[1]} {i[0]}")
    lisbuku.sort()

    pertama = 0
    terakhir = len(lis)-1
    # ketemu = False
    ada = False
    lisear = []

    while pertama<=terakhir and not ada:
        tengah = (pertama+terakhir)//2
        center = lisbuku[tengah].split(" ")[0]
        if center == buku:
            ada = True
            counter = 1
            for i in lisbuku:
                if buku in i:
                    lisear.append(f"{counter+1}. {i.split()[1]}\nID Buku : {i.split()[0]}\n")
                    counter+=1
        else:
            if buku < lisbuku[tengah]:
                terakhir -=1
            else:
                pertama +=1

    print("\nHasil :\n")
    for i in lisear:
        print(i)

    pilihan = input("Pilihanmu : ")

cariBuku()