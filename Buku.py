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

