'''
Name:Observe the code snippet
Description:What would the code above return if the statement x = 25 were replaced by x = -25
Author:Rishi Kumar
Date:2/12/2017
'''
x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
  print 'low =', low, 'high =', high, 'ans =', ans
  numGuesses += 1
if ans**2 < x:
  low = ans
else:
  high = ans
  ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x

#low = 0.0 high = 1.0 ans = 0.5