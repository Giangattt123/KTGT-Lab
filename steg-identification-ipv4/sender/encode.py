#!/usr/bin/env python3
import sys

def text_to_ids(message):
    """Chuyển thông điệp thành các ID IPv4 (16-bit)"""
    ids = []
    for char in message:
        # Mỗi ký tự ASCII → 2 ID (8-bit/ID)
        high_byte = (ord(char) >> 8) & 0xFF
        low_byte = ord(char) & 0xFF
        ids.extend([high_byte, low_byte])
    return ids

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./encode.py <message>")
        sys.exit(1)
    
    ids = text_to_ids(sys.argv[1])
    with open("ip_ids.txt", "w") as f:
        f.write("\n".join(map(str, ids)))
    print(f"Encoded {len(ids)} IP IDs to ip_ids.txt")
