import re

"""
Has minimum 8 characters in length. {8,}
At least one uppercase English letter. (?=.*?[A-Z])
At least one lowercase English letter. (?=.*?[a-z])
At least one digit. (?=.*?[0-9])
At least one special character. (?=.*?[#?!@$%^&*-])
"""

def cs(password):
  patt = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
  if patt.match(password):
    return True

  return False


print( cs("Aa123456!") )