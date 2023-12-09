# NAMA : Zaky Putra Pratama
class Mahasiswa():
    def __init__(self):
        self.mahasiswa = []

    def tambah(self):
        print("\nMASUKAN DATA")
        nama = str(input("Masukkan Nama: "))
        nim = int(input("Masukkan NIM: "))
        tugas = float(input("Masukkan Tugas: "))
        uts = float(input("Masukkan UTS: "))
        uas = float(input("Masukkan UAS: "))
        akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)
        data = {'Nama': nama,'NIM': nim,'Tugas': tugas,'UTS': uts,'UAS': uas,'Akhir': akhir}
        self.mahasiswa.append(data)
        print("berhasil ditambah")

    def lihat(self):
        if not self.mahasiswa:
            print("=" * 75)
            print("|{:^73}|".format("Tidak Ada Data"))
            print("=" * 75)
        else:
            print("=" * 77)
            print("|{:^75}|".format("DAFTAR NILAI MAHASISWA"))
            print("=" * 77)
            print("|{:^20}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
            print("=" * 77)
        for data in self.mahasiswa:
            print("|{:^20}|{:^10}|{:^10}|{:^10}|{:^10}|{:^10.2f}|".format(data['Nama'], data['NIM'], data['Tugas'], data['UTS'], data['UAS'], data['Akhir']))
            print("=" * 77)
    
    def hapus(self):
        print ("\nHAPUS DATA")
        nama = input("Masukkan Nama mahasiswa yang akan dihapus: ")
        for i in range(len(self.mahasiswa)):
         if self.mahasiswa[i]['Nama'] == nama:
            del self.mahasiswa[i]
            print("data berhasil dihapus")
            break
        else:
            print("Data tidak ditemukan")
        
    def ubah(self):
        print("\nUBAH DATA")
        nama = input("Masukkan Nama mahasiswa yang akan diubah: ")
        for data in self.mahasiswa:
         if data['Nama'] == nama:
            print("\nData sebelumnya:")
            print("NIM:", data['NIM'])
            print("Nilai Tugas:", data['Tugas'])
            print("Nilai UTS:", data['UTS'])
            print("Nilai UAS:", data['UAS'])
            
            print("\nMasukkan data baru:")
            data['NIM'] = int(input("NIM: "))
            data['Tugas'] = float(input("Nilai Tugas: "))
            data['UTS'] = float(input("Nilai UTS: "))
            data['UAS'] = float(input("Nilai UAS: "))
            data['Akhir'] = (0.3 * data['Tugas']) + (0.35 * data['UTS']) + (0.35 * data['UAS'])
            print("Data Berhasil Diubah")
            break
        else:
            print("Data Tidak Ditemukan")

#perulangan
data = Mahasiswa()
while True:
        print()
        menu = input("[(T)ambah, (L)ihat, (H)apus, (U)bah, (K)eluar] : ")
    
        if menu.lower() == 't':
            data.tambah()     
        elif menu.lower() == 'l':
            data.lihat()  
        elif menu.lower() == 'h':
            data.hapus()
        elif menu.lower() == 'u':
            data.ubah()
        elif menu.lower() == 'k':
            break