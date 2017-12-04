'''
Name:String Compare
Description:To write a function isIn() that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.
Author:Rishi kumar
Date:02/12/2017
'''
a=raw_input("Enter string A:")
b=raw_input("Enter string B:")
def isin(a,b):
  if a in b:
    print 'True'
  elif b in a:
    print 'True'
  else:
    print 'false'

isin(a,b)