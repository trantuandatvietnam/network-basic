
import socket            
 
s = socket.socket()
# Định nghĩa PORT cho server
port = 12345               
# Server có phương thức bind() liên kết nó với một IP và cổng cụ thể để có thể lắng nghe các yêu cầu đến trên IP và cổng đó
s.bind(('', port))
# Server có phương thức listen() đặt máy chủ ở chế độ listening. Điều này cho phép máy chủ lắng nghe các kết nối đến
# Số 5 ở đây có nghĩa là có 5 kết nối được `kept waiting` nếu server bận và nếu soket thứ 6 cố gắng kết nối thì sẽ bị từ chối
s.listen(5)           
print ("socket is listening")
while True:
  # Server có phương thức accept() để khởi tạo kết nối với client và close() để đóng kết nối với client.
  c, addr = s.accept()
  print ('Got connection from', addr )
  # Thực hiện encode khi gửi
  c.send("Thank you for connecting".encode())
  c.close()
  break