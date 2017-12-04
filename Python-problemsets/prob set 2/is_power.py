'''
Name:Is power
Description:To write a function called is_power that takes parameters a and b and returns True if a is a power of b
Author:Rishi Kumar
Date:2/12/2017
'''
def is_power(a,b):
    if(a%b != 0):
        return False
    elif(a/b == 1):
        return True
    else:
        return is_power(a/b,b)
a=int(raw_input("Enter the value of a :"))
b=int(raw_input("Enter the value of b :"))
c=is_power(a, b)

if(c==True):
    print "True"
else:
    print "False"