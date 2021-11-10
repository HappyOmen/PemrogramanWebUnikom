#Program Validasi Barang
#I.S.:Pengguna memasukkan kode barang dan jumlah barang, lalu menentukan diskon bila ada
#F.S.:Menampilkan harga total,diskon,total bayar,dan uang kembalian

#input
KodeBarang = str(input("Masukkan Kode Barang: ")).upper()

#Menenteukan Kode Barang dan Harga Barang
if(KodeBarang == "PK01"):
    NamaBarang = "Pakaian"
    HargaSatuan = 75000
elif(KodeBarang == "TS02"):
    NamaBarang ="Tas"
    HargaSatuan = 65500
elif(KodeBarang == "SP03"):
    NamaBarang = "Sepatu"
    HargaSatuan = 157000
elif(KodeBarang == "AK04"):
    NamaBarang = "Aksesoris"
    HargaSatuan = 45000
else:
    print("Kode Barang Salah")
    return

#Menentukan Jumlah Beli
JumlahBarang = int(input("Masukkan Jumlah Barang: "))
if(JumlahBarang >= 10) :
    AdaDiskon = str(input("Ada Diskon (Y/T): ")).upper()
    if(AdaDiskon == "Y") :
        BesarDiskon = float(input("Masukkan Besar Diskon: "))
    else:
        BesarDiskon = 0

#menghitung harga total
HargaTotal = HargaSatuan * JumlahBarang

#menentukan diskon
Diskon = HargaTotal * (BesarDiskon/100)

#menghitung total bayar
TotalBayar = HargaTotal - Diskon

#menampilkan diskon dan total bayar
print("Diskon: Rp.", Diskon)
print("Total Bayar: ", TotalBayar)

#Memasukkan uang pembayaran
UangBayar = int(input("Masukkan Uang Pembayaran: "))

#Mengecek uang pembayaran
if(UangBayar < TotalBayar) :
    print("Pembayaran Kurang")
    UangBayar = int(input("Masukkan Uang Pembayaran: "))
else:
    print("Pembayaran Berhasil")

#Menghitung Kembalian
Kembalian = UangBayar-TotalBayar

#menampilkan
print("Kode Barang :", KodeBarang)
print("Nama Barang: ", NamaBarang)
print("Jumlah Beli: ", JumlahBarang)
print("Harga Satuan: Rp.", HargaSatuan)
print("Harga Total: Rp.", HargaTotal)
print("Diskon: ", BesarDiskon, "%")
print("Total Bayar: Rp.", TotalBayar)
print("------------------------------------------")
print("Bayar: Rp.", UangBayar)
print("Uang Kembali: Rp.", Kembalian)


