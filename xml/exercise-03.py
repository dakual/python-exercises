import xml.etree.ElementTree as ET

xml ='''<?xml version ="1.0"?>
<States>
    <state name ="TELANGANA">
        <rank>1</rank>
        <neighbor name ="ANDHRA" language ="Telugu"/>
        <neighbor name ="KARNATAKA" language ="Kannada"/>
    </state>
    <state name ="GUJARAT">
        <rank>2</rank>
        <neighbor name ="RAJASTHAN" direction ="N"/>
        <neighbor name ="MADHYA PRADESH" direction ="E"/>
    </state>
    <state name ="KERALA">
        <rank>3</rank>
        <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
    </state>
</States>
'''

root = ET.fromstring(xml)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for state in root.findall('state'):
    rank = state.find('rank').text
    name = state.get('name')
    print(name, rank)