# Kỹ thuật giấu tin
## Lab1: Giấu tin trong trường Sequence Number của gói tin TCP
#### 1. Mục tiêu
- Hiểu cách giấu thông tin trong `header` TCP mà không làm thay đổi `payload`

- Thực hành sử dụng trường `Sequence Number (32-bit)` để mã hóa dữ liệu

- Phân tích lưu lượng mạng bằng `Wireshark/Tcpdump`

#### 2. Nguyên lý hoạt động
- Trường `Sequence Number`:

    - Thường dùng để chống phân mảnh gói tin

    - Có thể tái sử dụng 32-bit này để chứa dữ liệu mã hóa

    - Mỗi 4 ký tự ASCII → 1 giá trị Sequence Number (ví dụ: "ABCD" → 0x41424344)

- Kỹ thuật giấu tin:

```
# Mã hóa từ chuỗi sang số nguyên 32-bit
seq_num = int.from_bytes("HELL".encode(), 'big')  # → 1214606444
# Gán vào gói tin
pkt = IP()/TCP(seq=seq_num, flags="S")
```

#### 3. Ứng dụng thực tế
- Truyền tin mật trong hệ thống giám sát

- CTF (Capture The Flag) an ninh mạng

- Nghiên cứu phát hiện tấn công giấu tin

#### 4. Hướng dẫn thực hành 
##### a. Tải bài lab:
- Dùng lệnh sau để tải bài lab:

```
imodule https://raw.githubusercontent.com/Giangattt123/KTGT-Lab/refs/heads/main/lab.tar
```

- Pull docker image: `labtainer -r steg-sequence-number`

![image]()

##### b. Chuẩn bị
- Môi trường: 2 container (sender/receiver) trong Labtainer

- Công cụ:

    - Scapy (tạo/gửi gói tin)

    - Wireshark (phân tích pcap)

    - tcpdump (bắt gói tin)

##### c. Các bước thực hiện
- Bước 1: Trên container `receiver`:

    - Download `wireshark` để bắt gói tin gửi đến giao diện mạng với câu lệnh: `sudo apt install wireshark -y` 
    - Chạy `wireshark` với câu lệnh: `sudo wireshark`

- Bước 2: Trên container `sender`:

    - Mã hóa thông điệp (trên `sender`): `python3 encode.py "secretat"`
    - Gửi gói `SYN` chứa dữ liệu + gói nhiễu: `sudo python3 sender.py`

- Bước 3: Trên container `receiver`: 

    - Trên `wireshark` bắt và lọc gói tin với bộ lọc: `tcp.flags.syn == 1 and tcp.flags.ack == 0 and tcp.dstport == 80 and ip.ttl == 64 and tcp.srcport == 12345`
    - Sau khi bên `sender` gửi gói tin xong stop và lưu lại các gói tin vào file `result.pcap`:

        - File → Export Specified Packets → chọn Displayed packets only
        - Save file `result.pcap`

- Bước 4: Giải mã:
    - Ở container `sender` tiến hành giải mã dựa trên các gói tin bắt được bằng câu lệnh: `sudo python3 receiver.py result.pcap`
    - Kết quả đầu ra: 
        - `decode_msg.txt`: Nội dung giải mã
        - `number_packet.txt`: Số gói tin dùng
        - Đọc nội dung của hai file bằng câu lệnh cat sẽ thấy chính xác `message` giải mã là `secretat`: `cat decode_msg.txt`, `cat number_packet.txt `

- Bước 5: `Checkwork` và `stoplab`
    - Hoàn thành đủ 4 checkwork và dừng bài lab

    ![image-1]()