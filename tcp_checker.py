import socket

ip = input("Enter IP: ")
port = int(input("Enter Port: "))

try:
    socket.create_connection((ip, port), timeout=5)
    print("Connection successful")
except:
    print("Connection failed")
