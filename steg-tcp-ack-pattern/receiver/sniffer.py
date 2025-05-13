from scapy.all import sniff, wrpcap

print("[*] Sniffing started... Waiting for packets")

packets = sniff(filter="tcp and src host 172.30.0.3", iface="eth0", timeout=30)

wrpcap("capture.pcap", packets)
print(f"[+] Captured {len(packets)} packets and saved to capture.pcap")

