# Exercise 7: Display numbers divisible by 5 from a list

def check(arr):
  for x in arr:
    if x%5 == 0:
      print(x)

numbers = [10, 20, 33, 46, 55]
check(numbers)