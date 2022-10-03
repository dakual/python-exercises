import requests, shutil

url = "https://www.w3schools.com/images/w3lynx_200.png"

x = requests.get(url, stream=True)
with open("download.png", 'wb') as f:
  shutil.copyfileobj(x.raw, f)

print("file downloaded!")