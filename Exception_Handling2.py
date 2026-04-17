try:
    user_input = input("Son kiriting: ")
    son = int(user_input)  # Agar harf kiritilsa ValueError beradi
    natija = 100 / son     # Agar 0 kiritilsa ZeroDivisionError beradi
    print(f"Natija: {natija}")

except ValueError:
    print("Xato: Iltimos, faqat raqam kiriting!")

except ZeroDivisionError:
    print("Xato: Nolga bo'lish taqiqlangan!")

except Exception as e:
    print(f"Kutilmagan xato yuz berdi: {e}")
