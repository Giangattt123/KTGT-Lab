#!/usr/bin/env python3
from scapy.all import *
import sys

KEY = 0x42  # Khóa XOR phải giống encode.py

def decode_pcap(pcap_file):
    packets = rdpcap(pcap_file)
    message = b""
    packet_count = 0  # Chỉ đếm số lượng packet
    
    for pkt in packets:
        if (TCP in pkt and 
            pkt[TCP].flags == 0x02 and  # SYN
            pkt[TCP].dport == 80 and    # Cổng 80
            pkt[IP].ttl == 64):         # Chỉ lấy gói data (TTL=64)
            
            raw = pkt[TCP].seq.to_bytes(4, 'big')
            print(f"[+] Found data packet with seq: {raw.hex()}")
            message += raw
            packet_count += 1
    
    if not message:
        error_msg = "No valid packets found. Check:\n- SYN packets\n- Port 80\n- TTL=64"
        print(f"[-] {error_msg}")
        return None, 0
    
    # Giải mã XOR
    decrypted = bytes([b ^ KEY for b in message])
    decrypted = decrypted.rstrip(b'\x00')
    
    try:
        return decrypted.decode('ascii'), packet_count
    except UnicodeDecodeError:
        return f"[ERROR] Invalid decryption. Raw: {decrypted.hex()}", packet_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./receiver.py <pcap_file>")
        sys.exit(1)
    
    # Xử lý và ghi kết quả
    msg, count = decode_pcap(sys.argv[1])
    
    # Ghi message đã giải mã
    with open("decode_msg.txt", "w") as f_msg:
        if msg and not msg.startswith("[ERROR]"):
            f_msg.write(msg)
            print(f"[+] Successfully decoded message: {msg}")
        else:
            f_msg.write(msg if msg else "Decode failed")
            print(f"[-] {msg if msg else 'Decode failed'}")
    
    # Ghi số packet
    with open("number_packet.txt", "w") as f_count:
        f_count.write(str(count))
        print(f"[i] Data packets used: {count}")
