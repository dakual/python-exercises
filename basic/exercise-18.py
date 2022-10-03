# Exercise 18: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print("Solution 1:")
res_dict = dict(zip(keys, values))
print(res_dict)


print("Solution 2:")
res_dict = dict()
for x in range(len(keys)):
  res_dict.update({keys[x] : values[x]})

print(res_dict)