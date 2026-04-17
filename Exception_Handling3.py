try:
    fayl = open("malumot.txt", "r")
    tarkib = fayl.read()
except FileNotFoundError:
    print("Fayl topilmadi!")
else:
    print("Fayl muvaffaqiyatli o'qildi.")
finally:
    print("Amaliyot yakunlandi.")
    # Agar fayl ochilgan bo'lsa, uni yopish kerak
