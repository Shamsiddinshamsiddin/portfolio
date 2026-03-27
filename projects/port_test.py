# Asosiy maqsaq: 1 ta prtni skaner qilish uchun python code yozish
import socket
target = input("IP: ")
port = 80
s = socket.socket()
result = s.connect_ex((target, port))
if result == 0:
    print("Port ochiq")
else:
    print("Port yopiq")
s.close()
