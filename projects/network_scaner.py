import socket
from datetime import datetime

# Tekshiriladigan IP manzil yoki xost nomi
target = input("Tekshiriladigan IP yoki hostni kiriting (masalan: 127.0.0.1): ")

print("-" * 50)
print(f"Skanerlanmoqda: {target}")
print(f"Boshlanish vaqti: {datetime.now()}")
print("-" * 50)

try:
    # 1 dan 1024 gacha bo'lgan asosiy portlarni tekshiramiz
    for port in range(1, 1025):
        # Socket yaratish (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Ulanish uchun kutish vaqti (sekundda)
        socket.setdefaulttimeout(0.5)
        
        # Portga ulanib ko'rish
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OCHIQ")
        
        s.close()

except KeyboardInterrupt:
    print("\nDastur foydalanuvchi tomonidan to'xtatildi.")
except socket.gaierror:
    print("\nHost nomi aniqlanmadi.")
except socket.error:
    print("\nServerga ulanib bo'lmadi.")

print("-" * 50)
print("Skanerlash yakunlandi.")
