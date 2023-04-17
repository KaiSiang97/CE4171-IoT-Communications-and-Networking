import requests


resp = requests.post("http://192.168.43.215:8080", files={'file': open('two.jpg', 'rb')})

print(resp.text)
