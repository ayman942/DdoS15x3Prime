import socket
import threading
import time
import os
import random
from datetime import datetime

# ----------- Enhanced 3D Color Scheme -----------
class Colors3D:
    # Base colors with depth effect
    DARK_BG = '\033[48;5;232m'  # Near black background
    LIGHT_BG = '\033[48;5;235m'  # Dark gray background
    
    # 3D accent colors with gradient effect
    BLUE_GRADIENT = [
        '\033[38;5;27m',   # Dark blue (shadow)
        '\033[38;5;39m',   # Medium blue
        '\033[38;5;51m'    # Bright blue (highlight)
    ]
    
    ORANGE_GRADIENT = [
        '\033[38;5;202m',  # Dark orange (shadow)
        '\033[38;5;208m',  # Medium orange
        '\033[38;5;214m'   # Bright orange (highlight)
    ]
    
    PURPLE_GRADIENT = [
        '\033[38;5;55m',   # Dark purple (shadow)
        '\033[38;5;93m',   # Medium purple
        '\033[38;5;129m'   # Bright purple (highlight)
    ]
    
    GREEN_GRADIENT = [
        '\033[38;5;28m',   # Dark green (shadow)
        '\033[38;5;34m',   # Medium green
        '\033[38;5;46m'    # Bright green (highlight)
    ]
    
    RED_GRADIENT = [
        '\033[38;5;124m',  # Dark red (shadow)
        '\033[38;5;196m',  # Medium red
        '\033[38;5;203m'   # Bright red (highlight)
    ]
    
    CYAN_GRADIENT = [
        '\033[38;5;30m',   # Dark cyan (shadow)
        '\033[38;5;44m',   # Medium cyan
        '\033[38;5;51m'    # Bright cyan (highlight)
    ]
    
    # 3D text effects
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    
    # 3D depth backgrounds
    DEPTH_1 = '\033[48;5;233m'  # Deepest level
    DEPTH_2 = '\033[48;5;234m'  # Middle level
    DEPTH_3 = '\033[48;5;235m'  # Surface level

# ----------- Enhanced 3D Text Effects -----------
def text_3d_enhanced(text, gradient, shadow_offset=1):
    """Create enhanced 3D text effect"""
    result = ""
    for char in text:
        if char != " ":
            result += f"{gradient[0]}{char}{gradient[1]}{char}{gradient[2]}{char}{Colors3D.RESET}"
        else:
            result += " "
    return result

def print_3d_text_enhanced(text, gradient=Colors3D.BLUE_GRADIENT, delay=0.03):
    """Print text with enhanced 3D effect"""
    for char in text:
        print(f"{gradient[1]}{char}{gradient[2]}{char}{Colors3D.RESET}", end='', flush=True)
        time.sleep(delay)
    print()

# ----------- Enhanced 3D Banner -----------
def print_enhanced_banner():
    """Display an enhanced 3D-style banner"""
    banner = f"""
{Colors3D.DARK_BG}{Colors3D.BLUE_GRADIENT[2]}╔═╗╔═╗╔═╗╔═╗╦╔═┌─┐┌─┐┬┌─┌─┐┬ ┬{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.BLUE_GRADIENT[1]}╠═╣╠═╝╠═╣║  ╠╩╗├┤ │ ├┴┐├┤ └┬┘{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.BLUE_GRADIENT[0]}╩ ╩╩  ╩ ╩╚═╝╩ ╩└─┘└─┘┴ ┴└─┘ ┴ {Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.ORANGE_GRADIENT[2]}┌┐ ┬ ┬┌─┐┌┬┐┌─┐┬─┐┌─┐┌─┐┬{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.ORANGE_GRADIENT[1]}├┴┐└┬┘├─┘ ││├┤ ├┬┘├─┤└─┐│{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.ORANGE_GRADIENT[0]}└─┘ ┴ ┴  ─┴┘└─┘┴└─┴ ┴└─┘o{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.PURPLE_GRADIENT[2]}╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦╔╗╔╔═╗{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.PURPLE_GRADIENT[1]} ║║║╣ ╠╦╝╚═╗║╣  ║║║ ║║║║║║╣ {Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.PURPLE_GRADIENT[0]}═╩╝╚═╝╩╚═╚═╝╚═╝═╩╝╚═╝╩╝╚╝╚═╝{Colors3D.RESET}
    """
    print(banner)

# ----------- Enhanced 3D Box Drawing -----------
def draw_enhanced_3d_box(title, content, width=60, gradient=Colors3D.BLUE_GRADIENT):
    """Draw an enhanced 3D-style box with depth effect"""
    top_line = f"{gradient[0]}╔{'═'*(width-2)}╗{Colors3D.RESET}"
    title_line = f"{gradient[0]}║{Colors3D.RESET}{gradient[1]}{Colors3D.BOLD}{title.center(width-2)}{Colors3D.RESET}{gradient[0]}║{Colors3D.RESET}"
    middle_line = f"{gradient[0]}║{Colors3D.RESET}{' '*(width-2)}{gradient[0]}║{Colors3D.RESET}"
    bottom_line = f"{gradient[0]}╚{'═'*(width-2)}╝{Colors3D.RESET}"
    
    print(top_line)
    print(title_line)
    for line in content:
        padded_line = f"{gradient[0]}║{Colors3D.RESET}{gradient[2]}{line.ljust(width-2)}{Colors3D.RESET}{gradient[0]}║{Colors3D.RESET}"
        print(padded_line)
    print(bottom_line)

# ----------- Enhanced 3D Progress Bar -----------
def enhanced_progress_bar_3d(title, duration=3, gradient=Colors3D.ORANGE_GRADIENT):
    """Enhanced 3D-style progress bar with depth effect"""
    print(f"\n{gradient[1]}{Colors3D.BOLD}{title}{Colors3D.RESET}")
    
    for i in range(101):
        # Create 3D bar effect
        bar_shadow = f"{gradient[0]}░" * (i // 2)
        bar_main = f"{gradient[1]}█" * (i // 2)
        bar_highlight = f"{gradient[2]}▓" * (i // 2)
        bar_remaining = f"{Colors3D.DIM}░{Colors3D.RESET}" * (50 - i // 2)
        
        percentage = f"{i}%"
        print(f"\r[{bar_shadow}{bar_main}{bar_highlight}{bar_remaining}] {percentage}", end="", flush=True)
        time.sleep(duration / 100)
    print(f"{Colors3D.RESET}")

# ----------- Enhanced Methods Display -----------
def show_enhanced_methods():
    """Display enhanced methods in 3D style"""
    methods = [
        "HOME METHODS",
        "  RAIL LOAP HOLD",
        "  BYPASSES",
        "  SERVER",
        "  MFO-STUM MFO-FRAG MFO-PORT",
        "  10BUP XFORTNITE TRUMP-SEC",
        "  SERVER",
        "  10BUP-CDU MTP-SMOKE HOME-CLAD",
        "  BYPASSES",
        "  OVM-MUKE OVM-VITIAL OVM-YULV2",
        "  OVM-AMBEL OVM-FAITH OVM-RAPE",
        "  FEVEM SSH ROBLOX",
        "VIP",
        "  LAYER7 UDP-XV DMS-C2",
        "VIP",
        "  OVM-UDP NTP-XV VSE-C2"
    ]
    
    draw_enhanced_3d_box("ENHANCED METHODS", methods, width=70, gradient=Colors3D.PURPLE_GRADIENT)

# ----------- Enhanced Port Scanner -----------
class EnhancedPortScanner:
    def __init__(self):
        self.open_ports = []
        self.scanning = False
        self.start_time = None
        self.common_ports = {
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            465: "SMTPS",
            587: "SMTP",
            993: "IMAPS",
            995: "POP3S",
            3306: "MySQL",
            3389: "RDP",
            5432: "PostgreSQL",
            6379: "Redis",
            27017: "MongoDB"
        }
    
    def scan_port(self, target, port, timeout=1):
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def scan_range(self, target, start_port, end_port, max_threads=100):
        """Scan a range of ports with threading"""
        self.open_ports = []
        self.scanning = True
        self.start_time = datetime.now()
        
        ports_to_scan = range(start_port, end_port + 1)
        total_ports = len(ports_to_scan)
        scanned_ports = 0
        
        # Create a thread lock for printing
        print_lock = threading.Lock()
        
        def scanner_thread(port):
            nonlocal scanned_ports
            if self.scan_port(target, port):
                with print_lock:
                    self.open_ports.append(port)
                    progress = (scanned_ports / total_ports) * 100
                    service = self.common_ports.get(port, "Unknown")
                    print(f"{Colors3D.GREEN_GRADIENT[1]}✅ PORT {port} OPEN ({service}){Colors3D.RESET} - Progress: {progress:.1f}%")
            scanned_ports += 1
        
        # Create and start threads
        threads = []
        for port in ports_to_scan:
            while threading.active_count() > max_threads:
                time.sleep(0.01)
            
            thread = threading.Thread(target=scanner_thread, args=(port,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        self.scanning = False
        return self.open_ports
    
    def display_results(self, target, start_port, end_port):
        """Display scanning results in 3D format"""
        elapsed = datetime.now() - self.start_time
        draw_enhanced_3d_box("SCAN RESULTS", [
            f"Target: {target}",
            f"Port range: {start_port}-{end_port}",
            f"Open ports: {len(self.open_ports)}",
            f"Time elapsed: {elapsed.total_seconds():.2f} seconds",
            "",
            "OPEN PORTS:"
        ], width=70, gradient=Colors3D.PURPLE_GRADIENT)
        
        if self.open_ports:
            # Display open ports with service names
            for port in sorted(self.open_ports):
                service = self.common_ports.get(port, "Unknown")
                print(f"   {Colors3D.GREEN_GRADIENT[2]}{port:5}{Colors3D.RESET} - {service}")
        else:
            print(f"   {Colors3D.RED_GRADIENT[1]}No open ports found{Colors3D.RESET}")
        
        print(f"\n{Colors3D.BLUE_GRADIENT[1]}Scan completed!{Colors3D.RESET}")

# ----------- Enhanced Menu System -----------
def enhanced_menu():
    """Display enhanced 3D-style menu"""
    options = [
        "🚀 QUICK HTTP TEST (Localhost)",
        "🔧 ADVANCED TEST (Custom Parameters)",
        "📊 PERFORMANCE ANALYTICS",
        "⚙️  SYSTEM DIAGNOSTICS",
        "🌐 IP:PORT SCANNER",
        "🔓 ENHANCED METHODS",
        "❌ EXIT"
    ]
    
    print(f"\n{Colors3D.PURPLE_GRADIENT[1]}{Colors3D.BOLD}        ENHANCED MAIN MENU{Colors3D.RESET}\n")
    
    for i, option in enumerate(options, 1):
        # Create 3D button effect
        if i == len(options):  # Exit option
            color = Colors3D.ORANGE_GRADIENT
        elif i == 5:  # IP:PORT Scanner option
            color = Colors3D.CYAN_GRADIENT
        elif i == 6:  # Enhanced Methods option
            color = Colors3D.GREEN_GRADIENT
        else:
            color = Colors3D.BLUE_GRADIENT
            
        button = f"{color[0]}[{color[1]}{i}{color[0]}]{Colors3D.RESET} {color[2]}{option}{Colors3D.RESET}"
        print(f"   {button}")
        time.sleep(0.1)
    
    try:
        choice = int(input(f"\n{Colors3D.PURPLE_GRADIENT[1]}Select option: {Colors3D.RESET}"))
        return choice
    except ValueError:
        return -1

# ----------- Main Application -----------
def main_enhanced():
    """Main application with enhanced 3D design"""
    # Clear screen and set dark background
    os.system("cls" if os.name == "nt" else "clear")
    
    # Display enhanced 3D banner
    print_enhanced_banner()
    
    # Welcome message
    welcome_text = "ENHANCED NETSTRESS PRO - 3D EDITION"
    print_3d_text_enhanced(welcome_text, Colors3D.PURPLE_GRADIENT)
    
    # Initialize scanner
    scanner = EnhancedPortScanner()
    
    # Main menu loop
    while True:
        choice = enhanced_menu()
        
        if choice == 1:
            # Quick test option
            draw_enhanced_3d_box("QUICK HTTP TEST", [
                "Target: localhost:8080",
                "Duration: 15 seconds",
                "Users: 10 concurrent",
                "Protocol: HTTP"
            ])
            enhanced_progress_bar_3d("Initializing Enhanced Test Environment", 2)
            
        elif choice == 2:
            # Advanced test option
            draw_enhanced_3d_box("ADVANCED TEST CONFIGURATION", [
                "Custom parameters required",
                "Enter target IP/hostname",
                "Specify port and protocol",
                "Set duration and user count"
            ], gradient=Colors3D.ORANGE_GRADIENT)
            
        elif choice == 3:
            # Performance analytics
            draw_enhanced_3d_box("PERFORMANCE ANALYTICS", [
                "Real-time metrics dashboard",
                "Request/response statistics",
                "Network latency measurements",
                "Resource utilization graphs"
            ], gradient=Colors3D.PURPLE_GRADIENT)
            
        elif choice == 4:
            # System diagnostics
            draw_enhanced_3d_box("SYSTEM DIAGNOSTICS", [
                "CPU and memory usage",
                "Network interface status",
                "Connection pool health",
                "Hardware performance metrics"
            ])
            
        elif choice == 5:
            # IP:PORT Scanner
            draw_enhanced_3d_box("IP:PORT SCANNER", [
                "Enter target IP address",
                "Specify port range to scan",
                "Multi-threaded scanning",
                "Service detection"
            ], gradient=Colors3D.CYAN_GRADIENT)
            
            # Get target IP
            target = input(f"{Colors3D.BLUE_GRADIENT[1]}Enter target IP: {Colors3D.RESET}")
            if not target:
                target = "127.0.0.1"  # Default to localhost
            
            # Get port range
            try:
                start_port = int(input(f"{Colors3D.BLUE_GRADIENT[1]}Start port (default 1): {Colors3D.RESET}") or "1")
                end_port = int(input(f"{Colors3D.BLUE_GRADIENT[1]}End port (default 1024): {Colors3D.RESET}") or "1024")
            except ValueError:
                print(f"{Colors3D.RED_GRADIENT[1]}Invalid port number! Using defaults.{Colors3D.RESET}")
                start_port, end_port = 1, 1024
            
            # Validate port range
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print(f"{Colors3D.RED_GRADIENT[1]}Invalid port range! Using 1-1024.{Colors3D.RESET}")
                start_port, end_port = 1, 1024
            
            # Start scanning
            enhanced_progress_bar_3d("Initializing Enhanced Port Scanner", 2)
            
            # Perform the scan
            open_ports = scanner.scan_range(target, start_port, end_port)
            
            # Display results
            scanner.display_results(target, start_port, end_port)
            
            # Option to save results
            save = input(f"\n{Colors3D.BLUE_GRADIENT[1]}Save results to file? (y/n): {Colors3D.RESET}").lower()
            if save == 'y':
                filename = f"portscan_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w') as f:
                    f.write(f"Port Scan Results\n")
                    f.write(f"Target: {target}\n")
                    f.write(f"Port range: {start_port}-{end_port}\n")
                    f.write(f"Open ports: {len(open_ports)}\n")
                    f.write(f"Scan time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write("Open ports:\n")
                    for port in open_ports:
                        service = scanner.common_ports.get(port, "Unknown")
                        f.write(f"{port} - {service}\n")
                print(f"{Colors3D.GREEN_GRADIENT[1]}Results saved to {filename}{Colors3D.RESET}")
            
        elif choice == 6:
            # Enhanced Methods
            show_enhanced_methods()
            
        elif choice == 7:
            # Exit
            print(f"\n{Colors3D.ORANGE_GRADIENT[1]}Thank you for using Enhanced NetStress Pro!{Colors3D.RESET}")
            break
            
        else:
            print(f"{Colors3D.RED_GRADIENT[1]}Invalid choice. Please try again.{Colors3D.RESET}")
        
        input(f"\n{Colors3D.BLUE_GRADIENT[1]}Press Enter to continue...{Colors3D.RESET}")
        os.system("cls" if os.name == "nt" else "clear")
        print_enhanced_banner()

if __name__ == "__main__":
    main_enhanced()
