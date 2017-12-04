'''
Name:Greatest Common Divisor
Description: To write a function called gcd that takes parameters a and b and returns their greatest common divisor.
Author:Rishi Kumar
Date:2/12/2017
'''

def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)
a=int(raw_input("Enter number 1:"))
b=int(raw_input("Enter number 2:"))
print gcd(a,b)
