class User:
    def __init__(self, name):
        self.__name = name  # Yashirin (private) maydon

    @property  # Getter: Qiymatni o'qish uchun
    def name(self):
        return self.__name

    @name.setter  # Setter: Qiymatni o'zgartirish (va tekshirish) uchun
    def name(self, value):
        if len(value) > 2:
            self.__name = value
        else:
            print("Xato: Ism juda qisqa!")

# Ishlatilishi:
u = User("Ali")
print(u.name)      # Getter ishlaydi -> Ali

u.name = "Vali"    # Setter ishlaydi
print(u.name)      # -> Vali

u.name = "Ab"      # Xatolik xabari chiqadi
