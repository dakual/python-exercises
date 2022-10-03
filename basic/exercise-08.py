# Exercise 8: Return the count of a given substring from a string


str = "Emma is good developer. Emma is a writer"

print("Solution 1:")
cnt = str.count("Emma")
print(cnt)

print("Solution 2:")
cnt = 0
for i in range(len(str)-1):
  cnt += str[i:i+4] == "Emma"
print(cnt)
