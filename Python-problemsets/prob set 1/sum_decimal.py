'''
Name:Sum of Decimal numbers separated by commas
Description: Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'.A program that prints the sum of the numbers in s.
Author:Rishi Kumar
Date:2/12/2017
'''
print "Enter Decimal numbers separated by ',':"
s=raw_input()
a=[]
a=s.split(',')
su=0
for i in a:
  su=su+float(i)
print "The sum is:"+ str(su)
