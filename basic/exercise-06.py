# Exercise 6: Check if the first and last number of a list is the same

def check(arr):
  if arr[0] == arr[-1]:
    print("Result is True")
  else:
    print("Result is False")


numbers_x = [10, 20, 30, 40, 10]
check(numbers_x)

numbers_y = [75, 65, 35, 75, 30]
check(numbers_y)