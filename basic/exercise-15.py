# Exercise 15: Read line number 4 from the following file

import os

with open("./exercise-11.py", "r") as fp:
  lines = fp.readlines()
  for i in range(4):
    print("Line {0} = {1}".format(i, lines[i]))


