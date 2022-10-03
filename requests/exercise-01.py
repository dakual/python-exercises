from urllib.parse import urlencode
from urllib.request import Request, urlopen

url  = 'http://localhost:8080/server.php'
post = {'foo': 'bar'}

request  = Request(url, urlencode(post).encode())
response = urlopen(request).read().decode()
print(response)

