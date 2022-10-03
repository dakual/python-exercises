import requests

url = "http://localhost:8080/server.php"
xml = """<?xml version = "1.0" encoding = "UTF-8"?>
<Order>
  <Id>78912</Id>
  <Customer>Jason Sweet</Customer>
</Order>
"""

headers = {"Content-Type": "application/xml"}

r = requests.post(url, data=xml, headers=headers)

print(r.text)