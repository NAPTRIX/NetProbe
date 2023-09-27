import socket
import ipaddress
import concurrent.futures
from colorama import Fore, Style, init


init(autoreset=True)

def scan_port(ip, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"{Fore.GREEN}[+] Open{Style.RESET_ALL} Port {port} on {ip}") 
        sock.close()

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        pass

def main(target_ip, start_port, end_port):
    try:

        target_ip = str(ipaddress.IPv4Address(target_ip))

        ports_to_scan = range(start_port, end_port + 1)

        print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            for port in ports_to_scan:
                executor.submit(scan_port, target_ip, port)
                print() 

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    main(target_ip, start_port, end_port)
