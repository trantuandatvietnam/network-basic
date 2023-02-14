import socket
import sys

# Tạo instance socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
# Lấy địa chỉ ip từ domain name
try:
    host_ip = socket.gethostbyname('dantri.com.vn')
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()

print("host_ip: " + host_ip)
portList = [21, 22, 23, 80, 443]
# Kiểm tra các PORT đang mở, nếu result trả kết quả là 0 thì PORT đang được mở. Các trường hợp còn lại thể hiện PORT đang đóng
for port in portList:
    result = s.connect_ex((host_ip, port))
    if result == 0:
        print(f"PORT {port} is open")
    else:
        print(f"PORT {port} is not open")
s.close()