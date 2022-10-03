# Exercise 4: Print characters from a string that are present at an even index number

str = input("Enter word: ")

print("Solution 1:")
for i,x in enumerate(str):
  if i%2 == 0:
    print(x)

print("Solution 2:")
size = len(str)
for i in range(0, size-1, 2):
  print(str[i])

print("Solution 3:")
arr = list(str)
for i in arr[0::2]:
  print(i)