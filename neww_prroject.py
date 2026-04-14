import socket
import threading
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from scapy.all import IP, ICMP, sr1, TCP, conf
from colorama import Fore, Style, init

# 1. Professional Log tizimi
logging.basicConfig(filename='network_audit.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

init(autoreset=True) # Rangli terminal uchun

class ProNetworkScanner:
    def __init__(self, target, threads=50):
        self.target = target
        self.threads = threads
        self.open_ports = []
        conf.verb = 0 # Scapy shovqinini o'chirish

    # 2. ICMP Ping Sweep (Host tirikligini tekshirish)
    def ping_host(self):
        print(f"{Fore.CYAN}[*] Host tekshirilmoqda: {self.target}")
        packet = IP(dst=self.target)/ICMP()
        reply = sr1(packet, timeout=2)
        if reply:
            print(f"{Fore.GREEN}[+] Host online!")
            return True
        return False

    # 3. Professional Port Scanner (TCP Connect Scan)
    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                service = socket.getservbyport(port, 'tcp')
                print(f"{Fore.YELLOW}[!] Port {port} Ochiq ({service})")
                self.open_ports.append((port, service))
                logging.info(f"Open Port: {port} Service: {service}")
            sock.close()
        except:
            pass

    # 4. Threading bilan tezlikni oshirish
    def run_scanner(self, start_port=1, end_port=1024):
        print(f"{Fore.BLUE} Scanning {self.target} from {start_port} to {end_port}...")
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.scan_port, range(start_port, end_port + 1))

    # 5. OS Fingerprinting (Sodda ko'rinishi)
    def detect_os(self):
        # Bu qism TTL qiymatiga qarab OS ni taxmin qiladi
        pkt = sr1(IP(dst=self.target)/ICMP(), timeout=2)
        if pkt:
            ttl = pkt.getlayer(IP).ttl
            if ttl <= 64: return "Linux/Unix"
            elif ttl <= 128: return "Windows"
            else: return "Unknown Device"
        return "Noma'lum"

# ... (Bu yerda yana 400-500 qatorli qo'shimcha modullar: Brute-force checker, 
# Banner grabbing, Reporting modullari bo'lishi mumkin)

def main():
    target_ip = input("Target IP ni kiriting: ")
    scanner = ProNetworkScanner(target_ip)
    
    if scanner.ping_host():
        os_type = scanner.detect_os()
        print(f"{Fore.MAGENTA}[i] Taxminiy OS: {os_type}")
        scanner.run_scanner()
        
if __name__ == "__main__":
    main()
