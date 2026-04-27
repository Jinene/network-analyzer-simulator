from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        proto = ip_layer.proto
        
        print(f"\n[Packet]")
        print(f"Source: {ip_layer.src}")
        print(f"Destination: {ip_layer.dst}")
        
        if proto == 6:
            print("Protocol: TCP")
        elif proto == 17:
            print("Protocol: UDP")
        else:
            print("Protocol: Other")

def start_sniffer():
    print("Starting packet sniffer...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffer()
