import socket

def check_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] {domain} resolved to {ip}")
    except:
        print("DNS resolution failed")

domain = input("Enter domain: ")
check_dns(domain)
