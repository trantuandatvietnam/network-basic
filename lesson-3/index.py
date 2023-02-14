# modules
import socket
# Thực hiện lấy các thông tin từ domain name
try:
    domain_name = "www.actvn.edu.vn"
    print("Hostname: ", socket.gethostname())
    print("Hostname by name: ", socket.gethostbyname(domain_name))
    print("Hostname by name ex: ", socket.gethostbyname_ex(domain_name))
    print("Hostname by addr: ", socket.gethostbyaddr("103.21.148.154"))
    print("FQDN: ", socket.getfqdn(domain_name))
    print("Addr info: ", socket.getaddrinfo(domain_name, None, 0, socket.SOCK_STREAM))
except socket.error as err:
    print(str(err))