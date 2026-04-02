class Texnikum:
    def __init__(self, ism, familya):
        self.ism = ism
        self.familya =  familya
    def talaba_haqida_malumot(self):
        print(f"tehnikum talabasi, {self.ism},{self.familya}")
class Guruh_03_25(Texnikum):
    def __init__(self, ism, familya, bahosi):
        super().__init__(ism,familya)
        self.bahosi = bahosi
    def guruh_talabasi_bahosi(self):
        print(f"guruh 03-25 talabasi, {self.ism}, {self.familya}, {self.bahosi}")
talaba1 = Guruh_03_25("Shamsiddin", "Baxramov", "5")
talaba2 = Guruh_03_25("Dilrabo", "Ruzmetova", "4")
talaba1.guruh_talabasi_bahosi()
talaba2.guruh_talabasi_bahosi()
