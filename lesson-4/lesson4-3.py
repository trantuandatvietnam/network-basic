import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"
# lấy thông tin trả ra từ API
result = requests.get(URL)
# Hiển thị status code và giá trị của nó
print(f"{result.status_code}: " + result.reason)
if(result.status_code == 200):
    print(result.text)