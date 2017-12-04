'''
Name:Space padding
Description:To write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
Author:Rishi kumar
Date:02/12/2017
'''
def right_justify(s):
  return s.rjust(70)

s=raw_input("Enter any string")
obj=right_justify(s)
print obj