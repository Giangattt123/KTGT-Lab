#!/usr/bin/env python3
import sys

KEY = 0x42  # Khóa XOR

def encode_message_to_sequences(message):
    message_bytes = message.encode('ascii')
    # XOR từng byte
    encrypted_bytes = bytes([b ^ KEY for b in message_bytes])
    sequences = []

    # Chia thành khối 4 byte
    for i in range(0, len(encrypted_bytes), 4):
        chunk = encrypted_bytes[i:i+4]
        while len(chunk) < 4:
            chunk += b'\x00'
        seq = int.from_bytes(chunk, 'big')
        sequences.append(seq)

    return sequences

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 encode.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    sequences = encode_message_to_sequences(message)

    with open("sequences.txt", "w") as f:
        for seq in sequences:
            f.write(str(seq) + "\n")
    print(f"[+] Encoded message to {len(sequences)} sequence numbers.")

