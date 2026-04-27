import random

ip_pool = [f"192.168.1.{i}" for i in range(2, 50)]
leased_ips = {}

def discover(client_id):
    print(f"{client_id} -> DHCP Discover")

def offer(client_id):
    ip = random.choice(ip_pool)
    print(f"DHCP -> Offer {ip} to {client_id}")
    return ip

def request(client_id, ip):
    print(f"{client_id} -> Request {ip}")

def ack(client_id, ip):
    leased_ips[client_id] = ip
    print(f"DHCP -> ACK {ip} assigned to {client_id}")

def simulate_client(client_id):
    discover(client_id)
    ip = offer(client_id)
    request(client_id, ip)
    ack(client_id, ip)

if __name__ == "__main__":
    simulate_client("Client1")
    simulate_client("Client2")
