import re

# Email regex
res = re.match(r"^\S+@\S+\.\S+$", "hello@example.com") 
print(res)

res = re.findall(r"\S+@\S+\.\S+", 'You can reach me out at hello@example.com and contact@example.com')
print(res)

# Phone number regex
res = re.match("^\\+?[1-9][0-9]{7,14}$", "+12223334444")
print(res)

res = re.findall("\\+?[1-9][0-9]{7,14}", 'You can reach me out at +12223334444 and +56667778888')
print(res)

# IP address regex
ipv4_pattern = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
res = re.match(ipv4_pattern, '192.168.0.1')
print(res)

# Extract IPv4 from a string
ipv4_extract_pattern = "(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
res = re.findall(ipv4_extract_pattern, 'My server IP addresses are 192.168.0.1 and 192.168.0.2')
print(res)

# Date regex
res = re.match("^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$", '12/12/2022')
print(res)

res = re.findall("[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}", 'I\'m on vacation from 1/18/2021 till 1/29/2021')
print(res)

# URL regex
url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
res = re.match(url_pattern, 'https://github.com')
print(res)

url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
res = re.findall(url_extract_pattern, 'You can view more details at https://github.com or just ping via email.')
print(res)

# HTML regex
html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
res = re.sub(html_pattern, '', '<html><body>Hello, <b>world</b>!<br /></body></html>')
print(res)

html_pattern = "<div>(.*?)<\\/div>"
html_pattern = "(?:<div.*?class=\"some-class\".*?>)(.*?)(?:<\\/div>)"
res = re.findall(html_pattern, '<html><body>Probably.<div class="some-class">Hello, world!</div><br />Today</body></html>')
print(res)

# XML regex
xml_pattern = "(?:<from.*?>)(.*?)(?:<\\/from>)"
res = re.findall(xml_pattern, '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don\'t forget me this weekend!</body></note>')
print(res)

# Mac address
mac_address_validate_pattern = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"
res = re.match(mac_address_validate_pattern, "00:00:5e:00:53:af")
print(res)

extract_mac_address_pattern = "(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})"
res = re.findall(extract_mac_address_pattern, 'Unknown error in node 00:00:5e:00:53:af. Terminating.')
print(res)







