
import xml.etree.ElementTree as ET
 
mytree = ET.parse('sample-02.xml')
myroot = mytree.getroot()
 
for prices in myroot.iter('price'):
    prices.text = str(float(prices.text)+10)
    prices.set('newprices', 'yes')
 
ET.SubElement(myroot[0], 'tasty')
for temp in myroot.iter('tasty'):
    temp.text = str('YES')
 
myroot[1][0].attrib.pop('itemid')
myroot.remove(myroot[2])
mytree.write('output.xml', encoding='utf-8', xml_declaration=True)