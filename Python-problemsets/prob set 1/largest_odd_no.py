'''
Name:Largest odd number
Description:A program that examines three variables—x, y, and z— and prints the largest odd number among them. If none of them are odd, it prints a message to that effect.
Author:Rishi kumar
Date:02/12/2017
'''
x=raw_input("Enter value for x:")
y=raw_input("Enter value for y:")
z=raw_input("Enter value for z:")
a=int(x)
b=int(y)
c=int(z)
if a%2==0 and b%2==0 and c%2==0:
  print "None of the numbers are odd"
elif a>b and a>c:
  print "x is the largest odd no"
elif b>a and b>c:
  print "y is the largest odd no"
else:
  print "z is the largest odd no"