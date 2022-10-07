import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree   = ET.parse("sample-01.xml", parser=parser)
root   = tree.getroot()

action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

print(ET.tostring(action, encoding='utf8').decode('utf8'))


xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

print(ET.tostring(action, encoding='utf8').decode('utf8'))

tree.write("movies.xml")

comedy = root.find("./genre[@category='Comedy']")
years  = comedy.findall("./decade[@years='2010s']")
for i in years:
  print(i.tag, i.attrib)
  for k in i.iter("movie"):
    print(k.attrib.get("title"))
    print(k.find("./description").text)




