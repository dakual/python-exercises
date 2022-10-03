import requests
from requests.auth import HTTPBasicAuth

url     = "http://localhost:8080/server.php"
data    = "key1=value1&key2=value2"
data    = {"Id": 12345}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url, data=data, headers=headers, auth=HTTPBasicAuth('login', 'password'))

print(r.text)