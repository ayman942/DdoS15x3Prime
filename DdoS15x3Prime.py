import random
import time
import sys
import os
import socket
import threading
from datetime import datetime

# ----------- Colors -----------
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
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ----------- Typing Effect -----------
def type_effect(text, color=Colors.WHITE, delay=0.03):
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

# ----------- Clear Screen -----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ----------- Animated Banner -----------
def animated_banner():
    frames = [
        f"""
{Colors.ORANGE}╔═╗┬ ┬╔╦╗┌─┐┌┬┐  ╔═╗╔═╗╔═╗
{Colors.ORANGE}╠═╝│ │ ║║│ │ │   ╚═╗║  ║╣ 
{Colors.ORANGE}╩  └─┘╩ ╩└─┘ ┴   ╚═╝╚═╝╚═╝
{Colors.YELLOW}     NetStress - Advanced Testing
        """,
        f"""
{Colors.GREEN}╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦╔╗╔╔═╗
{Colors.GREEN} ║║║╣ ╠╦╝╚═╗║╣  ║║║ ║║║║║║╣ 
{Colors.GREEN}═╩╝╚═╝╩╚═╚═╝╚═╝═╩╝╚═╝╩╝╚╝╚═╝
{Colors.YELLOW}     Power Edition v4.0
        """,
        f"""
{Colors.CYAN}┌─┐┬─┐┌─┐┌─┐┬ ┬┌─┐┌┐┌┌┬┐
{Colors.CYAN}├─┘├┬┘│ │├─┘├─┤├─┤│││ │ 
{Colors.CYAN}┴  ┴└─└─┘┴  ┴ ┴┴ ┴┘└┘ ┴ 
{Colors.YELLOW}  Ultimate Load Tester
        """
    ]
    
    for i in range(8):
        clear_screen()
        print(frames[i % 3])
        time.sleep(0.2)

# ----------- Static Logo -----------
def print_logo():
    logo = f"""
{Colors.PINK}╭━━━╮╱╱╱╱╱╭━━━┳━━━┳━━━╮
{Colors.PINK}┃╭━╮┃╱╱╱╱╱┃╭━╮┃╭━╮┃╭━╮┃
{Colors.PINK}┃┃╱┃┣┳━━┳━╯┃╱┃┃┃╱╰┫┃╱┃┃
{Colors.PINK}┃┃╱┃┣┫╭╮┃╭╮┃╱┃┃┃╭━┫┃╱┃┃
{Colors.PINK}┃╰━╯┃┃╰╯┃╰╯┃╰━╯┃╰┻┫╰━╯┃
{Colors.PINK}╰━━━┻┻━━┻━━┻━━━┻━━┻━━━╯
{Colors.YELLOW}       Advanced Testing Suite
{Colors.RESET}"""
    print(logo)

# ----------- Welcome Message -----------
def welcome_message():
    print(f"{Colors.GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.BOLD}{Colors.CYAN}            WELCOME TO NETSTRESS PRO EDITION{Colors.RESET}{Colors.GREEN}            ║")
    print(f"║{Colors.BOLD}{Colors.CYAN}           Ultimate Performance Testing Suite{Colors.RESET}{Colors.GREEN}          ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    # Animated typing effect
    messages = [
        "🚀 Initializing advanced testing modules...",
        "🔧 Loading security protocols...",
        "📊 Preparing performance metrics...",
        "⚡ Powering up testing engine..."
    ]
    
    for msg in messages:
        type_effect(f"{Colors.YELLOW}{msg}{Colors.RESET}", Colors.YELLOW, 0.02)
        time.sleep(0.5)

# ----------- Legal Disclaimer -----------
def show_disclaimer():
    clear_screen()
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.BOLD}                    LEGAL DISCLAIMER{Colors.RESET}{Colors.RED}                    ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║ {Colors.YELLOW}🔒 FOR EDUCATIONAL PURPOSES ONLY{Colors.RED}                       ║")
    print(f"║ {Colors.YELLOW}📝 WRITTEN PERMISSION REQUIRED{Colors.RED}                         ║")
    print(f"║ {Colors.YELLOW}⚖️  ILLEGAL WITHOUT AUTHORIZATION{Colors.RESET}{Colors.RED}                      ║")
    print(f"║ {Colors.YELLOW}🔐 TEST LOCALHOST ONLY{Colors.RED}                                ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.GRAY}By continuing, you agree to:")
    print("• Use only for educational purposes")
    print("• Test only systems you own")
    print("• Obtain proper authorization")
    print("• Follow all applicable laws{Colors.RESET}")
    
    response = input(f"\n{Colors.GRAY}🤝 Do you agree? (y/n): {Colors.RESET}").lower()
    return response == 'y'

# ----------- Progress Bar -----------
def progress_bar(title, duration=3, color=Colors.GREEN):
    print(f"\n{Colors.BOLD}{title}{Colors.RESET}")
    for i in range(101):
        bar = "█" * (i // 2) + "░" * (50 - i // 2)
        percentage = f"{i}%"
        print(f"{color}\r[{bar}] {percentage}", end="", flush=True)
        time.sleep(duration / 100)
    print(f"{Colors.RESET}")

# ----------- Permission Check -----------
def check_permission(target):
    """Check if testing is authorized for the target"""
    print(f"{Colors.YELLOW}🔍 Checking authorization for {target}...{Colors.RESET}")
    time.sleep(1)
    
    # Only allow local testing
    allowed_targets = ["localhost", "127.0.0.1", "0.0.0.0", "::1"]
    if any(allowed in target for allowed in allowed_targets):
        print(f"{Colors.GREEN}✅ Authorization granted for local testing{Colors.RESET}")
        return True
    else:
        print(f"{Colors.RED}❌ EXTERNAL TARGET DETECTED{Colors.RESET}")
        print(f"{Colors.YELLOW}📝 Written permission required for external testing{Colors.RESET}")
        return False

# ----------- Advanced Load Tester -----------
class AdvancedLoadTester:
    def __init__(self):
        self.testing = False
        self.requests_sent = 0
        self.start_time = None
        self.threads = []
        
    def simulate_advanced_test(self, target, duration, concurrent_users, test_type="HTTP"):
        """Simulate advanced load testing"""
        if not check_permission(target):
            return False
            
        print(f"{Colors.GREEN}🚀 Starting {test_type} load test on {target}{Colors.RESET}")
        print(f"{Colors.CYAN}⏰ Duration: {duration}s | 👥 Users: {concurrent_users}{Colors.RESET}")
        print(f"{Colors.PURPLE}🎯 Test Type: {test_type}{Colors.RESET}")
        
        self.testing = True
        self.requests_sent = 0
        self.start_time = datetime.now()
        self.threads = []
        
        progress_bar("Initializing advanced testing environment", 2, Colors.BLUE)
        
        # Start simulation threads
        for i in range(concurrent_users):
            thread = threading.Thread(target=self._simulate_user, args=(target, duration, test_type, i+1))
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
        
        # Show progress
        for second in range(duration):
            if not self.testing:
                break
                
            time.sleep(1)
            elapsed = datetime.now() - self.start_time
            rps = self.requests_sent / max(1, elapsed.seconds)
            
            print(f"{Colors.BLUE}📊 [{second+1:03d}/{duration:03d}] | ", end="")
            print(f"Requests: {self.requests_sent:06d} | ", end="")
            print(f"RPS: {rps:06.1f} | ", end="")
            print(f"Users: {concurrent_users:03d}{Colors.RESET}")
        
        self.testing = False
        return True
    
    def _simulate_user(self, target, duration, test_type, user_id):
        """Simulate individual user"""
        start_time = time.time()
        
        while self.testing and (time.time() - start_time) < duration:
            try:
                # Simulate different test types
                if test_type == "HTTP":
                    self._simulate_http_request(target, user_id)
                elif test_type == "TCP":
                    self._simulate_tcp_connection(target, user_id)
                elif test_type == "UDP":
                    self._simulate_udp_packet(target, user_id)
                
                time.sleep(random.uniform(0.1, 0.5))
                
            except Exception as e:
                continue
    
    def _simulate_http_request(self, target, user_id):
        """Simulate HTTP request"""
        self.requests_sent += 1
        # Simulate response time
        time.sleep(random.uniform(0.01, 0.1))
    
    def _simulate_tcp_connection(self, target, user_id):
        """Simulate TCP connection"""
        self.requests_sent += 1
        time.sleep(random.uniform(0.05, 0.2))
    
    def _simulate_udp_packet(self, target, user_id):
        """Simulate UDP packet"""
        self.requests_sent += 1
        time.sleep(random.uniform(0.02, 0.15))
    
    def generate_advanced_report(self, target, test_type):
        """Generate advanced performance report"""
        if self.start_time:
            elapsed = datetime.now() - self.start_time
            rps = self.requests_sent / max(1, elapsed.seconds)
            
            print(f"\n{Colors.GREEN}📈 ADVANCED PERFORMANCE REPORT{Colors.RESET}")
            print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.CYAN}║ {Colors.BOLD}Test Summary{Colors.RESET}{Colors.CYAN}                                  ║{Colors.RESET}")
            print(f"{Colors.CYAN}╠══════════════════════════════════════════════════════╣{Colors.RESET}")
            print(f"{Colors.CYAN}║ 🔗 Target:    {target:35s} ║{Colors.RESET}")
            print(f"{Colors.CYAN}║ 🎯 Type:      {test_type:35s} ║{Colors.RESET}")
            print(f"{Colors.CYAN}║ ⏰ Duration:   {elapsed.seconds:7d} seconds{Colors.RESET}{' ':25s}{Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}║ 📦 Requests:  {self.requests_sent:7d}{Colors.RESET}{' ':25s}{Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}║ 🚀 RPS:       {rps:7.1f}{Colors.RESET}{' ':25s}{Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}║ 📊 Status:    {'COMPLETED':35s} ║{Colors.RESET}")
            print(f"{Colors.CYAN}╚══════════════════════════════════════════════════════╝{Colors.RESET}")
            
            return {
                'target': target,
                'type': test_type,
                'duration': elapsed.seconds,
                'total_requests': self.requests_sent,
                'rps': rps,
                'status': 'completed'
            }

# ----------- Main Menu -----------
def main_menu():
    print(f"\n{Colors.GREEN}╔══════════════════════════════════════════════════════════════╗")
    print(f"║{Colors.BOLD}                     MAIN MENU{Colors.RESET}{Colors.GREEN}                               ║")
    print(f"╠══════════════════════════════════════════════════════════════╣")
    print(f"║ {Colors.CYAN}1.{Colors.RESET} 🚀 Quick HTTP Test {Colors.GREEN}(Localhost){Colors.RESET}                  ║")
    print(f"║ {Colors.CYAN}2.{Colors.RESET} 🔧 Advanced Test {Colors.GREEN}(Custom Parameters){Colors.RESET}           ║")
    print(f"║ {Colors.CYAN}3.{Colors.RESET} 📊 Performance Analytics{Colors.RESET}                         ║")
    print(f"║ {Colors.CYAN}4.{Colors.RESET} ⚙️  System Diagnostics{Colors.RESET}                           ║")
    print(f"║ {Colors.CYAN}5.{Colors.RESET} 🔄 Multi-Protocol Test{Colors.RESET}                           ║")
    print(f"║ {Colors.RED}0.{Colors.RESET} ❌ Exit{Colors.RESET}                                           ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    try:
        choice = int(input(f"\n{Colors.GRAY}🎯 Choose an option (0-5): {Colors.RESET}"))
        return choice
    except ValueError:
        return -1

# ----------- Main Program -----------
def main():
    # Initial presentation
    animated_banner()
    clear_screen()
    print_logo()
    welcome_message()
    
    # Check legal conditions
    if not show_disclaimer():
        print(f"{Colors.RED}\n❌ Authorization required. Exiting...{Colors.RESET}")
        time.sleep(2)
        return
    
    # Initialize testing tool
    tester = AdvancedLoadTester()
    
    # Main menu loop
    while True:
        clear_screen()
        print_logo()
        
        choice = main_menu()
        
        if choice == 0:
            print(f"{Colors.GREEN}\n👋 Thank you for using NetStress Pro!{Colors.RESET}")
            break
            
        elif choice == 1:
            # Quick test on localhost
            target = "http://localhost:8080"
            if tester.simulate_advanced_test(target, 15, 10, "HTTP"):
                tester.generate_advanced_report(target, "HTTP")
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
            
        elif choice == 2:
            # Advanced test
            target = input(f"{Colors.GRAY}🎯 Enter target URL: {Colors.RESET}")
            test_type = input(f"{Colors.GRAY}🎯 Test Type (HTTP/TCP/UDP): {Colors.RESET}").upper()
            try:
                duration = int(input(f"{Colors.GRAY}⏰ Duration (seconds): {Colors.RESET}"))
                users = int(input(f"{Colors.GRAY}👥 Concurrent users: {Colors.RESET}"))
                
                if tester.simulate_advanced_test(target, duration, users, test_type):
                    tester.generate_advanced_report(target, test_type)
            except ValueError:
                print(f"{Colors.RED}❌ Please enter valid numbers{Colors.RESET}")
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
            
        elif choice == 3:
            # Performance analytics
            print(f"{Colors.YELLOW}📈 Performance analytics would be here{Colors.RESET}")
            progress_bar("Generating performance analytics", 3, Colors.PURPLE)
            print(f"{Colors.GREEN}✅ Analytics completed{Colors.RESET}")
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
            
        elif choice == 4:
            # System diagnostics
            print(f"{Colors.YELLOW}🛠️ System diagnostics would be here{Colors.RESET}")
            progress_bar("Running system diagnostics", 2, Colors.ORANGE)
            print(f"{Colors.GREEN}✅ Diagnostics completed{Colors.RESET}")
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
            
        elif choice == 5:
            # Multi-protocol testing
            print(f"{Colors.YELLOW}🔄 Multi-protocol testing would be here{Colors.RESET}")
            progress_bar("Initializing multi-protocol test", 4, Colors.CYAN)
            print(f"{Colors.GREEN}✅ Multi-protocol test completed{Colors.RESET}")
            input(f"\n{Colors.GRAY}Press Enter to continue...{Colors.RESET}")
            
        else:
            print(f"{Colors.RED}❌ Invalid choice. Please try again.{Colors.RESET}")
            time.sleep(1)

# Run the program
if __name__ == "__main__":
    main()
