# Exercise 16: Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]

print("Solution 1:")
result = []
for x in numbers:
  result.append(x*x)

print(result)

print("Solution 2:")
result = [x * x for x in numbers]
print(result)


