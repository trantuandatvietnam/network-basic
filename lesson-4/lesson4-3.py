import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"

result = requests.get(URL)
print(f"{result.status_code}: " + result.reason)
if(result.status_code == 200):
    print(result.text)