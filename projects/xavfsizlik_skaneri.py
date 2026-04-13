# 1. Dekorator - bu bizning Xavfsizlik Posti (Skaner)
def xavfsizlik_skaneri(vazifa):
    # wrapper - bu eshshakning tashqari kiyimi, hamma tekshiruv shu yerda bo'ladi
    def wrapper(ism, unvon):
        print(f"\n[TIZIM]: {ism} yaqinlashmoqda. Unvoni: {unvon}")
        print("--- Skaner: Ma'lumotlar bazasidan tekshirilmoqda... ---")
        
        # Kiber-xavfsizlik qoidasi: Faqat 'General'ga ruxsat bor
        if unvon == "General":
            print(f"--- [OK]: Ruxsat berildi. Xush kelibsiz, {ism}! ---")
            # Asosiy funksiya (Eshshak) o'z ishini bajaradi
            vazifa() 
        else:
            print(f"--- [XATO]: Kirish taqiqlangan! {ism}, xonangizga boring! ---")
            
    return wrapper

# 2. Asosiy funksiya - bu bizning Maxfiy Tugma (Eshshakning vazifasi)
@xavfsizlik_skaneri
def yadroviy_tugma():
    print(">>> [DIQQAT]: Qizil tugma bosildi! Raketalar havoga ko'tarildi! 🚀")

# 3. Keling, tizimni sinab ko'ramiz (Simulyatsiya)

# Oddiy askar kirmoqchi bo'ladi
yadroviy_tugma("Eshmat", "Oddiy askar")

print("-" * 50)

# General kirmoqchi bo'ladi
yadroviy_tugma("Toshmat", "General")
