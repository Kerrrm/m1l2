import random





karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu = int(input("şifre uzunluğu giriniz"))
sifre = " "
for i in range(sifre_uzunlugu):
    sifre = sifre + random.choice(karakterler)
print(sifre)
