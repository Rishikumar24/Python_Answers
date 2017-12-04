'''
Name:Addition of numbers
Description:Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5
Author:Rishi Kumar
Date:2/12/2017
'''
def add_numbers(n):
    s=0
    for i in n :
      if i in['0','1','2','3','4','5','6','7','8','9']:
          i=int(i)
          s=s+i
    print "The sum is ",s
n=raw_input("Enter a string with characters and numbers:")
add_numbers(n)