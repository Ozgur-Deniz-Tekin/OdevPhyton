sozluk={}
i = int(input("Kaç tane bilgi girmek istiyorsunuz?: "))
x = 0
while x != i:
    islem=input('İşlem Nedir?: ')
    miktar=input('Ne Kadar Para Kazanıldı/Kaybedildi?: ')
    sozluk[islem]=miktar
    x+=1
print(sozluk[input("Görmek istediğniz işlem nedir?")])





