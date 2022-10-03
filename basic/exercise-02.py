# Exercise 2: Validate username

import re

def validate(username):
  pattern = "^[a-zA-Z0-9_.-]+$"
  if re.match(pattern, username):
    print("valid")
  else:
    print("not valid")


validate("bill_gates")
validate("bill gates")