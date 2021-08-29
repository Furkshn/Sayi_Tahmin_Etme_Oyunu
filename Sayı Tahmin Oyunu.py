import random
import time

def random_number_game():

    rastgele_sayı = random.randint(1, 40)
    tahmin_hakkı = 5

    while True:
        tahmin = int(input("Lütfen Tahmin Ettiğiniz Sayıyı Giriniz:"))

        if (tahmin < rastgele_sayı):
            print("Bilgiler Sorgulanıyor...")
            time.sleep(1)

            print("Daha Yüksek Bir Değer Giriniz.")

            tahmin -= 1
        elif (tahmin > rastgele_sayı):
            print("Bilgiler Sorgulanıyor...")
            time.sleep(1)

            print("Daha Düşük Bir Değer Giriniz.")

            tahmin -= 1
        else:

            print("Bilgiler Sorgulanıyor...")
            time.sleep(1)
            print("Tebrikler! Sayımız:", rastgele_sayı)
            break
        if (tahmin_hakkı == 0):
            print("Tahmin Hakkınız Bitti...")
            print("Sayımız:", rastgele_sayı)
            break


random_number_game()