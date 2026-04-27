mac_table = {}

def learn_mac(mac, port):
    mac_table[mac] = port

def forward_frame(src_mac, dst_mac, in_port):
    learn_mac(src_mac, in_port)
    
    if dst_mac in mac_table:
        out_port = mac_table[dst_mac]
        print(f"Unicast: Forwarding to port {out_port}")
    else:
        print("Broadcast: Sending to all ports")

# Simulation
forward_frame("AA:BB:CC:DD:01", "AA:BB:CC:DD:02", 1)
forward_frame("AA:BB:CC:DD:02", "AA:BB:CC:DD:01", 2)
