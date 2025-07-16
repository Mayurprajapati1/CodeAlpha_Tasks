from scapy.all import sniff

# Function to process each captured packet
def process_packet(packet):
    print("=" * 60)
    print(f"Packet Summary: {packet.summary()}")
    print("-" * 60)
    print("Packet Details:")
    print(packet.show(dump=True))  # dump=True returns a string instead of printing
    print("=" * 60 + "\n")

# Start packet sniffing
print("🔍 Starting packet capture... (Capturing 10 packets)")
sniff(count=10, prn=process_packet)
