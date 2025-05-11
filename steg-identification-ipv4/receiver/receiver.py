#!/usr/bin/env python3

ids = list(map(int, open("decode.txt").read().split()))

decoded_message = "".join([chr((ids[i]<<8) | ids[i+1]) for i in range(0, len(ids), 2)])

# Save result file decoded_msg.txt
with open("decoded_msg.txt", "w") as f:
    f.write(decoded_message)

print(f"Decoded message has been saved to decoded_msg.txt")
