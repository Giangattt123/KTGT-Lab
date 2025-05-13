import base64

def base64_xor_encode(message, key):
    # Mã hóa thông điệp thành Base64
    base64_msg = base64.b64encode(message.encode())
    # XOR với khóa
    xor_encoded = bytes([b ^ key[i % len(key)] for i, b in enumerate(base64_msg)])
    return xor_encoded

if __name__ == "__main__":
    # Đọc thông điệp từ file
    with open("message.txt") as f:
        message = f.read().strip()
    # Đọc khóa từ file
    key = open("key.txt", "rb").read().strip()
    
    # Mã hóa thông điệp
    encoded = base64_xor_encode(message, key)
    
    # Lưu thông điệp đã mã hóa vào file
    with open("encoded.bin", "wb") as f:
        f.write(encoded)
    
    print("[+] Encoded and saved to encoded.bin")
