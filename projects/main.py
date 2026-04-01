# 1. Inheritance (Vorislik) va Encapsulation (Enkapsulyatsiya) namunasi
class Foydalanuvchi:
    def __init__(self, ismi, login, parol):
        self.ismi = ismi            # Public
        self.login = login          # Public
        self.__parol = parol        # Private (Enkapsulyatsiya - yashirin)

    def profil_malumoti(self):
        return f"Foydalanuvchi: {self.ismi}, Login: {self.login}"

    # Parolni tekshirish uchun maxsus metod (Getter)
    def parolni_tekshir(self, kiritilgan_parol):
        return self.__parol == kiritilgan_parol

# 2. Vorislik (Inheritance)
class Admin(Foydalanuvchi):
    def __init__(self, ismi, login, parol, daraja):
        super().__init__(ismi, login, parol)
        self.daraja = daraja # Adminning o'ziga xos xususiyati

    def admin_huquqi(self):
        return f"{self.ismi} tizimda {self.daraja} huquqiga ega."

# Obyektlar bilan ishlash
shamsiddin = Admin("Shamsiddin", "shams_cyber", "secret123", "SuperAdmin")

print(shamsiddin.profil_malumoti())
print(shamsiddin.admin_huquqi())

# Enkapsulyatsiya testi
# print(shamsiddin.__parol) # Bu xato beradi, chunki parol yashirin!
print(f"Parol to'g'rimi?: {shamsiddin.parolni_tekshir('secret123')}")
