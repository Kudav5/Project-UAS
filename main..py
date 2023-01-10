data = {}
class Data():
     def __init__(self,nim,nama,tugas,uts,uas,akhir):
        while True:

            print("\n")
            print('='*43)
            print('             DATA MAHASISWA              ')
            print('='*43)
            print('Menu Utama Data Mahasiswa : \n')
            print('|1| Input Data Mahasiswa        ')
            print('|2| Tampilkan Data Mahasiswa    ')
            print('|3| Cari Data Mahasiswa         ')
            print('|4| Ubah Data Mahasiswa         ')
            print('|5| Hapus Data Mahasiswa        ')
            print('|6| Keluar                      \n')

            x = input("> PILIH MENU : ")

            print("\n")

            if x == '1':
                self.TAMBAH()
            elif x == '2':
                self.TAMPILKAN()
            elif x == '3':
                self.CARI()
            elif x == '4':
                self.UBAH()
            elif x == '5':
                self.HAPUS()
            elif x == '6':
                self.KELUAR()
                break
    
            else:
                exit()

     def TAMBAH(self):
        print("Tambah Data")
        self.nim    = input('Nim Mahasiswa\t   : ')
        self.nama   = input('Nama Mahasiswa\t   : ')
        self.tugas  = int(input('Nilai Tugas\t   : '))
        self.uts    = int(input('Nilai UTS\t   : '))
        self.uas    = int(input('Nilai UAS\t   : '))
        self.akhir = (self.tugas * 30/100) + (self.uts * 35/100) + (self.uas * 35/100)
        data[self.nim] = self.nama, self.tugas, self.uts, self.uas, self.akhir

class mahasiswa(Data):

    def TAMPILKAN(self):
        if data.items():
            print('==============================================================================================')
            print('|   NO  |    NIM         |     NAMA             |  TUGAS  |   UTS   |   UAS   |     AKHIR    |')
            print('==============================================================================================')
            i = 0
            for a in data.items():
                i += 1
                print("|    {no:2d} | {0:14s} | {1:14s} | {2:7d} | {3:7d} | {4:7d} |    {5:6.2f}    |".format (a[0][: 14],a[1][0],a[1][1],a[1][2],a[1][3],a[1][4], no = i))
                print('==============================================================================================')

    def CARI(self):
        print("Cari Data")
        nim = input("Masukkan Nim  :")
        if data.keys():
            print('==============================================================================================')
            print('|   NO  |    NIM         |     NAMA             |  TUGAS  |   UTS   |   UAS   |     AKHIR    |')
            print('==============================================================================================')
            i = 0
            for a in data.items():
                i += 1
                print("|    {no:2d} | {0:14s} | {1:14s} | {2:7d} | {3:7d} | {4:7d} |    {5:6.2f}    |".format (a[0][: 14],a[1][0],a[1][1],a[1][2],a[1][3],a[1][4], no = i))
                print('==============================================================================================')

    def UBAH(self):
        print("Ubah Data")
        self.nim = input("Masukkan Nim        : ")
        if self.nim in data.keys():
            self.nama = input("Masukkan Nama\t    : ")
            self.tugas = int(input("Nilai tugas\t    : "))
            self.uts = int(input("Nilai UTS\t    : "))
            self.uas = int(input("Nilai UAS\t    : "))
            self.akhir = (self.tugas * 30/100) + (self.uts * 35/100) + (self.uas * 35/100)
            data[self.nim] = self.nama, self.tugas, self.uts, self.uas, self.akhir
        else:
            print("MAAF, DATA TIDAK DITEMUKAN")

    def HAPUS(self):
        print("Hapus Data")
        self.nim = input("masukkan Nim  : ")

        if self.nim in data.keys():
            del data[self.nim]
        else:
            print("MAAF, DATA TIDAK DITEMUKAN")

    def KELUAR(self):
        print()
        print("---------------------------------------------------------------------------------")
        print("                           PROGRAM TELAH SELESAI                    ")
        print("---------------------------------------------------------------------------------")

datamhs = mahasiswa("nama", "nim", "uts", "uas", "tugas", "akhir")