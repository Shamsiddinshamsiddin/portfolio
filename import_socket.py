import socket

# 1. Soket yaratamiz (IPv4, TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. IP va Portni belgilaymiz (localhost, 9999-port)
server.bind(('127.0.0.1', 9999))

# 3. Aloqani kutamiz
server.listen(1)
print("Server ishga tushdi, aloqa kutilmoqda...")

client_socket, address = server.accept()
print(f"Aloqa o'rnatildi: {address}")

# 4. Ma'lumotni qabul qilamiz
data = client_socket.recv(1024).decode('utf-8')
print(f"Clientdan kelgan xabar: {data}")

# 5. Javob qaytaramiz va yopamiz
client_socket.send("Xabaringiz qabul qilindi!".encode('utf-8'))
client_socket.close()
server.close()
