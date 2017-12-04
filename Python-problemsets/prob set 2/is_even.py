'''
Name:First even number
Description:Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number
Author:Rishi Kumar
Date:2/12/2017
'''
def is_even(n):
    for i in n.split(' '):
        a=int(i)
        if(a%2==0):
            print a," is the first even number"
            b=1
            break
        else:
            continue
b=0   
n =raw_input("Enter the numbers")
is_even(n)
if b==0:
  print "No even nos are present"