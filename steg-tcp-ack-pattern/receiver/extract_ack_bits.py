from scapy.all import rdpcap, TCP

def extract_bits(pcap_file):
    packets = rdpcap(pcap_file)
    bits = []
    for pkt in packets:
        if TCP in pkt:
            flags = pkt[TCP].flags
            bits.append(1 if flags & 0x10 else 0)  # Kiểm tra ACK flag
    return bits

# Trích xuất các bit từ pcap
bits = extract_bits("capture.pcap")

# Lưu các bit vào tệp bits.txt
with open("bits.txt", "w") as f:
    f.write("".join(map(str, bits)))

print(f"[+] Extracted {len(bits)} bits to bits.txt")
