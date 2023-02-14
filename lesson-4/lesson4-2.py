import requests

# defined url
URL = "https://www.python.org/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

def chrome_user_agent():
    reponse = requests.get(URL)
    reponse.headers.update({'User-agent': USER_AGENT})
    headers = reponse.headers
    for header in headers:
        print(header + ":" + headers[header])
    print("----------------")
    
chrome_user_agent()