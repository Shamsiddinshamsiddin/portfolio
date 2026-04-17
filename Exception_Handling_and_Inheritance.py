# 1. Vorislik yordamida o'z xato klassimizni yaratamiz
class BankXatosi(Exception):
    """Bank amallari uchun umumiy xato klassi"""
    pass

class MablagYetarliEmas(BankXatosi):
    """Mablag' yetmaganda chiqadigan maxsus xato"""
    def __init__(self, balans, summa):
        self.balans = balans
        self.summa = summa
        super().__init__(f"Balansda mablag' kam! Balans: {balans}, so'ralgan: {summa}")

# 2. Bank hisobi klassi
class BankHisobi:
    def __init__(self, balans):
        self.balans = balans

    def pul_yechish(self, summa):
        if summa > self.balans:
            # Maxsus xatoni chaqiramiz (raise)
            raise MablagYetarliEmas(self.balans, summa)
        
        self.balans -= summa
        print(f"Muvaffaqiyatli yechildi. Qolgan balans: {self.balans}")

# 3. Try-Except bloki bilan ishlash
hisob = BankHisobi(100000) # Balansda 100 ming bor

try:
    miqdor = int(input("Qancha pul yechmoqchisiz? "))
    hisob.pul_yechish(miqdor)

except MablagYetarliEmas as e:
    # Bu yerda biz yaratgan maxsus xato ushlab qolinadi
    print(f"Tranzaksiya rad etildi: {e}")

except ValueError:
    print("Xato: Iltimos, faqat raqam kiriting!")

except Exception as e:
    print(f"Kutilmagan muammo: {e}")

finally:
    print("Bank xizmatidan foydalanganingiz uchun rahmat!")
