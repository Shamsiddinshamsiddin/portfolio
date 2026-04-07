class shohjahon:
    def speak(self):
        return "Salom, men shohjahonman!"
class shamsiddin:
    def speak(self):
        return "Salom, men shamsiddinman!"
class ustoz:
    def speak(self):
        return "Salom, men ustozman va ikkangga ham 5 qo'yib bermoqchiman!"
insonlar = [shohjahon(), shamsiddin(), ustoz()]
for inson in insonlar:
    print(inson.speak())