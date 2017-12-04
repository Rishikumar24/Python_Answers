'''
Name:Factorial
Description:  Implementing  factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation
Author:Rishi Kumar
Date:2/12/2017
'''

def facR(n):
  if n == 0:
    return 1
  else:
      return n * factR(n-1)
def factI(n):
    x = 1
    for each in range(1,n+1):
      x = x * each
    return  x
n=int(raw_input("Enter a number:"))
obj=factR(n)
obj2=factI(n)
print "Recursive function:" +str(obj)
print "iterative function:" +str(obj2)
