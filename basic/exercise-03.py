# Exercise 3: Print the sum of the current number and the previous number

prev = 0
for i in range(10):
  tot = i + prev
  print(f"Current Number {i} Previous Number  {prev}  Sum:  {tot}")
  prev = i