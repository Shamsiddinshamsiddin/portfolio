def xavfsizlik_posti(vazifa):
    def wrapper(parol):
        print("--- Xavfsizlik posti: Parolni tekshiryapman... ---")
        if parol == "admin123":
            print("Ruxsat berildi! Marhamat kirishingiz mumkin.")
            vazifa() # Binoga kirishga ruxsat berildi
        else:
            print("XATO! Siz kiber-hujumchi bo'lsangiz kerak! Politsiya chaqirildi!")
    return wrapper
@xavfsizlik_posti
def maxfiy_bino():
    print("Siz maxfiy ma'lumotlarni ko'ryapsiz: 12345")

# Endi tekshirib ko'ramiz:
maxfiy_bino("notogri_parol") # Bu odam haydaladi
print("-" * 30)
maxfiy_bino("admin123")      # Bu odamga ruxsat beriladi
