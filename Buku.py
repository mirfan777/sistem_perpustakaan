import csv
import os
import json

help(json)

        
def daftarBuku():
    with open("buku.csv" , "r") as bukuFile:
        file = csv.reader(bukuFile)

        for row in file:
            if row :
                print(row)
            else :
                print("tidak ada data")
    

def tambahBuku(id, judul, author, deskripsi):
    with open("buku.csv" , "a") as tambahBuku:
        file = csv.writer(tambahBuku)

        file.writerow(data)

def hapusBuku(id):

    records = []
    with open("buku.csv" , "r") as bukuFile:

        file = csv.reader(bukuFile)
        for row in file:

            records.append(row)

    with open("buku.csv" , "w") as bukuFile:

        file = csv.writer(bukuFile)
        for record in records:

            if record[0] != id:
                file.writerow(record)

def editBuku(id, judul, author, deskripsi):
    records = []

    with open("buku.csv" , "r") as bukuFile:
        file = csv.reader(bukuFile)
        for row in file:
            records.append(row)


    with open("buku.csv" , "w", newline='') as bukuFile:
        file = csv.writer(bukuFile)
        for record in records:
            if record[0] == id:
                record[1] = judul
                record[2] = author
                record[3] = deskripsi
            file.writerow(record)
    return
