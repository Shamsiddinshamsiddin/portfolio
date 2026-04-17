try:
    son = int(input("Son kiriting: "))
    print(10 / son)
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
except ValueError:
    print("Faqat son kiriting!")
