import random
sozluk={}
liste=list('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPrqQRsStTuUvVwWyYzZ1234567890')
nu=int(input('Kaç Tane Şifre Oluşturmak İstiyorsunuz? : '))
for i in range(nu):
    sifre=random.sample(liste,16)
    sozluk['Şifre',i+1]=sifre
print(sozluk)







