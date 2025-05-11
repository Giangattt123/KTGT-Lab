# decode_from_timestamps.py
times = []
with open("timestamps.txt") as f:
    for line in f:
        times.append(float(line.strip()))

bits = ''
for i in range(1, len(times)):
    delta = times[i] - times[i-1]
    bits += '0' if delta < 0.3 else '1'

chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
with open("decoded.txt", "w") as f:
    f.write("".join(chars))
print("[+] Decoded message:", "".join(chars))

