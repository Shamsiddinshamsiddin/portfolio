import random

harflar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sonlar = "1234567890"
belgilar = "!@#$%^&*"

belgilar_toplami = ""

print("Harflar qo‘shilsinmi? (y/n)")
if input().lower() == "y":
    belgilar_toplami += harflar

print("Sonlar qo‘shilsinmi? (y/n)")
if input().lower() == "y":
    belgilar_toplami += sonlar

print("Belgilar qo‘shilsinmi? (y/n)")
if input().lower() == "y":
    belgilar_toplami += belgilar

# Tekshiruv
if belgilar_toplami == "":
    print("Kamida bitta variant tanlash kerak!")
else:
    uzunlik = int(input("Parol uzunligi: "))

    parol = ""

    for i in range(uzunlik):
        parol += random.choice(belgilar_toplami)

    print("Sizning parolingiz:", parol)
