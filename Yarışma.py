import random
import time
yco = 0
dco = 0
bco = 0
soruliste=["""II Dünya Savaşı'nda Danimarka'nin düşmesi ne kadar zaman almıştır?  
    A)4 Saat  
    B)2 Hafta  
    C)3 Gün  
    D)30 Dakika""","""TYT sınavında Matematik alanından kaç tane soru var?
    A)35
    B)20
    C)50
    D)40""","""Sinekli Bakkal" romanının yazarı kimdir?
    A)Reşat Nuri Güntekin
    B)Halide Edip Adıvar
    C)Ziya Gökalp
    D)Ömer Seyfettin""","""Aşağıda Verilen İlk Çağ Uygarlıklarından Hangisi Yazıyı İcat Etmiştir?
    A) Hititler 
    B) Elamlar 
    C) Sümerler 
    D) Urartular""","""Tsunami Felaketinde En Fazla Zarar Gören Güney Asya Ülkesi Aşağıdakilerden Hangisidir?
    A) Endonezya 
    B) Srilanka 
    C) Tayland 
    D) Hindistan""","""2003 Yılında Euro Vizyon Şarkı Yarışmasında Ülkemizi Temsil Eden ve Yarışmada Birinci Gelen Sanatçımız Kimdir?
    A) Grup Athena 
    B) Sertap Erener 
    C) Şebnem Paker 
    D) Ajda Pekkan""","""Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir?
    A) Bursa 
    B) Ankara 
    C) İstanbul 
    D) Gaziantep""","""Aşağıdakilerden Hangisi Dünya Sağlık Örgütünün Kısaltılmış İsmidir?
    A) UHW
    B) UNICEF 
    C) WHO 
    D) NATO""","""Roma Rakamlarında Hangi Sayı Yoktur?
    A) 0 
    B) 50 
    C) 100
    D) 1000""","""Bir Gün Kaç Saniyedir?
    A) 86000 
    B) 88600 
    C) 86400 
    D) 84800""","""Üç Büyük Dince Kutsal Sayılan Şehir Hangisidir?
    A) Mekke 
    B) Kudüs 
    C) Roma 
    D) İstanbul""","""Hangi İlimizde Demiryolu Yoktur?
    A) Batman 
    B) Kütahya 
    C) Aydın 
    D) Muğla""","""Hangi Ülkenin İki Tane Başkenti Vardır?
    A)Güney Afrika 
    B)Senegal 
    C)El Salvador 
    D)Venezuela""","""Cevdet Bey ve Oğulları Eseri Kime Aittir?
    A)Orhan Pamuk 
    B)Yahya Kemal Bayatlı 
    C)Atilla İlhan 
    D)Samipaşazade Sezai ""","""Bir Sebepten Dolayı Tek Kulağına Küpe Takan Osmanlı Padişahı Kimdir?
    A)Kanuni Sultan Süleyman 
    B)Yavuz Sultan Selim 
    C)Orhan Bey 
    D)Fatih Sultan Selim""",""""Aşağıdaki Ülkelerden Hangisinin Nüfusu Daha Fazladır?
    A)İspanya 
    B)Fransa 
    C)İngiltere
    D)Almanya""","""Aspirinin Hammaddesi Nedir?
    A)Söğüt 
    B)Köknar 
    C)Kavak 
    D)Meşe""","""Hangi Galakside yaşıyoruz?
    A)Cüce Ejderha
    B)Samanyolu
    C)Andromeda
    D)Büyükayı""","""Bu kod yazılırken kullanılınan kodlama dili nedir?
    A)C++
    B)JavaScript
    C)Phyton
    D)C#"""]
f = 0
liste2 = soruliste.copy()
while f != 10:
    i = random.randint(0,18)
    print(soruliste.pop(i))
    soruliste = liste2.copy()
    f += 1
    t = 5
    if i == 0:
        x = input('Cevap Nedir?')
        if x == 'a' or 'A':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
            while t > 0:
                if t == 0:
                    print('Zaman Tükendi!')
                    bco += 1
                t -= 1
                time.sleep(1)
                continue
    if i == 1:
        x = input('Cevap Nedir?')
        if x == 'd' or 'D':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 2:
        x = input('Cevap Nedir?')
        if x == 'b' or 'B':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 3:
        x = input('Cevap Nedir?')
        if x == 'c' or 'C':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
    if i == 4:
        x = input('Cevap Nedir?')
        if x == 'a' or 'A':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 5:
        x = input('Cevap Nedir?')
        if x == 'b' or 'B':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 6:
        x = input('Cevap Nedir?')
        if x == 'd' or 'D':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 7:
        x = input('Cevap Nedir?')
        if x == 'c' or 'C':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 8:
        x = input('Cevap Nedir?')
        if x == 'a' or 'A':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 9:
        x = input('Cevap Nedir?')
        if x == 'c' or 'C':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 10:
        x = input('Cevap Nedir?')
        if x == 'b' or 'B':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 11:
        x = input('Cevap Nedir?')
        if x == 'd' or 'D':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 12:
        x = input('Cevap Nedir?')
        if x == 'a' or 'A':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 13:
        x = input('Cevap Nedir?')
        if x == 'a' or 'A':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 14:
        x = input('Cevap Nedir?')
        if x == 'b' or 'B':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 15:
        x = input('Cevap Nedir?')
        if x == 'd' or 'D':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 16:
        x = input('Cevap Nedir?')
        if x == 'a' or 'A':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 17:
        x = input('Cevap Nedir?')
        if x == 'd' or 'D':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
    if i == 18:
        x = input('Cevap Nedir?')
        if x == 'c' or 'C':
            print("Doğru Bildiniz!")
            dco += 1
        else:
            print("Yanlış Bildiniz!")
            yco += 1
        if t == 0:
            print('Zaman Tükendi!')
            bco += 1
        while t > 0:
            if t == 0:
                print('Zaman Tükendi!')
                bco += 1
            t -= 1
            time.sleep(1)
            continue
        continue
print("Sonuçlarınız Bunlar:", "Doğru Sayısı:", dco - bco ,"Yanlış Sayısı:" , yco , "Boş Sayısı:" , bco , sep="\n")
