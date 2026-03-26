import socket
def check_dns(domain: str) -> None:
    try:
        ip = socket.gethostbyname(domain)
        print(f"[SUCCESS] {domain} resolved to {ip}")
    except socket.gaierror:
        print(f"[ERROR] DNS resolution failed for {domain}")
if __name__ == "__main__":
    domain = input("Enter domain: ").strip()
    if domain:
        check_dns(domain)
    else:
        print("[ERROR] Domain cannot be empty")
