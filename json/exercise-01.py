import json

jsonData   = open("./sample.json").read()
jsonObject = json.loads(jsonData)

print(
    "=======================================================================================" "\n"
    "Name & Surname                Specialty                  Experience         Relocation " "\n" 
    "----------------------------- -------------------------  ------------------ -----------")

features = jsonObject["features"]
for row in features:
  name = "{0} {1}".format(row["candidate"]["first_name"], row["candidate"]["last_name"])
  spec = row["candidate"]["specialty"]
  expe = row["candidate"]["experience"]
  relo = row["candidate"]["relocation"]

  print("{0:29} {1:26} {2:18} {3:10}".format(name, spec, expe, relo))