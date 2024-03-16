print("Welcome to Toko Alat Tulis Gojo")
print("Kami Menyediakan segala kebutuhan alat tulis kamu! Khusus hari ini, Diskon 10% ALL PRODUCT")

pulpen = 1000
buku = 2000
stapler = 3000
kertas = 5000
spidol = 7000
penghapus = 1500

diskon = 0.1
pajak = 0.11
servicefee = 500

def hitung_harga(jumlah, harga):
    return jumlah * harga

def beli_barang(barang, jumlah):
    if barang == 1:
        return hitung_harga(jumlah, pulpen)
    elif barang == 2:
        return hitung_harga(jumlah, buku)
    elif barang == 3:
        return hitung_harga(jumlah, stapler)
    elif barang == 4:
        return hitung_harga(jumlah, kertas)
    elif barang == 5:
        return hitung_harga(jumlah, spidol)
    elif barang == 6:
        return hitung_harga(jumlah, penghapus)

def tampilkan_rincian(harga_sebelum_diskon, hargasetelahdiskon, total_pajak, hargasetelahpajak, total_harga):
    print("===============================================")
    print("Harga sebelum diskon:", harga_sebelum_diskon)
    print("Harga setelah diskon:", hargasetelahdiskon)
    print("Total pajak:", total_pajak)
    print("Harga setelah pajak:", hargasetelahpajak)
    print("Biaya layanan:", servicefee)
    print("===============================================")
    print("Total Harga yang Harus Dibayar:", total_harga)
    print("Terima Kasih Telah Berbelanja bersama kami!")

print("Pilih barang yang ingin dibeli:") #ini program swtich case/pemilihan
print("1. Pulpen")
print("2. Buku")
print("3. Stapler")
print("4. Kertas")
print("5. Spidol")
print("6. Penghapus")
print("7. Selesai")

total_harga_sebelum_diskon = 0

while True: #ini prpgramnya pake while true(semacam kondisi kalo user milih opsi benar)
    pilihan_barang = int(input("Pilih Opsi (1-7): "))
    
    if pilihan_barang == 7:
        break  #Keluar dari proses loop/pengulangan berbelanja
               #break gunanya untuk berhenti dari proses looping tadi

    if pilihan_barang < 1 or pilihan_barang > 6: #kalo user mencet angaka selain dari opsi
                                                 #bakal balik ke awal lagi
        print("Pilihan tidak valid. Silakan pilih lagi.")
        continue #kalo user salah input bakal balik awal, itu kegunaan dari continue

    jumlah_barang = int(input("Jumlah barang yang ingin dibeli: "))
    total_harga_sebelum_diskon += beli_barang(pilihan_barang, jumlah_barang)

hargasetelahdiskon = total_harga_sebelum_diskon * (1 - diskon)
total_pajak = hargasetelahdiskon * pajak
hargasetelahpajak = hargasetelahdiskon + total_pajak
total_harga = hargasetelahpajak + servicefee

tampilkan_rincian(total_harga_sebelum_diskon, hargasetelahdiskon, total_pajak, hargasetelahpajak, total_harga)
