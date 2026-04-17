# Asosiy xato klassidan voris olamiz - Xavfsizlik xatolarini guruhlash uchun
class SecurityError(Exception):
    """Barcha xavfsizlik bilan bog'liq xatolar uchun asosiy klass"""
    pass

class AccessDeniedError(SecurityError):
    """Ruxsat berilmagan harakatlar uchun maxsus xato"""
    def __init__(self, user, action):
        self.user = user
        self.action = action
        # Xavfsizlik uchun xato xabarini umumiy ko'rinishda saqlaymiz
        super().__init__(f"DIQQAT: '{user}' foydalanuvchiga '{action}' amali taqiqlangan!")

class Firewall:
    def __init__(self):
        self.blocked_ips = ["192.168.1.50", "10.0.0.5"]

    def check_connection(self, ip, user_role):
        # 1. IP manzilni tekshirish
        if ip in self.blocked_ips:
            raise SecurityError("Xavfli IP aniqlandi!")
        
        # 2. Huquqni tekshirish (Vorislik mantiqi bilan bog'liq)
        if user_role != "admin":
            raise AccessDeniedError(user_role, "Admin-panelga kirish")

# --- AMALIY QO'LLASH (Try-Except xavfsizlik qalqoni) ---
firewall = Firewall()

try:
    current_ip = "192.168.1.50"
    role = "guest"
    
    firewall.check_connection(current_ip, role)

except AccessDeniedError as e:
    # Xatoni log faylga yozamiz, lekin foydalanuvchiga batafsil ma'lumot bermaymiz
    print(f"[LOG]: Xavfsizlik buzilishi! {e}")
    print("Xabar: Sizda bu amalni bajarish uchun huquq yetarli emas.")

except SecurityError:
    # Kiberxavfsizlik oltin qoidasi: Hujumchiga tizim haqida ma'lumot berma!
    print("Xabar: Tarmoq ulanishida xatolik. IT bo'limiga murojaat qiling.")

except Exception:
    # Kutilmagan xato bo'lsa ham, dastur 'crash' bo'lmasligi kerak
    print("Tizimda texnik profilaktika.")

finally:
    print("Xavfsizlik tizimi faol holatda.")
