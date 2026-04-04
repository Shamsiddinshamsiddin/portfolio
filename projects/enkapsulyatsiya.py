class Bankkarta:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.__balans = balans # Buni yashirdik (private)

    def pul_qoshish(self, summa):
        if summa > 0:
            self.__balans += summa # Balansga pul qo'shiladi
            print(f"Hisobingizga {summa} so'm qo'shildi.")
        else:
            print("Xatolik: Summa musbat bo'lishi kerak!")

    def balansni_tekshir(self):
        # Tashqaridan __balans ni ko'rib bo'lmagani uchun shu metod kerak
        print(f"Hurmatli {self.egasi}, hisobingizda {self.__balans} so'm bor.")

# Ishlatib ko'ramiz:
karta = Bankkarta("Shamsiddin", 50000)

karta.pul_qoshish(20000)  # Pul qo'shamiz
karta.balansni_tekshir()  # Balansni ko'ramiz

# print(karta.__balans)   # BU XATO BERADI (Xavfsizlik tizimi ishladi!)
