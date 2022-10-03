# Exercise 1: Calculate the multiplication and sum of two numbers

class Calculate:

  def __init__ (self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def sum(self):
    result = self.num1 + self.num2
    print(result)

  def mul(self):
    result = self.num1 * self.num2
    print(result)

a = Calculate(20, 30)
a.sum()
a.mul()
