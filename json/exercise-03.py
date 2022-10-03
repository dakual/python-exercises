import json
from collections import namedtuple


jsonObject = []
try:
  jsonData   = open("sample.json").read()
  jsonObject = json.loads(jsonData)
except Exception as e:
  print(e)

# get all the values of a key ‘first_name’
dataList = [x.get('candidate').get('first_name') for x in jsonObject['features']]
print(dataList)

# making the object
x = json.loads(jsonData, object_hook =
               lambda d : namedtuple('X', d.keys())
               (*d.values()))

print(x.features[0].candidate)

