import requests
from requests.auth import HTTPBasicAuth

url  = 'http://localhost:8080/server.php'
json = {'somekey': 'somevalue'}

x = requests.post(url, json=json)

print(x.text)