'''
Name:Largest of 10 odd numbers
Description: A program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it prints a message to that effect.
Author:Rishi kumar
Date:02/12/2017
'''
a=0
print "Enter 10 intgers"
for i in range(1,11):
  n=int(raw_input('Enter value %d:'% i))
  if(n%2==0):
    pass
  else:
    if n>a:
      a=n
print ('The largest odd no is: %d' % a)