# Exercise 10: Check Palindrome Number

def palindrome(number):
  orginal = number
  revsed  = 0  
  while(number > 0):
    rem    = number % 10
    revsed = (revsed * 10) + rem  
    number = number // 10

  if orginal == revsed: 
    print("Yes. given number is palindrome number")
  else:
    print("No. given number is not palindrome number")

palindrome(121)
palindrome(345)