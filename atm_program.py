import random
import datetime
from customer import Customer

atm = Customer(id)


def report():
    print("Resi tercetak otomatis saat anda keluar\nHarap simpan tanda terima ini\nsebagai bukti transaksi anda")
    print("No. Rekord: ", random.randint(100000, 1000000))
    print("Tanggal: ", datetime.datetime.now())
    print("Saldo akhir: ", atm.checkBalance())
    print("Terimakasih telah menggunakan ATM-CLI")
    exit()


def comfirmExit():
    while True:
        cF = input("Apakah anda ingin melanjutkan transaksi? (y/n) ")
        if cF == "y" and "Y":
            break
        elif cF == "n" and "N":
            report()
        else:
            continue


while True:
    id = int(input("Masukan pin anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin yang anda masukan salah, silakan coba lagi: "))
        trial += 1

        if trial == 3:
            print("Error: Silakan ambil kartu dan coba lagi.")
            exit()

    while True:
        print("Selamat datang di ATM-CLI")
        print("\n1 - Cek Saldo\n2 - Penarikan\n3 - Penyimpanan\n4 - Ganti Pin\n5 - Keluar")
        selectMenu = int(input("\nSilakan pilih menu: "))
        if selectMenu == 1:
            print("\nSaldo anda Rp. " +
                  str(atm.checkBalance()) + "\n")
            comfirmExit()

        elif selectMenu == 2:
            nominal = int(input("Masukkan nominal: "))
            verify_withdraw = input(
                "Anda akan melakukan penarikan dengan nominal " + str(nominal) + "? (y/n) ")

            if verify_withdraw == "y" and "Y":
                print("Saldo awal anda Rp. " +
                      str(atm.checkBalance()) + "")
            else:
                continue
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Penarikan berhasil\nSaldo anda sekarang Rp. " +
                      str(atm.checkBalance()))
            else:
                print("Maaf, Saldo anda tidak cukup untuk melakukan penarikan tersebut")
            comfirmExit()

        elif selectMenu == 3:
            nominal = int(input("Masukkan nominal saldo: "))
            verify_deposit = input(
                "Anda akan melakukan penyimpanan dengan nominal " + str(nominal) + "? y/n ")

            if verify_deposit == "y" and "Y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp." +
                      str(atm.checkBalance()) + "\n")
            else:
                continue
            comfirmExit()

        elif selectMenu == 4:
            verify_pin = int(input("Masukkan pin anda: "))

            while verify_pin != int(atm.checkPin()):
                print("Pin anda salah, silakan masukkan pin: ")

            updated_pin = int(input("Silakan masukkan pin baru: "))
            print("Pin anda berhasil diganti")

            verify_newpin = int(input("Coba masukkan pin baru: "))

            if verify_newpin == updated_pin:
                print("Pin baru anda sukses")
            else:
                print("Maaf, pin anda salah")
            comfirmExit()

        elif selectMenu == 5:
            report()

        else:
            print("Error: Maaf, menu tidak tersedia")
