'''
Name:Root and Power
Description:  A program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it prints a message to that effect.
Author:Rishi Kumar
Date:2/12/2017
'''
import math
n=int(raw_input("enter an integer"))
s=math.sqrt(n)
p=n/s
if((p<6)&(p>0)):
  if((math.pow(s,p))==n):
   print "square root: " +str(s)
   print "power: " +str(p)
  else:
      print "power multiplied by square root doesnt give the entered number"
else:
    print "No such pair of integers exist"


