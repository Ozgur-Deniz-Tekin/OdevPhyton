from random import randint

rand = randint(3, 300)
sayac = 0

while True:
    sayac += 1
    sayi1 = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if sayi1 == 0:
        print("Oyunu İptal Ettiniz")
        break
    sayi2 = int(input("1 ile 100 arasında değer girin:"))
    sayi3 = int(input("1 ile 100 arasında değer girin:"))
    if sayi1 == 0:
        print("Oyunu İptal Ettiniz")
        break
    elif sayi1 + sayi2 + sayi3 < rand:
        print("Daha Yüksek Sayılar Girin.")
        continue
    elif sayi1 + sayi2 + sayi3 > rand:
        print("Daha Düşük Sayılar Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
        break