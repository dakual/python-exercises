# Exercise 12: Print multiplication table form 1 to 10

for i in range(1, 11):
  for x in range(1, 11):
    y = i * x
    print("{0:3}".format(y), end=" ")
  
  print()