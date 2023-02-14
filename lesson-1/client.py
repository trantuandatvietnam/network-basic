import socket            

s = socket.socket()        
 
# Định nghĩa PORT mà client muốn kết nối tới
port = 12345               
 
# Máy tính có địa chỉ localhost là: 127.0.0.1
localhost_ip = "127.0.0.1"
# Thực hiện kết nối tới local server 
s.connect((localhost_ip, port))
 
# Nhận được dữ liệu từ server và giải mã code => Nhận được ở dạng string ban đầu
print(s.recv(1024).decode())
# close the connection
s.close()    