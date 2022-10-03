# Exercise 13: Write a function called exponent(base, exp) that returns
# an int value of base raises to the power of exp.

def exponent(base, exp):
  result = 1
  for i in range(exp):
    result = result * base

  print(f"{base} raises to the power of {exp}: {result}")


exponent(5, 4)


