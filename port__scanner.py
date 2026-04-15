import socket

class Scanner:
    def __init__(self, target):
        self.target = target

    def scan_port(self, port):
        # Soket yaratish (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Kutish vaqtini belgilash (1 soniya)
        s.settimeout(1)
        
        # Portni tekshirish
        result = s.connect_ex((self.target, port))
        
        if result == 0:
            print(f"[+] Port {port} OCHIQ")
        else:
            print(f"[-] Port {port} yopiq")
        
        s.close()

# Ishlatish qismi
target_ip = "127.0.0.1" # O'zingizning kompyuteringiz
my_scanner = Scanner(target_ip)

print(f"Skanerlanmoqda: {target_ip}")
# 75-dan 85-gacha bo'lgan portlarni tekshiramiz
for port in range(75, 85):
    my_scanner.scan_port(port)
