import requests

url    = 'http://localhost:8080/server.php'
myFile = {'file': open('upload.txt' ,'rb')}

x = requests.post(url, files=myFile)

print(x.text)