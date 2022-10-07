import xml.etree.ElementTree as ET

def GenerateXML(fileName) :
  root = ET.Element("Catalog")
    
  m1 = ET.Element("mobile")
  m1.set("version", "1.0")
  root.append(m1)
    
  b1 = ET.SubElement(m1, "brand")
  b1.text = "Redmi"
  b2 = ET.SubElement(m1, "price")
  b2.set("currency", "TL")
  b2.text = "6999"
    
  m2 = ET.Element("mobile")
  m2.set("version", "1.1")
  root.append (m2)
    
  c1 = ET.SubElement(m2, "brand")
  c1.text = "Samsung"
  c2 = ET.SubElement(m2, "price")
  c2.set("currency", "TL")
  c2.text = "9999"
    
  m3 = ET.Element("mobile")
  m3.set("version", "1.2")
  root.append (m3)
    
  d1 = ET.SubElement(m3, "brand")
  d1.text = "RealMe"
  d2 = ET.SubElement(m3, "price")
  d2.set("currency", "TL")
  d2.text = "11999"
    
  tree = ET.ElementTree(root)
  ET.indent(tree, space="\t", level=0)

  with open (fileName, "wb") as files :
    tree.write(files, encoding='utf8', xml_declaration=True)


if __name__ == "__main__": 
    GenerateXML("output.xml")