class Dog:
    def speak(self):
        return "Vov-vov!"

class Cat:
    def speak(self):
        return "Miyau!"

class Duck:
    def speak(self):
        return "Quack-quack!"

# Polimorfizm: Bir xil interfeys (speak metodi), turli natijalar
animals = [Dog(), Cat(), Duck()]

for animal in animals:
    print(animal.speak())
