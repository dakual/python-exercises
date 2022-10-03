import json

class Vehicle:
  def __init__(self, name, engine, price):
    self.name = name
    self.engine = engine
    self.price = price

  def dump(self):
      return {"name": self.name, "engine": self.engine, "price": self.price}

lst = list()
lst.append(Vehicle("Ford", "1.6", 12600))
lst.append(Vehicle("Mazda", "1.3", 10300))

# method 1
vehicleJson = json.dumps([o.dump() for o in lst], indent=3)
print(vehicleJson)


# method 2
class VehicleEncoder(json.JSONEncoder):
  def default(self, o):
    return o.__dict__
    
vehicleJson = json.dumps(lst, cls=VehicleEncoder, indent=3)
print(vehicleJson)

# export json file
with open("output.json","w") as f:
  # method 1
  json.dump(lst, f, cls=VehicleEncoder, indent=3)
  # method 2
  f.write(vehicleJson)