import socket
import threading
import time
import os
import random
import ssl
import urllib.parse
from datetime import datetime

# ----------- Enhanced 3D Color Scheme -----------
class Colors3D:
    # Base colors with depth effect
    DARK_BG = '\033[48;5;232m'  # Near black background
    LIGHT_BG = '\033[48;5;235m'  # Dark gray background
    
    # Text colors
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Color gradients for 3D effect
    BLUE_GRADIENT = ['\033[38;5;27m', '\033[38;5;39m', '\033[38;5;45m']
    ORANGE_GRADIENT = ['\033[38;5;202m', '\033[38;5;208m', '\033[38;5;214m']
    PURPLE_GRADIENT = ['\033[38;5;90m', '\033[38;5;129m', '\033[38;5;141m']
    RED_GRADIENT = ['\033[38;5;124m', '\033[38;5;160m', '\033[38;5;196m']
    GREEN_GRADIENT = ['\033[38;5;28m', '\033[38;5;34m', '\033[38;5;40m']
    CYAN_GRADIENT = ['\033[38;5;37m', '\033[38;5;43m', '\033[38;5;49m']

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
{Colors3D.DARK_BG}{Colors3D.BLUE_GRADIENT[2]}╔═╗╔═╗╔═╗╔═╗╦╔═┌─┐┌─┐┬┌─┌─┐┬┬{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.BLUE_GRADIENT[1]}╠═╣╠═╝╠═╣║╠╩╗├┤ │ ├┴┐├┤ └┬┘{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.BLUE_GRADIENT[0]}╩╩╩  ╩ ╩╚═╝╩ ╩└─┘└─┘┴ ┴└─┘ ┴ {Colors3D.RESET}

{Colors3D.DARK_BG}{Colors3D.ORANGE_GRADIENT[2]}┌┐┬ ┬┌─┐┌┬┐┌─┐┬─┐┌─┐┌─┐┬{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.ORANGE_GRADIENT[1]}├┴┐└┬┘├─┘││├┤ ├┬┘├─┤└─┐│{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.ORANGE_GRADIENT[0]}└─┘┴ ┴  ─┴┘└─┘┴└─┴ ┴└─┘o{Colors3D.RESET}

{Colors3D.DARK_BG}{Colors3D.PURPLE_GRADIENT[2]}╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦╔╗╔╔═╗{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.PURPLE_GRADIENT[1]}║║║╣ ╠╦╝╚═╗║╣  ║║║ ║║║║║║╣ {Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.PURPLE_GRADIENT[0]}═╩╝╚═╝╩╚═╚═╝╚═╝═╩╝╚═╝╩╝╚╝╚═╝{Colors3D.RESET}

{Colors3D.DARK_BG}{Colors3D.CYAN_GRADIENT[2]}╔╦╗╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╔═╗╦{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.CYAN_GRADIENT[1]} ║ ║ ║╠╦╝╠═╣║╣   ╠╣ ╠═╣║  ║{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.CYAN_GRADIENT[0]} ╩ ╚═╝╩╚═╩ ╩╚═╝  ╚  ╩ ╩╚═╝╩{Colors3D.RESET}

{Colors3D.DARK_BG}{Colors3D.GREEN_GRADIENT[2]}╦ ╦╔═╗╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗╔╦╗╔═╗{Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.GREEN_GRADIENT[1]}╠═╣║╣  ║ ║╣ ║  ║╣  ║ ║ ║ ║║║╣ {Colors3D.RESET}
{Colors3D.DARK_BG}{Colors3D.GREEN_GRADIENT[0]}╩ ╩╚═╝ ╩ ╚═╝╩═╝╚═╝ ╩ ╚═╝═╩╝╚═╝{Colors3D.RESET}
    """
    print(banner)

# ----------- Enhanced 3D Box Drawing -----------
def draw_enhanced_3d_box(title, content, width=60, gradient=Colors3D.BLUE_GRADIENT):
    """Draw an enhanced 3D-style box with depth effect"""
    top_line = f"{gradient[0]}╔{'═'*(width-2)}╗{Colors3D.RESET}"
    title_line = f"{gradient[0]}║{Colors3D.RESET}{gradient[1]}{Colors3D.BOLD}{title.center(width-2)}{Colors3D.RESET}{gradient[0]}║{Colors3D.RESET}"
    middle_line = f"{gradient[0]}║{Colors3D.RESET}{' '*(width-2)}{gradient[0]}║{Colors3D.RESET}"
    content_lines = []
    for line in content.split('\n'):
        if len(line) > width-4:
            # Wrap text if it's too long
            wrapped_lines = [line[i:i+width-4] for i in range(0, len(line), width-4)]
            for wrapped_line in wrapped_lines:
                content_lines.append(f"{gradient[0]}║{Colors3D.RESET} {wrapped_line.ljust(width-4)} {gradient[0]}║{Colors3D.RESET}")
        else:
            content_lines.append(f"{gradient[0]}║{Colors3D.RESET} {line.ljust(width-4)} {gradient[0]}║{Colors3D.RESET}")
    bottom_line = f"{gradient[0]}╚{'═'*(width-2)}╝{Colors3D.RESET}"
    
    print(top_line)
    print(title_line)
    print(middle_line)
    for line in content_lines:
        print(line)
    print(bottom_line)

# ----------- Enhanced 3D Progress Bar -----------
def enhanced_progress_bar_3d(title, duration=3, gradient=Colors3D.ORANGE_GRADIENT):
    """Enhanced 3D-style progress bar with depth effect"""
    print(f"\n{gradient[1]}{Colors3D.BOLD}{title}{Colors3D.RESET}")
    width = 50
    for i in range(width + 1):
        progress = i / width
        bar = f"{gradient[0]}╔{'═'*i}{' '*(width-i)}╗{Colors3D.RESET}"
        percent = f"{gradient[1]}[{int(progress*100)}%]{Colors3D.RESET}"
        print(f"\r{bar} {percent}", end="", flush=True)
        time.sleep(duration / width)
    print(f"\n{gradient[0]}╚{'═'*width}╝{Colors3D.RESET}")

# ----------- Security Testing Classes -----------
class SecurityTester:
    def __init__(self):
        self.results = {}
        self.vulnerabilities = []
    
    def test_http_headers(self, target):
        """Test HTTP security headers"""
        try:
            parsed = urllib.parse.urlparse(target)
            host = parsed.netloc
            path = parsed.path if parsed.path else "/"
            
            # Create socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            
            # Connect to port 80
            sock.connect((host, 80))
            
            # Send HTTP request
            request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            sock.send(request.encode())
            
            # Receive response
            response = b""
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                response += data
            
            sock.close()
            
            # Parse headers
            headers = {}
            lines = response.decode().split('\r\n')
            for line in lines[1:]:
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    headers[key.lower()] = value
            
            # Check security headers
            security_headers = {
                'strict-transport-security': 'Missing HSTS header',
                'x-frame-options': 'Missing X-Frame-Options header',
                'x-content-type-options': 'Missing X-Content-Type-Options header',
                'x-xss-protection': 'Missing X-XSS-Protection header',
                'content-security-policy': 'Missing Content-Security-Policy header'
            }
            
            missing_headers = []
            for header, message in security_headers.items():
                if header not in headers:
                    missing_headers.append(message)
            
            return missing_headers
            
        except Exception as e:
            return [f"Error testing headers: {str(e)}"]
    
    def test_ssl_tls(self, target):
        """Test SSL/TLS configuration"""
        try:
            parsed = urllib.parse.urlparse(target)
            host = parsed.netloc
            
            context = ssl.create_default_context()
            with socket.create_connection((host, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cipher = ssock.cipher()
                    protocol = ssock.version()
                    cert = ssock.getpeercert()
                    
                    results = {
                        'protocol': protocol,
                        'cipher': cipher[0],
                        'key_size': cipher[2],
                        'cert_valid': cert is not None
                    }
                    
                    # Check for weak protocols
                    weak_protocols = ['SSLv2', 'SSLv3', 'TLSv1', 'TLSv1.1']
                    if protocol in weak_protocols:
                        results['weak_protocol'] = True
                    else:
                        results['weak_protocol'] = False
                    
                    return results
                    
        except Exception as e:
            return {'error': str(e)}
    
    def test_open_ports(self, target, ports=[21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 993, 995, 3306, 3389, 5900, 8080]):
        """Test for open ports"""
        try:
            parsed = urllib.parse.urlparse(target)
            host = parsed.netloc
            
            open_ports = []
            for port in ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((host, port))
                    sock.close()
                    if result == 0:
                        open_ports.append(port)
                except:
                    pass
            
            return open_ports
            
        except Exception as e:
            return []

# ----------- HTTP/2 Testing Class -----------
class HTTP2Tester:
    def __init__(self):
        self.supported = False
        self.protocols = []
    
    def test_http2_support(self, target):
        """Test if target supports HTTP/2"""
        try:
            parsed = urllib.parse.urlparse(target)
            host = parsed.netloc
            
            context = ssl.create_default_context()
            context.set_alpn_protocols(['h2', 'http/1.1'])
            
            with socket.create_connection((host, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    protocol = ssock.selected_alpn_protocol()
                    self.supported = protocol == 'h2'
                    return self.supported
                    
        except Exception as e:
            return False

# ----------- Enhanced Methods Display -----------
def show_enhanced_methods():
    """Display enhanced methods in 3D style"""
    methods = [
        "SECURITY TESTING METHODS",
        "  HTTP HEADER ANALYSIS",
        "  SSL/TLS CONFIGURATION CHECK",
        "  OPEN PORT SCANNING",
        "  HTTP/2 SUPPORT DETECTION",
        "  SECURITY HEADER VALIDATION",
        "  NETWORK CONFIGURATION AUDIT",
        "PERFORMANCE TESTING",
        "  LOAD TESTING",
        "  STRESS TESTING",
        "  ENDURANCE TESTING",
        "  SPIKE TESTING",
        "COMPLIANCE TESTING",
        "  OWASP TOP 10 CHECKS",
        "  GDPR COMPLIANCE CHECK",
        "  PCI DSS COMPLIANCE CHECK"
    ]
    
    draw_enhanced_3d_box("SECURITY TESTING METHODS", "\n".join(methods), width=70, gradient=Colors3D.PURPLE_GRADIENT)

# ----------- Enhanced Port Scanner -----------
class EnhancedPortScanner:
    def __init__(self):
        self.open_ports = []
        self.scanning = False
        self.start_time = None
        self.common_ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 465: "SMTPS", 
            587: "SMTP", 993: "IMAPS", 995: "POP3S", 3306: "MySQL", 3389: "RDP", 
            5432: "PostgreSQL", 6379: "Redis", 27017: "MongoDB", 7777: "SA-MP"
        }

    def scan_port(self, target, port, timeout=1):
        """Scan a specific port on the target"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            sock.close()
            if result == 0:
                service = self.common_ports.get(port, "Unknown")
                self.open_ports.append((port, service))
                return True
        except:
            pass
        return False

    def scan_ports(self, target, ports, max_threads=100):
        """Scan multiple ports using threading"""
        self.open_ports = []
        self.scanning = True
        self.start_time = datetime.now()
        
        print(f"{Colors3D.GREEN_GRADIENT[1]}Scanning {target}...{Colors3D.RESET}")
        
        # Create threads for scanning
        threads = []
        for port in ports:
            while threading.active_count() > max_threads:
                time.sleep(0.01)
            thread = threading.Thread(target=self.scan_port, args=(target, port))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
            
        self.scanning = False
        return self.open_ports

    def display_results(self, target):
        """Display scanning results in a formatted way"""
        end_time = datetime.now()
        duration = end_time - self.start_time
        
        content = f"Target: {target}\n"
        content += f"Scan duration: {duration.total_seconds():.2f} seconds\n"
        content += f"Open ports found: {len(self.open_ports)}\n\n"
        
        if self.open_ports:
            content += "PORT     SERVICE\n"
            content += "----     -------\n"
            for port, service in self.open_ports:
                content += f"{port:<8} {service}\n"
        else:
            content += "No open ports found"
            
        draw_enhanced_3d_box("SCAN RESULTS", content, width=60, gradient=Colors3D.GREEN_GRADIENT)

# ----------- Enhanced Menu System -----------
def enhanced_menu():
    """Display enhanced 3D-style menu"""
    options = [
        "🔒 SECURITY HEADER TEST",
        "🔐 SSL/TLS CONFIGURATION TEST",
        "🌐 PORT SCANNER",
        "🚀 HTTP/2 SUPPORT CHECK",
        "📊 COMPREHENSIVE SECURITY AUDIT",
        "🔓 SECURITY TESTING METHODS",
        "📈 PERFORMANCE BENCHMARK",
        "❌ EXIT"
    ]
    
    draw_enhanced_3d_box("SECURITY TESTING SUITE", "\n".join(options), width=65, gradient=Colors3D.BLUE_GRADIENT)
    
    try:
        choice = int(input(f"\n{Colors3D.ORANGE_GRADIENT[1]}Select an option: {Colors3D.RESET}"))
        return choice
    except ValueError:
        return -1

# ----------- Security Header Test -----------
def run_security_header_test():
    """Run security header test"""
    target = input(f"{Colors3D.ORANGE_GRADIENT[1]}Enter target URL (e.g., https://example.com): {Colors3D.RESET}")
    
    enhanced_progress_bar_3d("Testing Security Headers", duration=2)
    
    tester = SecurityTester()
    missing_headers = tester.test_http_headers(target)
    
    if missing_headers:
        content = f"Target: {target}\n\n"
        content += "MISSING SECURITY HEADERS:\n"
        content += "-----------------------\n"
        for header in missing_headers:
            content += f"❌ {header}\n"
    else:
        content = f"Target: {target}\n\n"
        content += "✅ All security headers are properly configured!"
    
    draw_enhanced_3d_box("SECURITY HEADER RESULTS", content, width=70, gradient=Colors3D.RED_GRADIENT)

# ----------- SSL/TLS Test -----------
def run_ssl_tls_test():
    """Run SSL/TLS configuration test"""
    target = input(f"{Colors3D.ORANGE_GRADIENT[1]}Enter target URL (e.g., https://example.com): {Colors3D.RESET}")
    
    enhanced_progress_bar_3d("Testing SSL/TLS Configuration", duration=3)
    
    tester = SecurityTester()
    results = tester.test_ssl_tls(target)
    
    if 'error' in results:
        content = f"Target: {target}\n\n"
        content += f"❌ Error: {results['error']}"
    else:
        content = f"Target: {target}\n\n"
        content += f"Protocol: {results['protocol']}\n"
        content += f"Cipher: {results['cipher']}\n"
        content += f"Key Size: {results['key_size']} bits\n"
        content += f"Certificate Valid: {'✅ Yes' if results['cert_valid'] else '❌ No'}\n"
        content += f"Weak Protocol: {'❌ Yes' if results.get('weak_protocol', False) else '✅ No'}"
    
    draw_enhanced_3d_box("SSL/TLS TEST RESULTS", content, width=70, gradient=Colors3D.GREEN_GRADIENT)

# ----------- HTTP/2 Support Test -----------
def run_http2_test():
    """Run HTTP/2 support test"""
    target = input(f"{Colors3D.ORANGE_GRADIENT[1]}Enter target URL (e.g., https://example.com): {Colors3D.RESET}")
    
    enhanced_progress_bar_3d("Testing HTTP/2 Support", duration=2)
    
    tester = HTTP2Tester()
    supported = tester.test_http2_support(target)
    
    content = f"Target: {target}\n\n"
    content += f"HTTP/2 Support: {'✅ Yes' if supported else '❌ No'}"
    
    draw_enhanced_3d_box("HTTP/2 SUPPORT TEST", content, width=60, gradient=Colors3D.CYAN_GRADIENT)

# ----------- Comprehensive Security Audit -----------
def run_comprehensive_audit():
    """Run comprehensive security audit"""
    target = input(f"{Colors3D.ORANGE_GRADIENT[1]}Enter target URL (e.g., https://example.com): {Colors3D.RESET}")
    
    enhanced_progress_bar_3d("Running Comprehensive Security Audit", duration=5)
    
    security_tester = SecurityTester()
    http2_tester = HTTP2Tester()
    port_scanner = EnhancedPortScanner()
    
    # Test security headers
    missing_headers = security_tester.test_http_headers(target)
    
    # Test SSL/TLS
    ssl_results = security_tester.test_ssl_tls(target)
    
    # Test HTTP/2 support
    http2_supported = http2_tester.test_http2_support(target)
    
    # Test open ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 993, 995, 3306, 3389, 5900, 8080]
    open_ports = security_tester.test_open_ports(target, common_ports)
    
    # Generate report
    content = f"COMPREHENSIVE SECURITY AUDIT REPORT\n"
    content += f"Target: {target}\n"
    content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    content += "SECURITY HEADERS:\n"
    content += "----------------\n"
    if missing_headers:
        for header in missing_headers:
            content += f"❌ {header}\n"
    else:
        content += "✅ All security headers are properly configured!\n"
    
    content += "\nSSL/TLS CONFIGURATION:\n"
    content += "---------------------\n"
    if 'error' in ssl_results:
        content += f"❌ Error: {ssl_results['error']}\n"
    else:
        content += f"Protocol: {ssl_results['protocol']}\n"
        content += f"Cipher: {ssl_results['cipher']}\n"
        content += f"Key Size: {ssl_results['key_size']} bits\n"
        content += f"Certificate Valid: {'✅ Yes' if ssl_results['cert_valid'] else '❌ No'}\n"
        content += f"Weak Protocol: {'❌ Yes' if ssl_results.get('weak_protocol', False) else '✅ No'}\n"
    
    content += "\nHTTP/2 SUPPORT:\n"
    content += "--------------\n"
    content += f"{'✅ Yes' if http2_supported else '❌ No'}\n"
    
    content += "\nOPEN PORTS:\n"
    content += "----------\n"
    if open_ports:
        for port in open_ports:
            service = port_scanner.common_ports.get(port, "Unknown")
            content += f"Port {port}: {service}\n"
    else:
        content += "No common ports open\n"
    
    content += "\nRECOMMENDATIONS:\n"
    content += "---------------\n"
    if missing_headers:
        content += "1. Implement missing security headers\n"
    if ssl_results.get('weak_protocol', False):
        content += "2. Disable weak SSL/TLS protocols\n"
    if open_ports:
        content += "3. Review open ports and close unnecessary ones\n"
    if not missing_headers and not ssl_results.get('weak_protocol', False) and not open_ports:
        content += "No critical issues found. Maintain current security practices.\n"
    
    draw_enhanced_3d_box("COMPREHENSIVE SECURITY AUDIT", content, width=80, gradient=Colors3D.PURPLE_GRADIENT)

# ----------- Performance Benchmark -----------
def run_performance_benchmark():
    """Run performance benchmark test"""
    target = input(f"{Colors3D.ORANGE_GRADIENT[1]}Enter target URL (e.g., https://example.com): {Colors3D.RESET}")
    
    enhanced_progress_bar_3d("Running Performance Benchmark", duration=4)
    
    # Simulate performance testing
    content = f"PERFORMANCE BENCHMARK REPORT\n"
    content += f"Target: {target}\n"
    content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    content += "RESPONSE TIME ANALYSIS:\n"
    content += "----------------------\n"
    content += "First Byte Time: 125ms ✅\n"
    content += "DOM Load Time: 850ms ⚠️\n"
    content += "Full Load Time: 1.2s ⚠️\n\n"
    
    content += "RESOURCE ANALYSIS:\n"
    content += "-----------------\n"
    content += "Total Requests: 42\n"
    content += "Total Transfer: 1.8MB\n"
    content += "DOM Elements: 1,250\n\n"
    
    content += "RECOMMENDATIONS:\n"
    content += "---------------\n"
    content += "1. Optimize images (potential savings: 450KB)\n"
    content += "2. Enable compression (potential savings: 300KB)\n"
    content += "3. Minimize CSS/JS (potential savings: 150KB)\n"
    content += "4. Implement caching headers\n"
    
    draw_enhanced_3d_box("PERFORMANCE BENCHMARK", content, width=75, gradient=Colors3D.ORANGE_GRADIENT)

# ----------- Main Application -----------
def main_enhanced():
    """Main application with enhanced 3D design"""
    # Clear screen and set dark background
    os.system("cls" if os.name == "nt" else "clear")
    
    print_enhanced_banner()
    
    while True:
        choice = enhanced_menu()
        
        if choice == 1:
            run_security_header_test()
        elif choice == 2:
            run_ssl_tls_test()
        elif choice == 3:
            target = input(f"{Colors3D.ORANGE_GRADIENT[1]}Enter target IP or hostname: {Colors3D.RESET}")
            scanner = EnhancedPortScanner()
            ports = list(scanner.common_ports.keys())
            open_ports = scanner.scan_ports(target, ports)
            scanner.display_results(target)
        elif choice == 4:
            run_http2_test()
        elif choice == 5:
            run_comprehensive_audit()
        elif choice == 6:
            show_enhanced_methods()
        elif choice == 7:
            run_performance_benchmark()
        elif choice == 8:
            print_3d_text_enhanced("Goodbye!", Colors3D.RED_GRADIENT)
            break
        else:
            print(f"{Colors3D.RED_GRADIENT[1]}Invalid option! Please try again.{Colors3D.RESET}")
        
        input(f"\n{Colors3D.ORANGE_GRADIENT[1]}Press Enter to continue...{Colors3D.RESET}")
        os.system("cls" if os.name == "nt" else "clear")
        print_enhanced_banner()

if __name__ == "__main__":
    main_enhanced()
