# Bài 1:

### Bước 1: Tạo file server

```python
import socket
# next create a socket object
s = socket.socket()

# reserve a port on your computer in our (case it is 12345 but it can be anything)
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)

# a forever loop until we interrupt it or
# an error occurs
while True:
# Establish connection with client.
  c, addr = s.accept()
  print ('Got connection from', addr )

  # send a thank you message to the client. encoding to send byte type.
  c.send('Thank you for connecting'.encode())

  # Close the connection with the client
  c.close()

  # Breaking once connection closed
  break
```

=> Giải thích:

- Server - Server có phương thức bind() liên kết nó với một IP và cổng cụ thể để có thể lắng nghe các yêu cầu đến trên IP và cổng đó - Server có phương thức listen() đặt máy chủ ở chế độ listening. Điều này cho phép máy chủ listen các kết nối đến. Máy chủ cũng có phương thức accept() để khởi tạo kết nối với client và close() để đóng kết nối với client.

- Tạo socket object và để riêng một cổng trên máy tính của mình
- Sau đó liên kết server với cổng được chỉ định, việc truyền một chuỗi rỗng có nghĩa là máy chủ có thể nghe các kết nối từ những máy tính khác. Nếu chúng ta truyền `127.0.0.1` thì nó sẽ chỉ nghe được những cuộc gọi được thực hiện trong máy tính cục bộ
- Sau đó đặt máy tính ở chế độ `listening`. Số 5 ở đây có nghĩa là có 5 kết nối được `kept waiting` nếu server bận và nếu soket thứ 6 cố gắng kết nối thì sẽ bị từ chối
- Cuối cùng tạo một vòng lặp thời gian và bắt đầu chấp nhận tất cả các kết nối đến và đóng các kết nối đó sau khi thông báo cảm ơn đến tất cả các ổ cắm được kết nối.

### Bước 2: Tạo Client

```python
import socket

s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())
# close the connection
s.close()
```

- Kết nối với máy chủ cục bộ trên cổng 12345 (Port mà server đang chạy) và cuối cùng nhận dữ liệu từ máy chủ và đóng kết nối

- Kết quả:

```unbuntu
# start the server:
$ python server.py
socket is listening
Got connection from ('127.0.0.1', 52617)


# start the client:
$ python client.py
Thank you for connecting
```

# Bài 2:

```python
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

try:
    host_ip = socket.gethostbyname('dantri.com.vn')
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()

print("host_ip: " + host_ip)
portList = [21, 22, 23, 80, 443]

for port in portList:
    result = s.connect_ex((host_ip, port))
    if result == 0:
        print(f"PORT {port} is open")
    else:
        print(f"PORT {port} is not open")
s.close()
```
