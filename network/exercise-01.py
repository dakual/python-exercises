import socket, os, platform
from urllib.request import urlopen
from requests import get
import re as regular

hostname  = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)


def getExternalIP1():
  data = urlopen("http://checkip.dyndns.com/").read()
  data = regular.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(str(data)).group(1)
  print(data)

def getExternalIP2():
  data = get("https://checkip.amazonaws.com").text.strip()
  print(data)

print(os.system("ifconfig"))
print(platform.node())
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + ipaddress)

getExternalIP1()
getExternalIP2()