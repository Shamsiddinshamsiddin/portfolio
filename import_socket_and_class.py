import socket

class PortScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def scan(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.target_ip, port))
        if result == 0:
            print(f"Port {port} ochiq!")
        s.close()

# Ishlatish:
my_scan = PortScanner("127.0.0.1")
my_scan.scan(80)
