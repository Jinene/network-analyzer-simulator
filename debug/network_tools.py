import socket
import os

def ping(host):
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print("Host is up")
    else:
        print("Host is down")

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    result = sock.connect_ex((host, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    sock.close()

if __name__ == "__main__":
    ping("8.8.8.8")
    check_port("127.0.0.1", 5000)
