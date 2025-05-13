import base64

def bits_to_bytes(bits):
    return bytes([int(bits[i:i+8], 2) for i in range(0, len(bits), 8)])

def xor_decode(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Đọc các bit từ file bits.txt
with open("bits.txt") as f:
    bit_str = f.read().strip()

# Chuyển đổi bit thành byte
data = bits_to_bytes(bit_str)

# Đọc khóa từ file
key = open("key.txt", "rb").read().strip()

# Giải mã XOR
xor_decoded = xor_decode(data, key)

# Giải mã Base64
message = base64.b64decode(xor_decoded).decode()

print(f"[+] Decoded message: {message}")

