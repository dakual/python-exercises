# Exercise 17: Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

def remove(list, value):
  print( [x for x in list if x != value] )

remove(list1, 20)


