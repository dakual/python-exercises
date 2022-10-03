# Exercise 14: Check file is empty or not

import os

size = os.stat("./exercise-01.py").st_size
if size > 0:
  print("file is not empty")
else:
  print("file is empty")